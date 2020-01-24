import discord
from discord.ext import commands
from discord.ext.commands import bot

TOKEN = 'NjY5MTQ2NDIxNzE4NTQ4NDgx.XiiOgg.z57coY-CZGVTyhJ2jFGD4sZwNis'

client = commands.Bot(command_prefix = '.')

@client.command(pass_context=True)
async def report(ctx, *, message):
    me = await client.get_user_info("Your User ID")
    pm = "{} reported: {}".format(ctx.message.author, message)
    await client.send_message(me, pm)

@client.event
async def on_ready():
    print('Бот готов')

@client.command(aliases=["Ping","png","Png"])
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases=["Pong","pi","Дон"])
async def pong(ctx):
    await ctx.send(f"Ping! {round(client.latency * 1000)}ms")

@client.command (aliases=["Он_проиграл","Бот_победил","победа_Бота"])
async def pobeda(ctx):
    await ctx.send(f"Ага 😎")

@client.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f"hello{author.mention}")



client.run(TOKEN)