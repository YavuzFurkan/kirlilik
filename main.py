import discord
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)




@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def petşişe(ctx):
    await ctx.send(f'Pet şişe doğada 450 yılda kaybolur.')


@bot.command()
async def kolakutusu(ctx):
    await ctx.send("200 - 300 yıl arası doğada kaybolur.")


@bot.command()
async def bebekbezi(ctx):
    await ctx.send("550 yılda doğada kaybolur.")


@bot.command()
async def camşişe(ctx):
    await ctx.send("4000 yılda doğada kaybolur.")


@bot.command()
async def sigara(ctx):
    await ctx.send("10yılda doğada kaybolur.")


@bot.command()
async def elma(ctx):
    await ctx.send("2 ayda doğada kaybolur.")


@bot.command()
async def muzkabuğu(ctx):
    await ctx.send("2 - 5 haftada doğada kaybolur.")


@bot.command()
async def poşet(ctx):
    await ctx.send("1000 yılda doğadan kaybolur.")
bilgi = ["Geridönüşümün faydaları:https://cdn.istanbul.edu.tr/statics/toplumhekimligi.istanbul.edu.tr/wp-content/uploads/2015/11/Geri-d%C3%B6n%C3%BC%C5%9F%C3%BCm%C3%BCn-%C3%A7evre-ve-ekonomi-a%C3%A7%C4%B1s%C4%B1ndan-%C3%B6nemi-Yrd.Do%C3%A7.Dr_.%C3%96znur-%C3%96ZDEN.pdf","Geridönüşümün aşamaları:http://www.istanbulgeridonusum.com.tr/bilgi-sayfalari/geri-donusumun-basamaklari.html"]
@bot.command()
async def bilgiler(ctx):
    await ctx.send(random.choice(bilgi))




bot.run("Token")
