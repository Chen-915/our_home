from streamlit import *
from PIL import Image
from random import*
#no st
def page1():
    write("游戏链接")   
    c1,c2,c3,c4=tabs(["植物大战僵尸杂交版","植物大战僵尸嫁接版","植物大战僵尸融合版","植物娘大战僵尸"])
    with c1:
        a,b,=columns([1,5])
        with a:
            write("作者")
            write("版本")
            write("下载方式")
        with b:
            write("潜艇伟伟迷")
            write("2.3版")
            write("夸克网盘:https://pan.quark.cn/s/549d16cf28e3")
            link_button("按这个在夸克网盘下载","https://pan.quark.cn/s/549d16cf28e3")
            write("超小白下载方式:https://www.pvz.moe/resources/433/")
            link_button("按这个快速下载","https://www.pvz.moe/resources/433/")
    with c2:
        a,b,=columns([1,5])
        with a:
            write("作者")
            write("版本")
            write("下载方式")
        with b:
            write("童话小责")
            write("0.1版本")
            write("夸克网盘链接:https://pan.quark.cn/s/bf28d380085a")
            link_button("按这个在夸克网盘下载","https://pan.quark.cn/s/bf28d380085a")
    with c3:
        a,b,=columns([1,5])
        with a:
            write("作者")
            write("版本")
            write("下载方式")
        with b:
            write("蓝飘飘fly")
            write("1.2版")
            write("夸克网盘下载:https://pan.quark.cn/s/5fe9728b4913#/list/share")
            link_button("按这个在夸克网盘下载","https://pan.quark.cn/s/5fe9728b4913#/list/share")
            write("超小白下载方式:https://www.pvz.moe/resources/537/")
            link_button("按这个快速下载","https://www.pvz.moe/resources/537/")
    with c4:
        a,b,=columns([1,5])
        with a:
            write("作者")
            write("版本")
            write("下载方式")
        with b:
            write("第二公开版")
            write("夸克网盘：https://pan.quark.cn/s/c5c2e04acb74")
            link_button("按这个在夸克网盘下载","https://pan.quark.cn/s/c5c2e04acb74")
            write("超小白下载方式:https://www.pvz.moe/resources/299/")
            link_button("按这个快速下载","https://www.pvz.moe/resources/299/")
def page2():
    img=None
    write(":four_leaf_clover:图片处理工具:four_leaf_clover:")
    uploaded_file=file_uploader("上传图片",type=["png","jpeg","jpg","gif"])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        image(img)
    fanse=checkbox("反色处理")
    duibi=checkbox("增强对比度")
    huidu=checkbox("变为灰度图")
    change=checkbox("随机调换颜色值")
    b=button("处理图片")
    if b:
        if fanse:
            img=img_fanse(img)
        if duibi:
            img=img_duibi(img)
        if change:
            img=img_change(img)
        if huidu:
            img=img_huidu(img)
    if uploaded_file:
        image(img)
def page3():
    write("智慧词典")
    with open("words_space.txt","r",encoding="utf-8-sig") as f:
        words_list=f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split("#")
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    word=text_input("请输入要查询的单词:")
    with open("check_out_times.txt","r",encoding="utf-8-sig") as f:
        times_list=f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split("#")
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    if word:
        if word in words_dict:
            write(words_dict[word])
            n=words_dict[word][0]
            if n in times_dict:
                times_dict[n]+=1
            else:
                times_dict[n]=1
            with open("check_out_times.txt","w",encoding="utf-8-sig") as f:
                message=""
                for i,j in times_dict.items():
                    message+=str(i)+"#"+str(j)+"\n"
                message=message[:-1]
                f.write(message)
            write("查询次数:"+str(times_dict[n]))
        elif word=="python":
            code("""触发彩蛋:print("hello world")""")
            balloons()
        else:
            write("词典里没有这个单词")
def page4():
    write("我的留言区")
    with open("leave_messages.txt","r",encoding="utf-8") as f:
        messages_list=f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split("#")
    for i in messages_list:
        if i[1]=="阿短":
            with chat_message("♂"):
                write(" "+i[1]+"："+i[2])
        elif i[1]=="编程猫":
            with chat_message("♀"):
                write(" "+i[1]+"："+i[2])
        else:
            with chat_message("？"):
                write(i[1]+":"+i[2])
    name=selectbox("我是…………",["阿短","编程猫","自定义"])
    if name:
        if name=="自定义":
            name=text_input("请留下尊姓大名:")
    new_message=text_input("说点什么…………")
    if button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open("leave_messages.txt","w",encoding="utf-8") as f:
            message=""
            for i in messages_list:
                message+=i[0]+"#"+i[1]+"#"+i[2]+"\n"
            message=message[:-1]
            f.write(message)
def page5():
    pass
def img_change(img):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][0]
            g=img_array[x,y][1]
            b=img_array[x,y][2]
            r=randint(1,5)
            if r==1:
                img_array[x,y]=b,r,g
            if r==2:
                img_array[x,y]=r,b,g
            if r==3:
                img_array[x,y]=b,g,r
            if r==4:
                img_array[x,y]=g,r,b
            if r==5:
                img_array[x,y]=g,b,r
    return img
def img_duibi(img):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][0]
            g=img_array[x,y][1]
            b=img_array[x,y][2]
            if r==max(r, g, b):
                if r>=200:
                    r=255
                else:
                    r+=55
            elif g==max(r, g, b):
                if g>=200:
                    g=255
                else:
                    g+=55
            elif b==max(r,g,b):
                if b>=200:
                    b=255
                else:
                    b+=55
            img_array[x,y]=(r,g,b)
    return img
def img_fanse(img):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            img_array[x,y]=255-img_array[x,y][0],255-img_array[x,y][1],255-img_array[x,y][2]
    return img
def img_huidu(img):
    return img.convert("L")
page=sidebar.radio("我的首页",["各种游戏提供(完全免费！)","我的图片处理工具","我的智慧词典","我的留言区","五子棋"])
if page=="各种游戏提供(完全免费！)":
    page1()
elif page=="我的图片处理工具":
    page2()
elif page=="我的智慧词典":
    page3()
elif page=="我的留言区":
    page4()
elif page=="五子棋":
    page5()