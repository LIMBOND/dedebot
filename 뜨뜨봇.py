import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("안녕")


        client.run("NTkyMTgwMTMyOTIwNDI2NTA2.XQ7k6Q.mSGzHS7gcq17uPk3XzastiVdhak")