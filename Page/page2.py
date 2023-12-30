import streamlit as st
from streamlit_option_menu import option_menu

st.write("안녕")
password1 = "창설이벤트"
answer1 = "아기자기"
 # 1번
quiz1_password = st.text_input("1번 문제 오픈을 위한 비밀번호를 입력해주세요!",  key="quiz1_password")
if quiz1_password == password1:
    quiz1 = st.text_input("우리 길드의 이름은 뭘까?(⊙_⊙)？")
    if st.button("정답 확인", key="check_answer_button1"):
        if quiz1 == answer1:
            st.balloons()
            st.success("정답입니다!")
            st.write("우리 길드와 함께해줘서 고마워 ╰(*°▽°*)╯")
            st.write("2번 문제 오픈을 위한 비밀번호는 '아깅이' 입니다")
        else:
            st.warning("다시 한 번 생각해봐!")
    if st.button("힌트 보기", key="check_hint_button1"):
            st.write("이건 힌트를 줄 수가 없어! 잘 생각해 봐")
elif quiz1_password != "" and quiz1_password != password1:
    st.error("비밀번호가 틀렸어!")