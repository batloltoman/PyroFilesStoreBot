# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", "0"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-100"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1445283714"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Permanent Files Store Bot of [*☂️Renegades☂️**](https://t.me/cp_renegade)


🤖 **My Name:** [You Know Already 😉]





📡 **Hosted on:** [Heroku](https://heroku.com)



👥 **Support Group:** [Renegades](https://t.me/renegadesforever)

📢 **Channel:** [Renegade](https://t.me/cp_renegade)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @cp_renegade







	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **File Store Bot** of [Renegade](https://t.me/cp_renegade)


Owned By [Team Renegades](https://t.me/cp_renegade)
Check about bot button
