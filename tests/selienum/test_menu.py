from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from notebook.tests.selenium.utils import wait_for_selector, trigger_keystrokes, shift, cmdtrl
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver

def test_execute_from_menu(prefill_notebook):
    notebook = prefill_notebook(['print("hello world")'])
   
    wait_for_selector(notebook.browser, '#editlink', single=True).click()
    wait_for_selector(notebook.browser, '#copy_cell', single=True).click()
    wait_for_selector(notebook.browser, '#editlink', single=True).click()
    wait_for_selector(notebook.browser, '#paste_cell_below', single=True).click()

    wait_for_selector(notebook.browser, '#celllink', single=True).click()
    wait_for_selector(notebook.browser, '#run_all_cells', single=True).click()

    outputs = notebook.wait_for_cell_output(1)
    assert outputs[0].text == 'hello world'


def test_execute_from_key(prefill_notebook):
    notebook = prefill_notebook(['print("hello shift+enter")'])
    shift(notebook.browser, Keys.ENTER)
    outputs = notebook.wait_for_cell_output(0)
    assert outputs[0].text == 'hello shift+enter'

# def test_execute_from_key(prefill_notebook):
#     notebook = prefill_notebook(['print("hello")'])

#     wait_for_selector(notebook.browser, '#cmd_palette', single=True).click()
    
#     # notebook.browser.implicitly_wait(5)
#     action = webdriver.ActionChains(notebook.browser)
#     action.send_keys("asv")
#     wait_for_selector(notebook.browser, 'typeahead__list')[3].click()
#     # notebook.browser.implicitly_wait(10)
#     # # lists[3].click()
#     wait_for_selector(notebook.browser, 'search', single=True).send_keys("abc")