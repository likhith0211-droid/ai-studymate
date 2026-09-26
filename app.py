import random
import streamlit as st


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Learn",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# CONSTANTS
# =========================================================

LOGO_URL = (
    "https://raw.githubusercontent.com/"
    "likhith0211-droid/ai-studymate/main/"
    "0f6577fe444ba6b1365cd00394ee581e.jpg"
)

SUBJECTS = [
    "Python",
    "Mathematics & Statistics",
    "Machine Learning",
    "Deep Learning",
    "Generative AI",
]


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #ffffff;
}

/* Remove Streamlit top padding */
.block-container {
    padding-top: 0.8rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* ================= HEADER ================= */

.ai-header {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 0 18px 0;
    border-bottom: 1px solid #e8edf2;
    margin-bottom: 30px;
}

.ai-brand {
    display: flex;
    align-items: center;
    gap: 10px;
}

.ai-logo {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    object-fit: cover;
    border: 1px solid #edf1f5;
}

.ai-brand-name {
    font-size: 25px;
    font-weight: 700;
    color: #344454;
    letter-spacing: -0.5px;
}

.ai-header-actions {
    display: flex;
    align-items: center;
    gap: 12px;
}

.ai-gift {
    width: 44px;
    height: 44px;
    border: 1px solid #e2e8ee;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}

/* ================= HERO ================= */

.hero-section {
    padding: 48px 0 35px 0;
}

.hero-title {
    font-size: 58px;
    line-height: 1.05;
    font-weight: 800;
    color: #344454;
    letter-spacing: -2px;
    margin-bottom: 20px;
}

.hero-title span {
    color: #344454;
}

.hero-subtitle {
    font-size: 20px;
    line-height: 1.55;
    color: #667482;
    max-width: 650px;
    margin-bottom: 18px;
}

.hero-highlight {
    font-size: 16px;
    line-height: 1.6;
    color: #536170;
    max-width: 650px;
}

.hero-highlight strong {
    color: #00a878;
}

/* ================= VISUAL ================= */

.visual-wrapper {
    min-height: 440px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
}

.visual-main-circle {
    width: 270px;
    height: 270px;
    border-radius: 50%;
    background: #eef8ff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 110px;
    position: relative;
}

.visual-small {
    position: absolute;
    width: 90px;
    height: 90px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 42px;
    background: white;
    box-shadow: 0 10px 30px rgba(40, 60, 80, 0.12);
}

.visual-one {
    top: 35px;
    right: 80px;
}

.visual-two {
    bottom: 55px;
    left: 75px;
}

.visual-three {
    bottom: 25px;
    right: 55px;
}

.floating-card {
    position: absolute;
    padding: 12px 18px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 10px 28px rgba(40, 60, 80, 0.12);
    font-size: 14px;
    font-weight: 700;
    color: #344454;
}

.card-ai {
    top: 100px;
    left: 20px;
}

.card-progress {
    top: 25px;
    right: 5px;
}

.card-python {
    bottom: 80px;
    right: 5px;
}

/* ================= PROFILE ================= */

.profile-section {
    margin-top: 15px;
    padding: 30px;
    border: 1px solid #e5ebf0;
    border-radius: 18px;
    background: #ffffff;
    box-shadow: 0 8px 30px rgba(30, 50, 70, 0.05);
}

.profile-title {
    font-size: 26px;
    font-weight: 800;
    color: #344454;
    margin-bottom: 8px;
}

.profile-description {
    font-size: 15px;
    color: #71808e;
    margin-bottom: 25px;
}

/* Streamlit labels */

.stSelectbox label,
.stTextInput label {
    color: #344454 !important;
    font-weight: 600 !important;
}

/* ================= BUTTONS ================= */

.stButton > button {
    border-radius: 9px;
    min-height: 46px;
    font-weight: 700;
    border: 1px solid #344454;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-1px);
}

/* ================= FOUNDATIONS ================= */

.foundation-section {
    margin-top: 60px;
    margin-bottom: 30px;
}

.foundation-title {
    text-align: center;
    font-size: 30px;
    font-weight: 800;
    color: #344454;
    margin-bottom: 10px;
}

.foundation-description {
    text-align: center;
    font-size: 16px;
    color: #71808e;
    margin-bottom: 28px;
}

.foundation-card {
    text-align: center;
    padding: 25px 12px;
    border: 1px solid #e5ebf0;
    border-radius: 15px;
    background: white;
    min-height: 130px;
    box-shadow: 0 5px 18px rgba(40, 60, 80, 0.04);
}

.foundation-icon {
    font-size: 32px;
    margin-bottom: 8px;
}

.foundation-name {
    font-size: 14px;
    font-weight: 700;
    color: #344454;
}

/* ================= DIAGNOSTIC ================= */

.page-title {
    font-size: 36px;
    font-weight: 800;
    color: #344454;
    margin-bottom: 8px;
}

.page-description {
    color: #71808e;
    font-size: 16px;
    margin-bottom: 25px;
}

.question-card {
    padding: 22px;
    margin-bottom: 18px;
    border: 1px solid #e5ebf0;
    border-radius: 14px;
    background: #ffffff;
    box-shadow: 0 4px 16px rgba(40, 60, 80, 0.04);
}

.question-number {
    font-size: 13px;
    font-weight: 700;
    color: #00a878;
    margin-bottom: 7px;
}

.question-text {
    font-size: 17px;
    font-weight: 700;
    color: #344454;
    line-height: 1.5;
}

/* ================= SCORE CARD ================= */

.score-hero {
    text-align: center;
    padding: 35px;
    border-radius: 20px;
    background: #f5faf8;
    border: 1px solid #dfeee8;
    margin-bottom: 30px;
}

.score-label {
    font-size: 14px;
    font-weight: 700;
    color: #71808e;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.score-number {
    font-size: 64px;
    font-weight: 800;
    color: #344454;
    margin: 5px 0;
}

.score-subtitle {
    color: #71808e;
    font-size: 15px;
}

.subject-score-card {
    padding: 22px;
    border: 1px solid #e5ebf0;
    border-radius: 15px;
    margin-bottom: 16px;
    background: white;
}

.subject-name {
    font-weight: 700;
    color: #344454;
    font-size: 17px;
    margin-bottom: 8px;
}

.progress-background {
    width: 100%;
    height: 10px;
    border-radius: 10px;
    background: #edf1f4;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    border-radius: 10px;
    background: #00a878;
}

.subject-score {
    margin-top: 8px;
    color: #5e6c79;
    font-size: 14px;
}

.recommendation {
    margin-top: 28px;
    padding: 24px;
    border-radius: 15px;
    background: #f7f9fb;
    border: 1px solid #e4e9ee;
}

.recommendation-title {
    font-size: 20px;
    font-weight: 800;
    color: #344454;
}

.recommendation-subject {
    font-size: 26px;
    font-weight: 800;
    color: #00a878;
    margin: 7px 0;
}

/* ================= ROADMAP ================= */

.roadmap-card {
    padding: 22px;
    margin-bottom: 15px;
    border: 1px solid #e5ebf0;
    border-radius: 14px;
    background: white;
}

.roadmap-number {
    font-size: 13px;
    font-weight: 700;
    color: #00a878;
}

.roadmap-name {
    font-size: 20px;
    font-weight: 800;
    color: #344454;
    margin: 5px 0;
}

.roadmap-score {
    color: #71808e;
    font-size: 14px;
}

</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# QUESTION BANK
# 3 UNIQUE QUESTIONS PER SUBJECT PER LEVEL
# =========================================================

QUESTION_BANK = {

    "Python": {

        "Beginner": [
            {
                "q": "Which Python data type is used to store a sequence of characters?",
                "options": ["str", "int", "float", "bool"],
                "answer": "str",
            },
            {
                "q": "What does len([10, 20, 30]) return?",
                "options": ["2", "3", "4", "30"],
                "answer": "3",
            },
            {
                "q": "Which keyword is used to define a function in Python?",
                "options": ["func", "define", "def", "function"],
                "answer": "def",
            },
        ],

        "Intermediate": [
            {
                "q": "What is the output of [x * 2 for x in range(3)]?",
                "options": ["[0, 2, 4]", "[2, 4, 6]", "[0, 1, 2]", "[1, 2, 3]"],
                "answer": "[0, 2, 4]",
            },
            {
                "q": "Which Python structure stores key-value pairs?",
                "options": ["Tuple", "Dictionary", "Set", "List"],
                "answer": "Dictionary",
            },
            {
                "q": "What does a Python decorator primarily allow you to do?",
                "options": [
                    "Modify or extend function behavior",
                    "Create database tables",
                    "Compile Python into machine code",
                    "Delete unused variables",
                ],
                "answer": "Modify or extend function behavior",
            },
        ],

        "Advanced": [
            {
                "q": "What is the main purpose of a generator function using yield?",
                "options": [
                    "Produce values lazily",
                    "Create a new class",
                    "Encrypt values",
                    "Run code in parallel automatically",
                ],
                "answer": "Produce values lazily",
            },
            {
                "q": "Why can using a mutable default argument in a Python function cause unexpected behavior?",
                "options": [
                    "The object is reused across function calls",
                    "Python converts it into a tuple",
                    "The function cannot accept arguments",
                    "The object is always copied",
                ],
                "answer": "The object is reused across function calls",
            },
            {
                "q": "What does the Python 'with' statement commonly help manage?",
                "options": [
                    "Resources such as files",
                    "CPU clock speed",
                    "Python package versions",
                    "Network routing tables",
                ],
                "answer": "Resources such as files",
            },
        ],
    },

    "Mathematics & Statistics": {

        "Beginner": [
            {
                "q": "What is the mean of 2, 4, 6, and 8?",
                "options": ["4", "5", "6", "20"],
                "answer": "5",
            },
            {
                "q": "What is the probability of getting heads when tossing a fair coin once?",
                "options": ["0", "0.25", "0.5", "1"],
                "answer": "0.5",
            },
            {
                "q": "Which measure describes the middle value of an ordered dataset?",
                "options": ["Mean", "Median", "Range", "Variance"],
                "answer": "Median",
            },
        ],

        "Intermediate": [
            {
                "q": "If two events are independent, which statement is true?",
                "options": [
                    "P(A and B) = P(A)P(B)",
                    "P(A and B) = P(A) + P(B)",
                    "P(A) = P(B) always",
                    "They cannot occur together",
                ],
                "answer": "P(A and B) = P(A)P(B)",
            },
            {
                "q": "What does variance measure?",
                "options": [
                    "Spread of values around the mean",
                    "The largest value only",
                    "The number of observations",
                    "The median of the dataset",
                ],
                "answer": "Spread of values around the mean",
            },
            {
                "q": "In linear algebra, the dot product of two vectors produces what?",
                "options": [
                    "A scalar",
                    "A matrix only",
                    "A probability distribution",
                    "A polynomial",
                ],
                "answer": "A scalar",
            },
        ],

        "Advanced": [
            {
                "q": "What does the gradient of a multivariable function represent?",
                "options": [
                    "Direction of greatest increase",
                    "Always the minimum value",
                    "The function's variance",
                    "The number of variables",
                ],
                "answer": "Direction of greatest increase",
            },
            {
                "q": "If a p-value is very small under a chosen significance level, what is commonly concluded?",
                "options": [
                    "Reject the null hypothesis",
                    "Accept every possible hypothesis",
                    "The sample mean is zero",
                    "The experiment must be repeated",
                ],
                "answer": "Reject the null hypothesis",
            },
            {
                "q": "Why is matrix multiplication important in neural networks?",
                "options": [
                    "It represents transformations between layers",
                    "It removes all model parameters",
                    "It guarantees zero training error",
                    "It replaces the loss function",
                ],
                "answer": "It represents transformations between layers",
            },
        ],
    },

    "Machine Learning": {

        "Beginner": [
            {
                "q": "What is supervised learning trained on?",
                "options": [
                    "Labeled examples",
                    "Only random numbers",
                    "Unlabeled images only",
                    "No training data",
                ],
                "answer": "Labeled examples",
            },
            {
                "q": "Which task predicts a continuous numerical value?",
                "options": [
                    "Regression",
                    "Classification",
                    "Clustering",
                    "Association",
                ],
                "answer": "Regression",
            },
            {
                "q": "What is a feature in a machine learning dataset?",
                "options": [
                    "An input variable",
                    "The final prediction only",
                    "The model name",
                    "The training algorithm",
                ],
                "answer": "An input variable",
            },
        ],

        "Intermediate": [
            {
                "q": "Why is a validation set commonly used?",
                "options": [
                    "To tune or compare model choices",
                    "To replace the training set",
                    "To guarantee perfect predictions",
                    "To remove all features",
                ],
                "answer": "To tune or compare model choices",
            },
            {
                "q": "What is overfitting?",
                "options": [
                    "A model learns training-specific patterns too closely",
                    "A model has no parameters",
                    "A model refuses to train",
                    "A model always predicts the mean",
                ],
                "answer": "A model learns training-specific patterns too closely",
            },
            {
                "q": "Which metric is commonly used for binary classification?",
                "options": [
                    "F1 score",
                    "Mean squared error only",
                    "R-squared only",
                    "Euclidean distance only",
                ],
                "answer": "F1 score",
            },
        ],

        "Advanced": [
            {
                "q": "Why can feature scaling matter for gradient-based optimization?",
                "options": [
                    "Different feature scales can distort optimization steps",
                    "It guarantees no overfitting",
                    "It removes the need for training",
                    "It converts classification into regression",
                ],
                "answer": "Different feature scales can distort optimization steps",
            },
            {
                "q": "What is the purpose of regularization?",
                "options": [
                    "Penalize overly complex models",
                    "Increase every model parameter",
                    "Remove the test set",
                    "Guarantee a higher training score",
                ],
                "answer": "Penalize overly complex models",
            },
            {
                "q": "In a decision tree, what does a split attempt to achieve?",
                "options": [
                    "Create child groups with improved predictive purity",
                    "Increase the number of missing values",
                    "Remove the target variable",
                    "Randomly shuffle labels",
                ],
                "answer": "Create child groups with improved predictive purity",
            },
        ],
    },

    "Deep Learning": {

        "Beginner": [
            {
                "q": "What is the basic computational unit commonly used in a neural network?",
                "options": ["Neuron", "Database", "Compiler", "Router"],
                "answer": "Neuron",
            },
            {
                "q": "What is an activation function used for?",
                "options": [
                    "Introduce non-linearity",
                    "Store datasets permanently",
                    "Download models",
                    "Create database indexes",
                ],
                "answer": "Introduce non-linearity",
            },
            {
                "q": "What does CNN commonly stand for in deep learning?",
                "options": [
                    "Convolutional Neural Network",
                    "Central Numeric Node",
                    "Computer Network Number",
                    "Continuous Neural Notation",
                ],
                "answer": "Convolutional Neural Network",
            },
        ],

        "Intermediate": [
            {
                "q": "What is backpropagation used for?",
                "options": [
                    "Computing gradients for parameter updates",
                    "Creating test datasets",
                    "Compressing images only",
                    "Removing neural network layers",
                ],
                "answer": "Computing gradients for parameter updates",
            },
            {
                "q": "What does an optimizer such as Adam primarily update?",
                "options": [
                    "Model parameters",
                    "The dataset labels",
                    "The operating system",
                    "The user's browser",
                ],
                "answer": "Model parameters",
            },
            {
                "q": "Why are convolutional layers useful for images?",
                "options": [
                    "They can learn local spatial patterns",
                    "They eliminate all parameters",
                    "They convert every image into text",
                    "They require no training",
                ],
                "answer": "They can learn local spatial patterns",
            },
        ],

        "Advanced": [
            {
                "q": "What problem can residual connections help with in very deep networks?",
                "options": [
                    "Improving gradient flow",
                    "Removing the loss function",
                    "Eliminating training data",
                    "Guaranteeing zero inference time",
                ],
                "answer": "Improving gradient flow",
            },
            {
                "q": "Why can batch normalization help neural network training?",
                "options": [
                    "It normalizes intermediate activations during training",
                    "It removes all model weights",
                    "It replaces backpropagation",
                    "It guarantees generalization",
                ],
                "answer": "It normalizes intermediate activations during training",
            },
            {
                "q": "What is the main idea behind attention in neural networks?",
                "options": [
                    "Weight the relevance of different input positions",
                    "Delete irrelevant training examples permanently",
                    "Remove every hidden layer",
                    "Replace numerical computation with rules",
                ],
                "answer": "Weight the relevance of different input positions",
            },
        ],
    },

    "Generative AI": {

        "Beginner": [
            {
                "q": "What does an LLM primarily model?",
                "options": [
                    "Patterns in language",
                    "Only image pixels",
                    "Computer hardware temperature",
                    "Network cables",
                ],
                "answer": "Patterns in language",
            },
            {
                "q": "What is a prompt?",
                "options": [
                    "Input instructions or context given to a model",
                    "A database table",
                    "A GPU driver",
                    "A programming language",
                ],
                "answer": "Input instructions or context given to a model",
            },
            {
                "q": "What is generative AI designed to do?",
                "options": [
                    "Generate new content",
                    "Only sort existing files",
                    "Only calculate averages",
                    "Only store databases",
                ],
                "answer": "Generate new content",
            },
        ],

        "Intermediate": [
            {
                "q": "What is an embedding?",
                "options": [
                    "A numerical representation of information",
                    "A physical computer component",
                    "A database password",
                    "A model deployment server",
                ],
                "answer": "A numerical representation of information",
            },
            {
                "q": "What is RAG commonly used for?",
                "options": [
                    "Grounding generation with retrieved information",
                    "Increasing monitor resolution",
                    "Replacing all model parameters",
                    "Removing user context",
                ],
                "answer": "Grounding generation with retrieved information",
            },
            {
                "q": "What is a token in an LLM context?",
                "options": [
                    "A unit of text processed by the model",
                    "A physical GPU core",
                    "A database row",
                    "A network packet only",
                ],
                "answer": "A unit of text processed by the model",
            },
        ],

        "Advanced": [
            {
                "q": "Why can retrieval improve factual grounding in an LLM application?",
                "options": [
                    "Relevant external information can be supplied as context",
                    "It permanently changes the model weights",
                    "It guarantees every generated statement is true",
                    "It removes the need for prompts",
                ],
                "answer": "Relevant external information can be supplied as context",
            },
            {
                "q": "What is the purpose of fine-tuning a language model?",
                "options": [
                    "Adapt model behavior using additional training",
                    "Increase internet bandwidth",
                    "Replace the tokenizer with a database",
                    "Remove all learned representations",
                ],
                "answer": "Adapt model behavior using additional training",
            },
            {
                "q": "Why does context length matter in an LLM application?",
                "options": [
                    "It limits how much input context the model can process at once",
                    "It determines the user's internet speed",
                    "It guarantees factual accuracy",
                    "It determines GPU brand",
                ],
                "answer": "It limits how much input context the model can process at once",
            },
        ],
    },
}


# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "page": "home",
    "profile": {},
    "diagnostic_questions": [],
    "diagnostic_answers": {},
    "scores": {},
    "overall_score": 0,
    "roadmap": [],
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def status_for_score(score):
    if score < 40:
        return "Needs Foundation"
    elif score < 70:
        return "Developing"
    elif score < 100:
        return "Intermediate"
    return "Strong"


def build_diagnostic(level):
    """
    Select exactly 3 different questions from each subject.
    Total = 15 questions.
    """

    questions = []

    for subject in SUBJECTS:
        available = QUESTION_BANK[subject][level]

        selected = random.sample(available, 3)

        for item in selected:
            shuffled_options = item["options"].copy()
            random.shuffle(shuffled_options)

            questions.append(
                {
                    "subject": subject,
                    "question": item["q"],
                    "options": shuffled_options,
                    "answer": item["answer"],
                }
            )

    random.shuffle(questions)

    return questions


def calculate_scores():
    subject_correct = {subject: 0 for subject in SUBJECTS}

    for index, question in enumerate(st.session_state.diagnostic_questions):
        selected = st.session_state.diagnostic_answers.get(index)

        if selected == question["answer"]:
            subject_correct[question["subject"]] += 1

    scores = {}

    for subject in SUBJECTS:
        scores[subject] = round(
            (subject_correct[subject] / 3) * 100
        )

    return scores


def create_roadmap(scores):
    return sorted(
        SUBJECTS,
        key=lambda subject: scores.get(subject, 0)
    )


# =========================================================
# HEADER
# =========================================================

def render_header():

    st.markdown(
        f"""
        <div class="ai-header">

            <div class="ai-brand">
                <img
                    class="ai-logo"
                    src="{LOGO_URL}"
                >
                <div class="ai-brand-name">
                    AI Learn
                </div>
            </div>

            <div class="ai-header-actions">
                <div class="ai-gift">
                    🎁
                </div>
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# HOME PAGE
# =========================================================

def home_page():

    render_header()

    # ---------------- HERO ----------------

    col1, col2 = st.columns([1.05, 0.95], gap="large")

    with col1:

        st.markdown(
            """
            <div class="hero-section">

                <div class="hero-title">
                    Learn AI.<br>
                    <span>Your way.</span>
                </div>

                <div class="hero-subtitle">
                    Build your AI skills with a personalised
                    learning journey that adapts to your
                    knowledge, goals and pace.
                </div>

                <div class="hero-highlight">
                    <strong>AI Learn</strong> helps you discover
                    what you know, identify what to learn next,
                    and build practical AI skills step by step.
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
            <div class="visual-wrapper">

                <div class="visual-main-circle">
                    🤖
                </div>

                <div class="visual-small visual-one">
                    🧑‍💻
                </div>

                <div class="visual-small visual-two">
                    📚
                </div>

                <div class="visual-small visual-three">
                    🧠
                </div>

                <div class="floating-card card-ai">
                    ✨ AI Learning
                </div>

                <div class="floating-card card-progress">
                    📈 Progress
                </div>

                <div class="floating-card card-python">
                    🐍 Python
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    # ---------------- PROFILE ----------------

    st.markdown(
        """
        <div class="profile-section">

            <div class="profile-title">
                👤 Tell us about yourself
            </div>

            <div class="profile-description">
                Start with a short assessment and we'll
                build your personalised AI learning path.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # We put the actual Streamlit inputs immediately below
    # the visual profile heading.

    name = st.text_input(
        "Your Name",
        placeholder="Enter your name",
        key="home_name",
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        level = st.selectbox(
            "Current AI Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced",
            ],
            key="home_level",
        )

    with col2:
        goal = st.selectbox(
            "What is your main goal?",
            [
                "Learn AI fundamentals",
                "Build AI projects",
                "Prepare for a job",
                "Learn Generative AI",
                "Learn AI Agents",
            ],
            key="home_goal",
        )

    with col3:
        study_time = st.selectbox(
            "How much time can you study daily?",
            [
                "15 minutes",
                "30 minutes",
                "1 hour",
                "2+ hours",
            ],
            key="home_time",
        )

    st.write("")

    start_col1, start_col2, start_col3 = st.columns([1, 1, 1])

    with start_col2:

        if st.button(
            "🚀 Start My AI Journey",
            use_container_width=True,
            type="primary",
        ):

            if not name.strip():
                st.error("Please enter your name first.")
                return

            st.session_state.profile = {
                "name": name.strip(),
                "level": level,
                "goal": goal,
                "study_time": study_time,
            }

            st.session_state.diagnostic_questions = build_diagnostic(level)
            st.session_state.diagnostic_answers = {}
            st.session_state.scores = {}
            st.session_state.overall_score = 0

            st.session_state.page = "diagnostic"

            st.rerun()

    # ---------------- FOUNDATIONS ----------------

    st.markdown(
        """
        <div class="foundation-section">

            <div class="foundation-title">
                One journey. Five AI foundations.
            </div>

            <div class="foundation-description">
                Learn the foundations needed to understand,
                build and work with modern AI.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    foundation_data = [
        ("🐍", "Python"),
        ("📐", "Mathematics & Statistics"),
        ("🤖", "Machine Learning"),
        ("🧠", "Deep Learning"),
        ("✨", "Generative AI"),
    ]

    cols = st.columns(5)

    for col, (icon, name_text) in zip(cols, foundation_data):

        with col:

            st.markdown(
                f"""
                <div class="foundation-card">

                    <div class="foundation-icon">
                        {icon}
                    </div>

                    <div class="foundation-name">
                        {name_text}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


# =========================================================
# DIAGNOSTIC PAGE
# =========================================================

def diagnostic_page():

    st.markdown(
        """
        <div class="page-title">
            🎯 AI Knowledge Assessment
        </div>

        <div class="page-description">
            Answer all 15 questions. Your answers will be
            evaluated after you submit the assessment.
        </div>
        """,
        unsafe_allow_html=True,
    )

    profile = st.session_state.profile

    st.info(
        f"Assessment level: {profile.get('level', 'Beginner')}  •  "
        f"15 questions  •  3 questions from each foundation"
    )

    questions = st.session_state.diagnostic_questions

    if not questions:
        st.warning("No diagnostic has been created yet.")
        if st.button("Go to Home"):
            st.session_state.page = "home"
            st.rerun()
        return

    # IMPORTANT:
    # All questions are displayed at once.
    # No topic/subject name is displayed.

    with st.form("diagnostic_form"):

        for index, question in enumerate(questions):

            st.markdown(
                f"""
                <div class="question-card">

                    <div class="question-number">
                        QUESTION {index + 1} OF 15
                    </div>

                    <div class="question-text">
                        {question["question"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            selected = st.radio(
                "Select your answer",
                question["options"],
                index=None,
                key=f"diagnostic_answer_{index}",
                label_visibility="collapsed",
            )

            st.session_state.diagnostic_answers[index] = selected

        st.write("")

        submitted = st.form_submit_button(
            "Submit Assessment →",
            use_container_width=True,
            type="primary",
        )

    if submitted:

        unanswered = []

        for index in range(15):
            answer = st.session_state.get(
                f"diagnostic_answer_{index}"
            )

            if answer is None:
                unanswered.append(index + 1)

            st.session_state.diagnostic_answers[index] = answer

        if unanswered:

            st.error(
                "Please answer all 15 questions before submitting. "
                f"Unanswered questions: {', '.join(map(str, unanswered))}"
            )

            return

        scores = calculate_scores()

        st.session_state.scores = scores

        st.session_state.overall_score = round(
            sum(scores.values()) / len(scores)
        )

        st.session_state.roadmap = create_roadmap(scores)

        st.session_state.page = "score_card"

        st.rerun()


# =========================================================
# SCORE CARD
# =========================================================

def score_card_page():

    scores = st.session_state.scores

    if not scores:
        st.warning("Please complete the diagnostic first.")

        if st.button("Start Diagnostic"):
            st.session_state.page = "home"
            st.rerun()

        return

    overall = st.session_state.overall_score

    st.markdown(
        """
        <div class="page-title">
            🎓 Your AI Learning Score Card
        </div>

        <div class="page-description">
            Here is your current AI knowledge profile.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="score-hero">

            <div class="score-label">
                Overall Score
            </div>

            <div class="score-number">
                {overall}%
            </div>

            <div class="score-subtitle">
                Your current AI knowledge profile
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    for subject in SUBJECTS:

        score = scores[subject]
        status = status_for_score(score)

        st.markdown(
            f"""
            <div class="subject-score-card">

                <div class="subject-name">
                    {subject}
                </div>

                <div class="progress-background">
                    <div
                        class="progress-fill"
                        style="width:{score}%"
                    ></div>
                </div>

                <div class="subject-score">
                    <strong>{score}%</strong>
                    &nbsp; • &nbsp;
                    {status}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    weakest = min(
        SUBJECTS,
        key=lambda subject: scores[subject]
    )

    weakest_score = scores[weakest]

    st.markdown(
        f"""
        <div class="recommendation">

            <div class="recommendation-title">
                🎯 Recommended Starting Point
            </div>

            <div class="recommendation-subject">
                {weakest} — {weakest_score}%
            </div>

            <div style="
                color:#71808e;
                line-height:1.6;
            ">
                Build your foundation here before moving
                deeper into advanced AI topics.
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🗺️ View My Personalised Roadmap",
            use_container_width=True,
            type="primary",
        ):
            st.session_state.page = "roadmap"
            st.rerun()

    with col2:

        if st.button(
            "🔄 Retake Diagnostic",
            use_container_width=True,
        ):

            level = st.session_state.profile.get(
                "level",
                "Beginner",
            )

            st.session_state.diagnostic_questions = build_diagnostic(
                level
            )

            st.session_state.diagnostic_answers = {}

            st.session_state.page = "diagnostic"

            st.rerun()


# =========================================================
# ROADMAP
# =========================================================

def roadmap_page():

    scores = st.session_state.scores

    if not scores:
        st.warning("Complete the diagnostic first.")

        if st.button("Go Home"):
            st.session_state.page = "home"
            st.rerun()

        return

    roadmap = create_roadmap(scores)

    st.markdown(
        """
        <div class="page-title">
            🗺️ Your Personalised AI Roadmap
        </div>

        <div class="page-description">
            Your learning path is ordered from the areas
            that currently need the most attention.
        </div>
        """,
        unsafe_allow_html=True,
    )

    for index, subject in enumerate(roadmap):

        score = scores[subject]

        st.markdown(
            f"""
            <div class="roadmap-card">

                <div class="roadmap-number">
                    STEP {index + 1}
                </div>

                <div class="roadmap-name">
                    {subject}
                </div>

                <div class="roadmap-score">
                    Current score: {score}% •
                    Status: {status_for_score(score)}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    if st.button(
        "← Back to Score Card",
        use_container_width=True,
    ):
        st.session_state.page = "score_card"
        st.rerun()


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🎓 AI Learn")

    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "home"
        st.rerun()

    if st.session_state.scores:

        if st.button(
            "🎓 Score Card",
            use_container_width=True,
        ):
            st.session_state.page = "score_card"
            st.rerun()

        if st.button(
            "🗺️ Roadmap",
            use_container_width=True,
        ):
            st.session_state.page = "roadmap"
            st.rerun()


# =========================================================
# PAGE ROUTER
# =========================================================

if st.session_state.page == "home":

    home_page()

elif st.session_state.page == "diagnostic":

    diagnostic_page()

elif st.session_state.page == "score_card":

    score_card_page()

elif st.session_state.page == "roadmap":

    roadmap_page()

else:

    st.session_state.page = "home"
    st.rerun()
