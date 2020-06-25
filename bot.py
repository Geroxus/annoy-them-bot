import discord
from os import makedirs, listdir

bot_token_file = open('./discord-bot-token', 'tr')
BOT_TOKEN = bot_token_file.readline()
bot_token_file.close()

client = discord.Client()


@client.event
async def on_ready():
    print('Successfully logged in as user: {}'.format(client.user))
    print('Connected to:')
    for gld in client.guilds:
        print('  {}'.format(gld.name))


@client.event
async def on_guild_join(guild):
    wlcmmsgchn = guild.text_channels[0]  # WeLCoMe MesSaGe CHanNel
    for chn in guild.text_channels:
        if 'general' in chn.name:
            wlcmmsgchn = chn
    await wlcmmsgchn.send('Hello Everyone! I am {0}.\nThe first unfortunate soul to be pinged after this initial '
                          'message will be annoyed forever. Thank you for your consideration and let the games begin!')
    print('Welcome message shared in: {}'.format(wlcmmsgchn.name))
    makedirs('./{}'.format(guild.id))


@client.event
async def on_message(message):
    if 'target' not in listdir('./{}'.format(message.guild.id)):
        if len(message.mentions) > 0:
            f = open('./{}/target'.format(message.guild.id), 'tw')
            f.write('{}\n'.format(message.mentions[0].id))
            f.close()
    else:
        f = open('./{}/target'.format(message.guild.id), 'tr')
        tid = int(f.readline())  # Target ID
        f.close()

        if message.author.id == tid:
            await message.channel.send('Hey {}! How are you doing?'.format(message.author.mention))


client.run(BOT_TOKEN)
