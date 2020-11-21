import discord
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import asyncio
from discord import Embed, Emoji
from discord.utils import get
from discord.ext import commands
import os


class chatbot(discord.Client):
   
    async def on_ready(self):
        game = discord.Game("빡대가리라 공부")
        await client.change_presence(status=discord.Status.online, activity=game)
        print("READY")


    async def on_message(self, message):
        if message.author.bot:
            return None






        if message.content == "!시간":
            channel = message.channel
            await channel.send(time.strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))
            
        if message.content == "!이승환":
            channel = message.channel
            
            await ctx.channel.purge(limit=amount)
            await channel.send("저는 고아입니다... 때리지 마세요")

      
            
     




       
            
        if message.content.startswith("!명령어"):
            embed=discord.Embed(title="명령어 모음", description="명령해.", color=0x00ff56)
            embed.add_field(name="!시간",value='현재시간을 알려줍니다', inline=False)
            embed.add_field(name='!날씨', value='Ex) !날씨 대전복수동', inline=False)
            embed.add_field(name='!롤', value='Ex) !롤 닉네임', inline=False)
            embed.add_field(name='!추천트리', value='각 클래스별 추천트리를 알려줌', inline=False)
            embed.add_field(name='!(클래스명)', value='!소드맨, 아처, 위저드, 클레릭, 스카우트 등 상세트리를 알려줍니다', inline=False)
            await message.channel.send(embed=embed)
            
        if message.content.startswith("!추천트리"):
            embed=discord.Embed(title="소드맨", description="매화검수", color=0x00ff56)
            embed.set_thumbnail(url="https://upload3.inven.co.kr/upload/2020/06/20/bbs/i014051449493.gif")
            embed.add_field(name="도펠죌트너 + 매화검수 트리 : 양손검을 주력으로 사용하는 검사",value='http://www.inven.co.kr/board/tos/4604/1895', inline=False)
            await message.channel.send(embed=embed)
            embed=discord.Embed(title="아처", description="메르겐+레인저", color=0x00ff56)
            embed.set_thumbnail(url="https://optimal.inven.co.kr/upload/2019/06/19/bbs/i15603777360.gif")
            embed.add_field(name="메르겐 + 레인저 트리 : 다양하고 강력한 활 스킬을 주력으로 사냥하는 양손활 궁수",value='http://www.inven.co.kr/board/tos/4604/1870', inline=False)
            await message.channel.send(embed=embed)
            embed=discord.Embed(title="위저드", description="모두 준수한 성능", color=0x00ff56)
            embed.set_thumbnail(url="https://optimal.inven.co.kr/upload/2019/06/19/bbs/i16310187018.gif")
            embed.add_field(name="모두 준수한 성능 [섀도우 제외]",value='http://www.inven.co.kr/board/tos/4197/79587', inline=False)
            await message.channel.send(embed=embed)
            embed=discord.Embed(title="클레릭", description="하는 사람 Good", color=0x00ff56)
            embed.set_thumbnail(url="https://optimal.inven.co.kr/upload/2019/06/13/bbs/i15563194980.gif")
            embed.add_field(name="그냥 힐러, 몸빵",value='http://www.inven.co.kr/board/tos/4198/60840', inline=False)
            await message.channel.send(embed=embed)
            



            

        if message.content.startswith('!롤'):
            channel = message.channel
            try:
                name = message.content[3:len(message.content)]
                op = requests.get("https://www.op.gg/summoner/userName="+name)
                source = op.text
                op1 = BeautifulSoup(op.content,"html.parser")
                rank = op1.find_all("div", {"class":"TierRank"})
                lp = op1.find_all("span", {"class":"LeaguePoints"})
                wins = op1.find_all("span", {"class":"wins"})
                lossee = op1.find_all("span", {"class":"losses"})
                winratio = op1.find_all("span", {"class":"winratio"})
                most = op1.find_all("div", {"class":"ChampionName"})
                lol = '티어: '+rank[0].text+'\n점수: '+lp[0].text.strip()+'\n승: '+wins[0].text+'\n패: '+lossee[0].text+'\n승률: '+winratio[0].text[10:]
                embed=discord.Embed(title="롤 전적 검색", description=name, color=0x00ff56)
                embed.set_thumbnail(url="https://opgg-static.akamaized.net/images/medals/"+rank[0].text[:-2]+"_"+rank[0].text[-1:]+".png?image=q_auto&v=1")
                embed.add_field(name="티어",value=rank[0].text, inline=False)
                
                embed.add_field(name="점수",value=lp[0].text.strip(), inline=False)
                
                embed.add_field(name="승 \\ 패 \\ 승률",value=wins[0].text+" \a " +lossee[0].text+ " \a " + winratio[0].text[10:], inline=False)
                embed.add_field(name="most champions 3",value="a", inline=False)
                
                await message.channel.send(embed=embed)
            except:
                await channel.send("소환사 닉네임이 없습니다")

                               

                


                
        if message.content.startswith('!날씨'):
            channel = message.channel
            try:
                te = message.content[4:len(message.content)]
                op = requests.get("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="+te+"날씨")
                source = op.text
                op1 = BeautifulSoup(op.content,"html.parser")
                a = op1.find_all("span", {"class":"todaytemp"})
                b = op1.find_all("span", {"class":"min"})
                c = op1.find_all("span", {"class":"max"})
                d = op1.find_all("span", {"class":"sensible"})
                ee = op1.find_all("p", {"class":"cast_txt"})
                embed=discord.Embed(title="날씨 검색", description=te, color=0xffffff)
                embed.set_thumbnail(url="https://lh3.googleusercontent.com/yhywHEAGpOOVNNrk2-cFYo-MBaPE4_77wKVs-a0440ROFDZteEhdeP4wn8ZeOBrPP7_c=w300")
                embed.add_field(name="현재 온도",value=a[0].text+"℃", inline=True)
                embed.add_field(name="날씨",value=ee[0].text, inline=False)
                embed.add_field(name="최저 온도",value=b[0].text, inline=True)
                embed.add_field(name="최고 온도",value=c[0].text, inline=True)
                embed.add_field(name="체감 온도",value=d[0].text[4:], inline=True)
                await message.channel.send(embed=embed)

            except:
                await channel.send("지역명 똑디 입력해")
                
        

        if message.content.startswith('!메이플'):
            channel = message.channel
            try:
                name = message.content[5:len(message.content)]
                op = requests.get("https://maple.gg/u/"+name)
                source = op.text
                op1 = BeautifulSoup(op.content,"html.parser")
                a = op1.find_all("div", {"class":"col-lg-2 col-md-4 col-sm-4 col-6 mt-3"})
                imgr = op1.find_all("meta", {"property":"og:image"})
                imgg = str(imgr)[16:-23]
                world =a[2].text.strip()[8:-1] + a[3].text.strip()[8:-1]
                
                embed=discord.Embed(title="메이플 검색", description=name, color=0x00ff56)
                embed.set_thumbnail(url="https://avatar.maplestory.nexon.com/Character/ADAIIGNLAIDMGLAKMGELJEPKICPPJIKDBHNJADJBAOOIJLGKMPEPLPLGKJLHLEJDKHODDABNJGHICDALMALHPFDOGOPMLLDIOINCLKPIDBOKODAABJEMJLHOAIGEOKKJNOHLFPFNKFFPEMPAOJEHLPACGMCLKPDKICMPAOJGKNHHBLKJAHBNAEEECHHKGCOIJCNHJLBHAPBKCOIJHDFHPLCKLMGFLKKMHPHFPAKJNLOJCENDJCEHACGMPOOBAJKK")
                embed.add_field(name=a[0].text.strip()[:4],value=a[0].text.strip()[4:-1]+"위", inline=True)
                embed.add_field(name=a[1].text.strip()[:4],value=a[1].text.strip()[5:-1]+"위", inline=True)
                
                embed.add_field(name=a[2].text.strip()[:4]+"(월드) / (전체)",value="(월드) "+world.splitlines()[1]+"위" + " / (전체) "+world.splitlines()[2]+"위", inline=False)
                
                
                await message.channel.send(embed=embed)
            except:
                await channel.send("소환사 닉네임이 없습니다")


                       






access_token = os.environ['BOT_TOKEN']
if __name__ == "__main__":
    client = chatbot()
    client.run(access_token)
