# coding=utf-8
import pytest

# pytest_addoption是:
# 1.hook方法，名称不可改变；
# 2.仅能在conftest.py文件或者pytest plugins里实现；
# 3.在测试用例执行前被调用


def pytest_addoption(parser):
    parser.addoption(
        "--auth", action="store", default=None, help="Your own auth key pair"
    )

@pytest.fixture(scope='session')
def auth(request):
    # 用于接收命令行命令参数
    return request.config.getoption('--auth')
