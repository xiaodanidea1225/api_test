# conftest.py
import pytest
import codecs
import yaml
import json
import os


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default='test', help="set env"
    )


@pytest.fixture(scope='session')
def load_data_from_json_yaml(request):
    # 获取解析到的test_data所在的目录，以及调用test_data的文件
    data_folder, function_file = request.param
    # 根据传入的环境变量参数，计算出应该用那个环境下的数据文件
    data_file_name = function_file.replace('.py', '.%s.yaml' % request.getfixturevalue('get_env'))
    data_file = os.path.join(data_folder, data_file_name)
    _is_yaml_file = data_file.endswith((".yml", ".yaml"))
    with codecs.open(data_file, 'r', 'utf-8') as f:
        # Load the data from YAML or JSON
        if _is_yaml_file:
            data = yaml.safe_load(f)
        else:
            data = json.load(f)
    # 这里你可能需要根据业务需要，把数据解析以下再返回
    return data


'''
fixture作用范围
fixture里面有个scope参数可以控制fixture的作用范围:session > module > class > function
- function 每一个函数或方法都会调用
- class  每一个类调用一次，一个类可以有多个方法
- module，每一个.py文件调用一次，该文件内又有多个function和class
- session 是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
'''


@pytest.fixture(scope='session')
def get_env(request):
    return request.config.getoption('--env')
