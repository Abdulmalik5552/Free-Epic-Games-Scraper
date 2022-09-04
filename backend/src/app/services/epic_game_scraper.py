from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

from app.core import settings
from app.schemas.game import GameCreate

# FireFox binary path (Must be absolute path)
FIREFOX_BINARY = FirefoxBinary('/opt/firefox/firefox')
 
# FireFox PROFILE
PROFILE = webdriver.FirefoxProfile()
PROFILE.set_preference("browser.cache.disk.enable", False)
PROFILE.set_preference("browser.cache.memory.enable", False)
PROFILE.set_preference("browser.cache.offline.enable", False)
PROFILE.set_preference("network.http.use-cache", False)
PROFILE.set_preference("general.useragent.override","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0")
 
# FireFox Options
FIREFOX_OPTS = Options()
FIREFOX_OPTS.log.level = "trace"    # Debug
FIREFOX_OPTS.headless = True
GECKODRIVER_LOG = '/geckodriver.log'
 
class Scraper:
    def __init__(self):
        ff_opt = {
            "firefox_binary":FIREFOX_BINARY,
            "firefox_profile":PROFILE,
            "options":FIREFOX_OPTS,
            "service_log_path":GECKODRIVER_LOG
        }
        self.DRIVER = webdriver.Firefox(**ff_opt)

    def get_epic_games(self):

        games_list: list[GameCreate] = []
        self.DRIVER.delete_all_cookies()
        self.DRIVER.get(settings.URL)
        self.DRIVER.implicitly_wait(3)
        total = int(self.DRIVER.find_element(By.XPATH, settings.FIRST_GAME_ARIA).get_attribute("aria-label").split(',')[1][-1])
        for index in range(1, total+1):
            xpath_game = settings.XPATH_GAME %(index)
            xpath_start_time = settings.XPATH_TIME %(index, 1)
            xpath_end_time = settings.XPATH_TIME %(index, 2)
            games_list.append(
                GameCreate (
                    title=self.DRIVER.find_element(By.XPATH, xpath_game).text,
                    start_date=self.DRIVER.find_element(By.XPATH, xpath_start_time).get_attribute("datetime"),
                    end_date=self.DRIVER.find_element(By.XPATH, xpath_end_time).get_attribute("datetime"),
                )
            )
        return games_list

scraper = Scraper()