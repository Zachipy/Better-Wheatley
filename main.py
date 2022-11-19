import disnake
from disnake.ext import commands
import urllib
import random
import asyncio

answers = ['Yes', 'No', 'Maybe', 'Definitively', 'Could be', 'Absolutely!', 'Im sure about that', 'NO',
           'Nah', 'Probably', 'Im not sore about that', 'Very possible', 'I dont think so', 'Not possible']
buchstabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

insultsfile = open("assets/insults.txt")
insults = insultsfile.read()
oneinsult = insults.split("\n\n")
insultsfile.close()
tokenfile = open(".token")
bottoken = tokenfile.read()
print(f"Token:{bottoken}")
tokenfile.close()

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('\r\nI hate it, but it works somehow')
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name="In Space right now"),
                              status=disnake.Status.do_not_disturb)


# Commands

# Wetter CMD
@bot.slash_command(description="Shows the weather")
async def wetter(inter, *, wetter):
    urllib.request.urlretrieve('http://wttr.in/{0}.png?0?q'.format(wetter), 'cache/wheather.png')
    await inter.send(f"Weather at {wetter}:", file=disnake.File('cache/wheather.png'))


# Sagmir command
@bot.slash_command(description="Helps you answer tricky questions!")
async def sagmir(inter, *, question: str):
    embed = disnake.Embed(color=0x0055ff,
                          description=f" {inter.author.mention} asked me:\r\n\r\n**{question}** \r\n\r\n My Answer is:\r\n\r\n **{random.choice(answers)}**")
    await inter.send(embed=embed)


# Delete command
# @bot.slash_command(description="Löscht Nachrichten in einem Channel")
# async def delete(inter, amount):
#    if amount.isdigit():
#        count = int(amount) + 1
#        deleted = await inter.channel.purge(limit=count)
#        await inter.response.send_message(f"Ich habe {len(deleted)} Nachrichten gelöscht", ephemeral=True)

# Table
@bot.slash_command(description="Soundboard: oh noo, out table is broken")
async def table(inter):
    channel = inter.author.voice.channel
    vc = await channel.connect()
    await inter.send("Sound plays now", ephemeral=True)
    source = disnake.FFmpegPCMAudio("sounds/table.mp3")
    vc.play(source)
    await  asyncio.sleep(10)
    guild = inter.guild.voice_client
    await guild.disconnect()


# here we go again
@bot.slash_command(description="Soundboard: Ah shit, here wo go again!")
async def herewegoagain(inter):
    channel = inter.author.voice.channel
    vc = await channel.connect()
    await inter.send("Sound plays now", ephemeral=True)
    source = disnake.FFmpegPCMAudio("sounds/again.mp3")
    vc.play(source)
    await asyncio.sleep(3)
    guild = inter.guild.voice_client
    await guild.disconnect()


@bot.slash_command(description="Soundboard: boom")
async def boom(inter):
    channel = inter.author.voice.channel
    vc = await channel.connect()
    await inter.send("Sound plays now", ephemeral=True)
    source = disnake.FFmpegPCMAudio("sounds/vineboom.mp3")
    vc.play(source)
    await asyncio.sleep(3)
    guild = inter.guild.voice_client
    await guild.disconnect()


@bot.slash_command(description="Shows you the head of a Minecraft player")
async def kopf(inter, username):
    urllib.request.urlretrieve(f'https://cravatar.eu/helmhead/{username}/128.png', 'cache/Avatar.png')
    await inter.send(file=disnake.File('cache/Avatar.png'))


@bot.slash_command(description="Show you the skin of a Minecraft player")
async def skin(inter, username):
    urllib.request.urlretrieve(f'https://mc-heads.net/body/{username}', 'cache/skin.png')
    await inter.send(file=disnake.File('cache/skin.png'))


@bot.slash_command(description="LeTs YoUr TExT lOok lIkE tHIs")
async def mock(inter, *, text):
    def mock(input_text):
        output_text = ""

        for char in input_text:

            if char.isalpha():

                if random.random() > 0.5:
                    output_text += char.upper()

                else:
                    output_text += char.lower()

            else:
                output_text += char

        return output_text

    mocktext = text
    await inter.send(mock(mocktext))


@bot.slash_command(description="See if you can guess the number from the bot!")
async def guess(inter, zahl: int):
    nummerbot = random.randint(0, 10)
    if zahl > 10:
        embed = disnake.Embed(color=0xff0000)
        embed.add_field(name="Incorrect Input! ", value=f"Enter a number from **0** to **10**!", inline=False)
        await inter.send(embed=embed, ephemeral=True)
    else:
        if zahl == nummerbot:
            embed = disnake.Embed(color=0x00ff08)
            embed.add_field(name="Right! ", value=f"Ich thought about the number **{nummerbot}** and you thought about **{zahl}**!",
                            inline=False)
            await inter.send(embed=embed)
        else:
            embed = disnake.Embed(color=0xff0000)
            embed.add_field(name="Wrong! ", value=f"I thought about **{nummerbot}** and you thought about **{zahl}**!", inline=False)
            await inter.send(embed=embed)


@bot.slash_command(description="GlaDOS moment")
async def glados(inter):
    await inter.send("credits:RaidGreg", file=disnake.File("video/glados.mp4"))

@bot.slash_command(description="I AM NOT A MOROOOON")
async def moron(inter):
    await inter.send("I AM  NOT A MORON!", file=disnake.File("audio/I am not a moron.mp3"))

@bot.slash_command(description="Bentley!")
async def bentley(inter):
    await inter.send(file=disnake.File("assets/Bentley.png"))

@bot.slash_command(description="Insult someone")
async def insult(inter):
    await inter.send(random.choice(oneinsult))

@bot.slash_command(description="Shows you the Help Menu")
async def help(inter):
    embed = disnake.Embed(
        title="Wheatley Help Menu",
        description="A quick overview of all commands in Wheatley",
        color=disnake.Colour.blue(),
    )

    embed.set_author(
        name="Wheatley",
        url="https://ohas.website",
        icon_url="https://cdn.discordapp.com/avatars/714567851708645431/b609799d6fb8210f7e283adcb8b4c9d7.png",
    )
    embed.set_footer(
        text="WheatleyBot 1.2 (Zachi Fork) - Original developed by Oha Der Erste",
        icon_url="https://cdn.discordapp.com/avatars/714567851708645431/b609799d6fb8210f7e283adcb8b4c9d7.png",
    )



    embed.add_field(name="/wetter", value="Shows you the weather!", inline=False)
    embed.add_field(name="/insult", value="Spits out a random insult!", inline=False)
    embed.add_field(name="/sagmir {your yes-no-question}", value="Helps you make important decisions", inline=False)
    embed.add_field(name="/table", value="Soundboard command. Try it while you are in a voice channel!", inline=False)
    embed.add_field(name="/herewegoagain", value="Soundboard command. Try it while you are in a voice channel!", inline=False)
    embed.add_field(name="/boom", value="Soundboard command. Try it while you are in a voice channel!", inline=False)
    embed.add_field(name="/kopf {mc-name}", value="Shows you the head of a Minecraft Player", inline=False)
    embed.add_field(name="/skin {mc-name", value="Shows you the skin of a Minecraft Player", inline=False)
    embed.add_field(name="/mock", value="MoCkS yOuR mEsSaGe", inline=False)
    embed.add_field(name="/guess {number}", value="Im thinking about a number and you have to guess it", inline=False)
    embed.add_field(name="/glados", value="Try it out LMAO", inline=False)
    embed.add_field(name="/moron", value="I AM NOT A MORON", inline=False)
    embed.add_field(name="/bentley", value="gives you a pick of the cutest cat ever!", inline=False)
    await inter.send(embed=embed)

bot.run(bottoken)
