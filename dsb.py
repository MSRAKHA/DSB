import time
import streamlit as st
from PIL import Image
import base64
from datetime import datetime

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'
if 'wishes' not in st.session_state:  # Add this line for wishes
    st.session_state.wishes = []

# Page configuration
st.set_page_config(
    page_title="Happy Birthday Dr. Soni Bhavani!",
    page_icon="🎉",
    layout="wide"
)

# Navigation breadcrumb
def create_breadcrumb():
    pages = {
        "Birthday Wishes": "🎂 Birthday",
        "Memories": "🏫 Memories",
        "Our Fights": "⚡ Our Fights",
        "Friendship Moments": "💖 Friendship",
        "Home": "🏠 Home"
    }
    
    cols = st.columns([1.2, 1.2, 1.2, 1.2, 1])
    
    for (page, label), col in zip(pages.items(), cols):
        with col:
            if st.button(label):
                st.session_state.current_page = page
    
    return st.session_state.current_page

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #fde2e4;
    }
    .title {
        color: #ff4b6e;
        text-align: center;
        font-size: 50px;
        font-family: 'Brush Script MT', cursive;
    }
    .quote {
        color: Black;
        font-size: 24px;
        font-style: italic-bold;
        text-align: center;
        padding: 0px;
        
    }
    .memory-card {
        background-color: #fff5f5;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .fight-card {
        background-color: #ffe5e5;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .friendship-card {
        background-color: #fff0f3;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        width: 100%;
        background-color: #ff4b6e;
        color: white;
        border-radius: 5px;
        padding: 10px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #ff6b8b;
        color: white;
    }
    .countdown {
        text-align: center;
        font-size: 24px;
        color: #ff4b6e;
        padding: 15px;
        background: rgba(255, 75, 110, 0.1);
        border-radius: 10px;
        margin: 20px 0;
        animation: pulse 2s infinite;
    }
    .wish-card {
        background-color: #fff0f3;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        border-left: 4px solid #ff4b6e;
        animation: slideIn 0.5s ease-out;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    @keyframes slideIn {
        from { transform: translateX(-20px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    .age-calculator {
        background: linear-gradient(135deg, #ff4b6e15, #ff4b6e30);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        animation: fadeIn 1s ease-in;
    }
    .age-title {
        font-size: 24px;
        color: #ff4b6e;
        margin-bottom: 10px;
        font-weight: bold;
    }
    .age-number {
        font-size: 36px;
        color: #ff4b6e;
        font-family: 'Courier New', monospace;
        margin: 10px 0;
        font-weight: bold;
        animation: pulse 2s infinite;
    }
    .age-label {
        font-size: 18px;
        color: #ff4b6e;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .age-calculator {
        
            text-align: center;
        font-size: 24px;
        color: #ff4b6e;
        padding: 15px;
        background: rgba(255, 75, 110, 0.1);
        border-radius: 10px;
        margin: 20px 0;
        animation: pulse 2s infinite;
    }
    .age-title {
        font-size: 24px;
        color: #ff4b6e;
        margin-bottom:18px;
        font-weight: bold;
    }
    .age-number {
        font-size: 36px;
        color: #ff4b6e;
        font-family: 'Courier New', monospace;
        margin: 10px 0;
        font-weight: bold;
        animation: pulse 2s infinite;
    }
    .age-label {
        font-size: 18px;
        color: #ff4b6e;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
    """, unsafe_allow_html=True)
# Add these two new functions here
def countdown_timer():
    today = datetime.now()
    birthday = datetime(today.year, 12, 29)
    if today > birthday:
        birthday = datetime(today.year + 1, 12, 29)
    delta = birthday - today
    st.markdown(f"""
        <div class='countdown'>
            🎉 {delta.days} days until the next birthday! 🎉
        </div>
    """, unsafe_allow_html=True)
def calculate_age():
    # Birth date - December 29, 2000 (adjust the year as needed)
    birth_date = datetime(2000, 12, 29)
    today = datetime.now()
    
    # Calculate age with decimal points
    age_timedelta = today - birth_date
    age_years = age_timedelta.days / 365.25
    
    st.markdown(f"""
         <div class='age-calculator'>
            Current Age {age_years:.8f} years old 
            
        </div>
    """, unsafe_allow_html=True)

def add_wishes():
    st.markdown("<h3 style='text-align: center;'>✨ Leave a Birthday Wish ✨</h3>", unsafe_allow_html=True)
    with st.form("wish_form"):
        col1, col2 = st.columns([2, 1])
        with col1:
            wish = st.text_area("Your Message", placeholder="Write your birthday wish here...")
        with col2:
            name = st.text_input("Your Name", placeholder="Enter your name")
        
        submit_wish = st.form_submit_button("Send Wish 🎁")
        if submit_wish and wish and name:
            st.session_state.wishes.append({
                "name": name,
                "message": wish,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success("Thank you for your wish! 🎉")

    if st.session_state.wishes:
        st.markdown("<h3 style='text-align: center;'>💝 Birthday Wishes 💝</h3>", unsafe_allow_html=True)
        for wish in reversed(st.session_state.wishes):
            st.markdown(f"""
                <div class='wish-card'>
                    <p><strong>{wish['name']}</strong> says:</p>
                    <p>{wish['message']}</p>
                    <small>{wish['timestamp']}</small>
                </div>
            """, unsafe_allow_html=True)
# Get current page
current_page = create_breadcrumb()

# Content based on current page
if current_page == 'Home':
    st.markdown("<h1 class='title'>✨ 🎂 Happy Birthday  ✨</h1>", unsafe_allow_html=True)
    #rainbow 
    st.title("**:rainbow[Dr. Dhamam Soni Bhavani! From MS Rakha (Sofware Engineer)]**")
    
     # Create two columns for countdown and age calculator
    col1, col2 = st.columns(2)
    
    with col1:
        countdown_timer()
    
    with col2:
        calculate_age()
    st.balloons()
    time.sleep(1)
    st.snow()
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("images/dr.sonibhavani.png", 
                 caption="Representing our amazing doctor!")

    quotes = [
        "A doctor's heart is where healing begins. Happy Birthday to an amazing healer!",
        "Your dedication to saving lives makes you extraordinary. Celebrate your special day!",
        "To the person who makes medicine look magical - Happy Birthday!",
        "Your compassion heals more than medicine ever could. Have a wonderful birthday!"
    ]

    for quote in quotes:
        st.markdown(f"<p class='quote'>{quote}</p>", unsafe_allow_html=True)

elif current_page == 'Memories':
    st.markdown("<h1 class='title'>🏫 School Days</h1>", unsafe_allow_html=True)
    
    memories = [
        {
            "title": "First Day in Class",
            "year": "2007",
            "description": "Remember how we met in 3RD standard Telugu class? You were the one who helped me understand Telugu becuase you are a daughter of our class Teacher!"
        },
        {
            "title": "Study Sessions",
            "year": "2015",
            "description": "Those countless hours we spent studying together, sharing notes, and dreaming about becoming doctors."
        },
        {
            "title": "Biology Classes",
            "year": "2016",
            "description": "Remember when we discussed about Heart Pumping System? You were the one who helped me understand whole concepts of Biology :)"
        }
    ]
    
    for memory in memories:
        st.markdown(f"""
        <div class='memory-card'>
            <h3>{memory['title']} ({memory['year']})</h3>
            <p>{memory['description']}</p>
        </div>
        """, unsafe_allow_html=True)

elif current_page == 'Our Fights':
    st.markdown("<h1 class='title'>⚡ The Times We Fought</h1>", unsafe_allow_html=True)
   
        
    
    
    fights = [
        {
            "title": "The Great Debate",
            "resolution": "Ended with ice cream and laughter",
            "lesson": "Sometimes the silliest arguments make the strongest friendships"
        },
        {
            "title": "The Competition",
            "resolution": "Realized we're better as a team",
            "lesson": "Competition made us both better students"
        }
    ]
    
    for fight in fights:
        st.markdown(f"""
        <div class='fight-card'>
            <h3>{fight['title']}</h3>
            <p>How it ended: {fight['resolution']}</p>
            <p>What we learned: {fight['lesson']}</p>
        </div>
        """, unsafe_allow_html=True)

elif current_page == 'Friendship Moments':
    st.markdown("<h1 class='title'>💖 Friendship Moments</h1>", unsafe_allow_html=True)
    
    moments = [
        {
            "title": "Study Buddies",
            "description": "All those study sessions and coffee breaks and Fighting Unknowingly sometimes knowingly just to tease you and make you laugh and irritated."
        },
        {
            "title": "Celebration Time",
            "description": "When we both celebrate each other success together Happily"
        }

    ]
    
    for moment in moments:
        st.markdown(f"""
        <div class='friendship-card'>
            <h3>{moment['title']}</h3>
            <p>{moment['description']}</p>
        </div>
        """, unsafe_allow_html=True)

elif current_page == 'Birthday Wishes':
    st.markdown("<h1 class='title'>🎂 Birthday Celebrations</h1>", unsafe_allow_html=True)
    st.balloons()
 

    st.markdown("""
    <div style='text-align: center; padding: 20px; background-color: #fff5f5; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);'>
        <h2>Dear Soni,</h2>
        <p style='font-size: 20px;'>
        From our school days to seeing you become an amazing doctor, you've always been an inspiration. 
        Your dedication, compassion, and brilliance make you special. 
        May your birthday be as wonderful as the countless lives you've touched.
        </p>
        <h3>Wishing you:</h3>
        <ul style='list-style-type: none;'>
            <li>🌟 Success in all your endeavors</li>
            <li>💖 Love and happiness</li>
            <li>✨ Good health and prosperity</li>
            <li>🎉 Countless moments of joy</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
  
    # Photo gallery
    st.write("---")
    st.subheader("📸 Memories Through the Years")
    st.write("Here are some photos from our school days and graduation.")
    col1, col2, col3 ,col4  = st.columns([1,1,1 ,1])
    with col1:
        st.image("images/eiffeltower.png", caption="School Days", use_container_width =True)
    

    with col4:
        st.image("images/docter.png", caption="Dr. Soni Bhavani Graduation " ,use_container_width =True)

    with col3:
        st.image("images/life.png", caption="Docter's Life", use_container_width =True)

    with col2 :
        st.image("images/anchor.png", caption="Our School Farewell Achoring", use_container_width =True)

    col5, col6, col7 ,col8  = st.columns([1,1,1 ,1])
    with col5:
    
        st.image("images/school.png", caption="School Days")

    with col6:
        st.image("images/mem.png", caption="Memories")

    with col7:
        st.image("images/lau.png", caption="Laughing")

    with col8 :
        st.image("images/fig.png", caption="Fights")
    
    st.video("images/video.mp4")
    add_wishes()


# Footer
st.markdown("""
<div style='text-align: center; padding: 20px; margin-top: 50px;'>
    <p style='font-size: 24px;'>With love and best wishes ❤️</p>
    <p style='font-size: 20px;'>Your School Friend Rakha MS</p>
</div>
""", unsafe_allow_html=True)
