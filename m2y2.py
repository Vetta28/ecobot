import discord, os, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

ecologi = ["Замените обычную лампочку на энергосберегающую",
           "Оставьте машину в гараже и воспользуйтесь общественным транспортом",
           "Посадите дерево во дворе или в парке",
           "Приготовьте обед из продуктов, выращенных в вашем регионе",
           "Сдайте вторсырье в пункты приема",
           "Замените одноразовые полотенца традиционными из ткани, а для протирки стола применяйте микрофибровые салфетки вместо бумажных",
           "Выключайте свет",
           "Для разведения костра использовать старые кострища",
           "Не оставлять надписи на камнях и прочих природных объектах",
           "Не использовать на природе бытовую химию",
           "Не повреждать и не рвать без нужды растения"]

video = [
     "https://www.youtube.com/watch?v=2S0FRQYm498&pp=ygUUJ3Jqa2p1Ynh0Y3JidCBjamR0bnM%3D",
     "https://www.youtube.com/watch?v=ri5d8USqv9Q",
     "https://www.youtube.com/watch?v=PoxSvDLVKhU"
]

info = ''' Список комманд:
1. advice - выводит картинку с советом
2. advice_text - выводит текстовые совет пользователю
3. advice_video - выводит ролик с советом'''

@bot.command()
async def help_bot(ctx):
    await ctx.send(info)

@bot.command()
async def advice(ctx):
    img_name = random.choice(os.listdir("pictures"))
    with open(f'pictures/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def advice_text(ctx):
    await ctx.send(random.choice(ecologi))

@bot.command()
async def advice_video(ctx):
    await ctx.send(random.choice(video))

