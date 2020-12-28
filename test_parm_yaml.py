# 读取数据抽离出来改造
# @pytest.mark.parametrize("a,b,expected",
#                          yaml.safe_load(open("./data.yml"))["datas"],
#                          ids=yaml.safe_load(open("./data.yml"))["myid"])

import pytest
import yaml


def get_datas():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["add"]
        sub_datas = datas["sub"]
        mul_datas = datas["mul"]
        div_datas = datas["div"]
        ids = datas["myid"]
        return [add_datas, sub_datas, mul_datas, div_datas, ids]


def add_function(a, b):
    return a + b


def sub_function(a, b):
    return a - b


def mul_function(a, b):
    return a * b


def div_function(a, b):
    return a / b


@pytest.mark.parametrize("a,b,expected",
                         get_datas()[0],
                         ids=get_datas()[4])
def test_add(a, b, expected):
    assert add_function(a, b) == expected


@pytest.mark.parametrize("a,b,expected",
                         get_datas()[1],
                         ids=get_datas()[4])
def test_sub(a, b, expected):
    assert sub_function(a, b) == expected


@pytest.mark.parametrize("a,b,expected",
                         get_datas()[2],
                         ids=get_datas()[4])
def test_mul(a, b, expected):
    assert mul_function(a, b) == expected


@pytest.mark.parametrize("a,b,expected",
                         get_datas()[3],
                         ids=get_datas()[4])
def test_div(a, b, expected):
    assert div_function(a, b) == expected
