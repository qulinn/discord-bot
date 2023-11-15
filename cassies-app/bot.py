import discord
import random
from discord.ext import commands


class DiscordBot(discord.Client):
    async def on_ready(self):
        print(f"{self.user} has connected to Discord!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "hello":
            await message.channel.send("Hi!")
            # await message.add_reaction('😊')
            await message.add_reaction("<:anya01:1164201278088421417>")
            # await message.add_reaction('<:yabamimi:1128884756646461441>')

        if message.content == "bye":
            await message.channel.send("see you!")
            await self.close()

        if message.content == "🙂":
            await message.channel.send("🤗")

        if message.content.startswith("play"):
            if len(message.content.split(" ")) != 2:
                await message.channel.send(
                    "please input `play` and `your choice` (`rock/paper/scissors`)."
                )

            message_command = message.content.split(" ")[0]
            message_choice = message.content.split(" ")[1]

            if message_command == "play":
                print("Debug: Starting rock-paper-scissors.")
                choices = ["ROCK", "PAPER", "SCISSORS"]

                if message_choice.upper() in choices:
                    bot_choice_index = random.randint(0, len(choices) - 1)
                    user_choice_index = choices.index(message_choice.upper())

                    # The next index beats the current index.
                    # When bot_choice_index - user_choice_index == 1:
                    # bot_choice = paper, user_choice = rock
                    # bot_choice = scissors, user_choice = paper
                    # When bot_choice_index - user_choice_index == -2
                    # bot_choice = rock, user_choice = scissors
                    if (
                        bot_choice_index - user_choice_index == 1
                        or bot_choice_index - user_choice_index == -2
                    ):
                        result = "win"
                    # The reverse for when player wins
                    elif (
                        bot_choice_index - user_choice_index == -1
                        or bot_choice_index - user_choice_index == 2
                    ):
                        result = "lose"
                    elif bot_choice_index == user_choice_index:
                        result = "tie"

                    # Handling resulting messages.
                    if result == "win":
                        await message.channel.send(
                            f"My choice is {choices[user_choice_index].lower()}."
                        )
                        await message.channel.send(
                            f"{choices[bot_choice_index].lower()} beats {choices[user_choice_index].lower()}. I win! :D"
                        )
                    elif result == "lose":
                        await message.channel.send(
                            f"My choice is {choices[user_choice_index].lower()}."
                        )
                        await message.channel.send(
                            f"{choices[user_choice_index].lower()} beats {choices[bot_choice_index].lower()}. I lose!"
                        )
                    elif result == "tie":
                        await message.channel.send(
                            f"My choice is {choices[user_choice_index].lower()}."
                        )
                        await message.channel.send(
                            f"We both picked {choices[user_choice_index].lower()}, so it's a tie! \nWant to try again?"
                        )
                        print("Debug: Finishing game.")
                else:
                    await message.channel.send(
                        "Sorry, you have to format the message as `play rock-paper-scissors`"
                    )
                    print("Debug: Sending error message.")
