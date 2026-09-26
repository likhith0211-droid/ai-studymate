import streamlit as st

# ============================================================
# AI STUDYMATE
# Step 1: Five-Domain Diagnostic + Learner Knowledge Map
# ============================================================

st.set_page_config(
    page_title="AI StudyMate",
    page_icon="🎓",
    layout="wide"
)

# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "page": "welcome",
    "profile": {},
    "diagnostic_index": 0,
    "diagnostic_answers": {},
    "diagnostic_complete": False,
    "domain_scores": {},
    "recommended_domain": None,
    "recommended_module": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# CURRICULUM
# ============================================================

curriculum = {
    "Python": {
        "icon": "🐍",
        "modules": [
            "Python Basics",
            "Data Structures",
            "Functions",
            "Object-Oriented Programming",
            "NumPy",
            "Pandas",
        ],
    },

    "Mathematics & Statistics": {
        "icon": "📐",
        "modules": [
            "Statistics Fundamentals",
            "Probability",
            "Linear Algebra",
            "Calculus for AI",
        ],
    },

    "Machine Learning": {
        "icon": "🤖",
        "modules": [
            "Machine Learning Fundamentals",
            "Data Preparation",
            "Regression",
            "Classification",
            "Model Evaluation",
        ],
    },

    "Deep Learning": {
        "icon": "🧠",
        "modules": [
            "Neural Networks",
            "Activation Functions",
            "Backpropagation",
            "Convolutional Neural Networks",
            "Transformers",
        ],
    },

    "Generative AI": {
        "icon": "✨",
        "modules": [
            "LLM Fundamentals",
            "Tokens",
            "Embeddings",
            "Transformers for GenAI",
            "Prompt Engineering",
            "RAG Fundamentals",
        ],
    },
}


# ============================================================
# DIAGNOSTIC QUESTIONS
# ============================================================

diagnostic_questions = [

    # ---------------- PYTHON ----------------

    {
        "domain": "Python",
        "question": "Which symbol is used to start a comment in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#",
        "module": "Python Basics",
    },

    {
        "domain": "Python",
        "question": "Which Python data structure stores key-value pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Dictionary",
        "module": "Data Structures",
    },

    {
        "domain": "Python",
        "question": "What is the main purpose of a Python function?",
        "options": [
            "To store only numbers",
            "To group reusable instructions",
            "To create hardware",
            "To delete variables"
        ],
        "answer": "To group reusable instructions",
        "module": "Functions",
    },

    # ---------------- MATH ----------------

    {
        "domain": "Mathematics & Statistics",
        "question": "What does the mean of a dataset represent?",
        "options": [
            "The middle value only",
            "The average value",
            "The largest value",
            "The smallest value"
        ],
        "answer": "The average value",
        "module": "Statistics Fundamentals",
    },

    {
        "domain": "Mathematics & Statistics",
        "question": "What is the probability of getting heads when tossing a fair coin?",
        "options": ["0", "0.25", "0.5", "1"],
        "answer": "0.5",
        "module": "Probability",
    },

    {
        "domain": "Mathematics & Statistics",
        "question": "Which mathematical objects are commonly used to represent data in machine learning?",
        "options": [
            "Vectors and matrices",
            "Only circles",
            "Only equations",
            "Only graphs"
        ],
        "answer": "Vectors and matrices",
        "module": "Linear Algebra",
    },

    # ---------------- MACHINE LEARNING ----------------

    {
        "domain": "Machine Learning",
        "question": "What is supervised learning?",
        "options": [
            "Learning from labelled examples",
            "Learning without any data",
            "Writing programs manually",
            "Training only neural networks"
        ],
        "answer": "Learning from labelled examples",
        "module": "Machine Learning Fundamentals",
    },

    {
        "domain": "Machine Learning",
        "question": "Why is a dataset usually divided into training and testing data?",
        "options": [
            "To make the computer faster",
            "To evaluate how well a model generalizes",
            "To remove all features",
            "To avoid using algorithms"
        ],
        "answer": "To evaluate how well a model generalizes",
        "module": "Model Evaluation",
    },

    {
        "domain": "Machine Learning",
        "question": "Which problem is classification designed to solve?",
        "options": [
            "Predicting categories",
            "Only storing data",
            "Sorting files",
            "Writing Python code"
        ],
        "answer": "Predicting categories",
        "module": "Classification",
    },

    # ---------------- DEEP LEARNING ----------------

    {
        "domain": "Deep Learning",
        "question": "What is a neural network made up of?",
        "options": [
            "Connected layers of computational units",
            "Only databases",
            "Only Python files",
            "Web pages"
        ],
        "answer": "Connected layers of computational units",
        "module": "Neural Networks",
    },

    {
        "domain": "Deep Learning",
        "question": "What is the purpose of an activation function?",
        "options": [
            "To introduce non-linearity into a neural network",
            "To store files",
            "To create a database",
            "To replace training data"
        ],
        "answer": "To introduce non-linearity into a neural network",
        "module": "Activation Functions",
    },

    {
        "domain": "Deep Learning",
        "question": "What is backpropagation mainly used for?",
        "options": [
            "Updating neural network parameters using error information",
            "Creating a Python list",
            "Collecting internet data",
            "Designing a website"
        ],
        "answer": "Updating neural network parameters using error information",
        "module": "Backpropagation",
    },

    # ---------------- GENERATIVE AI ----------------

    {
        "domain": "Generative AI",
        "question": "What is an LLM?",
        "options": [
            "Large Language Model",
            "Local Learning Machine",
            "Linear Logic Method",
            "Language Loading Module"
        ],
        "answer": "Large Language Model",
        "module": "LLM Fundamentals",
    },

    {
        "domain": "Generative AI",
        "question": "What are embeddings commonly used for?",
        "options": [
            "Representing information as numerical vectors",
            "Creating computer hardware",
            "Deleting databases",
            "Compiling Python"
        ],
        "answer": "Representing information as numerical vectors",
        "module": "Embeddings",
    },

    {
        "domain": "Generative AI",
        "question": "What is RAG designed to do?",
        "options": [
            "Retrieve relevant information and use it to help generate an answer",
            "Replace Python",
            "Train a CPU",
            "Create spreadsheets"
        ],
        "answer": "Retrieve relevant information and use it to help generate an answer",
        "module": "RAG Fundamentals",
    },
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def calculate_domain_scores():
    """Calculate percentage score for each learning domain."""

    results = {}

    for domain in curriculum.keys():

        questions = [
            q for q in diagnostic_questions
            if q["domain"] == domain
        ]

        correct = 0

        for index, question in enumerate(diagnostic_questions):

            if question["domain"] != domain:
                continue

            if st.session_state.diagnostic_answers.get(index) == question["answer"]:
                correct += 1

        if questions:
            results[domain] = round((correct / len(questions)) * 100)

    return results


def get_status(score):
    if score >= 80:
        return "🟢 Strong"

    if score >= 50:
        return "🟡 Developing"

    if score > 0:
        return "🔴 Needs Practice"

    return "⚪ Not Assessed"


def recommend_learning_path(scores):
    """
    Select the weakest assessed domain.

    The first version intentionally uses deterministic rules.
    This keeps recommendations fast and reproducible.
    """

    # Find domains with the lowest score.
    weakest_domain = min(
        scores,
        key=scores.get
    )

    weakest_score = scores[weakest_domain]

    # Choose the first module for the domain.
    module = curriculum[weakest_domain]["modules"][0]

    # If the learner is already strong in a domain,
    # look for the next domain with a lower score.
    if weakest_score >= 80:

        ordered_domains = sorted(
            scores,
            key=scores.get
        )

        for domain in ordered_domains:
            if scores[domain] < 80:
                weakest_domain = domain
                module = curriculum[domain]["modules"][0]
                break

    return weakest_domain, module


def reset_diagnostic():
    st.session_state.diagnostic_index = 0
    st.session_state.diagnostic_answers = {}
    st.session_state.diagnostic_complete = False
    st.session_state.domain_scores = {}
    st.session_state.recommended_domain = None
    st.session_state.recommended_module = None
    st.session_state.page = "diagnostic"


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🎓 AI StudyMate")

    st.caption("Personalised AI Learning")

    st.divider()

    if st.session_state.profile:

        st.write(
            f"👋 **{st.session_state.profile.get('name', 'Learner')}**"
        )

        st.write(
            f"🎯 {st.session_state.profile.get('goal', 'Learn AI')}"
        )

    st.divider()

    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

    if st.button("🧪 Diagnostic", use_container_width=True):
        st.session_state.page = "diagnostic"
        st.rerun()

    if st.button("📚 My Roadmap", use_container_width=True):
        st.session_state.page = "roadmap"
        st.rerun()

    st.divider()

    st.caption("AI StudyMate")
    st.caption("Python → Math → ML → DL → GenAI")


# ============================================================
# WELCOME
# ============================================================

if st.session_state.page == "welcome":

    st.title("🎓 AI StudyMate")

    st.subheader(
        "Your personalised journey from Python to Generative AI."
    )

    st.write(
        """
        AI StudyMate helps you learn Artificial Intelligence
        through a personalised learning path.

        Instead of giving every learner the same course order,
        StudyMate first checks what you already know and uses
        your results to recommend where to start.
        """
    )

    st.divider()

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("🐍", "Python")

    with col2:
        st.metric("📐", "Math")

    with col3:
        st.metric("🤖", "ML")

    with col4:
        st.metric("🧠", "Deep Learning")

    with col5:
        st.metric("✨", "GenAI")

    st.divider()

    st.subheader("Let's understand your learning goals")

    name = st.text_input(
        "Your name"
    )

    level = st.selectbox(
        "Current AI experience",
        [
            "Complete Beginner",
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    goal = st.selectbox(
        "What is your main goal?",
        [
            "Learn AI from the beginning",
            "Become a Machine Learning Developer",
            "Build Generative AI Applications",
            "Prepare for an AI Job",
            "Build AI Projects"
        ]
    )

    study_time = st.selectbox(
        "How much time can you study each day?",
        [
            "15 minutes",
            "30 minutes",
            "1 hour",
            "2+ hours"
        ]
    )

    if st.button(
        "Start My AI Journey →",
        type="primary",
        use_container_width=True
    ):

        if not name.strip():

            st.warning("Please enter your name.")

        else:

            st.session_state.profile = {
                "name": name,
                "level": level,
                "goal": goal,
                "study_time": study_time
            }

            st.session_state.page = "diagnostic"

            st.rerun()


# ============================================================
# HOME
# ============================================================

elif st.session_state.page == "home":

    st.title(
        f"Welcome back, {st.session_state.profile.get('name', 'Learner')} 👋"
    )

    st.subheader("Your AI Learning Journey")

    if not st.session_state.diagnostic_complete:

        st.info(
            "Complete your diagnostic assessment so AI StudyMate "
            "can understand your current knowledge."
        )

        if st.button(
            "Take Diagnostic Assessment →",
            type="primary"
        ):
            st.session_state.page = "diagnostic"
            st.rerun()

    else:

        scores = st.session_state.domain_scores

        cols = st.columns(5)

        for i, (domain, score) in enumerate(scores.items()):

            with cols[i]:

                st.metric(
                    f"{curriculum[domain]['icon']} {domain}",
                    f"{score}%"
                )

                st.caption(get_status(score))

        st.divider()

        st.subheader("🎯 Your Recommended Starting Point")

        st.success(
            f"""
            **{st.session_state.recommended_module}**

            This is inside **{st.session_state.recommended_domain}**.

            Your diagnostic indicates that this area needs
            attention before moving deeper into the AI roadmap.
            """
        )

        if st.button(
            "Start Recommended Learning →",
            type="primary"
        ):

            st.session_state.page = "roadmap"
            st.rerun()

        st.divider()

        st.subheader("Your Knowledge Map")

        for domain, score in scores.items():

            st.write(
                f"{curriculum[domain]['icon']} **{domain}** — {score}%"
            )

            st.progress(score / 100)

            st.caption(get_status(score))


# ============================================================
# DIAGNOSTIC
# ============================================================

elif st.session_state.page == "diagnostic":

    st.title("🧪 AI Knowledge Diagnostic")

    st.write(
        """
        This assessment checks your current understanding across
        Python, Mathematics & Statistics, Machine Learning,
        Deep Learning and Generative AI.

        Answer honestly. The goal is not to get a high score.
        The goal is to create the right learning path for you.
        """
    )

    st.divider()

    total_questions = len(diagnostic_questions)

    if st.session_state.diagnostic_index < total_questions:

        index = st.session_state.diagnostic_index

        question = diagnostic_questions[index]

        domain = question["domain"]

        st.caption(
            f"{curriculum[domain]['icon']} {domain}"
        )

        st.progress(
            (index + 1) / total_questions
        )

        st.write(
            f"Question {index + 1} of {total_questions}"
        )

        st.subheader(
            question["question"]
        )

        answer = st.radio(
            "Choose your answer:",
            question["options"],
            key=f"diagnostic_{index}"
        )

        if st.button(
            "Submit Answer →",
            type="primary"
        ):

            st.session_state.diagnostic_answers[index] = answer

            st.session_state.diagnostic_index += 1

            st.rerun()

    else:

        # Calculate results
        scores = calculate_domain_scores()

        st.session_state.domain_scores = scores

        recommended_domain, recommended_module = recommend_learning_path(
            scores
        )

        st.session_state.recommended_domain = recommended_domain
        st.session_state.recommended_module = recommended_module

        st.session_state.diagnostic_complete = True

        st.success("Diagnostic complete! 🎉")

        st.subheader("Your Knowledge Map")

        cols = st.columns(5)

        for i, (domain, score) in enumerate(scores.items()):

            with cols[i]:

                st.metric(
                    f"{curriculum[domain]['icon']} {domain}",
                    f"{score}%"
                )

                st.caption(get_status(score))

        st.divider()

        st.subheader("🎯 Recommended Starting Point")

        st.info(
            f"""
            **{curriculum[recommended_domain]['icon']}
            {recommended_module}**

            Your current results suggest that this is the
            most useful place to begin your personalised journey.
            """
        )

        st.write(
            f"**Why?** Your score in "
            f"**{recommended_domain}** is "
            f"**{scores[recommended_domain]}%**."
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "📚 View My Roadmap",
                type="primary",
                use_container_width=True
            ):

                st.session_state.page = "roadmap"
                st.rerun()

        with col2:

            if st.button(
                "🔄 Retake Diagnostic",
                use_container_width=True
            ):

                reset_diagnostic()
                st.rerun()


# ============================================================
# ROADMAP
# ============================================================

elif st.session_state.page == "roadmap":

    st.title("📚 My Personalised AI Roadmap")

    st.write(
        """
        Your complete AI learning journey is organised into five
        connected learning domains.
        """
    )

    st.divider()

    domain_scores = st.session_state.domain_scores

    domain_order = list(curriculum.keys())

    for position, domain in enumerate(domain_order):

        info = curriculum[domain]

        score = domain_scores.get(domain, 0)

        if score >= 80:

            status = "✅ Strong"

        elif score >= 50:

            status = "🟡 Developing"

        elif score > 0:

            status = "🔴 Needs Practice"

        else:

            status = "🔒 Not Assessed"

        with st.container(border=True):

            col1, col2, col3 = st.columns([1, 5, 2])

            with col1:

                st.markdown(
                    f"# {info['icon']}"
                )

            with col2:

                st.subheader(
                    f"{position + 1}. {domain}"
                )

                st.write(
                    f"{len(info['modules'])} learning modules"
                )

            with col3:

                st.write(status)

                if domain in domain_scores:

                    st.write(f"**{score}%**")

            st.progress(score / 100)

            st.write("**Modules:**")

            for module in info["modules"]:

                st.write(f"• {module}")

    st.divider()

    st.subheader("🎯 Your Current Recommendation")

    if st.session_state.recommended_domain:

        st.success(
            f"Start with **{st.session_state.recommended_module}** "
            f"inside **{st.session_state.recommended_domain}**."
        )

    else:

        st.info(
            "Complete the diagnostic to receive a personalised recommendation."
        )

    if st.button("🧪 Retake Diagnostic"):

        reset_diagnostic()
        st.rerun()
