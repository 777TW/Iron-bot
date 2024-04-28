import discord
from discord.ext import commands
intents = discord.Intents.all()
intents.members = True
import json
import random
import datetime
import os
dirname = os.path.dirname(__file__).replace('\categories', '')

class react(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,msg):
        with open(r'{}\json\settings.json'.format(dirname),'r', encoding='utf8') as jfile:
            jdata = json.load(jfile)

        random_good = random.choice(jdata['goodmsg'])
        random_goodmentioned = random.choice(jdata['goodmsgmentioned'])
        if "好嗎" in msg.content and self.bot.user.mentioned_in(msg):
            await msg.channel.send(random_goodmentioned)
        elif "好嗎" in msg.content:
            await msg.channel.send(random_good)

        random_yes = random.choice(jdata['yesmsg'])
        random_yesmentioned = random.choice(jdata['yesmsgmentioned'])
        if "是嗎" in msg.content and self.bot.user.mentioned_in(msg):
            await msg.channel.send(random_yesmentioned)
        elif "是嗎" in msg.content:
            await msg.channel.send(random_yes)

        random_yess = random.choice(jdata['yessmsg'])
        random_yessmentioned = random.choice(jdata['yessmsgmentioned'])
        if "對嗎" in msg.content and self.bot.user.mentioned_in(msg):
            await msg.channel.send(random_yessmentioned)
        elif "對嗎" in msg.content:
            await msg.channel.send(random_yess)
          
        random_want = random.choice(jdata['wantmsg'])
        random_wantmentioned = random.choice(jdata['wantmsgmentioned'])
        if "要嗎" in msg.content and self.bot.user.mentioned_in(msg):
            await msg.channel.send(random_wantmentioned)
        elif "要嗎" in msg.content:
            await msg.channel.send(random_want)

        
        random_play = random.choice(jdata['playmsg'])
        random_playmentioned = random.choice(jdata['playmsgmentioned'])
        if ("來玩" in msg.content or "玩嗎" in msg.content or "玩ㄇ" in msg.content or "玩?" in msg.content) and self.bot.user.mentioned_in(msg):
            await msg.channel.send(random_playmentioned) 
        elif "來玩" in msg.content or "玩嗎" in msg.content or "玩ㄇ" in msg.content or "玩?" in msg.content:
            await msg.channel.send(random_play)


        random_whatmsgmentioned = random.choice(jdata['whatmsgmentioned'])
        if ("是什麼" in msg.content or "什麼是" in msg.content) and self.bot.user.mentioned_in(msg):
            await msg.channel.send(random_whatmsgmentioned + "\nhttps://www.google.com/" )
      

        random_ha = random.choice(jdata['HaMsg'])
        random_haha = random.choice(jdata['HaMsg2'])
        if random_ha in msg.content and msg.author != self.bot.user:
            await msg.channel.send(random_haha)
      
        if "現在幾點" in msg.content:
            time = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
            await msg.channel.send("現在時刻是： %4d年%02d月%02d日 %02d:%02d" %(time.year, time.month, time.day, time.hour, time.minute))

        random_hello = random.choice(jdata['hello'])
        random_hello_mentioned = random.choice(jdata['hellomentioned'])
        if ("早安" in msg.content or "午安" in msg.content or "晚安" in msg.content) and self.bot.user.mentioned_in(msg):
            await msg.channel.send(random_hello_mentioned)
        elif ("早安" in msg.content or "午安" in msg.content or "晚安" in msg.content) and msg.author != self.bot.user:
            await msg.channel.send(random_hello)

            

        if "菜" in msg.content:
            await msg.add_reaction("🥬")


        if "<@843678537511731220>" in msg.content:
            await msg.add_reaction("<:emoji_18:860847360065798184>")


        randnojio = random.choice(jdata['nojio'])
        randnojio_mentioned = random.choice(jdata['nojiomentioned'])

        if "不揪" in msg.content and self.bot.user.mentioned_in(msg):
            await msg.channel.send(randnojio_mentioned)
            
        elif "不揪" in msg.content and msg.author != self.bot.user:
            await msg.channel.send(randnojio)

async def setup(bot: commands.Bot):
    await bot.add_cog(react(bot))
