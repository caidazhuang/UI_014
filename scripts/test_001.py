import allure
class Test_001:
    @allure.step('下单')
    def test_001(self):
        print('111')
        assert True
    @allure.step('登录')
    def test_002(self):
        print('222')
        assert True
