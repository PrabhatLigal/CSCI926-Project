import pytest
from notebook.utils import url_escape, url_unescape





def test_url_escape_space():  
    path = url_escape('/some test case for spaces/')
    assert path == '/some%20test%20case%20for%20spaces/'



#https://en.wikipedia.org/wiki/Percent-encoding
#exisitng test covers =    / !@$#%^&* / test %^ notebook @#$ name.ipynb
#missing codes =    < > +  { } [] | ~   ' ; ? : 
#   !	 #	$	%	&	'	(	)	*	+	,	/	:	;	=	?	@	[	]  
# %21	%23	%24	%25	%26	%27	%28	%29	%2A	%2B	%2C	%2F	%3A	%3B	%3D	%3F	%40	%5B	%5D

def test_url_escape_1():
    #test for ~
    path = url_escape('hostname/~something/')
    assert path == 'hostname/%7Esomething/'


def test_url_escape_2():    
    #test for <
    path = url_escape('hostname/<something/')
    assert path == 'hostname/%3Csomething/'

def test_url_escape_3():
    #test for >
    path = url_escape('hostname/>something/')
    assert path == 'hostname/%3Esomething/'

def test_url_escape_4():
    #test for +
    path = url_escape('hostname/+something/')
    assert path == 'hostname/%2Bsomething/'
    
def test_url_escape_5():
    #test for {
    path = url_escape('hostname/{something/')
    assert path == 'hostname/%7Bsomething/'

def test_url_escape_6():
    #test for }
    path = url_escape('hostname/}something/')
    assert path == 'hostname/%7Dsomething/'

def test_url_escape_7():
    #test for |
    path = url_escape('hostname/|something/')
    assert path == 'hostname/%7Csomething/'

def test_url_escape_8():
    #test for [
    path = url_escape('hostname/[something/')
    assert path == 'hostname/%5Bsomething/'

def test_url_escape_9():
    #test for ]
    path = url_escape('hostname/]something/')
    assert path == 'hostname/%5Dsomething/'

def test_url_escape_10():
    #test for '
    path = url_escape('hostname/\'something/')
    assert path == 'hostname/%27something/'

def test_url_escape_11():
    #test for ;
    path = url_escape('hostname/;something/')
    assert path == 'hostname/%3Bsomething/'

def test_url_escape_12():
    #test for ?
    path = url_escape('hostname/?something/')
    assert path == 'hostname/%3Fsomething/'

def test_url_escape_13():
    #test for :
    path = url_escape('hostname/:something/')
    assert path == 'hostname/%3Asomething/'

def test_url_escape_14():
    #test for +
    path = url_escape('hostname/+something/')
    assert path == 'hostname/%2Bsomething/'

def test_url_unescape():

    #test for ~
    path = url_unescape('hostname/%7Esomething/')
    assert path == 'hostname/~something/'

 
def test_url_unescape():

    #test for < > +  { } [] | ~   ' ; ? : 
    path = url_unescape('hostname/%3C%3E%2B%7B%7C%7D%5B%5D%7E%27%3B%3F%3Asomething/')
    assert path == 'hostname/<>+{|}[]~\';?:something/'

def test_url_unescape_1():
    path = url_unescape('/some%20test%20case%20for%20spaces')
    assert path == '/some test case for spaces'

    

