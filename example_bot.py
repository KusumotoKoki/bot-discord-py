# This example requires the 'message_content' intent.
TOKEN = "XXXXXXXX"

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!hello":
        await message.channel.send("hello!")

    if message.content.startswith('!embed'):
        embed = discord.Embed(
            # Embedを定義する
            title="Embed Title",# タイトル
            color=0x00ff00, # フレーム色指定(今回は緑)
            description="Embed Discription", # Embedの説明文 必要に応じて
            url="https://example.com" # これを設定すると、タイトルが指定URLへのリンクになる
        )
        await message.channel.send(embed=embed)
    
    if message.content.startswith('!stop'):
        await message.channel.send("終了しました。")
        await client.close()

    if message.content == "!join":
        if message.author.voice is None:
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            return
        await message.author.voice.channel.connect()
        await message.channel.send("接続しました。")

    if message.content == "!leave":
        if message.guild.voice_client is None:
            await message.channel.send("ボイスチャンネルに接続していません。")
            return
        await message.guild.voice_client.disconnect()
        await message.channel.send("切断しました。")

        
    if message.content == "!play":
        if message.guild.voice_client is None:
            await message.channel.send("ボイスチャンネルに接続していません。")
            return
        source = await discord.FFmpegOpusAudio.from_probe("voices/onsei_test_nanoda.wav", before_options="-channel_layout mono")
        message.guild.voice_client.play(source)


client.run(TOKEN)
