from time import sleep

import pytest


class Test_demo():
    # 用例失败后自动重新运行
    #     @pytest.mark.flaky(reruns=3, reruns_delay=1)
    #     def test_demo1(self):
    #         print("我的第二个测试用例")
    #         assert 1 == 2

    # 多重校验：pytest-assume
    # def test_demo2(self):
    #     pytest.assume(1 == 2)  #断言失败，继续执行下面的断言
    #     pytest.assume(1 == 2)
    #     pytest.assume(1 == 2)

    # 分布式并发执行：pytest - xdist
    @pytest.mark.run(order=3)
    def test_demo3(self):
        sleep(1)
        assert 1 == 1

    @pytest.mark.run(order=2)
    def test_demo4(self):
        sleep(1)
        assert 1 == 1

    def test_demo5(self):
        sleep(1)
        assert 1 == 1

    @pytest.mark.run(order=1)
    def test_demo6(self):
        sleep(1)
        assert 1 == 1

    def test_demo7(self):
        sleep(1)
        assert 1 == 1
