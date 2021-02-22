import pytest
import yaml

from kc.pytest实战.calculator import Calculator

def get_data():
    with open('calc.yml') as f:
        datas=yaml.safe_load(f)
    add_datas=datas['add']['datas']
    add_ids=datas['add']['ids']
    return [add_datas,add_ids]

def steps(calc,a,b,expect):
    with open('steps.yml') as f:
        steps=yaml.safe_load(f)
    for step in steps:
        if step == 'add':
            print('add step')
            result = calc.add(a,b)
            assert expect == result
        elif step == 'sub':
            print('sub step')
            result=calc.sub(a,b)
            assert expect == result

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def teardown(self):
        print('计算结束')

    @pytest.mark.parametrize('a,b,expect',get_data()[0],ids=get_data()[1])
    def test_add(self,a,b,expect):
        result=self.calc.add(a,b)
        assert  result==expect

    def test_add2(self):
        a=1
        b=2
        expect=3
        steps(self.calc,a,b,expect)

    def test_add1(self):
        result=self.calc.add(100,100)
        assert  result==200