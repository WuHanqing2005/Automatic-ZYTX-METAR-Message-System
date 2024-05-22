# -*- coding:utf-8 -*-
# 软件名称：沈阳桃仙机场METAR报文自动推送程序
# 版本号：2024.05.21
# 软件版权归属：吴瀚庆
# 未经允许，禁止盗用，侵权必究

# 有意请联系软件作者 吴瀚庆
# 微信：whq20050121
# 手机：19528873640
# 邮箱：m19528873640@outlook.com
# 欢迎提出宝贵意见，感谢支持！


import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os
import random
import time


# 初始化界面信息
os.system('color a')

# 初始化datetime_list，记录已发送的METAR报的日期时间
datetime_list = []


# 写错误日志的函数
def write_error_log(error_message):
    # 获取当前时间
    now = datetime.datetime.now()
    # 格式化时间为字符串
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # 构造日志信息
    log_message = f"[{timestamp}]\nERROR: {error_message}\n\n"
    
    # 定义日志文件名
    log_filename = f"error_log.txt"
    
    # 打开文件，写入日志信息
    with open(log_filename, "a") as file:
        file.write(log_message)


# 获取METAR报文原文的函数，不需要任何参数，返回值为一个储存了多条METAR的一维数组，如：
# ['ZYTX 210830Z 24006MPS CAVOK 27/15 Q1013 NOSIG', 'ZYTX 210800Z 24005MPS 210V270 CAVOK 27/15 Q1013 NOSIG']
def get_metar_list():
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

        # 创建UserAgent对象
        ua = UserAgent()

        # 生成50个随机用户代理
        user_agents = [ua.random for _ in range(50)]

        # 随机选择一个用户代理
        selected_user_agent = random.choice(user_agents)

        # 初始化Chrome浏览器选项，设置用户代理
        chrome_options = Options()
        chrome_options.add_argument(f'user-agent={selected_user_agent}')

        # 初始化Chrome驱动
        driver = webdriver.Chrome(options=chrome_options)

        # 网页的URL（注意URL中的'&'后面跟的是'&amp;'而不是'&#39;'）
        url = 'https://www.flightaware.com/resources/airport/ZYTX/weather'

        # 发送请求并打开网页
        driver.get(url)

        # 等待网页加载（这里使用显式等待或隐式等待可能更精确，但简单起见先使用time.sleep）
        time.sleep(3)  # 等待几秒，这个时间可能需要调整

        # 使用BeautifulSoup解析网页内容
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # 找到所有包含original-title属性的<tr>标签
        tr_tags = soup.find_all('tr', {'original-title': True})  # 注意属性名可能是小写

        # 遍历所有找到的<tr>标签
        with open('original_METAR.txt', 'w', encoding='utf-8') as file:  # 使用'w'模式来覆盖文件
            for tr in tr_tags:
                # 提取original-title属性的值
                original_title = tr.get('original-title')
                if original_title:  # 确保original-title不为空
                    # print(original_title)
                    file.write(original_title + '\n')  # 写入文件，并在每行后添加换行符

        # 关闭浏览器
        driver.quit()


        # 读取output.txt文件内容
        with open('original_METAR.txt', 'r', encoding='utf-8') as file:
            metar_list = file.read().split(sep='\n')
            return metar_list
            # print(metar_list)
            # metar_list = ['ZYTX 210830Z 24006MPS CAVOK 27/15 Q1013 NOSIG', 'ZYTX 210800Z 24005MPS 210V270 CAVOK 27/15 Q1013 NOSIG']
    except Exception as error_message:
        print(f"get_metar_list() failed: {error_message}")
        write_error_log(error_message)
        a = input('Press Enter to exit...')









if __name__ == '__main__':
    # 以下代码循环执行
    while True:
        # 重新开始运行程序，该打印的信息先打印一下
        os.system('cls')
        os.system('color a')
        print('沈阳桃仙机场METAR报文自动推送程序')
        print('程序正在运行中，请稍候...')
        print('-' * 30)
        print('欢迎联系软件作者: 吴瀚庆')
        print('微信: whq20050121')
        print('邮箱: m19528873640@outlook.com')
        print('-' * 30)
        print('请务必更新uid_list，更新uid_list不必关闭本程序')
        print('如果没有推送消息，就是METAR信息没有更新，请耐心等待或者重启本程序')



        # 创建UserAgent对象
        ua = UserAgent()

        # 生成50个随机用户代理
        user_agents = [ua.random for _ in range(50)]

        # 随机选择一个用户代理
        selected_user_agent = random.choice(user_agents)

        # 网页的URL
        url = 'https://www.flightaware.com/resources/airport/ZYTX/weather'

        # 设置请求头，包含随机生成的用户代理
        headers = {
            'User-Agent': selected_user_agent
        }

        # 发送HTTP请求
        response = requests.get(url, headers=headers)

        # 确保请求成功
        if response.status_code == 200:
            # 使用BeautifulSoup解析网页内容
            soup = BeautifulSoup(response.content, 'html.parser')
    
            # 提取并打印网页中所有的文本信息
            text = soup.get_text(separator='\n', strip=True)
            # print(text)
        else:
            print(f"Error, Code: {response.status_code}")
    
        
        # 网站可能会抽风，不一定是中文还是英文
        if 'SHE近期METAR历史数据' in text:
            list_1 = text.split(sep='SHE近期METAR历史数据\n')
        elif 'Recent SHE METAR history' in text:
            list_1 = text.split(sep='Recent SHE METAR history\n')
            
        # print(list_1[1])
            
        list_2 = list_1[1].split(sep='More FBO and Airport Information\n')
        # print(list_2[0])


        # 打开文件准备写入
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(list_2[0])
            # file.write(text)

        # 读取文件内容并打印
        # with open('output.txt', 'r', encoding='utf-8') as file:
            # print(file.read())
        


        # 初步处理output.txt文件，如果读取到了Calm
        # 定义输入和输出文件名
        input_filename = 'output.txt'
        output_filename = 'output.txt'

        # 读取文件内容并替换文本
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()

        # 替换 "Calm" 为 "Calm\nCalm
        content = content.replace('Calm', 'Calm\nCalm')

        # 写入新内容到文件
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(content)



        # 用于存储每行气象信息的二维数组
        weather_data = []

        # 读取文件，并从第14行开始处理
        with open('output.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()  # 读取所有行
    
            lines = [item.rstrip('\n') for item in lines]   # 移除每个元素末尾的换行符
            # print(lines)
    
            for i in range(0, 10):
                weather_data.append([lines[18+13*i], lines[19+13*i], lines[20+13*i], lines[21+13*i], lines[22+13*i], lines[23+13*i], lines[24+13*i], lines[25+13*i], lines[26+13*i], lines[27+13*i], lines[28+13*i], lines[29+13*i], lines[30+13*i]])


        # print(weather_data)
        # weather_data = [['21-May', '12:00AM', 'VFR', '110°', '2 mps', 'Clouds and visibility are OK.', '14°', '57°', '11°', '51°', '82%', '1017 mb', '-34 ft'], 
        #                 ['20-May', '11:30PM', 'VFR', '110°', '3 mps', 'Clouds and visibility are OK.', '14°', '57°', '11°', '51°', '82%', '1017 mb', '-34 ft']]




        # 一维列表weather_data[0] 储存了最新的一条METAR信息，此后的操作均基于这个一维列表
        # 为方便操作，将其命名为metar
        # metar = ['21-May', '12:00AM', 'VFR', '110°', '2 mps', 'Clouds and visibility are OK.', '14°', '57°', '11°', '51°', '82%', '1017 mb', '-34 ft']
        metar = weather_data[0]
        metar_old = weather_data[1]
    

        # 通过风向推测使用跑道
        # ZYTX机场，可用跑道：06/24
        try:
            wind_degree = int(metar[3][:-1])    # 获取整数类型的风向度数
        except:
            wind_degree = 'Variable'

        try:
            wind_degree_old = int(metar_old[3][:-1])    # 获取整数类型的风向度数
        except:
            wind_degree_old = 'Variable'

        # 通过风向度数，来推测使用跑道的号码，其中，获取的跑道号码为字符串类型
        # 通过当前METAR    
        if wind_degree == 'Variable':
            using_runway = 'Not Know'
        elif wind_degree >= 330 and wind_degree <= 360:
            using_runway = '06'
        elif wind_degree >= 0 and wind_degree < 150:
            using_runway = '06'
        elif wind_degree >=150 and wind_degree < 330:
            using_runway = '24'

        # 通过风向度数，来推测使用跑道的号码，其中，获取的跑道号码为字符串类型
        # 通过上一条METAR      
        if wind_degree_old == 'Variable':
            using_runway_old = 'Not Know'
        elif wind_degree_old >= 330 and wind_degree_old <= 360:
            using_runway_old = '06'
        elif wind_degree_old >= 0 and wind_degree_old < 150:
            using_runway_old = '06'
        elif wind_degree_old >=150 and wind_degree_old < 330:
            using_runway_old = '24'
    

        # metar = ['21-May', '12:00AM', 'VFR', '110°', '2 mps', 'Clouds and visibility are OK.', '14°', '57°', '11°', '51°', '82%', '1017 mb', '-34 ft']
    

        datetime = metar[0] + '-' + metar[1]
        # print(datetime) # datetime = 21-May-02:30AM
    

        # 检测METER报是否发送过
        if datetime not in datetime_list:
            datetime_list.append(datetime)
        

            # 读取METAR报文原文
            metar_list = get_metar_list()
            # print(metar_list)


            metar_message = f'这是沈阳桃仙机场METAR报文的自动消息.\n\
软件版权归属于 @雾岛听风WuHanqing\n------------------------------\n\
机场代码: ZYTX\n------------------------------\n\
当前METAR报文信息\n\
日期: {metar[0]}\n北京时间: {metar[1]}\n预计使用跑道: {using_runway}\n\n飞行规则: {metar[2]}\n\
风向: {metar[3]}\n风速: {metar[4]}\n云层情况或云底高度(英尺): {metar[5]}\n气温(℃): {metar[6]}\n\
气温(℉): {metar[7]}\n露点(℃): {metar[8]}\n露点(℉): {metar[9]}\n\
相对湿度: {metar[10]}\n修正海压(百帕): {metar[11]}\n密度高度: {metar[12]}\n------------------------------\n\
上一条METAR报文信息\n\
日期: {metar_old[0]}\n北京时间: {metar_old[1]}\n预计使用跑道: {using_runway_old}\n\n飞行规则: {metar_old[2]}\n\
风向: {metar_old[3]}\n风速: {metar_old[4]}\n云层情况或云底高度(英尺): {metar_old[5]}\n气温(℃): {metar_old[6]}\n\
气温(℉): {metar_old[7]}\n露点(℃): {metar_old[8]}\n露点(℉): {metar_old[9]}\n\
相对湿度: {metar_old[10]}\n修正海压(百帕): {metar_old[11]}\n密度高度: {metar_old[12]}\n------------------------------\n\
沈阳桃仙机场历史METAR报文原文：\n\
{metar_list[0]}\n{metar_list[1]}\n{metar_list[2]}\n{metar_list[3]}\n------------------------------\n\
该程序还在测试阶段，有任何问题请联系软件作者: 吴瀚庆\n\
微信: whq20050121\n邮箱: m19528873640@outlook.com\n'

            
            # print(metar_message)


            import requests

            # 创建一个空列表来存储uid_list
            uid_list = []

            # 打开文件并读取每一行
            with open('uid_list.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    # 移除行尾的换行符并添加到列表中
                    uid_list.append(line.strip())

            # 打印uid_list
            # print(uid_list)

            # wxpusher的API接口地址
            api_url = "http://wxpusher.zjiecode.com/api/send/message"

            # 替换成自己的appToken和appKey
            appToken = "AT_JSUGQyhL9sfnoFcDASFphPGKLCC5VrtG"
            appKey = "62862"

            # 消息内容
            content = metar_message

            for uid in uid_list:
                # 构建发送消息的请求参数
                data = {
                    "appToken": appToken,
                    "content": content,
                    "summary": "沈阳桃仙机场METAR报文推送",
                    "contentType": 1,
                    "topicIds": [123],
                    "uids": [
                        uid  # 替换成要发送消息的微信用户的userId
                    ]
                }

                # 发送POST请求
                response = requests.post(api_url, json=data)

                # 打印返回的结果
                # print(response.json())
        


            print(f'METAR报 {datetime} 发送成功！')
            

        time.sleep(60)