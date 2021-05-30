from selenium.webdriver.common.keys import Keys
from notebook.tests.selenium.utils import wait_for_selector, wait_for_xpath

def test_demo(notebook):
    browser = notebook.browser
    notebook.add_and_execute_cell(index=0, content='a=10;print(a)')
    outputs = notebook.wait_for_cell_output(0)
    assert outputs[0].text == '10'
    notebook.add_and_execute_cell(1,cell_type="code",content='b=20;print(b)')
    outputs = notebook.wait_for_cell_output(1)
    assert outputs[0].text == '20'
    notebook.add_and_execute_cell(2,cell_type="code",content='c = a + b;print(c)')
    outputs = notebook.wait_for_cell_output(2)
    assert outputs[0].text == '30'

def test_demo_loop(notebook):
    notebook.add_and_execute_cell(index=0, content='sum=0')    
    notebook.add_and_execute_cell(1,cell_type="code",content='for i in range(10): sum+=i;')
    notebook.add_and_execute_cell(2,cell_type="code",content='print(sum)')
    outputs = notebook.wait_for_cell_output(2)
    assert outputs[0].text == '45'

def test_demo_function(notebook):
    notebook.add_and_execute_cell(index=0, content='def neg(i): return -i;')    
    notebook.add_and_execute_cell(1,cell_type="code",content='print(neg(-12345))')

    outputs = notebook.wait_for_cell_output(1)
    assert outputs[0].text == '12345'

def test_demo_import(notebook):
    notebook.add_and_execute_cell(index=0, content='import math')    
    notebook.add_and_execute_cell(1,cell_type="code",content='print(math.sin(math.radians(90)))')
    outputs = notebook.wait_for_cell_output(1)
    assert outputs[0].text == '1.0'

