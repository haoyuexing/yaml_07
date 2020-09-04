import pytest321

from base.base_analyze import analyze_data


class TestPython:

    # @pytest.mark.parametrize(("a", "b", "c"), [("111", "222", "333"),("444", "55", "66"),("7", "8", "9")])
    @pytest.mark.parametrize("args", analyze_data("python_data", "test_py1"))
    def test_py1(self, args):
        a = args["a"]





    # @pytest.mark.parametrize(("x", "y"), [("123", "321"), ("321", "123")])

    @pytest.mark.parametrize("args", analyze_data("python_data", "test_py2"))
    def test_py2(self, args):
        print(args)
        print("hello")
123123123123
