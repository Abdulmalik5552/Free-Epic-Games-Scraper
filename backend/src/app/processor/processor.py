import asyncio
from random import randint
import time
from datetime import datetime
import logging
from selenium.common.exceptions import NoSuchElementException
from app.services.epic_game_scraper import scraper
from app.crud import game
from app.db.session import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def set_games():
    db = SessionLocal()
    while True:
        # Get the stored games
        games = await game.get_multi(db = db)
        games_titles = [game.title for game in games]
        if games:
            logger.info(f"Waiting for {(games[0].start_date - datetime.now()).total_seconds() + 30} seconds 😴.")
            # time.sleep((games[0].start_date - datetime.now()).total_seconds() + 30)
        # [No stored games OR after waiting]... Scrape the games and create/update db.
        logger.info(f"Scrape intilizing, Getting epic free games 🥄.")
        games_in = []
        try:
            games_in = scraper.get_epic_games()
            logger.info(f"successful Scopping 😋.")
        except NoSuchElementException as ex:
            logger.info(f"Failed to Scope 💀. This was the exception:\n\n{ex}")
            time.sleep(randint(0, 10))
        for game_obj in games_in:
            if game_obj.title in games_titles:
                logger.info("Updating to DB ... 🙃.")
                await game.update(
                    db=db, 
                    db_obj=games[games_titles.index(game_obj.title)],
                    obj_in=game_obj
                )
            else:
                logger.info("Creating to DB ... 🙂.")
                await game.create(db = db, obj_in=game_obj)

if __name__ == "__main__":
    asyncio.run(set_games())