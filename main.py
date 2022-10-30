import os
import discord
from dotenv import load_dotenv

BOT_NAME = "Dumb Bitch"

intents = discord.Intents.default()
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} has logged in.")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "hello":
        await message.channel.send(f"Hey {message.author}")
    if message.content == "goodbye":
        await message.channel.send(f"Goodbye {message.author}")


if __name__ == "__main__":
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(DISCORD_TOKEN)
