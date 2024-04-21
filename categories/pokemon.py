import discord
intents = discord.Intents.all()
intents.members = True
from discord.ext import commands
from discord import app_commands
import requests
from bs4 import BeautifulSoup
from opencc import OpenCC
import random
import os
from PIL import Image, ImageDraw, ImageFont
import io
dirname = os.path.dirname(__file__)

class pokemon(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name = 'pokemon', description = '查詢寶可夢的基本資料')
    @app_commands.describe(pokemon = "寶可夢名稱(中文)")
    async def pokemon(self, interaction: discord.Interaction, pokemon: str):
        cc = OpenCC('s2tw')
        cc2 = OpenCC('tw2s')
        await interaction.response.send_message("正在為你查詢" + pokemon + "的資料...")
        url = "https://wiki.52poke.com/wiki/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89"
        r_data = requests.get(url)
        soup = BeautifulSoup(r_data.text, 'html.parser')
        s_data = soup.select('td.rdexn-name a')
        for i in range(len(s_data)):
            if cc.convert(s_data[i-1].text) == cc.convert(pokemon):
                a = i

        try:
            p_data = requests.get('https://wiki.52poke.com/' + s_data[a-1]['href'])
        except:
            await interaction.channel.send("沒有找到ㄟ... 你打錯字?")
        soupp = BeautifulSoup(p_data.text, 'html.parser')




        #種族值
        hp = soupp.select('tr.bgl-HP th')[0].text[3:] #HP種族值
        attack = soupp.select('tr.bgl-攻击 th')[0].text[3:] #攻擊種族值
        defense = soupp.select('tr.bgl-防御 th')[0].text[3:] #防禦種族值
        s_attack = soupp.select('tr.bgl-特攻 th')[0].text[3:] #特攻種族值
        s_defense = soupp.select('tr.bgl-特防 th')[0].text[3:] #特防種族值
        speed = soupp.select('tr.bgl-速度 th')[0].text[3:] #速度種族值
        total = int(hp) + int(attack) + int(defense) + int(s_attack) + int(s_defense) + int(speed)

        ss_text = "H P:  " + hp + "攻擊: " + attack + "防禦: " + defense + "特攻: " + s_attack + "特防: " + s_defense + "速度: " + speed + "總和: " + str(total) #種族值全




        #編號
        number = soupp.select('th', class_ = 'roundy bd-草 textblack bgwhite')[1].text #寶可夢編號




        #屬性
        two_attribute = True
        attribute_all = ['一般', '格斗', '飞行', '毒', '地面', '岩石', '虫', '幽灵', '钢', '火', '水', '草', '电', '超能力', '冰', '龙', '惡', '妖精',
                         '一般', '格鬥', '飛行', '毒', '地面', '岩石', '蟲', '幽靈', '鋼', '火', '水', '草', '電', '超能力', '冰', '龍', '惡', '妖精']
        for i in attribute_all:
            class_name = 'roundy b-' + i + ' bw-1'
            class_name_2 = 'roundy bl-' + i + ' bw-1'
            attribute = soupp.find_all('td', class_ = class_name)
            if attribute == []:
                attribute = soupp.find_all('td', class_ = class_name_2)
                if attribute != []:
                    attribute_one = i
                    classs = class_name_2
                    two_attribute = False
                    break
            else:
                attribute_one = i
                classs = class_name
                break 


        attribute_v = [] #寶可夢屬性

        if cc.convert(attribute[0].text.replace(attribute_one, '').replace('\n', '')) != '':
            attribute_v.append(cc.convert(attribute[0].text.replace(attribute_one, '').replace('\n', '')))

        attribute_v.append(cc.convert(attribute_one))




        #特性
        special_v = [] #寶可夢特性

        special = soupp.find_all('td', classs)
        i = 1
        while True:
            if '隱藏特性' in special[i].text:
                special_v.append(cc.convert('(' + special[i].text.replace('\n', '')).replace('隱藏特性', ')'))
                break
            elif '隱藏特性' not in special[2].text and '隱藏特性' not in special[3].text:
                special_v.append(cc.convert(special[i].text.replace('\n', '')))
                break
            else:
                temp_v = special[i].text.replace('\n', '').split('\xa0或 ')
                for j in range(len(temp_v)):
                    special_v.append(cc.convert(temp_v[j]))

            i += 1

        special_text = '' #寶可夢特性 字串
        for i in special_v:
            special_text = special_text + i + "\n"





        #捕獲率
        catch_rate = soupp.find_all('td', classs)
        for i in catch_rate:
            if "普通的精灵球在满体力下的捕获率" in str(i):
                data = i.text
                break

        catch_rate_int = float(data.split('（')[1].split('）')[0][:-1])
        if catch_rate_int <= 10:
            catch_rate_text = str(('%.2f'%catch_rate_int)) + "%" #捕獲率文字
        else:
            catch_rate_text = str(catch_rate_int) + "%"




        #小知識
        quote_v = [] #小知識庫
        quote = []
        ct = 0
        fail = False
        while quote == []:
            if two_attribute:
                classss = 'at-l roundy b-' + attribute_one
            else:
                classss = 'at-l roundy bd-' + attribute_one
            if ct%2 == 0:
                attribute_one = cc.convert(attribute_one)
            elif ct%2 == 1:
                attribute_one = cc2.convert(attribute_one)  
            quote = soupp.find_all('td', classss)
            ct += 1
            if ct > 10:
                quote = ['他...很強 (絕對不是機器人壞掉)']
                fail = True
                break

        if fail:
            quote_v.append(quote[0])
        else:
            for i in quote:
                if '{' not in i.text:
                    quote_v.append(i.text.replace('\n', '').replace('*', ''))

        random_quote = '' #隨機小知識
        while random_quote == '':
            random_quote = cc.convert(random.choice(quote_v))
            
        await interaction.channel.send("魔鋼鐵已經克服重重難關 就快要偷到資料了...")




        #圖片
        picture = str(soupp.select('a.image')[0]).split(" ")
        for i in picture:
            if 'data-url' in i:
                pic_url = 'https:' + i[10:-1]


        os.chdir(r'{}\pokemon picture'.format(dirname))
        imageFile = requests.get(pic_url)
        f = open(r'{}\pokemon picture\{}'.format(dirname, number.replace("\n", "") + '.png'), 'wb')
        f.write(imageFile.content)
        f.close()


        # print(pokemon, number)
        # print("種族值")
        # print(ss_text, "\n")
        # print("屬性:")
        # for i in attribute_v:
        #     print(i, end = " ")
        # print("\n")
        # print("特性:")
        # print(special_text)
        # print("捕獲率:",catch_rate_text)
        # print(random_quote[:22] + "\n" + random_quote[22:])
        # print(pic_url)

        num_int = int(number[1:].replace("\n", ""))
        if num_int <= 151:
            no = "1"
        elif num_int <= 251:
            no = "2"
        elif num_int <= 386:
            no = "3"
        elif num_int <= 493:
            no = "4"
        elif num_int <= 649:
            no = "5"
        elif num_int <= 721:
            no = "6"
        elif num_int <= 809:
            no = "7"
        elif num_int <= 905:
            no = "8"
        else:
            no = "9"
                
        image = Image.open(r"{}\background picture\{}.png".format(dirname, no))
        image = image.convert("RGBA")
        x,y = image.size
        for i in range(x):
            for j in range(y):
                color = image.getpixel((i,j))
                color = color[:-1] + (100, )
                image.putpixel((i,j), color)
        image = image.resize((800, 600))

        image2 = Image.open(r'{}\pokemon picture\{}'.format(dirname, number.replace("\n", "") + '.png'))
        image2 = image2.resize((200, 200))

        image.paste(image2, box = (30, 0), mask = image2)

        white = (255, 255, 255)
        grass_green = (11, 218, 81)
        poison_purple = (224, 176, 255)
        fight_orange = (255, 188, 55)
        ice_blue = (55, 255, 235)
        fly_blue = (64, 227, 252)
        ground_brown = (202, 94, 21)
        rock_brown = (209, 175, 152)
        bug_green = (173, 220, 156)
        ghost_purple = (192, 134, 230)
        steel_blue = (167, 194, 199)
        fire_red = (255, 125, 125)
        water_blue = (107, 167, 245)
        dragon_blue = (125, 134, 255)
        zap_yellow = (250, 246, 113)
        super_red = (255, 120, 196)
        bad_brown = (122, 110, 99)
        fairy_pink = (252, 161, 252)

        color_a = []
        for i in attribute_v:
            if i == "一般":
                color_a.append(white)
            elif i == "格鬥":
                color_a.append(fight_orange)
            elif i == "飛行":
                color_a.append(fly_blue)
            elif i == "毒":
                color_a.append(poison_purple)
            elif i == "地面":
                color_a.append(ground_brown)
            elif i == "岩石":
                color_a.append(rock_brown)
            elif i == "蟲":
                color_a.append(bug_green)
            elif i == "幽靈":
                color_a.append(ghost_purple)
            elif i == "鋼":
                color_a.append(steel_blue)
            elif i == "火":
                color_a.append(fire_red)
            elif i == "水":
                color_a.append(water_blue)
            elif i == "草":
                color_a.append(grass_green)
            elif i == "電":
                color_a.append(zap_yellow)
            elif i == "超能力":
                color_a.append(super_red)
            elif i == "冰":
                color_a.append(ice_blue)
            elif i == "龍":
                color_a.append(dragon_blue)
            elif i == "惡":
                color_a.append(bad_brown)
            elif i == "妖精":
                color_a.append(fairy_pink)

        one = [(380, 295)]
        two = [(360, 295)]
        three = [(340, 295)]
        one_one = [(320, 295), (450, 295)]
        one_two = [(320, 295), (430, 295)]
        one_three = [(320, 295), (390, 295)]
        two_one = [(300, 295), (450, 295)]
        two_two = [(300, 295), (430, 295)]
        two_three = [(300, 295), (390, 295)]
        three_two = [(290, 295), (430, 295)]

        if not two_attribute:
            if len(attribute_v[0]) == 1:
                pos = one
            elif len(attribute_v[0]) == 2:
                pos = two
            elif len(attribute_v[0]) == 3:
                pos = three
        else:
            if len(attribute_v[0]) == 1 and len(attribute_v[1]) == 1:
                pos = one_one
            elif len(attribute_v[0]) == 1 and len(attribute_v[1]) == 2:
                pos = one_two
            elif len(attribute_v[0]) == 1 and len(attribute_v[1]) == 3:
                pos = one_three
            elif len(attribute_v[0]) == 2 and len(attribute_v[1]) == 1:
                pos = two_one
            elif len(attribute_v[0]) == 2 and len(attribute_v[1]) == 2:
                pos = two_two
            elif len(attribute_v[0]) == 2 and len(attribute_v[1]) == 3:
                pos = two_three
            elif len(attribute_v[0]) == 3 and len(attribute_v[1]) == 2:
                pos = three_two


        draw = ImageDraw.Draw(image)
        font_type = r"{}\ChenYuluoyan-Thin.ttf".format(dirname)
        font = ImageFont.truetype(font_type, 100)
        draw.text((250, 50), pokemon + number, fill = white, font=font)

        draw.rectangle((30, 230, 260, 560), outline = white, width = 3)
        draw.rectangle((280, 230, 530, 350), outline = white, width = 3)
        draw.rectangle((550, 230, 790, 450), outline = white, width = 3)
        draw.rectangle((280, 370, 530, 450), outline = white, width = 3)

        font_type = r"{}\CEFFontsCJK-Regular.ttf".format(dirname)
        font = ImageFont.truetype(font_type, 40)
        draw.text((50, 240), ss_text, fill = white, font = font)

        draw.text((360, 235), "屬性", fill = white, font = font)
        draw.text(pos[0], attribute_v[0], fill = color_a[0], font = font)
        try:
            draw.text(pos[1], attribute_v[1], fill = color_a[1], font = font)
        except: ()

        draw.text((290, 380), "捕獲率:" + catch_rate_text, fill = white, font = font)
        draw.text((630, 235), "特性", fill = white, font = font)
        draw.text((560, 290), special_text, fill = white, font = font)

        font_type = r"{}\ChenYuluoyan-Thin.ttf".format(dirname)
        font = ImageFont.truetype(font_type, 30)
        draw.text((280, 480), random_quote[:21] + "\n" + random_quote[21:42] + "\n" + random_quote[42:], fill = white, font = font)

        with io.BytesIO() as image_binary:
            image.save(image_binary, 'PNG')
            image_binary.seek(0)
            await interaction.channel.send(file=discord.File(fp=image_binary, filename='image.png'))

async def setup(bot: commands.Bot):
    await bot.add_cog(pokemon(bot))