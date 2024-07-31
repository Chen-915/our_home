'''我的主页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('姜闲的主页',['简介','兴趣和日常','图片处理工具','智慧词典','留言区'])#创建侧边栏

def page_0():
    '''简介'''
    st.title('欢迎来到闲的主页')
    st.header('( •̀ .̫ •́ )✧')
def page_1():
    '''兴趣'''
    st.title(':spiral_calendar_pad:兴趣和日常:spiral_calendar_pad:')
    st.write('---------------------')
    st.subheader('游戏推荐:video_game:')
    col1,col2 = st.columns([1,2])
    with col1:    
        st.image('沙滩.gif')
    with col2:
        st.write('没找到合适的图片，先凑和一下(●`◡`●)')
        st.link_button('第五人格官网', 'https://id5.163.com/index.html')
    st.write("------------------")
    st.subheader('音乐推荐:headphones:')
    col1,col2 = st.columns([1,3])
    with col1:    
        st.write('茫')
        st.link_button('去听歌', 'https://music.163.com/#/song?id=1495058484')
    with col2:
        st.write('茫茫人海中，我们总是孤单的行走，仿佛身处一个黑暗的隧道里，找不到出口。但是，听着这首歌，你就能在这个无尽的隧道中找到你的归宿，像是划过黑暗的闪电，让你重新点亮生命中的灯塔。李润祺的歌词和曲调完美地融合在一起，令人陷入无尽的律动中。（以上截自QQ音乐评论区）')
        
def page_2():
    '''图片处理'''
    st.title(':movie_camera:图片处理工具:movie_camera:')
    st.write('----------------')
    uploaded_file = st.file_uploader("上传图片",type=['png','jpg','jpeg'])
    if uploaded_file:
        #获取图片文件名称 类型及大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        #分列展示
        col1,col2 = st.columns([3,2])
        with col1:
            st.image(img)
        with col2:
            fs = st.toggle("反色滤镜")
            co = st.toggle("增强对比度")
            bw = st.toggle("黑白滤镜")
        #点击按钮处理图片
        b = st.button("开始处理")
        if b:
            if fs:
                img = img_change_fs(img)
            if co:
                img = img_change_co(img)
            if bw:
                img = img_change_bw(img)
            st.write('右键“另存为”')
            st.image(img)

def img_change_fs(img):
    '''图片反色处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取RGB值
            r = 225 - img_array[x,y][0]
            g = 225 - img_array[x,y][1]
            b = 225 - img_array[x,y][2]
            img_array[x,y] = (b,g,r)#bgr...rbg...
    return img

def img_change_co(img):
    '''增强图片对比度'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取RGB值
            r = img_array[x,y][0]
            g = img_array[x,y][1]
            b = img_array[x,y][2]
            #RGB中，哪个大，哪个就再大一点
            if r == max(r,g,b):
                if r >= 200:
                    r = 255
                else:
                    r += 55
            elif g == max(r,g,b):
                if g >= 200:
                    g = 255
                else:
                    g += 55
            else:
                if b >= 200:
                    b = 255
                else:
                    b += 55
            img_array[x,y] = (r,g,b)
    return img

def img_change_bw(img):
    '''图片黑白滤镜'''
    img = img.convert('L')#转换为灰度图
    return img
    
def page_3():
    '''词典'''
    st.title(":file_folder:智慧词典:pushpin:")
    st.write('---------------')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
    #将列表的每一项再次分割,分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    #将列表内容转换为字典,格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
     #从文件中将单词的查询次数读取出来，存储于列表
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    #转字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    #创建输入框
    word = st.text_input("请输入要查询的单词")
    #显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：',times_dict[n])
        
    #彩蛋    
    if word == "python":
        st.subheader('''#触发彩蛋啦！！！这是一种编程语言，下面是该语言的示例''')
        st.write('''print("hello world")''')
    if word == "jxballoons":
        st.subheader('''#触发彩蛋啦！！！''')
        st.balloons()
    if word == "jxsnow":
        st.subheader('''#触发彩蛋啦！！！''')
        st.snow()
    if word == "jxtime":
        st.subheader('''#触发彩蛋啦！！！''')
        st.date_input('日期框',value=None,min_value=None,max_value=None)
        st.write('时光倒流吧！')
        st.write('#就只是一个冷笑话ヾ(•ω•`)o')
    if word == "dwrg":
        st.subheader('''#触发彩蛋啦！！！''')
        st.write('第五人格启动！！！')
        st.image('dwrg.jpg')
def page_4():
    '''留言区'''
    st.title('📝留言区📝')
    st.write('-------------')
    #从文件中加载内容，处理为列表
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '闲':
            with st.chat_message('🕹️'):
                st.write(i[1],':',i[2])
        elif i [1] == 'xian':
            with st.chat_message('🥏'):
                st.write(i[1],':',i[2])
        else:
            with st.chat_message('🍵'):
                st.write(i[1],':',i[2])
    name =  st.text_input('我是...')
    new_message = st.text_input("我想说...")
    if st.button('发表留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
if page == '兴趣和日常':
    page_1()
elif page == '图片处理工具':
    page_2()
elif page == '智慧词典':
    page_3()
elif page == '留言区':
    page_4()
elif page == '简介':
    page_0()
