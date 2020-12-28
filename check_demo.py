
import pytest


class Test_demo():
    @pytest.mark.demo
    def test_demo(self):
        print("我的第一个测试用例")

    # 在一个用例上打多个标签，多次使用@pytest.mark.标签名
    @pytest.mark.demo
    @pytest.mark.smoke
    def test_demo1(self):
        print("我的第二个测试用例")
