import streamlit as st
import random
import os
import base64


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI Learn",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# APP SETTINGS
# ============================================================

APP_NAME = "AI Learn"

LOGO_FILE = "0f6577fe444ba6b1365cd00394ee581e.jpg"

SUBJECTS = [
    "Python",
    "Mathematics & Statistics",
    "Machine Learning",
    "Deep Learning",
    "Generative AI",
]


# ============================================================
# SESSION STATE
# ============================================================

DEFAULTS = {
    "page": "home",
    "profile": {},
    "diagnostic_questions": [],
    "diagnostic_answers": [],
    "scores": {},
    "roadmap": [],
    "seen_questions": set(),
}

for key, value in DEFAULTS.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       GENERAL
    ====================================================== */

    .stApp {
        background: #ffffff;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 0.5rem;
        padding-bottom: 3rem;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* ======================================================
       HEADER
    ====================================================== */

    .ai-header {
        height: 76px;
        border-bottom: 1px solid #e7ebef;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 4px;
        margin-bottom: 0;
    }

    .brand-area {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .brand-logo {
        width: 48px;
        height: 48px;
        object-fit: contain;
        border-radius: 8px;
    }

    .brand-name {
        font-size: 26px;
        font-weight: 750;
        color: #25313c;
        letter-spacing: -0.5px;
    }

    .header-actions {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .gift-box {
        width: 44px;
        height: 44px;
        border: 1px solid #e1e6eb;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        background: #ffffff;
    }

    .login-button {
        border: 1px solid #344454;
        border-radius: 8px;
        padding: 12px 27px;
        color: #25313c;
        background: #ffffff;
        font-weight: 600;
        font-size: 15px;
    }

    .join-button {
        border-radius: 8px;
        padding: 13px 23px;
        color: #ffffff;
        background: #344454;
        font-weight: 700;
        font-size: 15px;
    }

    /* ======================================================
       HERO
    ====================================================== */

    .hero-title {
        font-size: 56px;
        line-height: 1.08;
        font-weight: 800;
        letter-spacing: -2px;
        color: #35424f;
        margin-top: 45px;
        margin-bottom: 18px;
    }

    .hero-title span {
        color: #111111;
    }

    .hero-subtitle {
        font-size: 20px;
        line-height: 1.55;
        color: #566573;
        max-width: 590px;
        margin-bottom: 20px;
    }

    .hero-highlight {
        font-size: 16px;
        line-height: 1.6;
        color: #566573;
        max-width: 590px;
        margin-bottom: 25px;
    }

    .hero-highlight strong {
        color: #10a37f;
    }

    /* ======================================================
       PROFILE CARD
    ====================================================== */

    .profile-card {
        background: #ffffff;
        border: 1px solid #e1e7ec;
        border-radius: 12px;
        padding: 22px;
        margin-top: 12px;
        box-shadow: 0 8px 28px rgba(35, 50, 65, 0.06);
    }

    .profile-title {
        font-size: 21px;
        font-weight: 750;
        color: #25313c;
        margin-bottom: 7px;
    }

    .profile-description {
        color: #687783;
        font-size: 14px;
        line-height: 1.5;
        margin-bottom: 15px;
    }

    /* ======================================================
       HERO VISUAL
    ====================================================== */

    .learning-visual {
        position: relative;
        width: 490px;
        height: 430px;
        margin-top: 45px;
    }

    .visual-circle {
        position: absolute;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 10px 30px rgba(30, 50, 70, 0.08);
    }

    .circle-one {
        width: 190px;
        height: 190px;
        left: 15px;
        top: 20px;
        background: #e9f3ff;
        font-size: 78px;
    }

    .circle-two {
        width: 165px;
        height: 165px;
        right: 20px;
        top: 15px;
        background: #fff4cf;
        font-size: 65px;
    }

    .circle-three {
        width: 175px;
        height: 175px;
        left: 120px;
        bottom: 15px;
        background: #e8f8f3;
        font-size: 70px;
    }

    .circle-four {
        width: 180px;
        height: 180px;
        right: 0;
        bottom: 5px;
        background: #f6eafa;
        font-size: 70px;
    }

    .floating-card {
        position: absolute;
        background: #ffffff;
        border: 1px solid #e7ebef;
        border-radius: 14px;
        padding: 13px 16px;
        box-shadow: 0 12px 35px rgba(40, 55, 70, 0.10);
        font-weight: 700;
        color: #344454;
    }

    .card-ai {
        left: 145px;
        top: 175px;
    }

    .card-progress {
        right: 80px;
        top: 195px;
    }

    .card-python {
        left: 5px;
        bottom: 105px;
    }

    /* ======================================================
       FOUNDATION SECTION
    ====================================================== */

    .section-title {
        text-align: center;
        font-size: 34px;
        color: #344454;
        font-weight: 800;
        margin-top: 55px;
    }

    .section-description {
        text-align: center;
        color: #687783;
        font-size: 17px;
        margin-bottom: 32px;
    }

    /* ======================================================
       DIAGNOSTIC
    ====================================================== */

    .diagnostic-header {
        background: #f7fafc;
        border: 1px solid #e3e9ee;
        border-radius: 16px;
        padding: 25px;
        margin-top: 25px;
        margin-bottom: 25px;
    }

    .question-card {
        background: #ffffff;
        border: 1px solid #e2e7ec;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 18px;
    }

    .question-number {
        color: #10a37f;
        font-size: 14px;
        font-weight: 750;
        margin-bottom: 7px;
    }

    .question-text {
        color: #26333e;
        font-size: 18px;
        line-height: 1.45;
        font-weight: 650;
    }

    /* ======================================================
       SCORE CARD
    ====================================================== */

    .score-header {
        background: #f7fafc;
        border: 1px solid #e3e9ee;
        border-radius: 18px;
        padding: 35px;
        text-align: center;
        margin-top: 25px;
        margin-bottom: 28px;
    }

    .score-number {
        font-size: 64px;
        line-height: 1;
        font-weight: 850;
        color: #344454;
        margin-top: 10px;
    }

    .score-label {
        color: #687783;
        font-size: 16px;
    }

    .recommendation-card {
        background: #f4faf8;
        border: 1px solid #d8eee7;
        border-radius: 14px;
        padding: 22px;
        margin-top: 15px;
        margin-bottom: 25px;
    }

    /* ======================================================
       MOBILE
    ====================================================== */

    @media (max-width: 900px) {

        .header-actions {
            display: none;
        }

        .hero-title {
            font-size: 42px;
        }

        .learning-visual {
            transform: scale(0.78);
            transform-origin: top center;
            margin: 0 auto;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# LOGO HELPER
# ============================================================

def get_logo_base64():

    if not os.path.exists(LOGO_FILE):

        return None

    try:

        with open(LOGO_FILE, "rb") as file:

            encoded = base64.b64encode(
                file.read()
            ).decode()

        return encoded

    except Exception:

        return None


# ============================================================
# QUESTION BANK
#
# 5 questions per level per subject.
# The diagnostic selects 3 from the learner's level.
# ============================================================

QUESTION_BANK = [

    # ========================================================
    # PYTHON - BEGINNER
    # ========================================================

    {
        "id": "py_b_01",
        "subject": "Python",
        "level": "Beginner",
        "question": "Which symbol starts a comment in Python?",
        "options": ["//", "#", "/*", "<!--"],
        "answer": "#",
    },
    {
        "id": "py_b_02",
        "subject": "Python",
        "level": "Beginner",
        "question": "Which Python type represents True or False?",
        "options": ["String", "Boolean", "List", "Integer"],
        "answer": "Boolean",
    },
    {
        "id": "py_b_03",
        "subject": "Python",
        "level": "Beginner",
        "question": "Which function prints text to the console?",
        "options": ["show()", "display()", "print()", "write()"],
        "answer": "print()",
    },
    {
        "id": "py_b_04",
        "subject": "Python",
        "level": "Beginner",
        "question": "Which collection is ordered and changeable?",
        "options": ["Tuple", "List", "Set", "Frozen set"],
        "answer": "List",
    },
    {
        "id": "py_b_05",
        "subject": "Python",
        "level": "Beginner",
        "question": "What is the result of 3 + 4 * 2?",
        "options": ["14", "11", "10", "9"],
        "answer": "11",
    },

    # PYTHON - INTERMEDIATE

    {
        "id": "py_i_01",
        "subject": "Python",
        "level": "Intermediate",
        "question": "What does a list comprehension provide?",
        "options": [
            "A concise way to create lists",
            "A database connection",
            "A Python compiler",
            "A way to define classes",
        ],
        "answer": "A concise way to create lists",
    },
    {
        "id": "py_i_02",
        "subject": "Python",
        "level": "Intermediate",
        "question": "What does a Python dictionary primarily store?",
        "options": [
            "Key-value mappings",
            "Only numbers",
            "Only strings",
            "Functions only",
        ],
        "answer": "Key-value mappings",
    },
    {
        "id": "py_i_03",
        "subject": "Python",
        "level": "Intermediate",
        "question": "What does len([10, 20, 30]) return?",
        "options": ["2", "3", "30", "60"],
        "answer": "3",
    },
    {
        "id": "py_i_04",
        "subject": "Python",
        "level": "Intermediate",
        "question": "Which keyword defines a function?",
        "options": ["function", "define", "def", "func"],
        "answer": "def",
    },
    {
        "id": "py_i_05",
        "subject": "Python",
        "level": "Intermediate",
        "question": "What is the purpose of a function?",
        "options": [
            "Group reusable logic",
            "Install packages",
            "Create an operating system",
            "Store files",
        ],
        "answer": "Group reusable logic",
    },

    # PYTHON - ADVANCED

    {
        "id": "py_a_01",
        "subject": "Python",
        "level": "Advanced",
        "question": "What is the main purpose of a generator?",
        "options": [
            "Produce values lazily during iteration",
            "Compile Python code",
            "Automatically parallelize code",
            "Prevent all memory allocation",
        ],
        "answer": "Produce values lazily during iteration",
    },
    {
        "id": "py_a_02",
        "subject": "Python",
        "level": "Advanced",
        "question": "What does a decorator generally allow you to do?",
        "options": [
            "Modify or extend function behavior",
            "Delete Python modules",
            "Disable exceptions",
            "Convert lists to databases",
        ],
        "answer": "Modify or extend function behavior",
    },
    {
        "id": "py_a_03",
        "subject": "Python",
        "level": "Advanced",
        "question": "Which OOP concept allows a class to acquire behavior from another class?",
        "options": [
            "Encapsulation",
            "Inheritance",
            "Iteration",
            "Serialization",
        ],
        "answer": "Inheritance",
    },
    {
        "id": "py_a_04",
        "subject": "Python",
        "level": "Advanced",
        "question": "What is a context manager commonly used for?",
        "options": [
            "Managing setup and cleanup of resources",
            "Removing all exceptions",
            "Automatically making code asynchronous",
            "Converting Python to C++",
        ],
        "answer": "Managing setup and cleanup of resources",
    },
    {
        "id": "py_a_05",
        "subject": "Python",
        "level": "Advanced",
        "question": "What does *args allow in a function definition?",
        "options": [
            "An arbitrary number of positional arguments",
            "Only keyword arguments",
            "Exactly one argument",
            "An arbitrary number of classes",
        ],
        "answer": "An arbitrary number of positional arguments",
    },


    # ========================================================
    # MATH - BEGINNER
    # ========================================================

    {
        "id": "math_b_01",
        "subject": "Mathematics & Statistics",
        "level": "Beginner",
        "question": "What is the mean of 2, 4, and 6?",
        "options": ["3", "4", "5", "6"],
        "answer": "4",
    },
    {
        "id": "math_b_02",
        "subject": "Mathematics & Statistics",
        "level": "Beginner",
        "question": "What does probability measure?",
        "options": [
            "Likelihood of an event",
            "Dataset size",
            "Average value",
            "Number of features",
        ],
        "answer": "Likelihood of an event",
    },
    {
        "id": "math_b_03",
        "subject": "Mathematics & Statistics",
        "level": "Beginner",
        "question": "Which measure represents the middle value of ordered data?",
        "options": ["Mean", "Median", "Variance", "Range"],
        "answer": "Median",
    },
    {
        "id": "math_b_04",
        "subject": "Mathematics & Statistics",
        "level": "Beginner",
        "question": "What is 10% of 200?",
        "options": ["10", "20", "30", "40"],
        "answer": "20",
    },
    {
        "id": "math_b_05",
        "subject": "Mathematics & Statistics",
        "level": "Beginner",
        "question": "What does the range of a dataset represent?",
        "options": [
            "Maximum minus minimum",
            "Mean divided by median",
            "Number of observations",
            "Average",
        ],
        "answer": "Maximum minus minimum",
    },

    # MATH - INTERMEDIATE

    {
        "id": "math_i_01",
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What does variance measure?",
        "options": [
            "Spread around the mean",
            "The middle value",
            "Maximum value",
            "Number of features",
        ],
        "answer": "Spread around the mean",
    },
    {
        "id": "math_i_02",
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What does a correlation coefficient describe?",
        "options": [
            "Strength and direction of a relationship",
            "Number of outliers",
            "Number of features",
            "Dataset size",
        ],
        "answer": "Strength and direction of a relationship",
    },
    {
        "id": "math_i_03",
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What does standard deviation measure?",
        "options": [
            "Spread of observations",
            "Largest observation",
            "Number of classes",
            "Dataset size",
        ],
        "answer": "Spread of observations",
    },
    {
        "id": "math_i_04",
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What is a statistical sample?",
        "options": [
            "A subset of a population",
            "The entire population",
            "A constant",
            "A neural network",
        ],
        "answer": "A subset of a population",
    },
    {
        "id": "math_i_05",
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What does negative correlation generally indicate?",
        "options": [
            "One variable tends to increase as the other decreases",
            "Both variables always increase",
            "Variables are identical",
            "There is no variation",
        ],
        "answer": "One variable tends to increase as the other decreases",
    },

    # MATH - ADVANCED

    {
        "id": "math_a_01",
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "Why is the gradient useful in optimization?",
        "options": [
            "It indicates the direction of greatest increase",
            "It labels training data",
            "It removes categorical features",
            "It determines dataset size",
        ],
        "answer": "It indicates the direction of greatest increase",
    },
    {
        "id": "math_a_02",
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "What does a covariance matrix contain?",
        "options": [
            "Variances and pairwise covariances",
            "Only means",
            "Only labels",
            "Only class counts",
        ],
        "answer": "Variances and pairwise covariances",
    },
    {
        "id": "math_a_03",
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "Why are eigenvectors useful in dimensionality reduction?",
        "options": [
            "They identify important directions of variation",
            "They create labels",
            "They replace missing values",
            "They remove training data",
        ],
        "answer": "They identify important directions of variation",
    },
    {
        "id": "math_a_04",
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "What does a derivative describe locally?",
        "options": [
            "Rate of change",
            "Number of observations",
            "Class probability",
            "Dataset size",
        ],
        "answer": "Rate of change",
    },
    {
        "id": "math_a_05",
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "What is Bayes' theorem used to calculate?",
        "options": [
            "Conditional probability using prior information",
            "Dataset mean",
            "Number of neurons",
            "Image dimensions",
        ],
        "answer": "Conditional probability using prior information",
    },


    # ========================================================
    # MACHINE LEARNING - BEGINNER
    # ========================================================

    {
        "id": "ml_b_01",
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "What is supervised learning?",
        "options": [
            "Learning from labelled examples",
            "Learning without data",
            "Only clustering",
            "Manually writing prediction rules",
        ],
        "answer": "Learning from labelled examples",
    },
    {
        "id": "ml_b_02",
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "What is a training dataset used for?",
        "options": [
            "Teaching a model patterns from data",
            "Displaying a website",
            "Deleting parameters",
            "Writing documentation",
        ],
        "answer": "Teaching a model patterns from data",
    },
    {
        "id": "ml_b_03",
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "Which is a classification problem?",
        "options": [
            "Predicting whether an email is spam",
            "Predicting house price",
            "Grouping customers",
            "Reducing image dimensions",
        ],
        "answer": "Predicting whether an email is spam",
    },
    {
        "id": "ml_b_04",
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "Which is a regression problem?",
        "options": [
            "Predicting a house price",
            "Detecting spam",
            "Grouping customers",
            "Finding image edges",
        ],
        "answer": "Predicting a house price",
    },
    {
        "id": "ml_b_05",
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "What is a feature?",
        "options": [
            "An input variable used by a model",
            "Only the prediction",
            "The model filename",
            "The training computer",
        ],
        "answer": "An input variable used by a model",
    },

    # ML - INTERMEDIATE

    {
        "id": "ml_i_01",
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "What is overfitting?",
        "options": [
            "A model learns training data too specifically",
            "A model has no parameters",
            "A model has no training data",
            "A model always performs perfectly",
        ],
        "answer": "A model learns training data too specifically",
    },
    {
        "id": "ml_i_02",
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "Why is a validation set useful?",
        "options": [
            "For evaluating choices during development",
            "For deleting training data",
            "For removing all features",
            "For converting regression to clustering",
        ],
        "answer": "For evaluating choices during development",
    },
    {
        "id": "ml_i_03",
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "What is feature scaling used for?",
        "options": [
            "Putting numerical features on comparable scales",
            "Adding labels",
            "Deleting the target",
            "Increasing classes",
        ],
        "answer": "Putting numerical features on comparable scales",
    },
    {
        "id": "ml_i_04",
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "What is clustering?",
        "options": [
            "Grouping similar observations without predefined labels",
            "Predicting a continuous target",
            "Training on labelled images",
            "Removing numerical features",
        ],
        "answer": "Grouping similar observations without predefined labels",
    },
    {
        "id": "ml_i_05",
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "What does recall measure?",
        "options": [
            "The proportion of actual positives correctly identified",
            "The proportion of predicted positives that are correct",
            "The number of parameters",
            "Dataset size",
        ],
        "answer": "The proportion of actual positives correctly identified",
    },

    # ML - ADVANCED

    {
        "id": "ml_a_01",
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "Why can data leakage produce misleading validation results?",
        "options": [
            "Information unavailable at prediction time influenced development",
            "The model has too few parameters",
            "The dataset is always too small",
            "The model uses gradient descent",
        ],
        "answer": "Information unavailable at prediction time influenced development",
    },
    {
        "id": "ml_a_02",
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "What is the bias-variance tradeoff concerned with?",
        "options": [
            "Balancing underfitting and sensitivity to training data",
            "Choosing programming languages",
            "Increasing storage",
            "Selecting a database",
        ],
        "answer": "Balancing underfitting and sensitivity to training data",
    },
    {
        "id": "ml_a_03",
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "Why might cross-validation be used?",
        "options": [
            "To estimate generalization across multiple data splits",
            "To guarantee zero test error",
            "To eliminate the target",
            "To make every model linear",
        ],
        "answer": "To estimate generalization across multiple data splits",
    },
    {
        "id": "ml_a_04",
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "What does regularization generally encourage?",
        "options": [
            "Simpler model parameters to reduce overfitting",
            "More labels",
            "Larger datasets automatically",
            "Removal of validation data",
        ],
        "answer": "Simpler model parameters to reduce overfitting",
    },
    {
        "id": "ml_a_05",
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "Why is class imbalance important?",
        "options": [
            "Accuracy can hide poor minority-class performance",
            "It always makes training impossible",
            "It guarantees overfitting",
            "It removes evaluation metrics",
        ],
        "answer": "Accuracy can hide poor minority-class performance",
    },


    # ========================================================
    # DEEP LEARNING - BEGINNER
    # ========================================================

    {
        "id": "dl_b_01",
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What is a neural network?",
        "options": [
            "A model made of interconnected computational units",
            "A database table",
            "A programming language",
            "A compression format",
        ],
        "answer": "A model made of interconnected computational units",
    },
    {
        "id": "dl_b_02",
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What is an activation function used for?",
        "options": [
            "Introducing nonlinear behavior",
            "Storing datasets",
            "Deleting weights",
            "Downloading Python",
        ],
        "answer": "Introducing nonlinear behavior",
    },
    {
        "id": "dl_b_03",
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What is an epoch?",
        "options": [
            "One complete pass through the training dataset",
            "One feature",
            "One neuron",
            "One test example",
        ],
        "answer": "One complete pass through the training dataset",
    },
    {
        "id": "dl_b_04",
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What are neural network weights?",
        "options": [
            "Learnable parameters used to transform inputs",
            "Dataset filenames",
            "Class labels",
            "Python packages",
        ],
        "answer": "Learnable parameters used to transform inputs",
    },
    {
        "id": "dl_b_05",
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What is a loss function used for?",
        "options": [
            "Measuring how far predictions are from desired outputs",
            "Increasing image resolution",
            "Creating database tables",
            "Removing parameters",
        ],
        "answer": "Measuring how far predictions are from desired outputs",
    },

    # DL - INTERMEDIATE

    {
        "id": "dl_i_01",
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What is backpropagation used for?",
        "options": [
            "Computing gradients used to update parameters",
            "Creating training labels",
            "Compressing images",
            "Selecting database rows",
        ],
        "answer": "Computing gradients used to update parameters",
    },
    {
        "id": "dl_i_02",
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What do convolutional neural networks commonly excel at?",
        "options": [
            "Learning spatial patterns in data such as images",
            "Managing operating systems",
            "Writing SQL",
            "Sorting Python lists",
        ],
        "answer": "Learning spatial patterns in data such as images",
    },
    {
        "id": "dl_i_03",
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What is an optimizer used for?",
        "options": [
            "Updating model parameters using gradient information",
            "Creating labels",
            "Removing the loss function",
            "Storing images",
        ],
        "answer": "Updating model parameters using gradient information",
    },
    {
        "id": "dl_i_04",
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "Why can ReLU help deep networks?",
        "options": [
            "It provides nonlinear activation and can help gradient flow",
            "It removes neurons",
            "It guarantees no overfitting",
            "It converts images into labels",
        ],
        "answer": "It provides nonlinear activation and can help gradient flow",
    },
    {
        "id": "dl_i_05",
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What is dropout commonly used for?",
        "options": [
            "Reducing over-reliance on particular neurons during training",
            "Increasing labels",
            "Replacing the optimizer",
            "Converting regression to classification",
        ],
        "answer": "Reducing over-reliance on particular neurons during training",
    },

    # DL - ADVANCED

    {
        "id": "dl_a_01",
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "Why can very deep networks suffer from vanishing gradients?",
        "options": [
            "Gradients can become extremely small during backward propagation",
            "The dataset has too many rows",
            "The optimizer always increases gradients",
            "Neural networks cannot use activation functions",
        ],
        "answer": "Gradients can become extremely small during backward propagation",
    },
    {
        "id": "dl_a_02",
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "What is the key idea behind residual connections?",
        "options": [
            "Provide a shortcut path while learning a residual transformation",
            "Remove all nonlinearities",
            "Prevent training",
            "Replace every convolution with pooling",
        ],
        "answer": "Provide a shortcut path while learning a residual transformation",
    },
    {
        "id": "dl_a_03",
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "What does batch normalization primarily do?",
        "options": [
            "Normalize activations within training batches",
            "Create new training examples",
            "Delete parameters",
            "Convert classification into clustering",
        ],
        "answer": "Normalize activations within training batches",
    },
    {
        "id": "dl_a_04",
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "Why are attention mechanisms useful in sequence modeling?",
        "options": [
            "They let the model weight different parts of the input",
            "They eliminate all parameters",
            "They only work with tables",
            "They guarantee perfect predictions",
        ],
        "answer": "They let the model weight different parts of the input",
    },
    {
        "id": "dl_a_05",
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "What does learning rate control?",
        "options": [
            "The size of parameter updates during optimization",
            "The number of examples",
            "The number of classes",
            "Model accuracy",
        ],
        "answer": "The size of parameter updates during optimization",
    },


    # ========================================================
    # GENERATIVE AI - BEGINNER
    # ========================================================

    {
        "id": "gen_b_01",
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What is Generative AI designed to do?",
        "options": [
            "Generate new content based on learned patterns",
            "Only store files",
            "Only calculate averages",
            "Only sort data",
        ],
        "answer": "Generate new content based on learned patterns",
    },
    {
        "id": "gen_b_02",
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What does LLM stand for?",
        "options": [
            "Large Language Model",
            "Logical Learning Machine",
            "Large Logic Memory",
            "Language Learning Method",
        ],
        "answer": "Large Language Model",
    },
    {
        "id": "gen_b_03",
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What is a prompt?",
        "options": [
            "Instructions or input given to an AI model",
            "A model database",
            "A hardware component",
            "A Python compiler",
        ],
        "answer": "Instructions or input given to an AI model",
    },
    {
        "id": "gen_b_04",
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What can a text-generating AI model produce?",
        "options": [
            "Text based on learned patterns and instructions",
            "Only spreadsheets",
            "Only hardware",
            "Only database indexes",
        ],
        "answer": "Text based on learned patterns and instructions",
    },
    {
        "id": "gen_b_05",
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What is an AI chatbot?",
        "options": [
            "A system that interacts with users using conversational responses",
            "A database engine",
            "A graphics card",
            "A programming language",
        ],
        "answer": "A system that interacts with users using conversational responses",
    },

    # GENAI - INTERMEDIATE

    {
        "id": "gen_i_01",
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "What are tokens in language models?",
        "options": [
            "Units of text processed by the model",
            "Database passwords",
            "Training computers",
            "Neural network layers",
        ],
        "answer": "Units of text processed by the model",
    },
    {
        "id": "gen_i_02",
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "What is an embedding?",
        "options": [
            "A numerical representation of information in vector space",
            "A database password",
            "A hardware component",
            "A Python exception",
        ],
        "answer": "A numerical representation of information in vector space",
    },
    {
        "id": "gen_i_03",
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "What does RAG stand for?",
        "options": [
            "Retrieval-Augmented Generation",
            "Random AI Generation",
            "Recursive Answer Generator",
            "Rapid Automated Grading",
        ],
        "answer": "Retrieval-Augmented Generation",
    },
    {
        "id": "gen_i_04",
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "Why can RAG be useful?",
        "options": [
            "It provides a model with relevant retrieved information",
            "It removes the need for data",
            "It guarantees correctness",
            "It replaces neural networks",
        ],
        "answer": "It provides a model with relevant retrieved information",
    },
    {
        "id": "gen_i_05",
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "What does temperature commonly influence?",
        "options": [
            "Randomness of token selection",
            "Model memory size",
            "Training examples",
            "Number of GPUs",
        ],
        "answer": "Randomness of token selection",
    },

    # GENAI - ADVANCED

    {
        "id": "gen_a_01",
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "What is the central idea of self-attention in Transformers?",
        "options": [
            "Tokens can assign different importance to other tokens",
            "Every token is treated identically",
            "Token order is removed",
            "Only one token is processed",
        ],
        "answer": "Tokens can assign different importance to other tokens",
    },
    {
        "id": "gen_a_02",
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "Why are vector embeddings useful for semantic search?",
        "options": [
            "Related items can be represented near each other in vector space",
            "They guarantee factual correctness",
            "They eliminate documents",
            "They directly produce answers",
        ],
        "answer": "Related items can be represented near each other in vector space",
    },
    {
        "id": "gen_a_03",
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "What is fine-tuning generally used for?",
        "options": [
            "Adapting a pretrained model to a specific task or dataset",
            "Deleting pretrained knowledge",
            "Increasing internet bandwidth",
            "Replacing tokenization",
        ],
        "answer": "Adapting a pretrained model to a specific task or dataset",
    },
    {
        "id": "gen_a_04",
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "What is an LLM hallucination?",
        "options": [
            "A generated response containing unsupported or incorrect information",
            "A GPU failure",
            "A dataset format",
            "A tokenization algorithm",
        ],
        "answer": "A generated response containing unsupported or incorrect information",
    },
    {
        "id": "gen_a_05",
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "Why does context-window size matter?",
        "options": [
            "It limits how much input context the model can process",
            "It determines the physical memory chip",
            "It guarantees factual accuracy",
            "It determines the number of users",
        ],
        "answer": "It limits how much input context the model can process",
    },
]


# ============================================================
# QUESTION CREATION
# ============================================================

def create_diagnostic(level):

    questions = []

    for subject in SUBJECTS:

        available = [
            q
            for q in QUESTION_BANK
            if q["subject"] == subject
            and q["level"] == level
            and q["id"] not in st.session_state.seen_questions
        ]

        # If previous questions have been exhausted,
        # allow previously seen questions again.
        if len(available) < 3:

            available = [
                q
                for q in QUESTION_BANK
                if q["subject"] == subject
                and q["level"] == level
            ]

        chosen = random.sample(
            available,
            3
        )

        for question in chosen:

            copied = question.copy()

            options = copied["options"].copy()

            random.shuffle(options)

            copied["options"] = options

            questions.append(copied)

            st.session_state.seen_questions.add(
                copied["id"]
            )

    random.shuffle(questions)

    return questions


# ============================================================
# SCORE CALCULATION
# ============================================================

def calculate_scores():

    scores = {}

    for subject in SUBJECTS:

        subject_questions = [
            q
            for q in st.session_state.diagnostic_questions
            if q["subject"] == subject
        ]

        correct = 0

        for index, question in enumerate(
            st.session_state.diagnostic_questions
        ):

            if question["subject"] != subject:
                continue

            answer = st.session_state.diagnostic_answers[index]

            if answer == question["answer"]:

                correct += 1

        if subject_questions:

            scores[subject] = round(
                correct
                / len(subject_questions)
                * 100
            )

        else:

            scores[subject] = 0

    return scores


# ============================================================
# STATUS
# ============================================================

def get_status(score):

    if score < 40:

        return "Needs Foundation"

    if score < 70:

        return "Developing"

    if score < 100:

        return "Intermediate"

    return "Strong"


# ============================================================
# ROADMAP
# ============================================================

def create_roadmap(scores):

    ordered = sorted(
        scores.items(),
        key=lambda x: x[1]
    )

    roadmap = []

    for position, (subject, score) in enumerate(
        ordered
    ):

        if position == 0:

            priority = "High Priority"

        elif position == 1:

            priority = "Priority"

        else:

            priority = "Continue"

        roadmap.append(
            {
                "subject": subject,
                "score": score,
                "priority": priority,
            }
        )

    return roadmap


# ============================================================
# HEADER
# ============================================================

def render_header():

    logo = get_logo_base64()

    if logo:

        logo_html = (
            f'<img class="brand-logo" '
            f'src="data:image/jpeg;base64,{logo}">'
        )

    else:

        logo_html = (
            '<div class="brand-logo" '
            'style="background:#111111; '
            'display:flex;align-items:center;'
            'justify-content:center;color:white;'
            'font-weight:800;">AI</div>'
        )

    st.markdown(
        f"""
        <div class="ai-header">

            <div class="brand-area">

                {logo_html}

                <div class="brand-name">
                    AI Learn
                </div>

            </div>

            <div class="header-actions">

                <div class="gift-box">
                    🎁
                </div>

                <div class="login-button">
                    Log in
                </div>

                <div class="join-button">
                    Join for free
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# HOME PAGE
# ============================================================

def home_page():

    render_header()

    left, right = st.columns(
        [1.08, 0.92],
        gap="large"
    )

    # --------------------------------------------------------
    # LEFT
    # --------------------------------------------------------

    with left:

        st.markdown(
            """
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

            <div class="profile-card">

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

        name = st.text_input(
            "Your Name",
            value=st.session_state.profile.get(
                "name",
                ""
            ),
            placeholder="Enter your name"
        )

        level = st.selectbox(
            "Current AI Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced",
            ]
        )

        goal = st.selectbox(
            "What is your main goal?",
            [
                "Learn AI fundamentals",
                "Build AI projects",
                "Prepare for a job",
                "Learn Generative AI",
                "Learn AI Agents",
            ]
        )

        study_time = st.selectbox(
            "How much time can you study daily?",
            [
                "15 minutes",
                "30 minutes",
                "1 hour",
                "2+ hours",
            ]
        )

        st.write("")

        if st.button(
            "🚀 Start My AI Journey",
            use_container_width=True,
            type="primary"
        ):

            if not name.strip():

                st.warning(
                    "Please enter your name first."
                )

            else:

                st.session_state.profile = {
                    "name": name.strip(),
                    "level": level,
                    "goal": goal,
                    "study_time": study_time,
                }

                st.session_state.diagnostic_questions = (
                    create_diagnostic(level)
                )

                st.session_state.diagnostic_answers = []

                st.session_state.scores = {}

                st.session_state.roadmap = []

                st.session_state.page = "diagnostic"

                st.rerun()

    # --------------------------------------------------------
    # RIGHT VISUAL
    # --------------------------------------------------------

    with right:

        st.markdown(
            """
            <div class="learning-visual">

                <div class="visual-circle circle-one">
                    🧑‍💻
                </div>

                <div class="visual-circle circle-two">
                    🤖
                </div>

                <div class="visual-circle circle-three">
                    📚
                </div>

                <div class="visual-circle circle-four">
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
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # FOUNDATIONS
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="section-title">
            One journey. Five AI foundations.
        </div>

        <div class="section-description">
            Learn the foundations needed to understand,
            build and work with modern AI.
        </div>
        """,
        unsafe_allow_html=True
    )

    cards = [
        ("🐍", "Python"),
        ("📐", "Mathematics & Statistics"),
        ("🤖", "Machine Learning"),
        ("🧠", "Deep Learning"),
        ("✨", "Generative AI"),
    ]

    columns = st.columns(5)

    for column, (icon, subject) in zip(
        columns,
        cards
    ):

        with column:

            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    border:1px solid #e5e9ed;
                    border-radius:14px;
                    padding:20px 8px;
                    background:white;
                    min-height:125px;
                ">

                    <div style="
                        font-size:30px;
                        margin-bottom:8px;
                    ">
                        {icon}
                    </div>

                    <div style="
                        font-size:14px;
                        font-weight:700;
                        color:#344454;
                        line-height:1.3;
                    ">
                        {subject}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# DIAGNOSTIC PAGE
# ============================================================

def diagnostic_page():

    questions = st.session_state.diagnostic_questions

    if not questions:

        st.session_state.page = "home"

        st.rerun()

        return

    render_header()

    learner_name = st.session_state.profile.get(
        "name",
        "Learner"
    )

    learner_level = st.session_state.profile.get(
        "level",
        "Beginner"
    )

    st.markdown(
        """
        <div class="diagnostic-header">

            <h1>
                🧠 AI Knowledge Diagnostic
            </h1>

            <p>
                Answer all 15 questions to help AI Learn
                understand your current knowledge.
            </p>

            <p>
                Your results will be shown only after
                you submit the complete assessment.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        f"Welcome, **{learner_name}**."
    )

    st.caption(
        f"Assessment level: {learner_level} • "
        "15 questions • 3 from each learning area"
    )

    st.divider()

    answers = []

    # ========================================================
    # ALL 15 QUESTIONS
    # ========================================================

    for index, question in enumerate(
        questions
    ):

        question_number = index + 1

        st.markdown(
            f"""
            <div class="question-card">

                <div class="question-number">
                    QUESTION {question_number} OF 15
                </div>

                <div class="question-text">
                    {question["question"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        selected = st.radio(
            "Select one answer:",
            question["options"],
            index=None,
            key=f"diagnostic_answer_{index}",
            label_visibility="collapsed"
        )

        answers.append(selected)

        st.write("")

    # ========================================================
    # SUBMIT
    # ========================================================

    st.divider()

    unanswered = [
        index + 1
        for index, answer in enumerate(answers)
        if answer is None
    ]

    if unanswered:

        st.info(
            f"{len(unanswered)} question(s) still need "
            "an answer before you can submit."
        )

    if st.button(
        "🎯 Submit Diagnostic",
        use_container_width=True,
        type="primary"
    ):

        if unanswered:

            numbers = ", ".join(
                str(number)
                for number in unanswered
            )

            st.warning(
                f"Please answer question(s): {numbers}"
            )

            st.stop()

        # ----------------------------------------------------
        # Convert selected text into stored answers
        # ----------------------------------------------------

        st.session_state.diagnostic_answers = answers

        # ----------------------------------------------------
        # Calculate scores only now
        # ----------------------------------------------------

        scores = calculate_scores()

        st.session_state.scores = scores

        st.session_state.roadmap = create_roadmap(
            scores
        )

        st.session_state.page = "score_card"

        st.rerun()


# ============================================================
# SCORE CARD
# ============================================================

def score_card_page():

    scores = st.session_state.scores

    if not scores:

        st.session_state.page = "home"

        st.rerun()

        return

    render_header()

    overall = round(
        sum(scores.values())
        / len(scores)
    )

    weakest_subject = min(
        scores,
        key=scores.get
    )

    weakest_score = scores[
        weakest_subject
    ]

    st.markdown(
        f"""
        <div class="score-header">

            <div style="font-size:42px;">
                🎓
            </div>

            <h1>
                YOUR AI LEARNING SCORE CARD
            </h1>

            <div class="score-label">
                Current AI knowledge profile
            </div>

            <div class="score-number">
                {overall}%
            </div>

            <div class="score-label">
                Overall Score
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader(
        "📚 Subject Scores"
    )

    for subject in SUBJECTS:

        score = scores[subject]

        st.markdown(
            f"### {subject}"
        )

        st.progress(
            score / 100
        )

        st.caption(
            f"{score}% • {get_status(score)}"
        )

        st.write("")

    st.markdown(
        f"""
        <div class="recommendation-card">

            <h3>
                🎯 Recommended Starting Point
            </h3>

            <h2>
                {weakest_subject} — {weakest_score}%
            </h2>

            <p>
                AI Learn recommends focusing on this
                area first based on your diagnostic result.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🗺️ View My Personalised Roadmap",
            use_container_width=True,
            type="primary"
        ):

            st.session_state.page = "roadmap"

            st.rerun()

    with col2:

        if st.button(
            "🔄 Retake Diagnostic",
            use_container_width=True
        ):

            level = st.session_state.profile.get(
                "level",
                "Beginner"
            )

            st.session_state.diagnostic_questions = (
                create_diagnostic(level)
            )

            st.session_state.diagnostic_answers = []

            st.session_state.scores = {}

            st.session_state.roadmap = []

            st.session_state.page = "diagnostic"

            st.rerun()


# ============================================================
# PERSONALIZED ROADMAP
# ============================================================

def roadmap_page():

    scores = st.session_state.scores

    if not scores:

        st.session_state.page = "home"

        st.rerun()

        return

    render_header()

    st.title(
        "🗺️ Your Personalised AI Roadmap"
    )

    st.write(
        "Your learning path is arranged according to "
        "your current diagnostic profile."
    )

    st.divider()

    roadmap = st.session_state.roadmap

    for index, item in enumerate(
        roadmap
    ):

        subject = item["subject"]

        score = item["score"]

        priority = item["priority"]

        st.markdown(
            f"## {index + 1}. {subject}"
        )

        st.progress(
            score / 100
        )

        st.write(
            f"Current score: **{score}%**"
        )

        st.write(
            f"Learning priority: **{priority}**"
        )

        if score < 40:

            recommendation = (
                "Start with the foundation concepts, "
                "terminology, examples and guided practice."
            )

        elif score < 70:

            recommendation = (
                "Strengthen your understanding with "
                "intermediate concepts and practice tasks."
            )

        else:

            recommendation = (
                "Continue with advanced concepts, "
                "projects and application-based practice."
            )

        st.info(
            recommendation
        )

        st.divider()

    if st.button(
        "🏠 Back to AI Learn Home",
        use_container_width=True
    ):

        st.session_state.page = "home"

        st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## 🎓 AI Learn"
    )

    st.caption(
        "Personalised AI Tutor"
    )

    st.divider()

    if st.button(
        "🏠 Home",
        use_container_width=True
    ):

        st.session_state.page = "home"

        st.rerun()

    if st.button(
        "📊 Score Card",
        use_container_width=True,
        disabled=not bool(
            st.session_state.scores
        )
    ):

        st.session_state.page = "score_card"

        st.rerun()

    if st.button(
        "🗺️ Roadmap",
        use_container_width=True,
        disabled=not bool(
            st.session_state.scores
        )
    ):

        st.session_state.page = "roadmap"

        st.rerun()


# ============================================================
# PAGE ROUTING
# ============================================================

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

    home_page()
