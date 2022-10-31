import os
import discord
from dotenv import load_dotenv

BOT_NAME = "Dumb Bitch"


class ComputerManager:
    def __init__(self):
        pass

    def start_computer(self):
        print("Starting Computer")


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.computer_manager = ComputerManager()
        self.information_message = None

    async def send_information_message(self, channel: discord.TextChannel):
        self.information_message = await channel.send(
            "Placeholder message for server information\n"
            "react with :arrow_forward: to start the server"
        )
        await self.information_message.add_reaction("▶")

    async def on_ready(self):
        print(f"Logged on as {self.user}.")

    async def on_message(self, message):
        if message.author == self.user:
            return
        print(f"Message from {message.author}: {message.content}")
        if message.content == "!information_message":
            await self.send_information_message(message.channel)

    async def on_reaction_add(self, reaction, user):
        if user == self.user:
            return
        print(f"User {user} reacted to message {reaction.message.id} with {reaction}")
        if reaction.message == self.information_message:
            if reaction.emoji == "▶":
                self.computer_manager.start_computer()


if __name__ == "__main__":
    load_dotenv()
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

    # intents = discord.Intents.default()
    # intents.message_content = True
    intents = discord.Intents.all()
    client = MyClient(intents=intents)
    client.run(DISCORD_TOKEN)
