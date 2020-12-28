# conftest.py这个文件名是固定的，不可以更改。
# 使用的时候不需要导入conftest.py，会自动寻找
import pytest


# def get_db_data():
#     return
# @pytest.fixture(params=get_db_data())  #从数据库里取数据

# @pytest.fixture(autouse="ture") # 每个测试函数都会自动调用该前置函数
# @pytest.fixture(scope="class")  # scope作用域 scope参数有四种选择：function（测试函数级别），
# class（测试类级别），module（测试模块“.py”级别），session（多个文件级别）。默认是function级别
# @pytest.fixture(scope="module")

# @pytest.fixture(params=["***参数1***","***参数2***"])   # 执行前需要定义
# def myfixture(request):
#     print("\n执行myfixture，里面的参数是%s\n" % request.param)
#     a = 1
#     # env = request.param
#     return a

@pytest.fixture(params=["***参数1***", "***参数2***"])
def myfixture(request):
    print("\n执行myfixture，里面的参数是%s\n" % request.param)
    yield request.param  # 类似return（返回），同时下面的语句也会执行，
    # yield前相当于setup，yield后相当于teardown，也取决于作用域
    print("清理数据，关闭数据库连接")  # teardown操作


def pytest_collection_modifyitems(session, config, items):
    print(type(items))  # items是一个列表
    items.reverse()  # 反转
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        print("item.name是%s" % item.name)
        print("item.nodeid是%s" % item.nodeid)

        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        if "div" in item._nodeid:
            item.add_marker(pytest.mark.div)


@pytest.fixture()
def connectdb():
    print("执行我的fixture--connectdb")
