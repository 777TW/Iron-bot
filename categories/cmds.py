import discord
from discord.ext import commands
import json
import random
import asyncio
import requests
from discord import app_commands
from datetime import datetime, timedelta, timezone
from discord.ui import Button, View
intents = discord.Intents.all()
intents.members = True
import os
dirname = os.path.dirname(__file__).replace('\categories', '')


with open(r'{}\json\settings.json'.format(dirname), 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class cmds(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f'Synced {len(fmt)} commands')


    @app_commands.command(name = "ping", description = "查詢魔鋼鐵的延遲")
    async def ping(self, interaction = discord.Interaction):
        await interaction.response.send_message(f'{round(self.bot.latency*1000)}ms')


    @app_commands.command(name = "magic", description = "看磨鋼鐵變魔術")
    async def magic(self, interaction: discord.Interaction):
        bookpic = discord.File(r"{}\files\book.jpg".format(dirname))
        await interaction.response.send_message("想看我變魔術嗎? 看好囉")
        await asyncio.sleep(1)
        await interaction.channel.send("這是一疊書")
        tmpmsg = await interaction.channel.send(file=bookpic)
        await asyncio.sleep(1)
        await interaction.channel.send("3...")
        await asyncio.sleep(1)
        await interaction.channel.send("2...")
        await asyncio.sleep(1)
        await interaction.channel.send("1...")
        await asyncio.sleep(1)
        await tmpmsg.delete()
        await interaction.channel.send("bang 不見~")
        await interaction.channel.send("厲害吧")

    
    @app_commands.command(name = "roll", description = "隨機選取範圍內的數字")
    @app_commands.describe(min = "要隨機的最小數字", max = "要隨機的最大數字")
    async def roll(self, interaction: discord.Interaction, min: int, max: int):
        number = random.randint(min, max)
        await interaction.response.send_message(number)

    
    @app_commands.command(name = "choose", description = "幫助你解決選擇困難")
    @app_commands.describe(things = "用空白隔開就可以喔~")
    async def choose(self, interaction: discord.Interaction, *, things: str):
        list = things.split( )
        thing = random.choice(list)
        await interaction.response.send_message(thing)

    
    @app_commands.command(name = "fish", description = "可以釣魚(?")
    async def fish(self, interaction: discord.Interaction):
        fish = random.choice(jdata['fish'])
        await interaction.response.send_message("你釣到了" + fish)

    
    @app_commands.command(name = "weather", description = "查看天氣")
    @app_commands.describe(city = "你要查詢的城市")
    @app_commands.choices(city=[
        app_commands.Choice(name = "臺北市", value = "Taipei City"),
        app_commands.Choice(name = "新北市", value = "New Taipei City"),
        app_commands.Choice(name = "基隆市", value = "Keelung City"),
        app_commands.Choice(name = "桃園市", value = "Taoyuan City"),
        app_commands.Choice(name = "新竹市", value = "Hsinchu City"),
        app_commands.Choice(name = "新竹縣", value = "Hsinchu County"),
        app_commands.Choice(name = "苗栗縣", value = "Miaoli County"),
        app_commands.Choice(name = "臺中市", value = "Taichung City"),
        app_commands.Choice(name = "彰化縣", value = "Changhua County"),
        app_commands.Choice(name = "南投縣", value = "Nantou County"),
        app_commands.Choice(name = "雲林縣", value = "Yunlin County"),
        app_commands.Choice(name = "嘉義縣", value = "Chiayi County"),
        app_commands.Choice(name = "嘉義市", value = "Chiayi City"),
        app_commands.Choice(name = "臺南市", value = "Tainan City"),
        app_commands.Choice(name = "高雄市", value = "Kaohsiung City"),
        app_commands.Choice(name = "屏東縣", value = "Pingtung County"),
        app_commands.Choice(name = "宜蘭縣", value = "Yilan County"),
        app_commands.Choice(name = "花蓮縣", value = "Hualien County"),
        app_commands.Choice(name = "臺東線", value = "Taitung County")
    ])
    async def weather(self, interaction: discord.Interaction, city: app_commands.Choice[str]):
        url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-40E1BDC5-2AB9-4DD6-B68C-4B525CF72906"
        data = requests.get(url)
        data_json = data.json()
        location = data_json['records']['location']
        for i in location:
            icity = i['locationName'] 
            wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']  
            maxt8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName'] 
            mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName'] 
            pop8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName'] 

            if city.name == icity:
                await interaction.response.send_message(f'{city.name}未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %')

    
    @app_commands.command(name = "map", description = "瓦羅蘭打自訂的時候不知道要選甚麼圖? 魔鋼鐵幫你決定")
    async def map(self, interaction: discord.Interaction):
        map = random.choice(jdata['valomap'])
        await interaction.response.send_message(map)

    
    @app_commands.command(name = "agent", description = "打瓦羅蘭不知道要用甚麼角色嗎? 魔鋼鐵幫你選")
    async def agent(self, interaction: discord.Interaction):
        agent = random.choice(jdata['valoagent'])
        await interaction.response.send_message(agent)

    
    @app_commands.command(name = "weapon", description = "打瓦羅蘭連要用甚麼武器不知道!?? 沒關係，魔鋼鐵也能幫你決定")
    async def weapon(self, interaction: discord.Interaction):
        weapon = random.choice(jdata['valoweapon'])
        await interaction.response.send_message(weapon)

    
    @app_commands.command(name = "add_counter", description = "創建一個計數器")
    @app_commands.describe(name = "計數器名字")
    async def add_counter(self, interaction: discord.Interaction, *, name: str):
        with open(r'{}\json\counter.json'.format(dirname), 'r', encoding = 'utf8') as jcounter_read:
            jcounter_loaded = json.load(jcounter_read)
        with open(r'{}\json\counter.json'.format(dirname), 'w', encoding = 'utf8') as jcounter_write:
            jcounter_loaded.append({"user_id": interaction.user.id, "name": name, "count": 0})
            json.dump(jcounter_loaded, jcounter_write)
        await interaction.response.send_message("已經成功新增計數器啦! 使用/counter 開始計數吧")

    
    @app_commands.command(name = "delete_counter", description = "刪除不要的計數器")
    @app_commands.describe(number = "要刪除的編號")
    async def delete_counter(self, interaction: discord.Interaction, number: int):
        user_id = interaction.user.id
        counter_list = []
        with open(r'{}\json\counter.json'.format(dirname), 'r', encoding = 'utf8') as jcounter_find_read:
            jcounter_find_loaded = json.load(jcounter_find_read)
        for data in jcounter_find_loaded:
            if int(data['user_id']) == int(user_id):
                counter_list.append(data)
        if str(counter_list) == "[]":
            await interaction.response.send_message("你沒有計數器喔~")
        else:
            for i, data in enumerate(counter_list):
                if int(i)+1 == int(number):
                    erase_counter = data
                    break
                if int(i)+1 == len(counter_list):
                    await interaction.response.send_message("輸入的數字不正確")
            text = ""
            num = 1
            for i, data in enumerate(counter_list):
                if data == erase_counter:
                    jcounter_find_loaded.pop(i)
                    with open(r'{}\json\counter.json'.format(dirname), 'w', encoding = 'utf8') as jcounter_find_write:
                        json.dump(jcounter_find_loaded, jcounter_find_write)
                        await interaction.response.send_message(f'成功幫你移除第{number}項啦')
                else:
                    text = text + (f'**{data["name"]}:** {data["count"]}次\n')
                    num += 1
            if text == "":
                text = "計數器列表空空如也...."
            title = (f'{interaction.user.name}的計數器列表')
            embed = discord.Embed(title = title, description = text,color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            await interaction.channel.send(embed = embed)

    
    @app_commands.command(name = "counter_list", description = "顯示你的計數器列表")
    async def counter_list(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        counter_list = []
        with open(r'{}\json\counter.json'.format(dirname), 'r', encoding = 'utf8') as jcounter_list_read:
            jcounter_list_loaded = json.load(jcounter_list_read)
        for data in jcounter_list_loaded:
            if int(data['user_id']) == int(user_id):
                counter_list.append(data)
        if str(counter_list) == "[]":
            await interaction.response.send_message("你沒有計數器喔~")
        else:
            text = ""
            num = 1
            for data in counter_list:
                text = text + (f'**{data["name"]}:** {data["count"]}次\n')
                num += 1
            title = (f'{interaction.user.name}的計數器列表')
            embed = discord.Embed(title = title, description = text,color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            await interaction.response.send_message("這是你的計數器列表")
            await interaction.channel.send(embed = embed)

    
    @app_commands.command(name = "counter", description = "叫出你的計數器")
    @app_commands.describe(number = "你要叫出都計數器編號")
    async def counter(self, interaction: discord.Interaction, number: int):
        button_plus = Button(label = "+1", style = discord.ButtonStyle.success)
        button_minus = Button(label = "-1", style = discord.ButtonStyle.danger)
        async def button_callback_plus(interaction):
            with open(r'{}\json\counter.json'.format(dirname), "r") as jcounter_edit_read:
                jcounter_edit_loaded = json.load(jcounter_edit_read)
            for data in jcounter_edit_loaded:
                if data['user_id'] == interaction.user.id and data['name'] == title:
                    data['count'] = int(data['count']) + 1
                    new_count = data['count']
            with open(r'{}\json\counter.json'.format(dirname), "w") as jcounter_edit_write:
                json.dump(jcounter_edit_loaded, jcounter_edit_write)
            new_embed = discord.Embed(title = title, description = new_count,color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            await interaction.response.edit_message(embed = new_embed)
        async def button_callback_minus(interaction):
            with open(r'{}\json\counter.json'.format(dirname), "r") as jcounter_edit_read:
                jcounter_edit_loaded = json.load(jcounter_edit_read)
            for data in jcounter_edit_loaded:
                if data['user_id'] == interaction.user.id and data['name'] == title:
                    data['count'] = int(data['count']) - 1
                    new_count = data['count']
            with open(r'{}\json\counter.json'.format(dirname), "w") as jcounter_edit_write:
                json.dump(jcounter_edit_loaded, jcounter_edit_write)
            new_embed = discord.Embed(title = title, description = new_count,color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            await interaction.response.edit_message(embed = new_embed)
        button_plus.callback = button_callback_plus
        button_minus.callback = button_callback_minus
        view = View()
        view.add_item(button_plus)
        view.add_item(button_minus)
        user_id = interaction.user.id
        counter_list = []
        with open(r'{}\json\counter.json'.format(dirname), 'r', encoding = 'utf8') as jcounter_list_read:
            jcounter_list_loaded = json.load(jcounter_list_read)
        for data in jcounter_list_loaded:
            if int(data['user_id']) == int(user_id):
                counter_list.append(data)
        if str(counter_list) == "[]":
            await interaction.response.send_message("你沒有計數器喔~")
        else:
            title = counter_list[number-1]['name']
            count = counter_list[number-1]['count']
            embed = discord.Embed(title = title, description = count,color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            await interaction.response.send_message(embed = embed, view = view)

    
    @app_commands.command(name = "split_vc", description = "分隊囉")
    @app_commands.describe(channel = "你要查詢的語音頻道", channel_2 = "你要分到的語音頻道")
    async def split_vc(self, interaction: discord.Interaction, channel: discord.VoiceChannel, channel_2: discord.VoiceChannel):
        member_list = []
        for member in channel.members:
            member_list.append(member)
        if str(member_list) == "[]":
            await interaction.response.send_message("這個語音頻道沒有人在")
        else:
            random.shuffle(member_list)
            team_B = member_list[len(member_list)//2:]
            for i in team_B:
                await i.move_to(channel_2)
            await interaction.response.send_message("分隊成功")


async def setup(bot: commands.Bot):
    await bot.add_cog(cmds(bot))
