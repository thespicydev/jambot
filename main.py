'''Entry point for our Discord bot.

Make sure your .env file in the same directory contains the environment
variable DISCORD_TOKEN. Example:

# .env file
DISCORD_TOKEN=whatever_your_token_is
'''
from bots.dummy_bot import DummyBot
from dotenv import load_dotenv

import os


def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    spicy_bot = DummyBot()
    spicy_bot.run(token)

if __name__ == '__main__':
    main()