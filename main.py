import streamlit as st
import random

st.set_page_config(page_title="Portfolio | SIPPAWIT AROONLARP", page_icon="👌", layout="wide")
col1, col2 = st.columns([1, 2.5]) 
with col1:
    st.image("yuaan.jpg")
with col2:
    st.title("Sippawit Aroonlarp (Yuaan)")
    st.subheader("educator")
    st.write("Yuaan is tuff")


st.divider()

tab1,tab2,tab3,tab4 = st.tabs(["Experience & Education", "Projects & Skills", "Minigames", "Job"])

with tab1:
    st.markdown("Experience in working")
    st.write("- ** 2026 : Present: ** educator, secondary education years")
    st.write("- student and sharinbg simple program education (Roblox studio / lua), scratch, Thunkable, Blocky, C#, C#, C++, Python")


    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Education")
    st.write("-2020 - 2026:** educating, SISB SCHOOLS")

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


# --- แท็บที่ 3: มินิเกม (Mini Games) ---
with tab3:
    st.markdown("### 🎮 มินิเกม Python สำหรับคลายเครียด")
    st.write("ทดลองเล่นมินิเกมที่เขียนขึ้นด้วยภาษา Python และทำงานบน Streamlit ได้เลยครับ!")
    
    game_col1, game_col2 = st.columns(2)
    
    # เกมที่ 1: เป่ายิ้งฉุบ
    with game_col1:
        with st.container(border=True):
            st.markdown("#### ✌️✊✋ เกมเป่ายิ้งฉุบ")
            choices = ["ค้อน ✊", "กรรไกร ✌️", "กระดาษ ✋"]
            user_choice = st.radio("เลือกอาวุธของคุณ:", choices, horizontal=True)
            
            if st.button("เป่ายิ้งฉุบ!"):
                bot_choice = random.choice(choices)
                
                st.write(f"🤖 บอทเลือก: **{bot_choice}**")
                
                if user_choice == bot_choice:
                    st.info("เสมอ! ใจตรงกันเลย 😲")
                elif (user_choice == "ค้อน ✊" and bot_choice == "กรรไกร ✌️") or \
                     (user_choice == "กรรไกร ✌️" and bot_choice == "กระดาษ ✋") or \
                     (user_choice == "กระดาษ ✋" and bot_choice == "ค้อน ✊"):
                    st.success("คุณชนะ! 🎉")
                else:
                    st.error("คุณแพ้! ลองใหม่นะ 😭")

    # เกมที่ 2: ทายตัวเลข
    with game_col2:
        with st.container(border=True):
            st.markdown("#### 🔢 เกมทายใจตัวเลข (1-50)")
            
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
                        st.success(f"🎉 ถูกต้อง! คำตอบคือ {st.session_state.target_num} (คุณทายไป {st.session_state.attempts} ครั้ง)")
                        st.balloons() # เอฟเฟกต์ลูกโป่งตอนชนะ
            with col_btn2:
                if st.button("เริ่มเกมใหม่ 🔄"):
                    st.session_state.target_num = random.randint(1, 50)
                    st.session_state.attempts = 0
                    st.info("รีเซ็ตเกมเรียบร้อย! เริ่มทายใหม่ได้เลย")