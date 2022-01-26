import pytest
import os

# 获取当前文件夹路径
# 获取当前文件的名称
current_folder, current_file = os.path.split(os.path.realpath(__file__))
print("current_folder is: {},current_file is: {}".format( current_folder, current_file))
# 计算出当前文件对应的数据文件的目录名称
data_folder = os.path.dirname(current_folder) + os.sep + 'test_data' + os.sep + current_file.strip('.py') + os.sep
print("data_folder is: {}".format(data_folder) )


class Demo:
    @staticmethod
    def login(username, password):
        # 这里写你的业务逻辑，简单起见，我返回True
        print('\n%s' % username)
        print('\n%s' % password)
        return True


class TestDemo:
    @pytest.mark.parametrize("load_data_from_json_yaml, expected", [((data_folder, current_file), True)],
                             indirect=['load_data_from_json_yaml'])
    def test_login(self, load_data_from_json_yaml, expected):
        assert Demo.login(load_data_from_json_yaml["headers"], load_data_from_json_yaml["headers2"]) == expected


# class TestDemo1:
#     def test_env_config(self, get_env):
#         print("\nNow the environment are --: {}".format(get_env))
#         assert True
