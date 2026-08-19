import streamlit as st
import random
import requests
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="Portfolio | SIPPAWIT AROONLARP", page_icon="👌", layout="wide")
lottie_coding = load_lottieurl("https://lottie.host/8061df43-1698-4c91-a185-181514736f1c/J77626tI7y.json")

col1, col2 = st.columns([1, 2.5]) 
with col1:
    if lottie_coding:
        st_lottie(lottie_coding, height=220, key="coding")
    else:
        st.image("yuaan.jpg")
with col2:
    st.title("Sippawit Aroonlarp (Yuaan)")
    st.subheader("Educator")
    st.write("Yuaan is tuff")

st.divider()

selected = option_menu(
    menu_title=None,
    options=["Experience & Education", "Projects & Skills", "Minigames"],
    icons=["briefcase", "rocket", "controller"], # ลบ "envelope" ออกเพราะตอนนี้มีแค่ 3 เมนู
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "icon": {"color": "#ffaa00", "font-size": "20px"}, 
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#333333"},
        "nav-link-selected": {"background-color": "#ca2a37"},
    }
)

# --- แท็บที่ 1: ประวัติ ---
if selected == "Experience & Education":
    st.markdown("### Experience in working")
    st.write("- ** 2026 : Present: ** educator, secondary education years")
    st.write("- student and sharing simple program education (Roblox studio / lua), scratch, Thunkable, Blocky, C#, C#, C++, Python")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Education")
    st.write("- **2020 - 2026:** educating, SISB SCHOOLS")

# --- แท็บที่ 2: โปรเจกต์และทักษะ ---
if selected == "Projects & Skills":
    st.markdown("### 🛠️ ทักษะ (Skills)")
    st.write("**Programming & Tech:** Python, React, Firebase, Vercel, n8n, Scratch")
    st.write("**Interests:** Web Development, Data Automation, Photography (Canon EOS R50)")

    st.markdown("### 🌟 ผลงานเด่น")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        with st.container(border=True):
            st.markdown("#### Can speak Three Languages!!!")
            st.write("Thai, chinese, and english")
    with col_p2:
        with st.container(border=True):
            st.markdown("#### Math level")
            st.write("Math Kumon level J equivilent to Year 10")
            
    col_p3, col_p4 = st.columns(2)
    with col_p3:
        with st.container(border=True):
            st.markdown("#### Robox studio obby games")
            st.write("A roblox obby game with high competition to complete")
    with col_p4:
        with st.container(border=True):
            st.markdown("#### Acing Thai language")
            st.write("Getting A* in thai language over the years")

# --- แท็บที่ 3: มินิเกม (Mini Games) ---
if selected == "Minigames":
    st.markdown("### 🎮 python minigames")
    st.write("try the minigames written with python on streamlit")
    
    game_col1, game_col2 = st.columns(2)
    
    # เกมที่ 1: เป่ายิ้งฉุบ
    with game_col1:
        with st.container(border=True):
            st.markdown("#### ✌️✊✋ rock")
            choices = ["rock ✊", "scissor ✌️", "paper ✋"]
            user_choice = st.radio("เลือกอาวุธของคุณ:", choices, horizontal=True)
            
            if st.button("เป่ายิ้งฉุบ!"):
                bot_choice = random.choice(choices)
                
                st.write(f"🤖 bot chooses: **{bot_choice}**")
                
                if user_choice == bot_choice:
                    st.info("oh we made the same choice 😲")
                elif (user_choice == "rock ✊" and bot_choice == "scissor ✌️") or \
                     (user_choice == "scissor ✌️" and bot_choice == "paper ✋") or \
                     (user_choice == "paper ✋" and bot_choice == "rock ✊"):
                    st.success("You win! 🎉")
                else:
                    st.error("You lost! try again next time 😭")

    # เกมที่ 2: ทายตัวเลข
    with game_col2:
        with st.container(border=True):
            st.markdown("#### 🔢 guessing number game (1-50)")
            
            # ใช้ session_state เพื่อเก็บค่าตัวเลขเป้าหมายไม่ให้เปลี่ยนทุกครั้งที่กดปุ่ม
            if 'target_num' not in st.session_state:
                st.session_state.target_num = random.randint(1, 50)
                st.session_state.attempts = 0

            guess = st.number_input("ใส่ตัวเลขที่ทาย:", min_value=1, max_value=50, step=1)
            
            col_btn1, col_btn2 = st.columns([1, 1])
            with col_btn1:
                if st.button("ทายตัวเลข!"):
                    st.session_state.attempts += 1
                    if guess < st.session_state.target_num:
                        st.warning(f"ครั้งที่ {st.session_state.attempts}: น้อยไปครับ! 🔼")
                    elif guess > st.session_state.target_num:
                        st.warning(f"ครั้งที่ {st.session_state.attempts}: มากไปครับ! 🔽")
                    else:
                        st.success(f"🎉 correct the answer is {st.session_state.target_num} (you took  {st.session_state.attempts} attempts)")
                        st.balloons() # เอฟเฟกต์ลูกโป่งตอนชนะ
            with col_btn2:
                if st.button("new game 🔄"):
                    st.session_state.target_num = random.randint(1, 50)
                    st.session_state.attempts = 0
                    st.info("A new game has started you may procced")