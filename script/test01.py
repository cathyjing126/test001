import pytest,allure
class Test001:
	@allure.step(title="测试步骤01")
    @pytest.mark.parametrize("a",[1,2,3])
    def test_001(self,a):
        assert a !=2
