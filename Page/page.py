import random
import pandas as pd
import streamlit as st

items = ['item1', 'item2', 'item3', 'item4']
result = []

def open_box():
    if not items:
        return None
    item = random.choice(items)
    items.remove(item)
    return item

while st.button('Open Box'):
    item = open_box()
    if item:
        st.write(f"You got {item}!")
        result.append(item)
    else:
        st.write("The box is empty!")
        break

df = pd.DataFrame(result, columns=['Items'])
st.write("Result:")
st.write(df)
