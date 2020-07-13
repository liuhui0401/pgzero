import pgzrun
import random
import math
import time
import collections


#真正意义上的3个全局变量
KEYWORD = 1
WIDTH = 1800
HEIGHT = 990


SCORES = 10#先声明在这里
ans = "win"#跨区变量的声明

#关卡一的计时器
st = 0#计时长起点
ed = 0#计时长终点

#关卡二的计时器
sttime = 0#计时长起点
edtime = 0#计时长终点

'''
从这里开始，是第1个页面；KEYWORD==1
第一关游戏及其前缀
'''
# 储存游戏所需图标
names = ['001c', '002c', '003c', '004c','005c','006c','007c','008c','009c','010c']
names_r = ['001d', '002d', '003d', '004d','005d','006d','007d','008d','009d','010d']
things = []

# 设置游戏的时间节点、模式等所需变量


tar = 1 # 标记music应该运行哪个文件和出现的图案序号
num = 0 # 使连续两个图标出现的位置不同
num_temp = 0 # 使连续两个图标出现的位置不同
total = 10 # 总图案个数
flag = 1 # 防止连续按键钢琴“弹奏”两次
node = 0 # 标记游戏界面
timex = 678 # 标记时间，卡钢琴音的时间点
SPEED = 5 # 图案下落速度
bias = 10 # 卡时
pattern = 0 # 初始化退出游戏再返回的界面
music_= 0 # 标记bgm是否播放


scores = -30 # 游戏分数
'''
游戏规则设定需要在第一关拿到正分才能进入第二关
可以在此设定第一关的初始分数
我们初始设为-30
'''


# 标记music出现时间
clk = [0,1449,1466,1484,1519,1551,1584,1599,1621,1694,1709,1724,1739]#0到12
clk += [1764,1787,1822,1962,1979,1997,2014,2062,2092,2112,2142,2207,2225]#13到25
clk += [2240,2255,2270,2285,2300,2317,2412,2430,2448,2488,2495,2510,2545,2562,2620]#26到40
clk += [2625,2640,2655,2702,2735,2750,2783,2810,2963,3013,3060,3078,3095,3143,3246]#41到55
clk += [3278,3310,3331,3451,3478,3493,3508,3523,3551,3609,3639,3656,3684,3736,3751]#56到70
clk += [3766,3781,3796,3819,3846,3876,3971,3986,4001,4016,4032,4064]#71到82
clk += [4119,4134,4149,4164,4247,4262,4277,4292,4309,4332,4357,4409]#83到94

# 给角色增加属性cnt代表目前出现的是第几个图案，num对应图标列表的下标
class Actor_(Actor):
    def __init__(self, image, cnt, num):
        super(Actor_, self).__init__(image)
        self.image = image
        self.cnt = cnt
        self.num = num


        
def draw_1():
    global node # node标记游戏进入哪一个界面
    global scores # scores标记游戏得分
    global timex # 卡时间点
    global pattern # # 初始化退出游戏再返回的界面
    
    # node为0时进入游戏首页
    if node == 0:       
        screen.clear()
        screen.blit('p1', (0, 0))
    # node为1时进入第一篇章首页并选择模式
    elif node == 1:
        screen.clear()
        screen.blit('p2', (0, 0))
    # node为2时进入模式一的规则介绍
    elif node == 2:
        screen.clear()
        screen.blit('p3', (0, 0))
    # node为3时进入模式二的规则介绍
    elif node == 3:
        screen.clear()
        screen.blit('p4', (0, 0))
    # node为4时进入游戏模式一的界面
    elif node == 4:
        screen.clear()
        screen.blit('p5', (0, 0))
        screen.draw.text("SCORES:%d" % scores, (780, 25), fontsize = 50,color = (255,255,255), fontname = 'lucon')
        # 标记出图形出现的位置所对应的键盘数字键
        screen.draw.text("1", (300, 120), fontsize = 100, color = (255,255,255))
        screen.draw.text('2', (700, 120), fontsize = 100, color = (255,255,255))
        screen.draw.text('3', (1100, 120), fontsize = 100, color = (255,255,255))
        screen.draw.text('4', (1500, 120), fontsize = 100, color = (255,255,255))
        
        # 进行倒计时计数
        if timex >= clk[1] - 180 and timex < clk[1] - 120:
            pattern = 0
            screen.draw.text('3', (700,200), fontsize = 1000, color = (255,255,255))        
        elif timex >= clk[1] - 120 and timex < clk[1] - 60:
            screen.draw.text('2', (700,200), fontsize = 1000, color = (255,255,255))
        elif timex >= clk[1] - 60 and timex < clk[1]:
            screen.draw.text('1', (700,200), fontsize = 1000, color = (255,255,255))
        elif pattern == 0:
            for tc in things:
                tc.draw()
        elif pattern == 1:
            pass
            
        screen.draw.text("You must get positive scores to keep going", (50,850), fontsize = 50,color = (255,255,255), fontname = 'comic')
    # node为5时进入游戏模式二的界面    
    elif node == 5:
        screen.clear()
        screen.blit('p5', (0, 0))
        color = 255, 255, 255
        # 标记出图形出现的位置
        screen.draw.filled_circle((900, 300), 100, color)
        screen.draw.filled_circle((900, 700), 100, color)
        screen.draw.filled_circle((700, 500), 100, color)
        screen.draw.filled_circle((1100, 500), 100, color)
        screen.draw.text('up', (880, 280), fontsize = 50, color = (139,0,18))
        screen.draw.text('down', (850, 680), fontsize = 50, color = (139,0,18))
        screen.draw.text('left', (670, 480), fontsize = 50, color = (139,0,18))
        screen.draw.text('right', (1070, 480), fontsize = 50, color = (139,0,18))
        screen.draw.text("SCORES:%d" % scores, (780, 25), fontsize = 50,color = (255,255,255), fontname = 'lucon')
        
        if timex >= clk[1] - 180 and timex < clk[1] - 120:
            # 进行倒计时计数
            pattern = 0
            screen.draw.text('3', (860,450), fontsize = 200, color = (255,255,255))
            
        elif timex >= clk[1] - 120 and timex < clk[1] - 60:
            # 进行倒计时计数
            screen.draw.text('2', (860,450), fontsize = 200, color = (255,255,255))
            
        elif timex >= clk[1] - 60 and timex < clk[1]:
            # 进行倒计时计数
            screen.draw.text('1', (860,450), fontsize = 200, color = (255,255,255))
        elif pattern == 0:
            for tc in things:
                tc.draw()
        elif pattern == 1:
            pass
                
        screen.draw.text("You must get positive scores to keep going", (50,850), fontsize = 50,color = (255,255,255), fontname = 'comic')                
    # node为6时进入游戏结束的界面
    elif node == 6:
        screen.clear()
        screen.blit('bgp', (0, 0))
        

def update_1():
    global timex # 用于卡时
    global tar # 标记音乐文件序号
    global scores # 积分
    global total # 图案总数
    global num # 用于使连续两个图标出现的位置不同
    global num_temp # 用于使连续两个图标出现的位置不同
    global flag # 防止连续按键钢琴音响多次
    global node # 标记游戏界面
    global things # 储存出现图案
    global music_ # 标记背景音乐是否播放
    
    global KEYWORD # 连接关卡一和关卡二
    global SCORES # 连接关卡一和关卡二
    global ans # 标记游戏结果
    global st # 计时长起点
    global ed # 计时长终点
    
    ed = time.time()
    
    # 控制bgm
    if music_ == 0 and node <= 3:
        sounds.s00_sub_01_1.play()
        music_ = 1
    # 模式一
    if node == 4:
        timex = 678 + 40.0 * (ed - st)
        # 图形在音乐卡点的时间出现
        if tar < 95 and timex >= clk[tar] + bias:
            tar += 1
            # total为图片总数
            nn = random.randint(0, total - 1)
            # tar标记actor序号，nn标记actor对应图片
            tc = Actor_(names[nn], tar, nn)
            # 使连续两个图标出现的位置不同
            while num == num_temp:
                num = random.randint(0, 3)
            num_temp = num
            if num == 0:
                tc.center = 310, 120
            elif num == 1:
                tc.center = 710, 120
            elif num == 2:
                tc.center = 1110, 120
            elif num == 3:
                tc.center = 1510, 120
            things.append(tc)
        for tc in things:
            tc.y += SPEED
            if tc.y >= 990:
                things.remove(tc)
    # 模式二与模式一类似
    elif node == 5:
        timex = 678 + 40.0 * (ed - st)
        if  tar < 95 and timex >= clk[tar] + bias :
            tar += 1
            nn = random.randint(0, total - 1)
            tc = Actor_(names[nn], tar, nn)          
            while num == num_temp:
                num = random.randint(0, 3)            
            num_temp = num
            things.append(tc) 
            for tc in things:
                if num == 0: 
                    tc.center = 900, 300
                elif num == 1:
                    tc.center = 900, 700
                elif num == 2:
                    tc.center = 700, 500
                elif num == 3:
                    tc.center = 1100, 500

    # 游戏结束
    if timex > 4550:
        node = 6
        if scores < 0:  # 无法进入第二关
            KEYWORD = 4
            ans = "lose"
        else:  # 转入下一关卡，进行初始分数设定
            KEYWORD = 2
            set_sc(scores)


def on_key_down_1(key):
    global flag # 防止连续按键钢琴音响多次
    global scores # 积分
    global node # 游戏界面
    global music_ # 标记背景音是否播放
    # 模式一
    if node == 4:
        # 需要在对应块落下一秒内且下一块落下前按键才可“弹奏”
        if timex > clk[tar-1] and timex <= clk[tar-1] + 60 and tar != flag:
            if (keyboard.k_1 and num == 0) or (keyboard.k_2 and num == 1) or (keyboard.k_3 and num == 2) or (keyboard.k_4 and num == 3):
                flag = tar
                playing(tar-1)
                set_suc(tar)
                scores += 1
            # 如果错误按键会扣分并且发出错误提示音
            elif (keyboard.k_1 and num != 0) or (keyboard.k_2 and num != 1) or (keyboard.k_3 and num != 2) or (keyboard.k_4 and num != 3):
                sounds.fail.play()
                scores -= 1
        else:
            if keyboard.k_1 or keyboard.k_2 or keyboard.k_3 or keyboard.k_4:
                sounds.fail.play()
                scores -= 1
    # 模式二与模式一类似
    elif node == 5:
        if timex > clk[tar-1] and timex <= clk[tar-1] + 60 and tar != flag:
            if (keyboard.up and num == 0) or (keyboard.down and num == 1) or (keyboard.left and num == 2) or (keyboard.right and num == 3):
                flag = tar
                playing(tar-1)
                set_suc(tar)
                scores += 1
            elif (keyboard.up and num != 0) or (keyboard.down and num != 1) or (keyboard.left and num != 2) or (keyboard.right and num != 3):
                sounds.fail.play()
                scores -= 1
        else:
            if keyboard.up or keyboard.down or keyboard.left or keyboard.right:
                sounds.fail.play()
                scores -= 1
    
def on_mouse_down_1(pos, button):
    global node # 游戏界面
    global scores # 积分
    global tar # 音乐文件序号
    global timex # 卡时
    global things # 图案储存
    global music_ # 标记背景音是否播放
    global st # 计时长起点
    global ed # 计时长终点
    global pattern # # 初始化退出游戏再返回的界面

    # 开始游戏页面，选择开始游戏
    if node == 0:
        if button == mouse.LEFT:
            if pos[0] >= 550 and pos[0] <= 1200 and pos[1] >= 600 and pos[1] <= 700:
                node = 1
    # 选择游戏模式界面，也可返回到上一界面
    elif node == 1:
        if button == mouse.LEFT:
            if pos[0] >= 600 and pos[0] <= 1250 and pos[1] >= 200 and pos[1] <= 350:
                node = 2
            elif pos[0] >= 600 and pos[0] <= 1250 and pos[1] >= 600 and pos[1] <= 800:
                node = 3
            elif pos[0] >= 1500 and pos[0] <= 1750 and pos[1] >= 20 and pos[1] <= 120:
                node = 0
    # 模式一的规则介绍，可以选择开始游戏，也可以返回到上一界面
    elif node == 2:
        if button == mouse.LEFT:
            if pos[0] >= 250 and pos[0] <= 900 and pos[1] >= 750 and pos[1] <= 900:
                node = 4
                sounds.s00_sub_01_1.stop()
                sounds.s00_8.play()
                st=time.time()
            elif pos[0] >= 1500 and pos[0] <= 1750 and pos[1] >= 20 and pos[1] <= 120:
                node = 1
    # 模式二的游戏介绍，可以选择开始游戏，也可以返回到上一界面
    elif node == 3:
        if button == mouse.LEFT:
            if pos[0] >= 250 and pos[0] <= 900 and pos[1] >= 750 and pos[1] <= 900:
                node = 5
                sounds.s00_sub_01_1.stop()
                music_=0
                sounds.s00_8.play()
                st=time.time()
            elif pos[0] >= 1500 and pos[0] <= 1750 and pos[1] >= 20 and pos[1] <= 120:
                node = 1
    # 模式一的游戏进行时，可以选择停止游戏并返回上一界面
    elif node == 4: 
        if button == mouse.LEFT:
            if pos[0] >= 1500 and pos[0] <= 1750 and pos[1] >= 20 and pos[1] <= 120:
                sounds.s00_8.stop()
                music_ = 0
                pattern = 1
                for tc in things:
                    tc.y = 2000
                    things.remove(tc)
                #初始化的设置
                scores = -30
                timex = 678
                tar = 1
                node = 2
    # 模式二的游戏进行时，可以选择停止游戏并返回上一界面
    elif node == 5:
        if button == mouse.LEFT:
            if pos[0] >= 1500 and pos[0] <= 1750 and pos[1] >= 20 and pos[1] <= 120:
                sounds.s00_8.stop()
                pattern = 1
                for tc in things:
                    tc.y = 2000
                    things.remove(tc)
                #初始化的设置
                scores = -30
                timex = 678
                tar = 1
                node = 3

# 正确按下按键设置图标变化
def set_suc(num):
    for tc in things:
            if tc.cnt == num:
                tc.image = names_r[tc.num]
                break

# 正确按下按键设置钢琴音“弹奏”
def playing(num):
    if num < 10:
        music_name = 's0' + str(num)
    else:
        music_name = 's' + str(num)
    music.play_once(music_name)



'''
KEYWORD==1到此结束
'''

#KEYWORD==2,一二关过度页面


fang=0#记录背景音的播放情况

def draw_2():
    screen.blit('p6', (0, 0))
      
    
def update_2():
    global fang
    if fang==0:
        sounds.s00_sub_02_1.play()
        fang=1
    elif fang==1:
        None
        
    return

def on_mouse_down_2(pos, button):#对应位置的点击方可完成模式的切换
    global KEYWORD
    global sttime
    
    
    if pos[0] >= 350 and pos[0] <= 900 and pos[1] >= 800 and pos[1] <= 870:
        sounds.s00_sub_02_1.stop()
        KEYWORD=3
        
        sounds.bgm.play()
        sttime=time.time()#点击开始的时刻也就是下个关卡时间计时的开始
        
        
def on_key_down_2(key):#无意义，为了后面表示更加统一化规整化，这样写
    return

#KEYWOED==2的情况到此结束
        
        
'''
从这里开始，是第3个页面；KEYWORD==3
第二关游戏
'''

NAMES = ["001", "002", "003", "004", "005", "006", "007", "008", "009"]  # 图形名
hui_NAMES = ["001a", "002a", "003a", "004a", "005a", "006a", "007a", "008a", "009a"]  # 暗化处理图形名


#下列三个装的是Actor
allthings = []  # 图形的列表
opposites = [[], [], [], [], [], [], [], []]  # 每行敌方旗帜的列表
weapons = []  # 承载所有武器的列表

# 设定可能的图案数量，越高代表游戏难度越大，经游戏体验，设为9比较合适
LEVEL = 9




#SCORES    放在最前面已经声明过，是第二关的初始分数

seconds = 0  # 时间，以帧为单位，一秒约为60帧，这里不要求一定要是60fps,只是记录帧数以便一些计算的展开

speed = 0.45  # 地方前进的速度，随进程变化，初值暂定为0.45

smallest_sum = 3  # 记录最低的连通块限制

ifone = False  # 记录第一个大招有没有开

iftwo = False  # 记录第二个大招有没有开

ifthree = False  # 记录第三个大招有没有开

add = 0#记录每次的加分数值，也就是子弹的发射数

total_length=60*115+50#乐曲总长度，以60分之1秒为单位（这里不是默认update为一秒恒定60次，因有time库支持的准确时间记录）
timey=0.0#timey就是1：60的准确时间记录

def set_sc(x):#一二关卡的过度，只会被调用最多一次
    global SCORES
    SCORES=x
    return

def judge_res():#是否要快速转入游戏结束
    global timey
    global opposites
    #挺过一首歌的时间，还没死就赢了
    if timey >=total_length:
        return "win"
    else:
        #有一路被团灭就输了
        for i in range(0, 8):
            for t in opposites[i]:
                if t.x <=-45:
                    #设为-45与设为0不会改变输赢结果，设为负的是为了留有一定缓冲时间，让用户视觉上接受
                    return "lose"
        #其余情形是暂时不设返回值的
            


def inside(xx, yy):#BFS边界判断
    if xx >= 0 and yy >= 0 and yy < 8 and xx < 11:
        if find(xx, yy).num < 20:
            return True
        else:
            return False
    else:
        return False


target = None  # 被点击的操作数对象，鼠标事件追随
target_another = None  # 交换时的另一个操作数对象


def judge(xx, yy):  # 找点击位置的对象，利用鼠标在屏幕的绝对位置
    for t in allthings:
        if abs(t.x - xx) < 45 and abs(t.y - yy) < 45:
            return t
    else:
        return None

def find(xx, yy):  # 找坐标位置的对象，利用格点坐标的元组定位
    for t in allthings:
        if t.posi[0] == xx and t.posi[1] == yy:
            return t
    else:
        return None

def draw_3():
    screen.clear()
    screen.fill((128, 0, 0))#北大红！
    #打印提示信息
    screen.draw.text("SCORE:%d" % SCORES, (1300, 870), fontsize=50)
    screen.draw.text("PROTECTING PKU!", (1100, 910), fontsize=66)
    if smallest_sum == 3:
        screen.draw.text("YOU CAN CLICK 1 TO USE 'LIMIT 3 to 2' (USE 30 SCORES)!", (10, 880), fontsize=40)
    else:
        screen.draw.text("THE LIMIT HAS BEEN DECREASED TO 2!", (10, 880), fontsize=40)
    if iftwo == False:
        screen.draw.text("YOU CAN CLICK 2 TO USE 'GO AWAY' (USE 30 SCORES)!", (10, 920), fontsize=40)
    else:
        screen.draw.text("YOU HAVE USED 'GO AWAY' ABILITY!", (10, 920), fontsize=40)
    if ifthree == False:
        screen.draw.text("YOU CAN CLICK 3 TO USE 'BETTER WEAPON' (USE 30 SCORES)!", (10, 960), fontsize=40)
    else:
        screen.draw.text("THE WEAPON HAS BEEN IMPROVED!", (10, 960), fontsize=40)
    #显示所有对象
    for t in allthings:
        t.draw()
    for i in range(8):
        for tt in opposites[i]:
            tt.draw()
    for h in weapons:
        h.draw()


haveone = [[-1, -1, -1, -1, -1, -1, -1, -1] for i in range(11)]#坐标系格点阵

def deal_color():#每一行根据对方旗帜行进，判断己方图标是否失效，用haveone列表来支持
    global things
    global haveone
    
    #失效了显示灰色版本，正常就是彩色版本
    for j in range(8):#意味着按照行来遍历
        wei = opposites[j][0].x
        for i in range(0, 11):
            tem = find(i, j)
            if tem == None:
                continue
            else:
                if tem.num >= 20:
                    if 100 * i + 50 > wei:
                        continue
                    else:
                        tem.num -= 20
                        tem.image = NAMES[tem.num]
                elif tem.num < 20 and tem.num >= 0:
                    if 100 * i + 50 < wei:
                        continue
                    else:
                        #类型20的偏移量用来区分单位格的瞬时化状态
                        tem.image = hui_NAMES[tem.num]
                        tem.num += 20

def deal_speed():
    global speed
    global seconds
    
    mit = seconds // 60
    #以帧记录，并不意味默认60fps，这里允许速度的变化略有偏差，不会影响游戏整体

    if mit <= 15:
        speed = 0.5
    elif mit > 15 and mit <= 30:
        speed = 0.65
    elif mit > 30 and mit <= 45:
        speed = 0.8
    elif mit > 45 and mit <= 60:
        speed = 0.9
    elif mit > 60 and mit <= 75:
        speed = 1.15
    elif mit > 75 and mit <= 90:
        speed = 1.4
    elif mit>90 and mit<=100:
        speed = 1.8
    else:
        speed=2.2

def update_3():
    global seconds
    global KEYWORD
    global ans
    global sttime
    global edtime
    global timey
    
    #先走时间，timey确定
    edtime=time.time()
    timey=(edtime-sttime)*60.0
    
    
    # 先更新一下战斗结果，是否游戏结束；
    res = judge_res()
    if res == "win" or res == "lose":
        sounds.bgm.stop()
        #print(res,seconds)#注意看控制台信息
        ans=res
        KEYWORD=4
        return

    # 先更新一遍速度,10帧为单位，没有必要每帧都更新一下
    if seconds % 10 == 0:
        deal_speed()
        
    else:
        None

    if seconds == 0:#零帧数的时候，初始化
        # 初始化图层
        sounds.bgm.play()
        
        for i in range(0, 11):
            for j in range(0, 8):
                u = random.choice(range(0, LEVEL))
                t = Actor(NAMES[u])
                t.num = u
                haveone[i][j] = u
                t.posi = (i, j)
                t.center = 100 * i + 50, 100 * j + 50
                allthings.append(t)
                if i == 0:
                    tt = Actor("flag")
                    tt.center = 1600, 100 * j + 50
                    opposites[j].append(tt)

    else:
        for i in range(0, 8):
            for tt in opposites[i]:
                tt.x -= speed
        for h in weapons:
            h.x += 20
        for i in range(0, 8):
            for tt in opposites[i]:
                for h in weapons:
                    if tt.colliderect(h):#即撞即消除
                        if h.image == "heart":
                            weapons.remove(h)
                            tt.x += 220
                        elif h.image == "better_heart":
                            weapons.remove(h)
                            tt.x += 400
    
    seconds+=1
    #seconds与timey不同，前者记录绝对帧数
    if seconds >= 1 and seconds % 4 == 0:
        deal_color()
    if seconds % 4 == 2:
        makeup()

def makeup():
    #空白区域的填充
    global haveone
    global allthings
    
    #记录需要补充的个数
    bu = 0
    
    #用遍历的方式判断
    for i in range(0, 11):
        for j in range(0, 8):
            if haveone[i][j] == -1:#记-1意味着瞬时的空白
                bu += 1
                #随机新的
                u = random.choice(range(0, LEVEL))
                t = Actor(NAMES[u])
                t.num = u
                haveone[i][j] = u
                t.posi = (i, j)
                t.center = 100 * i + 50, 100 * j + 50
                allthings.append(t)
                
def on_key_down_3(key):
    global SCORES
    global target
    global target_another

    # 放大招的优先考虑
    if keyboard.k_1 or keyboard.k_2 or keyboard.k_3:
        if keyboard.k_1:
            set_skills_1()
        elif keyboard.k_2:
            set_skills_2()
        elif keyboard.k_3:
            set_skills_3()
        #注意这里优先考虑应return
        return

    if target == None:
        return
    else:
        None

    if keyboard.space:
        #空格，开始搜连通图
        xx = target.posi[0]
        yy = target.posi[1]
        bfs(xx, yy, target.num)
        target = None
        #第一层讨论的是联通个数是否充足
        if add >= smallest_sum:
            sounds.right.play()
            SCORES += add
            for i in range(0, 11):
                for j in range(0, 8):
                    if haveone[i][j] == -1:
                        if ifthree == False:
                            tt = Actor("heart")
                            tt.center = 100 * i + 50, 100 * j + 50
                            weapons.append(tt)
                        else:#讨论的是武器的种类
                            tt = Actor("better_heart")
                            tt.center = 100 * i + 50, 100 * j + 50
                            weapons.append(tt)

                        tem = find(i, j)
                        tem.center = -500, -500
                        tem.posi = (-500, -500)
                        allthings.remove(tem)


        else:
            sounds.wrong.play()
            for i in range(0, 11):
                for j in range(0, 8):
                    if haveone[i][j] == -1:
                        haveone[i][j] = find(i, j).num

    elif keyboard.up or keyboard.down or keyboard.left or keyboard.right:#交换的指令
        if SCORES <= 1:  # 分数有限
            target = None
            target_another = None
            sounds.wrong.play()  # 不能动，卡顿提示音
            return

        xx = target.posi[0]
        yy = target.posi[1]
        if keyboard.up:
            yy -= 1
        elif keyboard.down:
            yy += 1
        elif keyboard.right:
            xx += 1
        elif keyboard.left:
            xx -= 1
        #根据选择对象与交换方向，靶向到另一个对象
        if inside(xx, yy) == False:
            target = None
            target_another = None
            sounds.wrong.play()  # 不能动，卡顿提示音
            return
        else:
            target_another = find(xx, yy)
            changing()
            SCORES -= 2#changing一次要消耗的积分值
            target = None
            target_another = None
    else:
        target = None
        target_another = None
        return

def on_mouse_down_3(pos, button):

    global target
    
    if button == mouse.LEFT:

        xx = pos[0]
        yy = pos[1]
        tt = judge(xx, yy)
        if tt != None:
            if tt.num < 20:
                target = tt
    elif button == mouse.RIGHT:

        xx = pos[0]
        yy = pos[1]
        tt = judge(xx, yy)#利用点击位置进行选取对象
        if tt != None:
            if tt.num < 20:
                target = tt
    if target != None:
        set_pic_dark(target)

def changing():  # 交换两个对象的位置
    global target
    global target_another
    
    e1 = target
    e2 = target_another
    if e1 == None or e2 == None:
        return
    else:
        None
    
    #u.v标签作为交换辅助因子，交换显示位置，坐标记录，以及相应的haveone
    u = e2.center
    v = e1.center
    e1.center = u
    e2.center = v

    u = e2.posi
    v = e1.posi
    haveone[u[0]][u[1]] = e1.num
    haveone[v[0]][v[1]] = e2.num
    
    e1.posi = u
    e2.posi = v

    sounds.switch.play()

def set_pic_dark(tem):#短暂的点击时，图标变化为灰暗显示
    if tem != None:
        if tem.num >= 20:
            return
        else:
            tem.image = hui_NAMES[tem.num]
            clock.schedule_unique(set_pic_bright, 0.15)


def set_pic_bright():#图标回复至正常显示
    global target
    
    if target!=None:
        target.image = NAMES[target.num]
    
    

# 经典广搜列表对
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(xx, yy, num):
    # 连通图，经典广搜套路，haveone本身就扮演了visited数组

    global haveone
    global add
    haveone[xx][yy] = -1
    add = 1
    d = collections.deque()
    d.append((xx, yy))

    while len(d) != 0:
        r = d.popleft()
        x1 = r[0]
        y1 = r[1]
        for i in range(0, 4):
            if inside(x1 + dx[i], y1 + dy[i]):
                if haveone[x1 + dx[i]][y1 + dy[i]] == num:
                    haveone[x1 + dx[i]][y1 + dy[i]] = -1
                    add += 1
                    d.append((x1 + dx[i], y1 + dy[i]))
    


# 减少连通块的限制
# smallest_sum本身就是记录这个大招的调用
def set_skills_1():
    global SCORES
    global smallest_sum#大招的作用就在于对这个全局变量的修改
    
    if smallest_sum == 2:
        return
    else:
        if SCORES >= 30:
            SCORES -= 30
            smallest_sum = 2
            sounds.skills.play()
        else:
            return


# 对手瞬移半屏
# iftwo记录这个大招是否调用
def set_skills_2():
    global SCORES
    global opposites
    global iftwo

    if iftwo == True:
        return
    else:
        None

    if SCORES >= 30:
        SCORES -= 30
        iftwo = True
        sounds.skills.play()
        for i in range(0, 8):#遍历，集体性
            for tt in opposites[i]:
                tt.x += 850#长距离的后退
    else:
        return


# 更换子弹为高杀伤子弹
# ifthree记录第三个大招有没有使用
def set_skills_3():
    global SCORES
    global opposites
    global ifthree
    if ifthree == True:
        return
    else:
        if SCORES >= 30:
            ifthree = True
            SCORES -= 30
            sounds.skills.play()
        else:
            return

'''
第二关游戏的页面
KEYWORD==3的情形
到此结束
'''

#最后是KEYWORD==4的临别页面


#ans在最前面声明，表示游戏结果
saygoodbye=0#记录结尾提示音的播放情况

def draw_4():
   if ans=="win":
       screen.blit('pwin', (0, 0))
   else:
       screen.blit('plose', (0, 0))
       
def update_4():
    global saygoodbye
    if saygoodbye==0:
        sounds.s00_sub_03_1.play()
        saygoodbye=1
        
#下面这两个是为了形式上统一，增加可读性，易于理解   
def on_key_down_4(key):
    return

def on_mouse_down_4(pos, button):
    return

#临别页面（KEYWORD为4的区域）到此结束

#事件触发的说明，KEYWORD确定作用区域
def draw():
    if KEYWORD == 1:
        draw_1()
    elif KEYWORD == 2:
        draw_2()
    elif KEYWORD == 3:
        draw_3()
    elif KEYWORD == 4:
        draw_4()

def update():
    if KEYWORD == 1:
        update_1()
    elif KEYWORD == 2:
        update_2()
    elif KEYWORD == 3:
        update_3()
    elif KEYWORD == 4:
        update_4()


def on_key_down(key):
    global KEYWORD
    
    if KEYWORD == 1:
        on_key_down_1(key)
    elif KEYWORD == 2:
        on_key_down_2(key)
    elif KEYWORD == 3:
        on_key_down_3(key)
    elif KEYWORD == 4:
        on_key_down_4(key)

def on_mouse_down(pos, button):
    global KEYWORD
    
    if KEYWORD == 1:
        on_mouse_down_1(pos, button)
    elif KEYWORD == 2:
        on_mouse_down_2(pos, button)
    elif KEYWORD == 3:
        on_mouse_down_3(pos, button)
    elif KEYWORD == 4:
        on_mouse_down_4(pos, button)
   
   
   
pgzrun.go()
