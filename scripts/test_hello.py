import pytest

from base.base_analyze import analyze_data


class TestHello:

    # @pytest.mark.parametrize("i", ["zhangsan", "lisi", "wangwu"])
    @pytest.mark.parametrize("args", analyze_data("hello_data", "test_hello1"))
    def test_hello1(self, args):
        i = args["i"]
        print(i)

    # @pytest.mark.parametrize("username,password", [("zs", "zs123"), ("ls", "ls123")])
    @pytest.mark.parametrize("args", analyze_data("hello_data", "test_hello2"))
    def test_hello2(self, args):
        username = args["username"]
        password = args["password"]
        print(username)
        print(password)
