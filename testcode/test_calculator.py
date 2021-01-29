import yaml
import pytest

from devcode.Calculator import Calculator


class TestCalculator:
    test_data = yaml.safe_load(open("./data/calculator_data.yml"))
    addData: list = (test_data['add']['test_data'], test_data['add']['ids'])
    divData: list = (test_data['div']['test_data'], test_data['div']['ids'])

    def setup_class(self):
        print("-----开始测试计算器 setup_class-----")
        self.calc = Calculator()

    def teardown_class(self):
        print("-----结束测试计算器 teardown_class-----")

    def setup(self):
        print("-----开始执行用例-----")

    def teardown(self):
        print("-----用例执行结束-----")

    @pytest.mark.parametrize("a,b,result", addData[0], ids=addData[1])
    def test_add(self, a, b, result):
        print("测试数据：" + f"a={a} , b ={b} , result={result}")
        assert result == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,result", divData[0], ids=divData[1])
    def test_div(self, a, b, result):
        print("测试数据：" + f"a={a} , b ={b} , result={result}")
        assert result == self.calc.div(a, b)
