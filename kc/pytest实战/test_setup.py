def setup_module():
    print("模块级的开始")

def teardown_module():
    print("模块级的结束")

def setup_function():
    print("这是函数add的开始")
def test_add():
    print('这是函数add')
def teardown_function():
    print('这是函数add的结束')

def setup():
    print("这是函数add1的开始")
def test_add1():
    print('这是函数add1')
def teardown():
    print('这是函数add1的结束')

class Testadd2:
    def setup_class(self):
        print('这是类add2的开始')
    def teardown_class(self):
        print('这是类add2的结束')

    def test_add2(self):
        print('这是类中的函数add2')

    def setup_method(self):
        print('这是类方法add2的开始')

    def teardown_method(self):
        print('这是类add2的结束')

    def test_add3(self):
        print('这是类中方法add3')

    def setup(self):
        print('这是类方法add3的开始')

    def teardown(self):
        print('这是类方法add3的结束')


