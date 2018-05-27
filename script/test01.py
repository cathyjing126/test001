import pytest
class Test001:
    @pytest.mark.parametrize("a",[1,2,3])
    def test_001(self,a):
        assert a ==2
