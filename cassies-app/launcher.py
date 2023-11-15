import os
import discord
from bot import DiscordBot


TOKEN = os.getenv("DISCORD_BOT_TOKEN")


def main():
    intents = discord.Intents.all()
    client = DiscordBot(intents=intents)
    client.run(TOKEN)


if __name__ == "__main__":
    main()
