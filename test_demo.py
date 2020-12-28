

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
# def test_add(a, b, expect):
#     assert add_function(a, b) == expect

# @pytest.mark.parametrize("a,b", [(3, 5), (-1, -2,),
#                                  ], ids=["int", "minus"])
# def test_add(a, b):
#     assert add_function(a, b) == a + b
def add_function(a, b):
    return a + b


# @pytest.mark.parametrize("参数名",列表数据)
# 参数名：作为测试用例的参数. 字符串格式，多个参数中间用逗号隔开。
# 列表数据：一组测试数据。list格式，多组数据用元组类型，list的每个元素都是一个元组，元组里的每个元素和按参数顺序一一对应。


@pytest.mark.parametrize("a", [0, 1])
@pytest.mark.parametrize("b", [2, 3])
def test_add(a, b):
    print("测试数据组合: a -> %s,b -> %s" % (a, b))
