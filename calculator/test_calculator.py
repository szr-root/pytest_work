import pytest

from calculator.calculate import Calculator
from calculator.get_datas import get_datas

datas = get_datas("./datas.yml")
# print(datas)
# myids = datas[1]['addids']
# print(myids)

class TestCal():
    def setup_class(self):
        #在类开始的时候实例化一个计算器
        self.calc = Calculator()

    #方法开始时调用
    def setup_method(self):
        print("【开始计算】")

    #方法结束时调用
    def teardown_method(self):
        print("【计算结束】")

    # 测试加法
    @pytest.mark.parametrize("a,b,expect", datas[0]['adddatas'], ids=(datas[1]['addids']))
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    # 测试减法
    @pytest.mark.parametrize("a,b,expect", datas[0]['subdatas'], ids=(datas[1]['subids']))
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    # 测试乘法法
    @pytest.mark.parametrize("a,b,expect", datas[0]['muldatas'], ids=(datas[1]['mulids']))
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    # 测试除法
    @pytest.mark.parametrize("a,b,expect", datas[0]['divdatas'], ids=(datas[1]['divids']))
    def test_div(self, a, b, expect):
        try:
            result = self.calc.div(a, b)
            assert result == expect
        except ZeroDivisionError:
            print("0不能作为被除数")
