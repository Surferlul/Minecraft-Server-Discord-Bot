import os
import discord
from dotenv import load_dotenv

BOT_NAME = "Dumb Bitch"


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}.")

    async def on_message(self, message):
        print(f"Message from {message.author}: {message.content}")
        if message.author == self.user:
            return
        if message.content == "hello":
            await message.channel.send(f"Hey {message.author}")
        if message.content == "goodbye":
            await message.channel.send(f"Goodbye {message.author}")


if __name__ == "__main__":
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

    # intents = discord.Intents.default()
    # intents.message_content = True
    intents = discord.Intents.all()
    client = MyClient(intents=intents)
    client.run(DISCORD_TOKEN)
