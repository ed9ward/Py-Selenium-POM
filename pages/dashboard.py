from pages.base_page import BasePage


class Dashboard(BasePage):
    login_xpath = '//input[@id="login"]'
    pass_xpath = '//input[@id="password"]'
    my_team = "input[name='myTeam']"
    pass