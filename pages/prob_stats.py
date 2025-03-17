import streamlit as st

st.set_page_config(page_title="Probability and Statistics", page_icon=":material/precision_manufacturing:", layout="wide", initial_sidebar_state="collapsed")

st.title("Probability and Statistics")

if st.button("Robotics :material/precision_manufacturing:", key = "robotics"):
    st.switch_page("pages/robotics.py")
st.write("---")

c = st.columns([1,1])

with c[0]:
    st.write("""
    Math tools for working with uncertainty and data. Probability calculates chances (like rain), statistics finds meaning in data (like average heights). Helps robots handle mistakes.
    """)
    st.write("""
    Here are examples of documentation that should help you understand more:  
    """)

with c[1]:
    st.image("images/prob_stats.png")