'''Entry point for our Discord bot.

Make sure your .env file in the same directory contains the environment
variable DISCORD_TOKEN. Example:

# .env file
DISCORD_TOKEN=whatever_your_token_is
'''
from bots import dummy_bot, jam_bot
from dotenv import load_dotenv

import os


def main():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    spicy_bot = jam_bot.JamBot()
    spicy_bot.run(token)

if __name__ == '__main__':
    main()