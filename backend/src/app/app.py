import sched, time
from .services.epic_game_scraper import get_epic_games

while True:

    scheduler = sched.scheduler(time.localtime, time.sleep)
    scheduler.enterabs(time.strptime('Tue May 01 11:05:17 2018'), 0, get_epic_games)
    scheduler.run()