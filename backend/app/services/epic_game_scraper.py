from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from app.schemas import Game
from app.core import settings

games_list: list[Game] = []

driver = webdriver.Remote(
            desired_capabilities=DesiredCapabilities.FIREFOX,
            command_executor="http://%s:4444" % settings.SELENIUM_GRID_HOST
        )
driver.get(settings.URL)
driver.implicitly_wait(2)

total = int(driver.find_element(By.XPATH, settings.FIRST_GAME_ARIA).get_attribute("aria-label").split(',')[1][-1])
for index in range(1, total+1):
    xpath_game = settings.XPATH_GAME %(index)
    xpath_start_time = settings.XPATH_TIME %(index, 1)
    xpath_end_time = settings.XPATH_TIME %(index, 2)
    games_list.append(
        Game (
            id=index,
            title=driver.find_element(By.XPATH, xpath_game).text,
            start_date=driver.find_element(By.XPATH, xpath_start_time).get_attribute("datetime"),
            end_date=driver.find_element(By.XPATH, xpath_end_time).get_attribute("datetime"),
        )
    )
for game in games_list:
    print(game)
driver.close()
