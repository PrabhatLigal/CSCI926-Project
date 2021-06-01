from notebook import i18n

# https://en.wikipedia.org/wiki/Language_localisation

def test_parse_accept_lang_header_new():
    palh = i18n.parse_accept_lang_header
    assert palh('kr') == ['kr']
    assert palh('dog') == ['dog']
    assert palh('dog-cat') == ['dog','dog_cat']

# support langauage


	# "domain": "nbjs",
	# "supported_languages": [
	# 	"fr-FR",
	# 	"zh-CN",
	# 	"nl",
	# 	"ja_JP"

def test_loadTest_supported():
    lang = i18n.load('nl')
    assert len(lang) > 0


def test_loadTest_supported1():
    lang = i18n.load('zh_CN')
    assert len(lang) > 0

def test_loadTest_supported2():
    lang = i18n.load('fr_FR')
    assert len(lang) > 0

def test_loadTest_supported3():
    lang = i18n.load('ja_JP')
    assert len(lang) > 0

def test_loadTest_unsupported():
    lang = i18n.load('kr')
    assert len(lang) == 0

    lang = i18n.load('es_AR')
    assert len(lang) == 0

    lang = i18n.load('kr')
    assert len(lang) == 0

