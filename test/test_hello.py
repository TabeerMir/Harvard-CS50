from helloworld import hello

def test_default():
    assert hello() == 'hello, world'

def test_argument():
    assert hello('tabeer') == 'hello, tabeer'