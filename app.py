import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI StudyMate",
    page_icon="🎓",
    layout="wide"
)

# Title
st.title("🎓 AI StudyMate")
st.subheader("Your personalised AI tutor for learning AI")

st.write(
    "Learn AI at your own level. "
    "AI StudyMate understands what you already know, "
    "creates a learning path for you, and adapts as you learn."
)

st.divider()

# Welcome section
st.header("🚀 Start Your Learning Journey")

st.write("Tell us a little about yourself so we can personalise your learning experience.")

# Learner profile
name = st.text_input("👤 Your Name")

level = st.selectbox(
    "📚 What is your current AI level?",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

goal = st.selectbox(
    "🎯 What is your main goal?",
    [
        "Learn AI fundamentals",
        "Build AI projects",
        "Prepare for a job",
        "Learn Generative AI",
        "Learn AI Agents"
    ]
)

study_time = st.selectbox(
    "⏱️ How much time can you study each day?",
    [
        "15 minutes",
        "30 minutes",
        "1 hour",
        "2+ hours"
    ]
)

if st.button("✨ Create My Learning Path", type="primary"):
    if name.strip():
        st.success(f"Welcome, {name}! 🎉")

        st.write("### Your starting profile")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Level", level)

        with col2:
            st.metric("Daily Study", study_time)

        with col3:
            st.metric("Goal", goal)

        st.info(
            "Your personalised diagnostic test will be the next step. "
            "It will help us understand what you already know."
        )
    else:
        st.warning("Please enter your name first.")
