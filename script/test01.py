import pytest,allure
class Test001:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤01")
    @pytest.mark.parametrize("a",[1,2,3])
    def test_001(self,a):
        allure.attach("描述","这是测试步骤01的描述...")
        assert a !=2

    @allure.step(title="测试步骤02")
    @pytest.mark.parametrize("a", [1, 2, 3])
    def test_002(self,a):
        allure.attach("描述","这是测试步骤02的描述...")
        assert a !=2
