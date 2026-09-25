import streamlit as st

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="AI StudyMate",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "started" not in st.session_state:
    st.session_state.started = False

if "diagnostic_started" not in st.session_state:
    st.session_state.diagnostic_started = False

if "profile" not in st.session_state:
    st.session_state.profile = {}

# -----------------------------
# HEADER
# -----------------------------
st.title("🎓 AI StudyMate")
st.subheader("Your personalised AI tutor for learning AI")

st.write(
    "Learn AI at your own level. "
    "AI StudyMate understands what you already know, "
    "creates a learning path for you, and adapts as you learn."
)

st.divider()

# -----------------------------
# PROFILE
# -----------------------------
if not st.session_state.started:

    st.header("🚀 Start Your Learning Journey")

    st.write(
        "Tell us a little about yourself so we can "
        "personalise your learning experience."
    )

    name = st.text_input("👤 Your Name")

    level = st.selectbox(
        "📚 What is your current AI level?",
        ["Beginner", "Intermediate", "Advanced"]
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

            st.session_state.profile = {
                "name": name,
                "level": level,
                "goal": goal,
                "study_time": study_time
            }

            st.session_state.started = True
            st.rerun()

        else:
            st.warning("Please enter your name first.")

# -----------------------------
# DIAGNOSTIC TEST
# -----------------------------
else:

    profile = st.session_state.profile

    st.success(f"Welcome, {profile['name']}! 🎉")

    st.header("🧠 AI Knowledge Diagnostic")

    st.write(
        "Before creating your learning path, "
        "let's understand what you already know."
    )

    st.info(
        "Answer the following questions without searching. "
        "This helps us estimate your current knowledge."
    )

    # Questions
    questions = [
        {
            "topic": "AI Fundamentals",
            "question": "What does AI stand for?",
            "options": [
                "Automated Internet",
                "Artificial Intelligence",
                "Advanced Information",
                "Artificial Internet"
            ],
            "answer": "Artificial Intelligence"
        },
        {
            "topic": "AI Fundamentals",
            "question": "Which of these is an example of AI?",
            "options": [
                "A calculator doing 2 + 2",
                "A system recognizing objects in images",
                "A USB drive",
                "A keyboard"
            ],
            "answer": "A system recognizing objects in images"
        },
        {
            "topic": "Python",
            "question": "Which symbol is used to create a comment in Python?",
            "options": [
                "//",
                "#",
                "<!-- -->",
                "/* */"
            ],
            "answer": "#"
        },
        {
            "topic": "Python",
            "question": "Which data type stores True or False?",
            "options": [
                "String",
                "Integer",
                "Boolean",
                "List"
            ],
            "answer": "Boolean"
        },
        {
            "topic": "Machine Learning",
            "question": "What is supervised learning?",
            "options": [
                "Learning with labelled examples",
                "Learning without data",
                "Learning only from images",
                "Learning without a model"
            ],
            "answer": "Learning with labelled examples"
        },
        {
            "topic": "Machine Learning",
            "question": "What is a training dataset?",
            "options": [
                "Data used to teach a model",
                "A computer program",
                "A password",
                "A web browser"
            ],
            "answer": "Data used to teach a model"
        },
        {
            "topic": "Generative AI",
            "question": "What can a generative AI model do?",
            "options": [
                "Only store files",
                "Generate new content",
                "Only calculate numbers",
                "Only browse websites"
            ],
            "answer": "Generate new content"
        },
        {
            "topic": "Generative AI",
            "question": "What is an LLM?",
            "options": [
                "Large Language Model",
                "Long Learning Machine",
                "Large Logic Machine",
                "Language Learning Method"
            ],
            "answer": "Large Language Model"
        },
        {
            "topic": "RAG",
            "question": "What does RAG commonly stand for in AI?",
            "options": [
                "Retrieval-Augmented Generation",
                "Random AI Generation",
                "Rapid Answer Generation",
                "Recursive Agent Gateway"
            ],
            "answer": "Retrieval-Augmented Generation"
        },
        {
            "topic": "AI Agents",
            "question": "What is an AI agent designed to do?",
            "options": [
                "Only display text",
                "Perceive information and take actions toward a goal",
                "Only store information",
                "Only generate images"
            ],
            "answer": "Perceive information and take actions toward a goal"
        }
    ]

    st.write("### Answer the 10 questions")

    answers = {}

    for i, q in enumerate(questions):

        st.markdown(f"### Question {i + 1}")
        st.write(q["question"])

        answers[i] = st.radio(
            "Choose your answer:",
            q["options"],
            key=f"question_{i}"
        )

    st.divider()

    if st.button("📊 Calculate My AI Knowledge", type="primary"):

        topic_scores = {}

        for i, q in enumerate(questions):

            topic = q["topic"]

            if topic not in topic_scores:
                topic_scores[topic] = {
                    "correct": 0,
                    "total": 0
                }

            topic_scores[topic]["total"] += 1

            if answers[i] == q["answer"]:
                topic_scores[topic]["correct"] += 1

        st.session_state.topic_scores = topic_scores

        st.success("Diagnostic completed! 🎉")

        st.header("📊 Your AI Knowledge Profile")

        for topic, score in topic_scores.items():

            percentage = int(
                score["correct"] / score["total"] * 100
            )

            st.write(f"**{topic}** — {percentage}%")

            st.progress(percentage / 100)

        st.divider()

        st.header("🗺️ Your Next Step")

        scores = {
            topic: int(
                value["correct"] / value["total"] * 100
            )
            for topic, value in topic_scores.items()
        }

        weakest_topic = min(scores, key=scores.get)

        st.info(
            f"Your current focus area is **{weakest_topic}**. "
            "AI StudyMate will use this information to "
            "create your personalised learning path."
        )
