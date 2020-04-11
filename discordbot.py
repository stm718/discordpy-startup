# from discord.ext import commands
# import os
# import traceback

# bot = commands.Bot(command_prefix='/')
# token = os.environ['DISCORD_BOT_TOKEN']


# @bot.event
# async def on_command_error(ctx, error):
#     orig_error = getattr(error, "original", error)
#     error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
#     await ctx.send(error_msg)


# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')


# bot.run(token)

# インストールした discord.py を読み込む
import discord
from discord.ext import commands
import os
import traceback
import random
import math

# 自分のBotのアクセストークンに置き換えてください
bot = commands.Bot(command_prefix='/')
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    # ～をプレイ中
    game = discord.Game("$recommend | 屋上の百合霊さん")
    await client.change_presence(activity=game)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        reply = f'{message.author.mention} 百合はいいぞ' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信
    
    if message.content == '$recommend':
        options = [
            "『推しが武道館行ってくれたら死ぬ』", "『やがて君になる』", "『彼女の沈清』", 
            "『屋上の百合霊さん』", "『白衣性恋愛症候群』", "『夢現Re:M@ster』", 
            "『リップヴァンウィンクルの花嫁』", "『花とアリス』", "『噂の二人』",
            "『お嬢さん』",
            ]
        response = options[math.floor(random.random()*len(options))]
        await message.channel.send(response)
    
    elif message.content == '$help':
        dm = await message.author.create_dm()
        help_message =  "メンションすると何か返事します。\n$recommend と投稿するとランダムで百合作品をお勧めします。"
        await dm.send(help_message)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)