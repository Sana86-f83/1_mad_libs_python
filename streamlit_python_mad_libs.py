import base64
import os
import streamlit as st

# Set page configuration (must be the first Streamlit command)
st.set_page_config(
    page_title="1-Mad_Libs_Story",
    page_icon="📖",  # Default book emoji
    layout="centered"
)

# Function to Convert Local Image to Base64
def set_bg(local_img_path):
    if os.path.exists(local_img_path):
        with open(local_img_path, "rb") as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode()
        bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """
        st.markdown(bg_img, unsafe_allow_html=True)
    else:
        st.error(f"⚠️ Background image not found: {local_img_path}")

set_bg("images/big_image4.jpg")

# Custom CSS for the app
st.markdown(
    """
    <style>
    .title {
        text-align: center;
        text-transform: uppercase;
        color: rgb(70, 207, 70) !important;
        font-weight: bold;
        animation: fadeIn 2s ease-in-out;
        transition: color 0.3s ease-in-out;
    }
    .title:hover {
        color: #0756a5 !important;
    }
    .stButton button {
        background-color: #1e90ff; /* Dark blue for buttons */
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #0077cc; /* Slightly darker blue on hover */
    }
    .story-box {
        background-color: rgba(255, 255, 255, 0.9); /* Semi-transparent white background */
        padding: 20px;
        color: #333333;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        border-bottom: 5px solid #1e90ff; /* Dark blue left border */
        border-left: 5px solid #1e90ff; /* Dark blue left border */


    }
    .feedback-card {
        background-color: rgba(240, 248, 255, 0.9); /* Semi-transparent light blue for feedback card */
        padding: 20px;
        color: #333333;
        font-size: large;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        margin-bottom: 10px;
        border-left: 5px solid #1e90ff; /* Dark blue left border */
        border-bottom: 5px solid #1e90ff; /* Dark blue left border */

    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for multi-page navigation
if "page" not in st.session_state:
    st.session_state.page = "input_page"

# Function to display the input page
def input_page():
    # Custom HTML for colored page title and icon (only on input page)
    st.markdown(
        """
        <h1 style="color: #1e90ff; text-align: center;">
            <span style="font-size: 1.5em;">📚 Mad Libs 📖 </span>
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='title'> My Amazing Teacher </h1>", unsafe_allow_html=True)
    st.write("Fill in the details below to create a story about your class!")

    # Input field for teacher's name
    st.session_state.teacher_name = st.text_input("1. 👨‍🏫 Enter your teacher's name:")

    # Dropdown for topic selection
    st.session_state.topic = st.selectbox(
        "2. Select a Programming topic for your story:",
        ["Python", "Nextjs", "Typescript", "Html/Css"],
    )

    # Input fields with short hints and emojis
    st.session_state.class_timing = st.selectbox(
        "3. 🕒 Enter your class timing:",
        ["Morning 09am - 12pm", "Afternoon 02pm - 05pm", "Evening 07pm - 10pm"],
    )
    st.session_state.class_day = st.selectbox(
        "4. 📅 Enter your class day:",
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    )
    st.session_state.python_topic = st.text_input(f"5. 📚 Enter a {st.session_state.topic} topic you learned:")
    st.session_state.teaching_style = st.text_input("6. 🎓 Enter a word to describe your teacher's teaching style:")
    st.session_state.class_activity = st.text_input("7. 🎲 Enter a class activity:")
    st.session_state.favourite_moment = st.text_input("8. 🌟 Enter your favourite moment in class:")
    st.session_state.homework_assignment = st.text_input("9. 📝 Enter the homework assignment:")
    st.session_state.class_date = st.text_input("10. 📅 Enter the date of the class:")
    st.session_state.feedback = st.text_input("11. 💬 Enter your feedback about your teacher:")

    # Generate the story when the user clicks the button
    if st.button("✨ Generate Story"):
        if (
            st.session_state.teacher_name
            and st.session_state.class_timing
            and st.session_state.class_day
            and st.session_state.python_topic
            and st.session_state.teaching_style
            and st.session_state.class_activity
            and st.session_state.favourite_moment
            and st.session_state.homework_assignment
            and st.session_state.class_date
            and st.session_state.feedback
        ):
            st.session_state.page = "story_page"
            st.rerun()
        else:
            st.error("Please fill in all the fields to generate the story.")

# Function to display the story page
def story_page():
    # Center the story on the story page
    st.markdown(
        """
        <style>
        .story-container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        </style>
        <div class="story-container">
        """,
        unsafe_allow_html=True
    )

    st.title("📖 Your Mad Libs Story")

    # Highlight keywords with underlined text and color change
    highlight_style = """
    color: #1e90ff;
    text-decoration: underline;
    font-weight: bold;
    """

    # Mad Libs-style story template
    story = f"""
    On **<span style="{highlight_style}">{st.session_state.class_date}</span>**, during **<span style="{highlight_style}">{st.session_state.class_timing}</span>**, our {st.session_state.topic} class with **<span style="{highlight_style}">{st.session_state.teacher_name}</span>** was in full swing.  
    We learned about **<span style="{highlight_style}">{st.session_state.python_topic}</span>**, and as always, {st.session_state.teacher_name} explained it in a **<span style="{highlight_style}">{st.session_state.teaching_style}</span>** way.  

    During the class, {st.session_state.teacher_name} organized a **<span style="{highlight_style}">{st.session_state.class_activity}</span>**, and everyone was fully engaged.  
    My favourite moment was when **<span style="{highlight_style}">{st.session_state.favourite_moment}</span>**.  

    For homework, we had to **<span style="{highlight_style}">{st.session_state.homework_assignment}</span>**, and it was both challenging and fun.  
    By the end of the class, everyone thought, "**<span style="{highlight_style}">{st.session_state.feedback}</span>**!"  

    It was another amazing day in {st.session_state.topic} class with the best teacher ever! 🎉
    """

    # Display the story in a styled box
    st.markdown(
        f"""
        <div class="story-box">
        <p>{story}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Display feedback in a card-like style with colorful emoji
    st.markdown(
        f"""
        <div class="feedback-card">
        <h3>🌈 Your Feedback:</h3>
        <p>{st.session_state.feedback}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Button to go back to the input page
    if st.button("🔄 Create Another Story"):
        st.session_state.page = "input_page"
        st.rerun()

    # Close the story container
    st.markdown("</div>", unsafe_allow_html=True)

# Display the appropriate page based on session state
if st.session_state.page == "input_page":
    input_page()
elif st.session_state.page == "story_page":
    story_page()

# Footer
st.markdown(
    """
    <hr>
    <div style="text-align: center; padding: 10px; font-size: 18px; color: white;">
        © 2025 | Developed by <b style='color: #1e90ff;font-size:20px;'>Sana Faisal
        <a href="https://www.linkedin.com/in/sana-faisal-developer/" target="_blank" style="color: #4CAF50; text-decoration:none;">
            🔗 Connect on LinkedIn
        </a>
    </div>
    """,
    unsafe_allow_html=True
)