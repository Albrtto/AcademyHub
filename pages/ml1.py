import streamlit as st


st.set_page_config(page_title="Machine Learning I", page_icon=":material/precision_manufacturing:", layout="wide", initial_sidebar_state="collapsed")

st.title("Machine Learning I")

if st.button("Robotics :material/precision_manufacturing:", key = "robotics"):
    st.switch_page("pages/robotics.py")
st.write("---")

c = st.columns([1,1])

with c[0]:
    st.write("""
    Teaches computers to learn from examples, like recognizing cats after seeing many cat pictures. Uses math rules to find patterns. Helps robots make smart decisions.
    """)
    st.write("""
    Here are examples of documentation that should help you understand more:  
    """)
    st.write("* What You Need to Know about Machine Learning [:material/download: ](https://mmisolpoghkkvyspwayj.supabase.co/storage/v1/object/public/academyhub-bucket//q7-ML1-WYNKAML.pdf)")

        

with c[1]:
    st.image("images/ml1.png")