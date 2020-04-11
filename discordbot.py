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
    game = discord.Game("屋上の百合霊さん")
    await client.change_presence(status=discord.Status.idle, activity=game)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        reply = f'{message.author.mention} 百合はいいぞ' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)