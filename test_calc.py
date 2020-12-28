import pytest

from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize("a, b, expect", [(
            3, 5, 8), (-1, -2, -3), (100, 200, 400)], ids=["中文int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        assert expect == self.cal.add(a, b)

    @pytest.mark.parametrize("a, b, expect",
                             [(3, 8, -5), (4, 1, 3), (500, 200, 400)])
    def test_sub(self, a, b, expect):
        assert expect == self.cal.sub(a, b)

    @pytest.mark.parametrize("a, b, expect",
                             [(3, 8, 24), (4, 1, 4), (500, 200, 400)])
    def test_mul(self, a, b, expect):
        assert expect == self.cal.mul(a, b)

    @pytest.mark.parametrize("a, b, expect",
                             [(24, 8, 3), (4, 0, 4), (500, 200, 400)])
    def test_div(self, a, b, expect):
        assert expect == self.cal.div(a, b)
