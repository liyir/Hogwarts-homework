import pytest


# class Test_demo():
#     def test_one(self):
#         a = 5
#         b = 1
#         assert a != b
#         print("这是我的第一个测试用例")
#     def test_two(self):
#         a = 9
#         b = 1
#         assert a != b
#         print("这是我的第二个测试用例")


# @pytest.mark.parametrize("a,b,expect", [(3, 5, 8), (-1, -2, -3),
#                                           (1000, 1000, 2000)], ids=["int", "minus", "bigint"])
# def test_add(a, b, excepted):
#     assert add_function(a, b) == expect

# @pytest.mark.parametrize("a,b", [(3, 5), (-1, -2,),
#                                  ], ids=["int", "minus"])
# def test_add(a, b):
#     assert add_function(a, b) == a + b
def add_function(a, b):
    return a + b


@pytest.mark.parametrize("a", [0, 1])
@pytest.mark.parametrize("b", [2, 3])
def test_add(a, b):
    print("测试数据组合: a -> %s,b -> %s" % (a, b))
