import streamlit as st

st.set_page_config(
    page_title="AI StudyMate",
    page_icon="🤖",
    layout="centered"
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

if "current_topic" not in st.session_state:
    st.session_state.current_topic = None

if "tutor_started" not in st.session_state:
    st.session_state.tutor_started = False


# -----------------------------
# TOPIC LESSONS
# -----------------------------
lessons = {
    "AI Fundamentals": {
        "title": "Understanding Artificial Intelligence",
        "lesson": """
Artificial Intelligence (AI) is the field of creating computer systems
that can perform tasks that normally require human intelligence.

Examples include:
- Understanding language
- Recognizing objects in images
- Making predictions
- Recommending content
- Making decisions from data

Think of AI as a system that receives information, processes it,
and produces an intelligent output.
""",
        "question": "In your own words, what is Artificial Intelligence?",
        "keywords": ["computer", "machine", "intelligence", "human", "task"]
    },

    "Python": {
        "title": "Python Basics for AI",
        "lesson": """
Python is one of the most commonly used programming languages in AI.

Important Python concepts for AI include:
- Variables
- Data types
- Conditions
- Loops
- Functions
- Lists and dictionaries

For example:

x = 10

Here, x is a variable containing the value 10.
""",
        "question": "Why is Python useful when learning Artificial Intelligence?",
        "keywords": ["simple", "easy", "ai", "machine", "libraries", "programming"]
    },

    "Machine Learning": {
        "title": "Introduction to Machine Learning",
        "lesson": """
Machine Learning (ML) is a branch of AI where computers learn patterns
from data.

For example, instead of manually programming a system to recognize cats,
we can provide many examples of images containing cats.

The model learns patterns from those examples and can then make
predictions on new data.
""",
        "question": "What does a machine learning model learn from?",
        "keywords": ["data", "examples", "patterns", "training"]
    },

    "Generative AI": {
        "title": "Understanding Generative AI",
        "lesson": """
Generative AI refers to AI systems that can create new content.

They can generate:
- Text
- Images
- Audio
- Video
- Code

Large Language Models (LLMs) are an important example of Generative AI.
They can generate and transform text based on the input they receive.
""",
        "question": "What makes Generative AI different from a system that only classifies information?",
        "keywords": ["create", "generate", "new", "content", "text", "image"]
    },

    "RAG": {
        "title": "Understanding RAG",
        "lesson": """
RAG stands for Retrieval-Augmented Generation.

A RAG system retrieves relevant information from a knowledge source
and provides that information to a language model before generating
an answer.

A simple flow is:

Question → Retrieve information → Generate answer
""",
        "question": "What is the main purpose of retrieving information in a RAG system?",
        "keywords": ["information", "context", "knowledge", "answer", "relevant"]
    },

    "AI Agents": {
        "title": "Introduction to AI Agents",
        "lesson": """
An AI agent is a system designed to perceive information and take
actions toward a goal.

A simple agent workflow can be:

Observe → Think → Act → Observe again

For example, an AI agent could receive a user's goal, decide what
steps are needed, use available tools, and then return the result.
""",
        "question": "What is one important difference between an AI agent and a simple chatbot?",
        "keywords": ["action", "goal", "tools", "steps", "act", "autonomous"]
    }
}


# -----------------------------
# HEADER
# -----------------------------
st.title("🤖 AI StudyMate")
st.caption("Your Personalized AI Tutor")


# -----------------------------
# TUTOR SCREEN
# -----------------------------
if st.session_state.tutor_started:

    topic = st.session_state.current_topic

    if topic not in lessons:
        st.error("No lesson is available for this topic.")
        st.stop()

    lesson = lessons[topic]

    st.success(f"🎯 Personalized lesson selected: **{topic}**")

    st.header(f"📚 {lesson['title']}")

    st.write(lesson["lesson"])

    st.divider()

    st.subheader("🧠 Check Your Understanding")

    st.write(lesson["question"])

    answer = st.text_area(
        "Write your answer in your own words:",
        height=150,
        placeholder="Type your answer here..."
    )

    if st.button("✅ Check My Understanding"):

        if not answer.strip():
            st.warning("Please write an answer first.")
        else:
            answer_lower = answer.lower()

            matched = 0

            for keyword in lesson["keywords"]:
                if keyword in answer_lower:
                    matched += 1

            if matched >= 2:
                st.success(
                    "🎉 Good job! Your answer shows that you understand "
                    "the main idea."
                )

                st.write(
                    "### 🌟 Tutor Feedback"
                )

                st.write(
                    "You identified important concepts correctly. "
                    "Let's increase the difficulty slightly in the next activity."
                )

                st.session_state.mastery = "Improving"

            elif matched == 1:
                st.info(
                    "👍 You're on the right track, but your answer could "
                    "include a little more detail."
                )

                st.write(
                    "💡 **Hint:** Review the lesson above and mention "
                    "the main concept in your answer."
                )

                st.session_state.mastery = "Needs Practice"

            else:
                st.error(
                    "Let's try that again. Your answer doesn't yet show "
                    "the main concept."
                )

                st.write(
                    "💡 **Tutor Hint:** Read the lesson once more and "
                    "answer using your own words."
                )

                st.session_state.mastery = "Needs Review"

    st.divider()

    st.subheader("📈 Your Current Learning Status")

    if "mastery" in st.session_state:

        if st.session_state.mastery == "Improving":
            st.success("🟢 Mastery Status: Improving")

        elif st.session_state.mastery == "Needs Practice":
            st.warning("🟡 Mastery Status: Needs Practice")

        else:
            st.error("🔴 Mastery Status: Needs Review")

    if st.button("⬅️ Back to Personalized Path"):
        st.session_state.tutor_started = False
        st.rerun()

    st.stop()


# -----------------------------
# WELCOME SCREEN
# -----------------------------
if not st.session_state.started:

    st.subheader("Learn AI at your own pace.")

    st.write(
        "AI StudyMate first understands what you already know, "
        "then creates a personalized learning experience."
    )

    st.write("### What your AI tutor will do")

    st.write("🔎 Assess your current knowledge")
    st.write("🎯 Identify your weakest topics")
    st.write("🛣️ Create a personalized learning path")
    st.write("🤖 Teach concepts step by step")
    st.write("📈 Track your improvement")

    if st.button("🚀 Start Learning"):

        st.session_state.started = True
        st.rerun()

    st.stop()


# -----------------------------
# PROFILE
# -----------------------------
if not st.session_state.profile:

    st.header("👤 Tell Me About Yourself")

    name = st.text_input("Your Name")

    level = st.selectbox(
        "Current AI Experience",
        ["Beginner", "Intermediate", "Advanced"]
    )

    goal = st.selectbox(
        "What do you want to achieve?",
        [
            "Learn AI fundamentals",
            "Build AI projects",
            "Prepare for a job",
            "Learn Generative AI",
            "Learn AI Agents"
        ]
    )

    study_time = st.selectbox(
        "How much time can you study each day?",
        ["15 minutes", "30 minutes", "1 hour", "2+ hours"]
    )

    if st.button("Continue →"):

        if not name.strip():
            st.warning("Please enter your name.")
        else:

            st.session_state.profile = {
                "name": name,
                "level": level,
                "goal": goal,
                "study_time": study_time
            }

            st.rerun()

    st.stop()


# -----------------------------
# DIAGNOSTIC TEST
# -----------------------------
if not st.session_state.diagnostic_completed:

    st.header("🧠 AI Knowledge Diagnostic")

    st.write(
        f"Hi **{st.session_state.profile['name']}**! "
        "Let's quickly understand what you already know."
    )

    st.write(
        "There are 10 questions. Answer honestly — "
        "the goal is to personalize your learning path."
    )

    questions = [
        ("AI Fundamentals", "What does AI stand for?",
         ["Artificial Intelligence", "Automated Internet", "Advanced Information", "Artificial Interface"],
         "Artificial Intelligence"),

        ("AI Fundamentals", "Which is an example of AI?",
         ["A calculator", "A system recognizing objects in images", "A light bulb", "A keyboard"],
         "A system recognizing objects in images"),

        ("Python", "Which symbol is commonly used to write a comment in Python?",
         ["//", "#", "<!--", "**"],
         "#"),

        ("Python", "Which Python data type represents True or False?",
         ["String", "Integer", "Boolean", "List"],
         "Boolean"),

        ("Machine Learning", "What is supervised learning?",
         ["Learning without data", "Learning from labelled examples",
          "Only writing rules manually", "Deleting incorrect data"],
         "Learning from labelled examples"),

        ("Machine Learning", "What is a training dataset?",
         ["Data used to teach a model",
          "A programming language", "A computer", "A user interface"],
         "Data used to teach a model"),

        ("Generative AI", "What can a generative AI model do?",
         ["Only classify data", "Generate new content",
          "Only store files", "Only calculate numbers"],
         "Generate new content"),

        ("Generative AI", "What does LLM stand for?",
         ["Large Language Model", "Long Learning Machine",
          "Logical Language Method", "Large Logic Machine"],
         "Large Language Model"),

        ("RAG", "What does RAG stand for?",
         ["Retrieval-Augmented Generation",
          "Random AI Generation",
          "Rapid Automated Guidance",
          "Retrieved AI Graph"],
         "Retrieval-Augmented Generation"),

        ("AI Agents", "What are AI agents designed to do?",
         ["Only answer fixed questions",
          "Perceive information and take actions toward a goal",
          "Only store data",
          "Only generate images"],
         "Perceive information and take actions toward a goal")
    ]

    answers = []

    for i, (topic, question, options, correct) in enumerate(questions):

        st.subheader(f"Question {i + 1}")

        answer = st.radio(
            question,
            options,
            key=f"question_{i}"
        )

        answers.append((topic, answer, correct))

    if st.button("📊 Generate My Personalized Path"):

        topic_scores = {}

        for topic, answer, correct in answers:

            if topic not in topic_scores:
                topic_scores[topic] = {
                    "correct": 0,
                    "total": 0
                }

            topic_scores[topic]["total"] += 1

            if answer == correct:
                topic_scores[topic]["correct"] += 1

        for topic in topic_scores:

            correct = topic_scores[topic]["correct"]
            total = topic_scores[topic]["total"]

            topic_scores[topic]["percentage"] = int(
                correct / total * 100
            )

        st.session_state.topic_scores = topic_scores
        st.session_state.diagnostic_completed = True

        st.rerun()

    st.stop()


# -----------------------------
# PERSONALIZED PATH
# -----------------------------
st.header("🛣️ Your Personalized Learning Path")

st.write(
    f"Based on your diagnostic assessment, "
    f"here is the learning path created for **"
    f"{st.session_state.profile['name']}**."
)

scores = st.session_state.topic_scores

ordered_topics = sorted(
    scores.keys(),
    key=lambda topic: scores[topic]["percentage"]
)

for position, topic in enumerate(ordered_topics, start=1):

    percentage = scores[topic]["percentage"]

    if percentage >= 80:
        status = "🟢 Strong"
    elif percentage >= 50:
        status = "🟡 Practice More"
    else:
        status = "🔴 Priority"

    st.write(
        f"**{position}. {topic}** — {percentage}% — {status}"
    )

    st.progress(percentage / 100)

weakest_topic = ordered_topics[0]

st.session_state.current_topic = weakest_topic

st.divider()

st.subheader("🎯 Your Recommended Focus")

st.info(
    f"Your tutor recommends starting with **{weakest_topic}** "
    "because this is currently your weakest area."
)

if st.button("🤖 Start My Personalized Lesson"):

    st.session_state.tutor_started = True
    st.rerun()
