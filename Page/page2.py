import streamlit as st

st.title("퀴즈 만들어보기")
password1 = "도전"
answer1 = "바나나"
 # 1번
quiz1_password = st.text_input("퀴즈를 풀고싶다면, [도전]이라고 적어주세요",  key="quiz1_password")
if quiz1_password == password1:
    quiz1 = st.text_input("원숭이가 좋아하는 과일은？")
    if st.button("정답 확인", key="check_answer_button1"):
        if quiz1 == answer1:
            st.balloons()
            st.success("정답입니다!")
            st.write("우리 길드와 함께해줘서 고마워 ╰(*°▽°*)╯")
        else:
            st.warning("다시 한 번 생각해봐!")
    if st.button("힌트 보기", key="check_hint_button1"):
            st.write("노랗고 길죽한 과일이야!")
elif quiz1_password != "" and quiz1_password != password1:
    st.error("비밀번호가 틀렸어!")