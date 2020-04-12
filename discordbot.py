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
import re
import random
from time import sleep
# import math
import pandas as pd

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
    game = discord.Game("$recommend | $help")
    await client.change_presence(activity=game)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        reply = f'{message.author.mention} 百合はいいぞ' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信
        print("メッセージ送信")
    
    if message.content == '$recommend': # $recommendが投稿されたとき、百合作品をお勧めする
        # csv読み込み
        # ヘッダーがあるファイルの読み込み
        df = pd.read_csv('yurilist.csv', usecols=['タイトル'])
        # 疑似乱数生成
        osusume = random.randint(0, len(df))
        # 返信メッセージを生成
        reply = df.iat[osusume, 0]
        # 返信メッセージを送信
        await message.channel.send(reply)
        print("お勧め作品タイトル送信")
    
    elif message.content == '$help': # $helpが投稿されたとき、このbotの使い方をDMで送る
        # DMを送信
        dm = await message.author.create_dm()
        help_message =  "メンションすると何か返事します。\n$recommend と投稿するとランダムで百合作品をお勧めします。\n$help と投稿するとDMでこのbotの使い方を説明します。（今見てるこれ。）\n百合はいいぞ"
        await dm.send(help_message)
        # DMを送信したことの通知
        await message.channel.send(f"{message.author.mention}さん、DMを送りました")
        print("ヘルプメッセージを送信")

    elif message.content.startswith('$love') == True:
        # $love <name1> <name2>が投稿されたとき、<name1>から<name2>にラブビームを送る
        m = re.match(r'(\$love)[ ]([a-z|A-Z|0-9]+)[ ]([a-z|A-Z|0-9]+)', message.content)
        if m == None:
            print("$love <name1> <name2>の形で入力してください！")
        else:
            name1 = m.group(2)
            name2 = m.group(3)
            for i in range(5):
                sleep(1)
                beam = name1 + (':heart:' * i) + (':white_heart:' * (5-i)) + name2
                await message.channel.send(beam)
            print("ラブビーム")

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)