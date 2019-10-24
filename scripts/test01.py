import allure
import pytest


class Test:
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="步骤")
    def test01(self):
        allure.attach("失恋了，怎么办","找链家")

        print("aa")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test02(self):

        print("aa")

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test03(self):
        print("aa")

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test04(self):
        assert 0
        print("aa")

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test05(self):
        print("aa")

