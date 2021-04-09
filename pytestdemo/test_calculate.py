import pytest
import yaml

from Calculator import Calculator


class TestCal:
    def setup_class(self):
        print("开始")
        self.calc = Calculator()
    def setup(self):
        print("【开始计算】 ")
    def teardown(self):
            print("【计算结束】 ")
    def teardown_class(self):
        print("【结束】")

#其中还可能需要考虑两个数的大小是否超过int类型的最大值，相加后是否超过，如果超过也需要进行报错提示的
    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open("add.yaml")))
    def test_add(self, a, b, expect):
        if isinstance(a, (int, float)) is not True or isinstance(b, (int, float))  is not True or isinstance(expect, (int, float))  is not True:
            if a==0 and b==0:
                print(1)
                assert expect == self.calc.add(a, b)
            else:
                print(2)
                assert expect == self.calc.add(a, b),'请检查输入参数，加法计算的参数只能是int类型或者是float类型'
        else:
            print(3)
            assert expect == self.calc.add(a, b)
#这边首先判断类型是否为数字型，其次判断除数是否为0，不为0的时候我们进行计算，计算结果我们保留1位小数进行比较
    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open("div.yaml")))
    def test_div(self, a, b, expect):
        if isinstance(a, (int, float)) is not True or isinstance(b, (int, float))  is not True or isinstance(expect, (int, float))  is not True:
            if b == 0:
                assert expect == self.calc.div(a, b),'请检查输入参数，除法计算除数不能为0'
            elif a==0:
                assert expect == self.calc.div(a, b)
            else:
                assert expect == self.calc.div(a, b),'请检查输入参数，除法计算的参数只能是int类型或者是float类型'
        else:
            assert expect == round(self.calc.div(a, b),1)
