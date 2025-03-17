import streamlit as st

st.set_page_config(page_title="Control Engineering", page_icon=":material/precision_manufacturing:", layout="wide", initial_sidebar_state="collapsed")

st.title("Control Engineering")

if st.button("Robotics :material/precision_manufacturing:", key = "robotics"):
    st.switch_page("pages/robotics.py")
st.write("---")

c = st.columns([1,1])

with c[0]:
    st.write("""
    This teaches how to make machines work automatically and correctly. Examples: robot arms moving smoothly, thermostats keeping temperature steady. Uses sensors and math rules to adjust machines.
    """)
    st.write("""
    Here are some examples of documentation that should help you understand more:
    """)

with c[1]:
    st.image("images/control_eng.png")