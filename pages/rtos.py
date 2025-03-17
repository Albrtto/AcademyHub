import streamlit as st

st.set_page_config(page_title="Real-Time Operating Systems", page_icon=":material/precision_manufacturing:", layout="wide", initial_sidebar_state="collapsed")

st.title("Real-Time Operating Systems")

if st.button("Robotics :material/precision_manufacturing:", key = "robotics"):
    st.switch_page("pages/robotics.py")
st.write("---")

c = st.columns([1,1])

with c[0]:
    st.write("""
        RTOS is a special computer system for machines that need to work exactly on time, like robots or medical devices. It finishes urgent tasks first, so nothing goes wrong. Normal computers (like your laptop) are too slow for these jobs.
            """)
    st.write("""
        Here are some examples of documentation that should help you understand more:
            """)
    
with c[1]:
    st.image("images/rtos.webp")