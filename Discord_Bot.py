# -*- coding:utf-8 -*- 
import discord
from discord import message
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
import asyncio
from json import loads
import datetime
import pytz
 

client = discord.Client()
token = "ODUwNjk4MDU5NTExNDk2NzI0.YLtgTg.vbX1Dsu7eW1Lrt3XiIoAqHcPT-E"
twitch_Client_ID = 'y1hsew8veil7mhijz109iwt5rv3oco'
twitch_Client_secret = '56ys0anukydyf1pwj5ymh1pjo9qfk1'
twitchID = "nlmiso95"
oauth_key = requests.post("https://id.twitch.tv/oauth2/token?client_id=" + twitch_Client_ID + "&client_secret=" + twitch_Client_secret + "&grant_type=client_credentials")
access_token = loads(oauth_key.text)["access_token"]
token_type = 'Bearer '
authorization = token_type + access_token
headers = {'client-id': twitch_Client_ID, 'Authorization': authorization}


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("시츠야 도움말"))


@client.event
async def on_message(message): 

    #봇이 입력할 경우
    if message.author.bot: 
        return None 

    #응답 테스트
    if message.content == "시츠야":
        await message.channel.send("네!")

    #기본 명령어
    if message.content.split(" ")[0] == "시츠야":

        #명령어 목록
        if message.content.split(" ")[1] == "명령어":
            embed = discord.Embed(title="기본 명령어", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x62c1cc)
            embed.add_field(name='급식 명령어',value='급식 관련 명령어', inline=False)
            embed.add_field(name='방송 명령어',value='방송 관련 명령어', inline=False)
            embed.add_field(name='번역 명령어',value='번역 관련 명령어', inline=False)
            await message.channel.send(embed = embed)
        
        #트위치 생방 여부
        if message.content.split(" ")[1] == "방송":

            #방송 관련 명령어
            if message.content.split(" ")[2] == "명령어":
                embed = discord.Embed(title="방송 명령어", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x62c1cc)
                embed.add_field(name='방송 목록',value='방송 온·오프라인 상태 여부', inline=False)
                embed.add_field(name='방송 링크 [이름]',value='[이름] 방송 링크', inline=False)
                await message.channel.send(embed = embed)

            #스트리머 명단
            if message.content.split(" ")[2] == "목록":
                #value값 삼항연산자 해보기
                embed = discord.Embed(title="방송 명령어", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x62c1cc)
                embed.add_field(name='재승샷',value='', inline=False)
                embed.add_field(name='케인',value='', inline=False)
                await message.channel.send(embed = embed)

            #스트리머 링크    
            if message.content.split(" ")[2] == "링크":
                #재승샷
                if message.content.split(" ")[3] == "재승샷":
                    response_channel = requests.get('https://api.twitch.tv/helix/streams?user_login=' + 'nlmiso95', headers=headers)
                    try:
                        if loads(response_channel.text)['data'][0]['type'] == 'live':
                            await message.channel.send('방송 ON' +'\n https://www.twitch.tv/' + 'nlmiso95')
                    except:
                        await message.channel.send('방송 OFF' +'\n https://www.twitch.tv/' + 'nlmiso95')
                        await message.channel.send('방송하고 있지 않아요!')
                #케인
                if message.content.split(" ")[3] == "케인":
                    response_channel = requests.get('https://api.twitch.tv/helix/streams?user_login=' + 'kanetv8', headers=headers)
                    try:
                        if loads(response_channel.text)['data'][0]['type'] == 'live':
                            await message.channel.send('방송 ON' +'\n https://www.twitch.tv/' + 'kanetv8')
                    except:
                        await message.channel.send('방송 OFF' +'\n https://www.twitch.tv/' + 'kanetv8')
                        await message.channel.send('방송하고 있지 않아요!')
                

        #학교 급식 알림     (급식 데이터 받아오기)
        if message.content.split(" ")[1] == "급식":
            if message.content.split(" ")[2] == "명령어":
                embed = discord.Embed(title="급식 명령어", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x62c1cc)
                embed.add_field(name='',value='' , inline=False)
                await message.channel.send(embed = embed)

        #번역기            (구글 번역데이터 가져오기) (번역 명령어 임베드 만들기)
        if message.content.split(" ")[1] == "번역":
            if message.content.split(" ")[2] == "명령어":
                embed = discord.Embed(title="번역 명령어", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x62c1cc)
                embed.add_field(name='',value='', inline=False)
                await message.channel.send(embed = embed)
    
    



    #관리자 명령어
    if message.content.split(" ")[0] == "시츠야":
        authority = (message.author.guild_permissions.administrator)
        if authority is True:

            #관리자 명령어 목록
            if message.content.split(" ")[1] == "관리자":
                if message.content.split(" ")[2] == "명령어":
                    embed = discord.Embed(title="", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x62c1cc)                    
                    embed.add_field(name='삭제 [숫자]',value='[숫자]만큼 채팅 삭제', inline=False)
                    embed.add_field(name='도배 [내용] [횟수]',value='[내용]을 [횟수]만큼 도배', inline=False)
                    await message.channel.send(embed = embed)

            #채팅 삭제
            if message.content.split(" ")[1] == "삭제":
                amount = message.content.split(" ")[2]
                await message.channel.purge(limit=1)                
                await message.channel.purge(limit=int(amount))   

            #채팅 도배
            if message.content.split(" ")[1] == "도배":
                content = message.content.split(" ")[2]
                amount = message.content.split(" ")[3]
                if int(amount) <= 10:
                    for x in range(int(amount)):
                        await message.channel.send(content)
                else:
                    await message.channel.send("너무 많아요! 최대 10회까지만!")

        if authority is False:
            await message.channel.send("권한 없음")
















    #잡담
    if message.content == "노무현은":
        await message.channel.send("살아있다!")
    if message.content == "야~":
        await message.channel.send("기분좋다!")

client.run(token)