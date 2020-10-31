import os
import discord
import random
import re
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # Only do anything if OP is not a bot
    if not message.author.bot:
        # Respond to an image
        if len(message.attachments) > 0:
            if ".png" in message.attachments[0].filename:
                if random.randint(0, 9) == 9:
                    await message.channel.send("Seen it")
            if ".jpg" in message.attachments[0].filename:
                if random.randint(0, 9) == 9:
                    await message.channel.send("lmao eks dee")
            if ".jpeg" in message.attachments[0].filename:
                if random.randint(0, 9) == 9:
                    await message.channel.send("Lurk more")
            if ".gif" in message.attachments[0].filename:
                if random.randint(0, 9) == 9:
                    await message.channel.send("Good gif friend. Fun fact, it\'s pronounced gif")
            if ".webm" in message.attachments[0].filename:
                if random.randint(0, 9) == 9:
                    await message.channel.send("Funny meme, I laughed :^)")
            if ".webp" in message.attachments[0].filename:
                if random.randint(0, 9) == 9:
                    await message.channel.send("Retweet")

        # Workaround for name id shit
        cnt = re.sub("<.*>","", message.content)
        
        # Respond in the channel to keywords or phrases
        if "911" in cnt or "9/11" in cnt:
            await message.channel.send("Never forget.")
        if message.content.lower() == "ur gay" or message.content.lower() == "ur gey":
            await message.channel.send("no u")
        if "69" in cnt:
            await message.channel.send("Nice.")
        if "nigger" in message.content.lower() or "nigga" in message.content.lower():
            await message.channel.send("Woah there guy, it looks like you just used a bad word. What would your mother say?")
        
        # Add reactions in response to keywords or phrases
        if "the media" in message.content.lower():
            await message.add_reaction("🇮🇱")
        if "cum" in message.content.lower().split(" "):
            await message.add_reaction("💦")
        if "zuckerberg" in message.content.lower():
            await message.add_reaction("👀")
        if "bernie would win" in message.content.lower() or "bernie would have won" in message.content.lower() or "bernie will win" in message.content.lower():
            await message.add_reaction("🤡")
        if "covid" in message.content.lower() or "corona" in message.content.lower() or "cough" in message.content.lower():
            if random.randint(0, 9) == 9:
                await message.add_reaction("😷")
        if "hmm" in message.content.lower():
            if random.randint(0, 9) == 9:
                await message.add_reaction("🤔")
        if "420" in message.content.lower():
            await message.add_reaction("🌿")
 

client.run(TOKEN)
