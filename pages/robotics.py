import streamlit as st

st.set_page_config(page_title="Robotics", page_icon=":material/precision_manufacturing:", layout="wide", initial_sidebar_state="collapsed")

st.title("Robotics :material/precision_manufacturing:")

c = st.columns([1,1])

with c[0]:
    q1 = st.expander("1st Quarter", expanded=False, icon=":material/arrow_drop_down:") 
    with q1:
        st.write("#### Subjects:")
        if st.button("Mathematical Foundations", key="math_foundations", help="Mathematical Foundations Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Introduction to Computational Robotics", key="intro_robotics", help="Introduction to Computational Robotics Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("3D Mechanism CAD", key="3d_cad", help="3D Mechanism CAD Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Structured Programming", key="structured_programming", help="Structured Programming Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Communication and Digital Skills", key="digital_skills", help="Communication and Digital Skills Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

    q3 = st.expander("3rd Quarter", expanded=False, icon=":material/arrow_drop_down:")

    with q3:
        st.write("#### Subjects:")
        if st.button("Thought Development and Decision Making", key="decision_making", help="Thought Development and Decision Making Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Integral Calculus", key="integral_calculus", help="Integral Calculus Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Digital Systems", key="digital_systems", help="Digital Systems Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Rigid Body Mechanics", key="rigid_mechanics", help="Rigid Body Mechanics Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Microcontroller Programming", key="microcontrollers", help="Microcontroller Programming Books", use_container_width=True):
            st.switch_page("pages/robotics.py")
        

    q5 = st.expander("5th Quarter", expanded=False, icon=":material/arrow_drop_down:")

    with q5:
        st.write("#### Subjects:")
        if st.button("Differential Equations", key="diff_equations", help="Differential Equations Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Peripheral Programming", key="peripheral_prog", help="Peripheral Programming Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Industrial Robot Programming", key="industrial_robots", help="Industrial Robot Programming Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Computational Modeling", key="computational_modeling", help="Computational Modeling Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

    q7 = st.expander("7th Quarter", expanded=False, icon=":material/arrow_drop_down:")

    with q7:
        st.write("#### Subjects:")
        if st.button("Real-Time Operating Systems", key="rtos", help="Real-Time Operating Systems Books", use_container_width=True):
            st.switch_page("pages/rtos.py")

        if st.button("Control Engineering", key="control_eng", help="Control Engineering Books", use_container_width=True):
            st.switch_page("pages/control_eng.py")

        if st.button("Digital Image Processing", key="image_processing", help="Digital Image Processing Books", use_container_width=True):
            st.switch_page("pages/image_processing.py")

        if st.button("Machine Learning I", key="ml1", help="Machine Learning I Books", use_container_width=True):
            st.switch_page("pages/ml1.py")

        if st.button("Probability and Statistics", key="prob_stats", help="Probability and Statistics Books", use_container_width=True):
            st.switch_page("pages/prob_stats.py")

    q9 = st.expander("9th Quarter", expanded=False, icon=":material/arrow_drop_down:")

    with q9:
        st.write("#### Subjects:")
        if st.button("Computer Vision Systems", key="computer_vision", help="Computer Vision Systems Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Advanced Robotics", key="advanced_robotics", help="Advanced Robotics Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Intelligent Control Systems", key="intelligent_control", help="Intelligent Control Systems Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Industrial Automation", key="industrial_automation", help="Industrial Automation Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Robotics Research and Development", key="robotics_rd", help="Robotics Research and Development Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

with c[1]:

    q2 = st.expander("2nd Quarter", expanded=False, icon=":material/arrow_drop_down:")

    with q2:
        st.write("#### Subjects:")
        if st.button("Socioemotional Skills and Conflict Management", key="conflict_management", help="Socioemotional Skills and Conflict Management Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Differential Calculus", key="diff_calculus", help="Differential Calculus Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Physics", key="physics", help="Physics Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Mechatronic and Robotic Systems Maintenance", key="system_maintenance", help="Mechatronic and Robotic Systems Maintenance Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Industrial Safety and Hygiene", key="industrial_safety", help="Industrial Safety and Hygiene Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

    q4 = st.expander("4th Quarter", expanded=False, icon=":material/arrow_drop_down:")

    with q4:
        st.write("#### Subjects:")
        if st.button("Multivariable Calculus", key="multivariable_calc", help="Multivariable Calculus Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Electronic Interface Systems", key="interface_systems", help="Electronic Interface Systems Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Robot Kinematics and Dynamics", key="robot_dynamics", help="Robot Kinematics and Dynamics Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Programmable Logic Controllers", key="plc", help="Programmable Logic Controllers Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Manufacturing Processes and Metrology", key="metrology", help="Manufacturing Processes and Metrology Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

    q6 = st.expander("6th Quarter", expanded=False, icon=":material/arrow_drop_down:")

    with q6:    
        st.write("#### Subjects:")
        if st.button("Internship", key="internship", help="Internship info", use_container_width=True):
            st.switch_page("pages/robotics.py")

    q8 = st.expander("8th Quarter", expanded=False, icon=":material/arrow_drop_down:")

    with q8:
        st.write("#### Subjects:")
        if st.button("Neural Networks", key="neural_nets", help="Neural Networks Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Mobile Robotics", key="mobile_robotics", help="Mobile Robotics Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Autonomous Robot Control", key="autonomous_control", help="Autonomous Robot Control Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Digital Design and Manufacturing", key="digital_manufacturing", help="Digital Design and Manufacturing Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Machine Learning II", key="ml2", help="Machine Learning II Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

        if st.button("Hydraulic and Pneumatic Systems", key="hydraulic_pneumatic", help="Hydraulic and Pneumatic Systems Books", use_container_width=True):
            st.switch_page("pages/robotics.py")

    q10 = st.expander("10th Quarter", expanded=False, icon=":material/arrow_drop_down:")

    with q10:
        st.write("#### Subjects:")
        if st.button("Internship", key="internship2", help="Internship info", use_container_width=True):
            st.switch_page("pages/robotics.py")
