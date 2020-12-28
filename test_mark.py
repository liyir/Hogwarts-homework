# mark标签
# 对测试用例打标签，在运行测试用例的时候，可根据标签名来过滤要运行的用例
# -*- coding:utf8 -*-
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

    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    def test_demo1(self):
        print("我的第二个测试用例")
        assert 1 == 2
# 运行
# pytest -m 标签名
