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
    
    if message.content == '$recommend':
        # お勧めする作品のタイトルリスト
        # options = [
        #     "『推しが武道館行ってくれたら死ぬ』", "『やがて君になる』", "『彼女の沈清』", 
        #     "『屋上の百合霊さん』", "『白衣性恋愛症候群』", "『夢現Re:M@ster』", 
        #     "『リップヴァンウィンクルの花嫁』", "『花とアリス』", "『噂の二人』",
        #     "『お嬢さん』",
        #     ]
        # response = options[math.floor(random.random()*len(options))] # 返信メッセージの作成
        # await message.channel.send(response) # 返信メッセージを送信
        # csv読み込み
        # ヘッダーがあるファイルの読み込み
        df = pd.read_csv('yurilist.csv', usecols=['タイトル'])
        # 読み込んだデータの確認
        df.head()
        print('dataframeの行数・列数の確認==>\n', df.shape)
        print('indexの確認==>\n', df.index)
        print('columnの確認==>\n', df.columns)
        print('dataframeの各列のデータ型を確認==>\n', df.dtypes)
        # 疑似乱数生成
        osusume = random.randint(0, len(df))
        # 返信メッセージを生成
        reply = df[osusume:osusume+1]
        # 返信メッセージを送信
        await message.channel.send(reply)
    
    elif message.content == '$help':
        # DMを送信
        dm = await message.author.create_dm()
        help_message =  "メンションすると何か返事します。\n$recommend と投稿するとランダムで百合作品をお勧めします。\n$help と投稿するとDMでこのbotの使い方を説明します。（今見てるこれ。）\n百合はいいぞ"
        await dm.send(help_message)
        # DMを送信したことの通知
        await message.channel.send(f"{message.author.mention}さん、DMを送りました")



# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)