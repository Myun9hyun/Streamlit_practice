import random
import pandas as pd
import streamlit as st
import time
items = ['item1', 'item2', 'item3', 'item4']
result = []

def open_box():
    if not items:
        return None
    item = random.choice(items)
    items.remove(item)
    return item
box_open_key = f"box_open_{int(time.time())}"

if st.button("Open box", key=box_open_key):
    item = open_box()
    if item:
        st.write(f"You got {item}!")
        result.append(item)
    else:
        st.write("The box is empty!")


df = pd.DataFrame(result, columns=['Items'])
st.write("Result:")
st.write(df)


# 현재 시간을 이용하여 유일한 키 생성

