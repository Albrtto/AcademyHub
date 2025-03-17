import streamlit as st

st.set_page_config(page_title="Digital Image Processing", page_icon=":material/precision_manufacturing:", layout="wide", initial_sidebar_state="collapsed")

st.title("Digital Image Processing")

if st.button("Robotics :material/precision_manufacturing:", key = "robotics"):
    st.switch_page("pages/robotics.py")
st.write("---")

c = st.columns([1,1])

with c[0]:
    st.write("""
    Teaches computers to understand and change pictures. Examples: making photos brighter, finding shapes in images, face recognition. Robots use this to "see" their environment.
    """)
    st.write("""
    Here are examples of documentation that should help you understand more: 
    """)

with c[1]:
    st.image("images/image_processing.png")