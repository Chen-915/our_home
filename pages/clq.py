'''页面布局小练习'''
import streamlit as st

# 多选题
st.write('下面哪些小程序可以被嵌入网页中？')
cb1,cb2,cb3,cb4 = st.columns([1,1,1,1])
with cb1:
    cb1 = st.checkbox('A.turtle绘图作品')
with cb2:
    cb2 = st.checkbox('B.图片处理工具')
with cb3:
    cb3 = st.checkbox('C.智能词典工具')
with cb4:
    cb4 = st.checkbox('D.pygame小游戏')
b1 = st.button('第1题答案')
if b1:
    if cb1 == False and cb2 == True and cb3 == True and cb4 == False:
        st.write('回答正确！')
    else:
        st.write('再想想')
