import discord
intents = discord.Intents.all()
intents.members = True
from discord.ext import commands
from datetime import datetime, timedelta, timezone
from discord import app_commands

class help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name = "help", description = "想要詳細的了解指令可以看這裡喔~")
    @app_commands.describe(command = "你想了解的指令")
    @app_commands.choices(command = [
        app_commands.Choice(name = "ping", value = "ping"),
        app_commands.Choice(name = "magic", value = "magic"),
        app_commands.Choice(name = "roll", value = "roll"),
        app_commands.Choice(name = "choose", value = "choose"),
        app_commands.Choice(name = "weather", value = "weather"),
        app_commands.Choice(name = "fish", value = "fish"),
        app_commands.Choice(name = "map", value = "map"),
        app_commands.Choice(name = "weapon", value = "weapon"),
        app_commands.Choice(name = "agent", value = "agent"),
        app_commands.Choice(name = "split_vc", value = "split_vc"),
        app_commands.Choice(name = "pokemon", value = "pokemon")
    ])
    async def help(self, interaction: discord.Interaction, command: app_commands.Choice[str]):
        if command.name == "ping":
            embed=discord.Embed(title="ping", description="就...可以看到魔鋼鐵是不是很快", color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            embed.set_author(name="魔鋼鐵幫助你", icon_url="https://cdn.discordapp.com/avatars/1118424692680822835/3959c868c9f614bb50e64c771b0c63bb.png?size=512")
            await interaction.response.send_message(embed=embed)
          
        elif command.name == "magic":
            embed=discord.Embed(title="magic", description="魔鋼鐵可是有名的魔術師呢! 還不趕快來看魔術嗎?", color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            embed.set_author(name="魔鋼鐵幫助你", icon_url="https://cdn.discordapp.com/avatars/1118424692680822835/3959c868c9f614bb50e64c771b0c63bb.png?size=512")
            await interaction.response.send_message(embed=embed)

        elif command.name == "roll":
            embed=discord.Embed(title="roll", description="還在困擾要選甚麼數字嗎? 魔鋼鐵幫你選!\n使用 /roll 來獲得其中隨機的一個數字吧字吧!", color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            embed.set_author(name="魔鋼鐵幫助你", icon_url="https://cdn.discordapp.com/avatars/1118424692680822835/3959c868c9f614bb50e64c771b0c63bb.png?size=512")
            await interaction.response.send_message(embed=embed)

        elif command.name == "weather":
            embed=discord.Embed(title="weather", description="魔鋼鐵在氣象方面也是略懂略懂，使用 /weather 來查詢今天的天氣吧！", color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            embed.set_author(name="魔鋼鐵幫助你", icon_url="https://cdn.discordapp.com/avatars/1118424692680822835/3959c868c9f614bb50e64c771b0c63bb.png?size=512")
            await interaction.response.send_message(embed=embed)

        elif command.name == "fish":
            embed=discord.Embed(title="fish", description="魔鋼鐵養了一些魚... 不要把他們都釣走阿", color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            embed.set_author(name="魔鋼鐵幫助你", icon_url="https://cdn.discordapp.com/avatars/1118424692680822835/3959c868c9f614bb50e64c771b0c63bb.png?size=512")
            await interaction.response.send_message(embed=embed)

        elif command.name == "map":
            embed=discord.Embed(title="map", description="每次打特戰自訂都無法決定要打甚麼圖嗎? 做決定這件事我最在行了! 盡管用這個指令吧", color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            embed.set_author(name="魔鋼鐵幫助你", icon_url="https://cdn.discordapp.com/avatars/1118424692680822835/3959c868c9f614bb50e64c771b0c63bb.png?size=512")
            await interaction.response.send_message(embed=embed)

        elif command.name == "weapon":
            embed=discord.Embed(title="weapon", description="甚麼!? 你打特戰的時候連要用甚麼槍都不知道!?? 好啦好啦 交給我決定", color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            embed.set_author(name="魔鋼鐵幫助你", icon_url="https://cdn.discordapp.com/avatars/1118424692680822835/3959c868c9f614bb50e64c771b0c63bb.png?size=512")
            await interaction.response.send_message(embed=embed)

        elif command.name == "agent":
            embed=discord.Embed(title="agent", description="角色都玩膩了不知道要玩誰?讓我給你一些挑戰吧!", color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            embed.set_author(name="魔鋼鐵幫助你", icon_url="https://cdn.discordapp.com/avatars/1118424692680822835/3959c868c9f614bb50e64c771b0c63bb.png?size=512")
            await interaction.response.send_message(embed=embed)

        elif command.name == "choose":
            embed=discord.Embed(title="choose", description="選擇困難的話可以試試看....", color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            embed.set_author(name="魔鋼鐵幫助你", icon_url="https://cdn.discordapp.com/avatars/1118424692680822835/3959c868c9f614bb50e64c771b0c63bb.png?size=512")
            await interaction.response.send_message(embed=embed)

        elif command.name == "split_vc":
            embed=discord.Embed(title="split_vc", description="打自訂可以分隊喔", color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            embed.set_author(name="魔鋼鐵幫助你", icon_url="https://cdn.discordapp.com/avatars/1118424692680822835/3959c868c9f614bb50e64c771b0c63bb.png?size=512")
            await interaction.response.send_message(embed=embed)
        
        elif command.name == "pokemon":
            embed=discord.Embed(title="pokemon", description="查詢寶可夢基本資料", color=0x0040ff,timestamp=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8))))
            embed.set_author(name="魔鋼鐵幫助你", icon_url="https://cdn.discordapp.com/avatars/1118424692680822835/3959c868c9f614bb50e64c771b0c63bb.png?size=512")
            await interaction.response.send_message(embed=embed)
    

async def setup(bot: commands.Bot):
    await bot.add_cog(help(bot))