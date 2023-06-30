# This example requires the 'message_content' intent.
TOKEN = "XXXXXXXX"

import discord
import requests
import json

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

    if message.content.startswith("!read"):
        if message.guild.voice_client is None:
            await message.channel.send("ボイスチャンネルに接続していません。")
            return
        text = message.content
        text = text[len("!read"):]
        audio_query = requests.post('http://localhost:50021/audio_query', params = {'text': text, 'speaker': 1})
        synthesis = requests.post('http://localhost:50021/synthesis', params = {'speaker': 1},data=json.dumps(audio_query.json()))
        with open('voices/test.wav', mode='wb') as f:
            f.write(synthesis.content)
        source = await discord.FFmpegOpusAudio.from_probe("voices/test.wav", before_options="-channel_layout mono")
        message.guild.voice_client.play(source)

client.run(TOKEN)
