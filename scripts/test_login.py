import pytest
import yaml


def analyze_data():
    with open("./data/data.yaml", "r") as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
        print(content)
        return content


class TestLogin:

    @pytest.mark.parametrize("args", ["zhangsan", "lisi"])
    def test_login(self, args):
        print(args)

    @pytest.mark.parametrize("a,b", [[1, 2]])
    def test_login1(self, a, b):
        print(a)
        print(b)

    # @pytest.mark.parametrize("args", [{"name": "xiaoming", "phone": "188"}])
    # def test_login(self, args):
    #     print(args)
