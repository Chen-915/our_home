import streamlit as st
import json
import Image_processing as img_p
from streamlit_option_menu import option_menu
from PIL import Image
from csv import DictReader

with st.sidebar:
    page = option_menu(
        "首页",
        [
            "兴趣推荐",
            "图片处理工具",
            "智慧词典",
            "留言区"
        ],
        icons=['star-fill', 'emoji-sunglasses', "book", 'vector-pen'],
        menu_icon="house"
    )
col1, col2, col3 = st.columns([2, 3, 2])
with col1:
    st.write("")
with col2:
    st.sidebar.link_button(":blue[项目已在Github上开源]", "https://github.com/wanghu534/My-first-blog")
with col3:
    st.write("")


with open("text.json", "r", encoding="utf-8") as f:
    text_dict = json.load(f)

try:
    print(hide)
    if hide == False:
        hide = False
except:
    hide = True


def page1():
    '''兴趣推荐'''
    global text_dict, hide
    header_write("⭐️:red[**兴趣推荐**]⭐️")
    st.divider()

    for k_1 in text_dict["兴趣推荐"]["Headers"]:
        st.subheader(text_dict["兴趣推荐"]["Headers"][k_1], anchor=False)
        for k_2 in text_dict["兴趣推荐"][k_1]:
            st.write(text_dict["兴趣推荐"][k_1][k_2])
            if k_1 == "Audios":
                with open(k_2, "rb") as a:
                    st.audio(a, format="audio/mp3", start_time=0)
            st.write("")
            st.write("")
        st.divider()

    if hide:
        a = st.text_input("")
        if a == "hide space":
            hide = False
    if not hide:
        st.subheader("Games", anchor=False)
        st.write("Left 4 Dead 2, Genshin impact and ZZZ all are too good to make me play them unhappily!")
     
def page2():
    '''我的图片处理工具'''
    global text_dict
    header_write("📸:orange[**图片处理工具**]📸", [5, 10, 4])
    uploader_file = st.file_uploader("上传图片", type=["png", "jpg", "gif", "jped"])

    if uploader_file:
        f_name = uploader_file.name
        f_type = uploader_file.type
        f_size = uploader_file.size
        img = Image.open(uploader_file)

        col_1, col_2, col_3 = st.columns([20, 8, 9])
        toggle_d = {}
        with col_1:
            st.image(img)
        with col_2:
            toggle_d = dict(zip(["ch", "co", "bright", "sharp", "bw"], [st.toggle(k) for k in text_dict["图片处理工具"]]))
        with col_3:
            for v in text_dict["图片处理工具"].values():
                st.write(v)

        if toggle_d.get("co"):
            contrast_ratio = st.select_slider(
                ":blue[请调节增加的:orange[对比度(值)]]",
                options=[str(i) for i in range(1, 101)]
            )
        if toggle_d.get("bright"):
            bright = st.select_slider(
                ":blue[请调节图像的:orange[亮度(倍数)]]",
                options=[str(i) for i in range(1, 6)]
            )
        if toggle_d.get("sharp"):
            sharp = st.select_slider(
                ":blue[请调节图像的:orange[锐度(倍数)]]",
                options=[str(i) for i in range(1, 6)]
            )
            
        st.header("")
        b = st.button("开始处理")

        if b:
            with st.status(":bullettrain_side: :orange[正在处理中，请稍候]:bullettrain_side:", expanded=True) as status:
                for k in toggle_d:
                    if toggle_d.get(k):
                        try:
                            print(contrast_ratio)
                        except:
                            contrast_ratio = "0"
                        try:
                            print(bright)
                        except:
                            bright = "0"
                        try:
                            print(sharp)
                        except:
                            sharp = "0"
                        expression = "img_p.img_change_" + k + "(img, contrast_ratio, bright, sharp)"
                        print(expression)
                        img = eval(expression)
                st.write(":slightly_smiling_face: :green[图像处理完毕！请右键“另存为”以保存图片]:slightly_smiling_face:")
                st.image(img)
                status.update()

def page3():
    '''我的智慧词典'''
    global mode, hide
    header_write("📖:green[**智慧词典**]📖")

    with open("words_space.txt", "r", encoding="utf-8") as f:
        words_list = f.read().split("\n")
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]

    words_dict_2 = {}
    with open("EnWords.csv", encoding="utf-8") as csv:
        reader = DictReader(csv)
        for row in reader:
            words_dict_2[row["word"]] = row["translation"]

    with open("check_out_times.txt", "r", encoding="utf-8") as f:
        times_list = f.read().split("\n")
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")
    times_dict = {}
    for i in times_list:
        times_dict[i[0]] = int(i[1])

    mode = st.selectbox(
        ":red[请选择选择数据库]",
        options=("数据库1 词量少 速度快", "数据库2 词量多 速度慢")
    )
    if "1" in mode:
        mode = 1
    elif "2" in mode:
        mode = 2
            
    word = st.text_input("请输入要查询的:green[单词]: ")
    if word:
        if word == "genshin impact":
            st.balloons()
            st.write(":green[UID:297510837]")
        elif word == "hide space":
            hide = False
            st.balloons()
        elif mode == 1: 
            if word in words_dict:
                check_out_times(word, times_dict)
                st.write("单词编号: " + str(words_dict[word][0]))
                st.write("译义: " + words_dict[word][1])
                st.write("查询次数: ", times_dict[word])

            else:
                st.write("当前数据库无此单词,请更换数据库后尝试")
        elif mode == 2:
            check_out_times(word, times_dict)
            if word in words_dict_2:
                st.write("译义: " + words_dict_2[word])
                st.write("查询次数: ", times_dict[word])

def page4():
    '''我的留言区'''
    header_write(":lower_left_fountain_pen: :blue[**留言区**]:lower_left_fountain_pen:")
    with open("leave_messages.txt", "r", encoding="utf-8") as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i[1] == "man":
            with st.chat_message("👱‍♂️"):
                st.write(i[1], ":", i[2])
        elif i[1] == "woman":
            with st.chat_message("👩"):
                st.write(i[1],":",i[2])
        else:
            with st.chat_message("�"):
                st.write(i[1],":",i[2])
    name = st.selectbox("我是......", ["man", "woman", "unknown"])
    new_message = st.text_input("想要说的话......")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open("leave_messages.txt", "w", encoding="utf-8") as f:
            message = ""
            for i in messages_list:
                message += i[0] + "#" + i[1] + "#" + i[2] + "\n"
            message = message[:-1]
            f.write(message)

def check_out_times(word, times_dict):
    if word in times_dict:
        times_dict[word] += 1
    else:
        times_dict[word] = 1
    with open("check_out_times.txt", "w", encoding="utf-8") as f:
        message = ""
        for k, v in times_dict.items():
            message += str(k) + "#" + str(v) + "\n"
        message = message[:-1]
        f.write(message)

def header_write(content, n=[4, 6, 3]):
    col1, col2, col3 = st.columns(n)
    with col1:
        st.write("")
    with col2:
        st.header(content, anchor=False)
    with col3:
        st.write("")
    

if page == "兴趣推荐":
    page1()
elif page == "图片处理工具":
    page2()
elif page == "智慧词典":
    page3()
elif page == "留言区":
    page4()