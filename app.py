import streamlit as st

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

if "profile" not in st.session_state:
    st.session_state.profile = {}

if "diagnostic_completed" not in st.session_state:
    st.session_state.diagnostic_completed = False

if "topic_scores" not in st.session_state:
    st.session_state.topic_scores = {}


# -----------------------------
# QUESTIONS
# -----------------------------

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
# LEARNING AREA
# -----------------------------

else:

    profile = st.session_state.profile

    st.success(f"Welcome, {profile['name']}! 🎉")


    # -------------------------
    # DIAGNOSTIC
    # -------------------------

    if not st.session_state.diagnostic_completed:

        st.header("🧠 AI Knowledge Diagnostic")

        st.write(
            "Let's understand what you already know "
            "before creating your learning path."
        )

        answers = {}

        for i, q in enumerate(questions):

            st.markdown(f"### Question {i + 1}")

            answers[i] = st.radio(
                q["question"],
                q["options"],
                key=f"question_{i}"
            )

        if st.button(
            "📊 Calculate My AI Knowledge",
            type="primary"
        ):

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
            st.session_state.diagnostic_completed = True

            st.rerun()


    # -------------------------
    # PERSONALIZED PATH
    # -------------------------

    else:

        scores = {}

        for topic, result in st.session_state.topic_scores.items():

            percentage = int(
                result["correct"] /
                result["total"] *
                100
            )

            scores[topic] = percentage


        st.header("📊 Your AI Knowledge Profile")

        columns = st.columns(len(scores))

        for column, (topic, score) in zip(
            columns,
            scores.items()
        ):

            with column:

                st.metric(
                    topic,
                    f"{score}%"
                )

                st.progress(score / 100)


        st.divider()

        st.header("🗺️ Your Personalized Learning Path")

        st.write(
            "Your learning path is based on your diagnostic results."
        )


        # Sort topics from weakest to strongest

        sorted_topics = sorted(
            scores.items(),
            key=lambda item: item[1]
        )


        for index, (topic, score) in enumerate(sorted_topics):

            if score >= 80:

                status = "✅ Strong"

            elif score >= 50:

                status = "📘 Practice More"

            else:

                status = "🔴 Priority"


            col1, col2, col3 = st.columns([1, 4, 2])

            with col1:
                st.write(f"**{index + 1}**")

            with col2:
                st.write(f"### {topic}")

            with col3:
                st.write(status)


            st.progress(score / 100)


        st.divider()


        # Weakest topic

        weakest_topic = sorted_topics[0][0]
        weakest_score = sorted_topics[0][1]


        st.subheader("🎯 Your Recommended Focus")

        st.warning(
            f"Your current priority is **{weakest_topic}** "
            f"with a starting mastery of **{weakest_score}%**."
        )


        st.info(
            "AI StudyMate will give you targeted lessons "
            "and practice questions for this topic."
        )


        if st.button(
            "🤖 Start My Personalized Lesson",
            type="primary"
        ):

            st.session_state.current_topic = weakest_topic

            st.success(
                f"Great! Let's start learning **{weakest_topic}**."
            )
