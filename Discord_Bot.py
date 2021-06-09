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
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
 
 
'''
경고, 밴, 킥 기능 만들기
'''

#기본
client = discord.Client()
token = "ODUwNjk4MDU5NTExNDk2NzI0.YLtgTg.V9cs39610lTEuywu8IbTkjaBayk"

#트위치
twitch_Client_ID = 'y1hsew8veil7mhijz109iwt5rv3oco'
twitch_Client_secret = '56ys0anukydyf1pwj5ymh1pjo9qfk1'
discord_channelID = 851094741747761214


#봇 기본 상태 / 트위치 방송알림
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("이나야 도움말"))
    
    #트위치 방송 알림
    channel = client.get_channel(discord_channelID)
    oauth_key = requests.post("https://id.twitch.tv/oauth2/token?client_id=" + twitch_Client_ID + "&client_secret=" + twitch_Client_secret + "&grant_type=client_credentials")
    access_token = loads(oauth_key.text)["access_token"]
    token_type = 'Bearer '
    authorization = token_type + access_token
    headers = {'client-id': twitch_Client_ID, 'Authorization': authorization}

    check1 = False
    check2 = False
    check3 = False
    check4 = False

    while True:
        #진재승
        try:
            response_channel = requests.get('https://api.twitch.tv/helix/streams?user_login=' + 'nlmiso95', headers=headers)
            if loads(response_channel.text)['data'][0]['type'] == 'live' and check1 == False:
                await channel.send('방송중 ON!' +'\n https://www.twitch.tv/' + 'nlmiso95')
                check1 = True
        except:
            check1 = False

        #코뚱잉
        try:
            response_channel = requests.get('https://api.twitch.tv/helix/streams?user_login=' + 'qq102qq', headers=headers)
            if loads(response_channel.text)['data'][0]['type'] == 'live' and check2 == False:
                await channel.send('방송중 ON!' +'\n https://www.twitch.tv/' + 'qq102qq')
                check2 = True
        except:
            check2 = False

        #가재맨
        try:
            response_channel = requests.get('https://api.twitch.tv/helix/streams?user_login=' + 'rlgus1006', headers=headers)
            if loads(response_channel.text)['data'][0]['type'] == 'live' and check3 == False:
                await channel.send('방송중 ON!' +'\n https://www.twitch.tv/' + 'rlgus1006')
                check3 = True
        except:
            check3 = False
        
        #랄로
        try:
            response_channel = requests.get('https://api.twitch.tv/helix/streams?user_login=' + 'aba4647', headers=headers)
            if loads(response_channel.text)['data'][0]['type'] == 'live' and check4 == False:
                await channel.send('방송중 ON!' +'\n https://www.twitch.tv/' + 'aba4647')
                check4 = True
        except:
            check4 = False
                

        await asyncio.sleep(300)


@client.event
async def on_message(message): 

    #봇이 입력할 경우
    if message.author.bot: 
        return None 

    #응답 테스트
    if message.content == "이나야":
        await message.channel.send("네!")

    #기본 명령어
    if message.content.split(" ")[0] == "이나야":

        #명령어 목록
        if message.content.split(" ")[1] == "명령어":
            embed = discord.Embed(title="기본 명령어", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x62c1cc)
            embed.add_field(name='급식 명령어',value='급식 관련 명령어', inline=False)
            embed.add_field(name='번역 명령어',value='번역 관련 명령어', inline=False)
            await message.channel.send("여깄습니다!")
            await message.channel.send(embed = embed)


        #학교 급식 알림     (급식 데이터 받아오기)
        if message.content.split(" ")[1] == "급식":
            if message.content.split(" ")[2] == "명령어":
                embed = discord.Embed(title="급식 명령어", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x62c1cc)
                embed.add_field(name='연초고',value='오늘의 연초고 급식' , inline=False)
                embed.add_field(name='해성고',value='오늘의 해성고 급식' , inline=False)
                await message.channel.send(embed = embed)
            
            #연초고
            if message.content.split(" ")[2] == "연초고":
                html = 'http://yeoncho-h.gne.go.kr/yeoncho-h/main.do#'
                response = urlopen(html.format(num=1, key_word=urllib.parse.quote('급식')))
                soup = BeautifulSoup(response, "html.parser")
                tmps = soup.select('.meal_list')
                for tmp in tmps:
                    await message.channel.send(tmp.get_text())
            
            #해성고
            if message.content.split(" ")[2] == "해성고":
                html = 'http://haeseong-h.gne.go.kr/haeseong-h/main.do'
                response = urlopen(html.format(num=1, key_word=urllib.parse.quote('급식')))
                soup = BeautifulSoup(response, "html.parser")
                tmps = soup.select('.meal_list')
                for tmp in tmps:
                    await message.channel.send(tmp.get_text())


        #번역기            (구글 번역데이터 가져오기) (번역 명령어 임베드 만들기)
        if message.content.split(" ")[1] == "번역":
            if message.content.split(" ")[2] == "명령어":
                embed = discord.Embed(title="번역 명령어", description="",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x62c1cc)
                embed.add_field(name='',value='', inline=False)
                await message.channel.send(embed = embed)
    
    
    #관리자 명령어
    if message.content.split(" ")[0] == "이나야":
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

    if message.content == "야~":
        await message.channel.send("기분 좋다!")


client.run(token)
