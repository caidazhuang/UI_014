import allure
class Test_001:
    @allure.severity(allure.severity_level.BLOCKER)
    def test_001(self):
        print('111')
        assert True

    @allure.severity(allure.severity_level.CRITICAL)
    def test_001(self):
        print('111')
        assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_001(self):
        print('111')
        assert True

    @allure.severity(allure.severity_level.MINOR)
    def test_001(self):
        print('111')
        assert True

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_001(self):
        print('111')
        assert False