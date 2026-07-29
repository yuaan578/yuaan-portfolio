import streamlit as st
import random

st.set_page_config(page_title="Portfolio | SIPPAWIT AROONLARP", page_icon="👌", layout="wide")
col1, col2 = st.columns([1, 2.5]) 
with col1:
    st.image("yuaan.jpg")
with col2:
    st.title("Sippawit Aroonlarp (Yuaan)")
    st.subheader("Full Stack Developer & Game Designer")
    st.write("Yuaan is tuff")


st.divider()

tab1,tab2,tab3,tab4 = st.tabs(["Experience & Education", "Projects & Skills", "Minigames", "Job"])

with tab1:
    st.markdown("Experience in working")
    st.write("- ** 2026 : Present: ** Software developer, Front End")
    st.write("- teacher and sharinbg simple program education (Roblox studio / lua), scratch, Thunkable, Blocky, C#, C#, C++, Python")


    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Education")
    st.write("-2032 - 2036:** Computer Engineering, University of Oxford")

# --- แท็บที่ 2: โปรเจกต์และทักษะ ---
with tab2:
    st.markdown("### 🛠️ ทักษะ (Skills)")
    st.write("**Programming & Tech:** Python, React, Firebase, Vercel, n8n, Scratch")
    st.write("**Interests:** Web Development, Data Automation, Photography (Canon EOS R50)")

    st.markdown("### 🌟 ผลงานเด่น (Projects)")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        with st.container(border=True):
            st.markdown("#### 💰 WealthFlow Web App")
            st.write("พัฒนาเว็บไซต์สำหรับบันทึกรายรับ-รายจ่าย และติดตามพอร์ตการลงทุนส่วนตัว โดยใช้ React และเชื่อมต่อฐานข้อมูลด้วย Firebase เพื่อการจัดการการเงินอย่างเป็นระบบ")
    with col_p2:
        with st.container(border=True):
            st.markdown("#### 🤖 Data Automation System")
            st.write("สร้างระบบประมวลผลข้อมูลอัตโนมัติด้วย n8n (ตั้งค่า MQTT nodes) ร่วมกับ Scratch เพื่อดึงและบันทึกข้อมูลทางการเงินลงใน Google Sheets อัตโนมัติ")
            
    # เพิ่มโปรเจกต์ใหม่ที่นี่
    col_p3, col_p4 = st.columns(2)
    with col_p3:
        with st.container(border=True):
            st.markdown("#### ✈️ Travel Diary Web App")
            st.write("เว็บแอปพลิเคชันสำหรับบันทึกเรื่องราวและไดอารี่การท่องเที่ยว พัฒนาด้วย React ช่วยให้เก็บความทรงจำ สถานที่ และรูปภาพได้อย่างเป็นระเบียบ")
    with col_p4:
        with st.container(border=True):
            st.markdown("#### 🌳 Family Tree Web App")
            st.write("เว็บแอปพลิเคชันสร้างและแสดงแผนผังครอบครัว พัฒนาด้วย React เพื่อจัดการความสัมพันธ์และประวัติข้อมูลของสมาชิกในครอบครัวได้อย่างง่ายดายและสวยงาม")

    with game_col1:
        with st.container(border=True):
            st.markdown("#### The Game of Rock Paper Scissors")
            choices = ["Rock", "Paper", "Scissors"]
            user_choice = st.radio("choose your weapon:", choices, horizontal=True)

            if st.button("The Game of Rock Paper Scissors"):
                bot_choice = random.choice(choices)

                st.write(f"I choose: **{bot_choice}**")

                if user_choice == bot_choice:
                    st.info("We tied")
                elif (user_choice == "Rock" and bot_choice == "Scissors") or \
                     (user_choice == "Scissors" and bot_choice == "Paper") or \
                     (user_choice == "Paper" and bot_choice == "Rock"):
                    st.success("You Win!!")
                else:
                    st.error("You lost! try again")


    with game_col2:
        with st.container(border=True):
            st.markdown("The number guessing game(1-50)")


            if "target_num" not in st.session_state:
                st.session_state.target_num = random.randint(1, 50)
                st.session_state.attempts = 0

            guess = st.number_input("Insert your gueesed number:", min_value=1, max_value=50, steps=1)

            col_btn1, col_btn2 = st.columns([1,1])
            with col_btn1:
                if st.button("Guess the number!"):
                    st.session_state.attempts += 1
                    if guess < st.session_state.target_num:
                        st.warning(f"Attempt {st.session_state.attempts}: is too low")
                    elif guess > st.session_state.target_num:
                        st.warning(f"Attempt {st.session_state.attempts}: is too high")
                    else:
                        st.success(f"Correct the answer is {st.session_state.target_num} (You guessed {st.session_state.attempts} times)")
                        st.balloons()
            with col_btn2:
                if st.button("restart the game"):
                    st.session_state.target_num = random.randint(1, 50)
                    st.session_state.attempts = 0
                    st.info("The game has been reseted! You may take you guess")