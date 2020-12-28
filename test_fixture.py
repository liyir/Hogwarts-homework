import pytest


# @pytest.fixture()
# def myfixture():
#     print("执行我的fixture")

class Test_demo():
    def test_one(self, myfixture):
        print("执行test_one")
        myenv = myfixture
        print("---in test_one--- %s" % myenv)
        assert 1 + 1 == 2
    # def test_two(self,myfixture):
    #     print("执行test_two")
    #     assert 1+1==2
    # def test_three(self,connectdb):
    #     print("执行test_three")
    #     assert 1+1==2
