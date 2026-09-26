import streamlit as st
import random
import os


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
# SUBJECTS
# ============================================================

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

DEFAULT_STATE = {
    "page": "home",
    "profile": {},
    "diagnostic_questions": [],
    "diagnostic_answers": [],
    "scores": {},
    "roadmap": [],
}

for key, value in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    """
    <style>

    /* -------------------------------------------------------
       MAIN APP
    ------------------------------------------------------- */

    .stApp {
        background: #ffffff;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 0.5rem;
        padding-bottom: 3rem;
    }

    /* -------------------------------------------------------
       REMOVE DEFAULT STREAMLIT HEADER SPACE
    ------------------------------------------------------- */

    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* -------------------------------------------------------
       HEADER
    ------------------------------------------------------- */

    .ai-header {
        height: 72px;
        border-bottom: 1px solid #e8edf2;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 8px;
        margin-bottom: 0;
    }

    .brand-area {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .brand-name {
        font-size: 25px;
        font-weight: 700;
        color: #17202a;
        letter-spacing: -0.5px;
    }

    .brand-mark {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        background: #111111;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 22px;
        font-weight: 800;
    }

    .header-actions {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .gift-box {
        width: 44px;
        height: 44px;
        border: 1px solid #e2e7ec;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        background: white;
    }

    .login-button {
        border: 1px solid #34495e;
        border-radius: 8px;
        padding: 12px 28px;
        color: #17202a;
        background: white;
        font-weight: 600;
        font-size: 15px;
    }

    .join-button {
        border-radius: 8px;
        padding: 13px 24px;
        color: white;
        background: #344454;
        font-weight: 700;
        font-size: 15px;
    }

    /* -------------------------------------------------------
       HERO
    ------------------------------------------------------- */

    .hero {
        min-height: 520px;
        display: flex;
        align-items: center;
        padding: 45px 0 35px 0;
    }

    .hero-left {
        width: 53%;
        padding-right: 50px;
    }

    .hero-right {
        width: 47%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .hero-title {
        font-size: 54px;
        line-height: 1.08;
        font-weight: 750;
        letter-spacing: -2px;
        color: #35424f;
        margin: 0 0 18px 0;
    }

    .hero-title span {
        color: #111111;
    }

    .hero-subtitle {
        font-size: 20px;
        line-height: 1.55;
        color: #566573;
        max-width: 580px;
        margin-bottom: 25px;
    }

    .hero-highlight {
        font-size: 16px;
        color: #34495e;
        margin-bottom: 28px;
    }

    .hero-highlight strong {
        color: #10a37f;
    }

    /* -------------------------------------------------------
       HERO VISUAL
    ------------------------------------------------------- */

    .learning-visual {
        position: relative;
        width: 480px;
        height: 420px;
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
        left: 20px;
        top: 20px;
        background: #e9f3ff;
        font-size: 80px;
    }

    .circle-two {
        width: 165px;
        height: 165px;
        right: 25px;
        top: 15px;
        background: #fff4cf;
        font-size: 65px;
    }

    .circle-three {
        width: 175px;
        height: 175px;
        left: 125px;
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
        background: white;
        border: 1px solid #e7ebef;
        border-radius: 14px;
        padding: 13px 16px;
        box-shadow: 0 12px 35px rgba(40, 55, 70, 0.10);
        font-weight: 700;
        color: #344454;
    }

    .card-ai {
        left: 145px;
        top: 170px;
    }

    .card-progress {
        right: 90px;
        top: 190px;
    }

    .card-python {
        left: 5px;
        bottom: 105px;
    }

    /* -------------------------------------------------------
       FORM CARD
    ------------------------------------------------------- */

    .profile-card {
        background: #ffffff;
        border: 1px solid #e1e7ec;
        border-radius: 12px;
        padding: 22px;
        box-shadow: 0 8px 30px rgba(35, 50, 65, 0.06);
    }

    .profile-title {
        font-size: 21px;
        font-weight: 700;
        color: #25313c;
        margin-bottom: 8px;
    }

    .profile-description {
        color: #687783;
        font-size: 14px;
        margin-bottom: 15px;
    }

    /* -------------------------------------------------------
       STREAMLIT INPUTS
    ------------------------------------------------------- */

    div[data-baseweb="input"] {
        border-radius: 8px;
    }

    div[data-baseweb="select"] {
        border-radius: 8px;
    }

    /* -------------------------------------------------------
       PRIMARY BUTTON
    ------------------------------------------------------- */

    .stButton > button {
        border-radius: 8px;
        min-height: 48px;
        font-weight: 700;
    }

    /* -------------------------------------------------------
       SECTION
    ------------------------------------------------------- */

    .section-title {
        text-align: center;
        font-size: 34px;
        color: #344454;
        font-weight: 750;
        margin-top: 40px;
    }

    .section-description {
        text-align: center;
        color: #687783;
        font-size: 17px;
        margin-bottom: 35px;
    }

    /* -------------------------------------------------------
       SCORE CARD
    ------------------------------------------------------- */

    .score-header {
        background: #f7fafc;
        border: 1px solid #e4e9ee;
        border-radius: 18px;
        padding: 35px;
        text-align: center;
        margin-bottom: 25px;
    }

    .score-number {
        font-size: 64px;
        font-weight: 800;
        color: #344454;
    }

    .score-label {
        color: #687783;
        font-size: 16px;
    }

    /* -------------------------------------------------------
       MOBILE
    ------------------------------------------------------- */

    @media (max-width: 900px) {

        .hero {
            display: block;
        }

        .hero-left,
        .hero-right {
            width: 100%;
            padding-right: 0;
        }

        .hero-title {
            font-size: 40px;
        }

        .learning-visual {
            transform: scale(0.85);
            transform-origin: center;
            margin: 0 auto;
        }

        .header-actions {
            display: none;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# QUESTION BANK
# ============================================================

QUESTION_BANK = [

    # ========================================================
    # PYTHON
    # ========================================================

    {
        "subject": "Python",
        "level": "Beginner",
        "question": "Which symbol is used to start a comment in Python?",
        "options": ["//", "#", "<!--", "/*"],
        "answer": 1,
    },
    {
        "subject": "Python",
        "level": "Beginner",
        "question": "Which Python data type stores True or False values?",
        "options": ["String", "Boolean", "List", "Integer"],
        "answer": 1,
    },
    {
        "subject": "Python",
        "level": "Beginner",
        "question": "Which function displays output in Python?",
        "options": ["display()", "show()", "print()", "output()"],
        "answer": 2,
    },
    {
        "subject": "Python",
        "level": "Beginner",
        "question": "Which collection is ordered and changeable?",
        "options": ["Tuple", "List", "Set", "Frozen set"],
        "answer": 1,
    },
    {
        "subject": "Python",
        "level": "Beginner",
        "question": "What is the result of 3 + 4 * 2?",
        "options": ["14", "11", "10", "9"],
        "answer": 1,
    },
    {
        "subject": "Python",
        "level": "Beginner",
        "question": "Which keyword creates a conditional statement?",
        "options": ["if", "when", "check", "condition"],
        "answer": 0,
    },

    {
        "subject": "Python",
        "level": "Intermediate",
        "question": "What does a list comprehension provide?",
        "options": [
            "A concise way to create lists",
            "A way to define classes",
            "A database connection",
            "A Python compiler",
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Intermediate",
        "question": "What is the main purpose of a dictionary?",
        "options": [
            "Store values using key-value mappings",
            "Store only numbers",
            "Store only strings",
            "Execute functions",
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Intermediate",
        "question": "What does len([10, 20, 30]) return?",
        "options": ["2", "3", "30", "60"],
        "answer": 1,
    },
    {
        "subject": "Python",
        "level": "Intermediate",
        "question": "What is the purpose of a function?",
        "options": [
            "Group reusable logic",
            "Store files",
            "Install packages",
            "Create an operating system",
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Intermediate",
        "question": "Which keyword defines a function?",
        "options": ["function", "define", "def", "func"],
        "answer": 2,
    },

    {
        "subject": "Python",
        "level": "Advanced",
        "question": "What is the main purpose of a generator?",
        "options": [
            "Produce values lazily during iteration",
            "Automatically parallelize code",
            "Compile Python",
            "Prevent all memory allocation",
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Advanced",
        "question": "What does a decorator generally allow?",
        "options": [
            "Modify or extend function behavior",
            "Delete Python modules",
            "Convert lists to databases",
            "Disable exceptions",
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Advanced",
        "question": "Which concept allows a class to inherit behavior?",
        "options": [
            "Encapsulation",
            "Inheritance",
            "Iteration",
            "Serialization",
        ],
        "answer": 1,
    },
    {
        "subject": "Python",
        "level": "Advanced",
        "question": "What is the purpose of a context manager?",
        "options": [
            "Manage setup and cleanup of resources",
            "Automatically make code asynchronous",
            "Prevent every exception",
            "Convert Python to C++",
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Advanced",
        "question": "What does *args allow?",
        "options": [
            "An arbitrary number of positional arguments",
            "An arbitrary number of classes",
            "Only keyword arguments",
            "Only one required argument",
        ],
        "answer": 0,
    },

    # ========================================================
    # MATH
    # ========================================================

    {
        "subject": "Mathematics & Statistics",
        "level": "Beginner",
        "question": "What is the mean of 2, 4, and 6?",
        "options": ["3", "4", "5", "6"],
        "answer": 1,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Beginner",
        "question": "What does probability measure?",
        "options": [
            "Likelihood of an event",
            "Size of a dataset",
            "Average of values",
            "Number of features",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Beginner",
        "question": "Which value represents the middle of an ordered dataset?",
        "options": ["Mean", "Median", "Variance", "Range"],
        "answer": 1,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Beginner",
        "question": "What is 10% of 200?",
        "options": ["10", "20", "30", "40"],
        "answer": 1,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Beginner",
        "question": "What does the range represent?",
        "options": [
            "Maximum minus minimum",
            "Mean divided by median",
            "Number of observations",
            "Average",
        ],
        "answer": 0,
    },

    {
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What does variance measure?",
        "options": [
            "Spread around the mean",
            "The middle value",
            "Maximum value",
            "Number of features",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What does a correlation coefficient measure?",
        "options": [
            "Strength and direction of a relationship",
            "Neural network layers",
            "Number of outliers",
            "Number of categorical variables",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What does standard deviation represent?",
        "options": [
            "A measure of data spread",
            "Dataset size",
            "Largest observation",
            "Number of classes",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What is a sample in statistics?",
        "options": [
            "A subset of a population",
            "The entire population",
            "A constant",
            "A neural network layer",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What does negative correlation generally indicate?",
        "options": [
            "One variable tends to increase as the other decreases",
            "Both variables always increase",
            "Variables are identical",
            "There is no variation",
        ],
        "answer": 0,
    },

    {
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "Why is the gradient important in optimization?",
        "options": [
            "It indicates the direction of greatest increase",
            "It labels training data",
            "It removes categorical features",
            "It determines dataset size",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "What does a covariance matrix describe?",
        "options": [
            "Variances and pairwise covariances",
            "Only means",
            "Only class labels",
            "Neural network layers",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "Why are eigenvectors useful in dimensionality reduction?",
        "options": [
            "They identify important directions of variation",
            "They create labels",
            "They replace missing values",
            "They remove training data",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "What does a derivative describe locally?",
        "options": [
            "Rate of change",
            "Number of observations",
            "Class probability",
            "Dataset size",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "What is Bayes' theorem used to calculate?",
        "options": [
            "Conditional probability using prior information",
            "Dataset mean",
            "Number of neurons",
            "Image dimensions",
        ],
        "answer": 0,
    },

    # ========================================================
    # MACHINE LEARNING
    # ========================================================

    {
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "What is supervised learning?",
        "options": [
            "Learning from labelled examples",
            "Learning without data",
            "Only clustering",
            "Manually writing prediction rules",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "What is a training dataset used for?",
        "options": [
            "Teaching a model patterns from data",
            "Displaying a website",
            "Deleting parameters",
            "Writing documentation",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "Which is a classification problem?",
        "options": [
            "Predicting whether an email is spam",
            "Predicting house price",
            "Grouping customers",
            "Reducing image dimensions",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "Which is a regression problem?",
        "options": [
            "Predicting a house price",
            "Detecting spam",
            "Grouping customers",
            "Finding image edges",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "What is a feature?",
        "options": [
            "An input variable used by a model",
            "Only the prediction",
            "The model filename",
            "The training computer",
        ],
        "answer": 0,
    },

    {
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "What is overfitting?",
        "options": [
            "A model learns training data too specifically",
            "A model has no parameters",
            "A model has no training data",
            "A model always performs perfectly",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "Why is a validation set useful?",
        "options": [
            "For evaluating choices during development",
            "For replacing training data permanently",
            "For removing all features",
            "For converting regression to clustering",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "What is feature scaling used for?",
        "options": [
            "Putting numerical features on comparable scales",
            "Adding labels",
            "Deleting the target",
            "Increasing classes",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "What is clustering?",
        "options": [
            "Grouping similar observations without predefined labels",
            "Predicting a continuous target",
            "Training on labelled images",
            "Removing numerical features",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "What does recall measure?",
        "options": [
            "The proportion of actual positives correctly identified",
            "The proportion of predicted positives that are correct",
            "The number of parameters",
            "Dataset size",
        ],
        "answer": 0,
    },

    {
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "Why can data leakage produce misleading validation results?",
        "options": [
            "Information unavailable at prediction time influenced development",
            "The model has too few parameters",
            "The dataset is always too small",
            "The model uses gradient descent",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "What is the bias-variance tradeoff concerned with?",
        "options": [
            "Balancing underfitting and sensitivity to training data",
            "Choosing programming languages",
            "Increasing storage",
            "Selecting a database",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "Why might cross-validation be used?",
        "options": [
            "Estimate generalization across multiple data splits",
            "Guarantee zero test error",
            "Eliminate the target",
            "Make every model linear",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "What does regularization generally encourage?",
        "options": [
            "Simpler model parameters to reduce overfitting",
            "More labels",
            "Larger datasets automatically",
            "Removal of validation data",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "Why is class imbalance important?",
        "options": [
            "Accuracy can hide poor minority-class performance",
            "It always makes training impossible",
            "It guarantees overfitting",
            "It removes evaluation metrics",
        ],
        "answer": 0,
    },

    # ========================================================
    # DEEP LEARNING
    # ========================================================

    {
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What is a neural network?",
        "options": [
            "A model made of interconnected computational units",
            "A database table",
            "A programming language",
            "A compression format",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What is an activation function used for?",
        "options": [
            "Introducing nonlinear behavior",
            "Storing datasets",
            "Deleting weights",
            "Downloading Python",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What is an epoch?",
        "options": [
            "One complete pass through the training dataset",
            "One feature",
            "One neuron",
            "One test example",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What are neural network weights?",
        "options": [
            "Learnable parameters used to transform inputs",
            "Dataset filenames",
            "Class labels",
            "Python packages",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What is a loss function used for?",
        "options": [
            "Measure how far predictions are from desired outputs",
            "Increase image resolution",
            "Create database tables",
            "Remove parameters",
        ],
        "answer": 0,
    },

    {
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What is backpropagation used for?",
        "options": [
            "Computing gradients used to update parameters",
            "Creating training labels",
            "Compressing images",
            "Selecting database rows",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What do convolutional neural networks commonly excel at?",
        "options": [
            "Learning spatial patterns in data such as images",
            "Managing operating systems",
            "Writing SQL",
            "Sorting Python lists",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What is an optimizer used for?",
        "options": [
            "Update model parameters using gradient information",
            "Create labels",
            "Remove the loss function",
            "Store images",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "Why can ReLU help deep networks?",
        "options": [
            "It provides nonlinear activation and can help gradient flow",
            "It removes neurons",
            "It guarantees no overfitting",
            "It converts images into labels",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What is dropout commonly used for?",
        "options": [
            "Reducing over-reliance on particular neurons during training",
            "Increasing labels",
            "Replacing the optimizer",
            "Converting regression to classification",
        ],
        "answer": 0,
    },

    {
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "Why can very deep networks suffer from vanishing gradients?",
        "options": [
            "Gradients can become extremely small during backward propagation",
            "The dataset has too many rows",
            "The optimizer always increases gradients",
            "Neural networks cannot use activation functions",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "What is the key idea behind residual connections?",
        "options": [
            "Provide a shortcut path while learning a residual transformation",
            "Remove all nonlinearities",
            "Prevent training",
            "Replace every convolution with pooling",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "What does batch normalization primarily do?",
        "options": [
            "Normalize activations within training batches",
            "Create new training examples",
            "Delete parameters",
            "Convert classification into clustering",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "Why are attention mechanisms useful in sequence modeling?",
        "options": [
            "They let the model weight different parts of the input",
            "They eliminate all parameters",
            "They only work with tables",
            "They guarantee perfect predictions",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "What does learning rate control?",
        "options": [
            "The size of parameter updates during optimization",
            "The number of examples",
            "The number of classes",
            "Model accuracy",
        ],
        "answer": 0,
    },

    # ========================================================
    # GENERATIVE AI
    # ========================================================

    {
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What is Generative AI designed to do?",
        "options": [
            "Generate new content based on learned patterns",
            "Only store files",
            "Only calculate averages",
            "Only sort data",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What does LLM stand for?",
        "options": [
            "Large Language Model",
            "Logical Learning Machine",
            "Large Logic Memory",
            "Language Learning Method",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What is a prompt?",
        "options": [
            "Instructions or input given to an AI model",
            "A model database",
            "A hardware component",
            "A Python compiler",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What can a text-generating AI model produce?",
        "options": [
            "Text based on learned patterns and instructions",
            "Only spreadsheets",
            "Only hardware",
            "Only database indexes",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What is an AI chatbot?",
        "options": [
            "A system that interacts with users using conversational responses",
            "A database engine",
            "A graphics card",
            "A programming language",
        ],
        "answer": 0,
    },

    {
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "What are tokens in language models?",
        "options": [
            "Units of text processed by the model",
            "Database passwords",
            "Training computers",
            "Neural network layers",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "What is an embedding?",
        "options": [
            "A numerical representation of information in vector space",
            "A database password",
            "A hardware component",
            "A Python exception",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "What does RAG stand for?",
        "options": [
            "Retrieval-Augmented Generation",
            "Random AI Generation",
            "Recursive Answer Generator",
            "Rapid Automated Grading",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "Why can RAG be useful?",
        "options": [
            "It provides a model with relevant retrieved information",
            "It removes the need for data",
            "It guarantees correctness",
            "It replaces neural networks",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "What does temperature commonly control?",
        "options": [
            "Randomness of token selection",
            "Model memory size",
            "Training examples",
            "Number of GPUs",
        ],
        "answer": 0,
    },

    {
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "What is the central idea of self-attention in Transformers?",
        "options": [
            "Tokens can assign different importance to other tokens",
            "Every token is treated identically",
            "Token order is removed",
            "Only one token is processed",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "Why are vector embeddings useful for semantic search?",
        "options": [
            "Related items can be represented near each other in vector space",
            "They guarantee factual correctness",
            "They eliminate documents",
            "They directly produce answers",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "What is fine-tuning generally used for?",
        "options": [
            "Adapting a pretrained model to a specific task or dataset",
            "Deleting pretrained knowledge",
            "Increasing internet bandwidth",
            "Replacing tokenization",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "What is an LLM hallucination?",
        "options": [
            "A generated response containing unsupported or incorrect information",
            "A GPU failure",
            "A dataset format",
            "A tokenization algorithm",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "Why does context-window size matter?",
        "options": [
            "It limits how much input context the model can process",
            "It determines the physical memory chip",
            "It guarantees factual accuracy",
            "It determines the number of users",
        ],
        "answer": 0,
    },
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_status(score):

    if score < 40:
        return "Needs Foundation"

    elif score < 70:
        return "Developing"

    elif score < 100:
        return "Intermediate"

    return "Strong"


def prepare_question(question):

    pairs = []

    for index, option in enumerate(
        question["options"]
    ):

        pairs.append(
            (
                option,
                index == question["answer"]
            )
        )

    random.shuffle(pairs)

    options = [
        pair[0]
        for pair in pairs
    ]

    correct_answer = next(
        index
        for index, pair in enumerate(pairs)
        if pair[1]
    )

    return {
        "subject": question["subject"],
        "level": question["level"],
        "question": question["question"],
        "options": options,
        "answer": correct_answer,
    }


def create_diagnostic(level):

    selected = []

    for subject in SUBJECTS:

        available = [
            q
            for q in QUESTION_BANK
            if q["subject"] == subject
            and q["level"] == level
        ]

        if len(available) < 3:

            raise ValueError(
                f"Not enough questions for "
                f"{subject} at {level} level."
            )

        chosen = random.sample(
            available,
            3
        )

        for question in chosen:

            selected.append(
                prepare_question(question)
            )

    random.shuffle(selected)

    return selected


def calculate_scores():

    correct = {
        subject: 0
        for subject in SUBJECTS
    }

    total = {
        subject: 0
        for subject in SUBJECTS
    }

    for question, answer in zip(
        st.session_state.diagnostic_questions,
        st.session_state.diagnostic_answers
    ):

        subject = question["subject"]

        total[subject] += 1

        if answer == question["answer"]:

            correct[subject] += 1

    scores = {}

    for subject in SUBJECTS:

        if total[subject] == 0:

            scores[subject] = 0

        else:

            scores[subject] = round(
                correct[subject]
                / total[subject]
                * 100
            )

    return scores


def create_roadmap(scores):

    sorted_subjects = sorted(
        scores.items(),
        key=lambda item: item[1]
    )

    roadmap = []

    for index, (subject, score) in enumerate(
        sorted_subjects
    ):

        if index == 0:
            priority = "High Priority"

        elif index == 1:
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

    logo_path = "aillearn_logo.jpg"

    st.markdown(
        """
        <div class="ai-header">

            <div class="brand-area">

                <div class="brand-mark">
                    AI
                </div>

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

    st.markdown(
        "<div class='hero'>",
        unsafe_allow_html=True,
    )

    left, right = st.columns(
        [1.05, 0.95],
        gap="large",
    )

    # --------------------------------------------------------
    # LEFT SIDE
    # --------------------------------------------------------

    with left:

        st.markdown(
            """
            <div class="hero-left">

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

        # ----------------------------------------------------
        # PROFILE FORM
        # ----------------------------------------------------

        st.markdown(
            """
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
            placeholder="Enter your name",
        )

        level = st.selectbox(
            "Current AI Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced",
            ],
        )

        goal = st.selectbox(
            "What is your main goal?",
            [
                "Learn AI fundamentals",
                "Build AI projects",
                "Prepare for a job",
                "Learn Generative AI",
                "Learn AI Agents",
            ],
        )

        study_time = st.selectbox(
            "How much time can you study daily?",
            [
                "15 minutes",
                "30 minutes",
                "1 hour",
                "2+ hours",
            ],
        )

        st.write("")

        if st.button(
            "🚀 Start My AI Journey",
            use_container_width=True,
            type="primary",
        ):

            if not name.strip():

                st.warning(
                    "Please enter your name before starting."
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
    # RIGHT SIDE VISUAL
    # --------------------------------------------------------

    with right:

        st.markdown(
            """
            <div class="hero-right">

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

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "</div>",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # BELOW HERO
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
        unsafe_allow_html=True,
    )

    cols = st.columns(5)

    cards = [
        ("🐍", "Python"),
        ("📐", "Mathematics & Statistics"),
        ("🤖", "Machine Learning"),
        ("🧠", "Deep Learning"),
        ("✨", "Generative AI"),
    ]

    for col, (icon, subject) in zip(
        cols,
        cards
    ):

        with col:

            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    border:1px solid #e5e9ed;
                    border-radius:14px;
                    padding:20px 10px;
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
                    ">
                        {subject}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


# ============================================================
# DIAGNOSTIC
# ============================================================

def diagnostic_page():

    questions = (
        st.session_state.diagnostic_questions
    )

    if not questions:

        st.session_state.page = "home"

        st.rerun()

        return

    render_header()

    st.title(
        "🧠 AI Knowledge Diagnostic"
    )

    learner_name = st.session_state.profile.get(
        "name",
        "Learner",
    )

    learner_level = st.session_state.profile.get(
        "level",
        "Beginner",
    )

    st.write(
        f"Hello **{learner_name}**."
    )

    st.write(
        "Answer all 15 questions. Your answers will "
        "remain hidden until you submit the complete diagnostic."
    )

    st.info(
        f"Assessment level: **{learner_level}**"
    )

    st.progress(0.0)

    st.caption(
        "15 questions • 3 questions from each learning area"
    )

    st.divider()

    answers = {}

    # --------------------------------------------------------
    # ALL 15 QUESTIONS
    # --------------------------------------------------------

    for index, question in enumerate(
        questions
    ):

        question_number = index + 1

        st.markdown(
            f"### Question {question_number}"
        )

        st.write(
            question["question"]
        )

        answers[index] = st.radio(
            "Choose one answer:",
            question["options"],
            key=f"diagnostic_{index}",
            index=None,
        )

        if question_number < 15:

            st.divider()

    # --------------------------------------------------------
    # SUBMIT
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "🎯 Ready to submit?"
    )

    st.write(
        "Make sure all 15 questions are answered."
    )

    if st.button(
        "🎯 Submit Diagnostic",
        use_container_width=True,
        type="primary",
    ):

        unanswered = [
            index + 1
            for index, answer in answers.items()
            if answer is None
        ]

        if unanswered:

            numbers = ", ".join(
                str(number)
                for number in unanswered
            )

            st.warning(
                f"Please answer question(s): {numbers}"
            )

            return

        final_answers = []

        for index, question in enumerate(
            questions
        ):

            selected = answers[index]

            selected_index = (
                question["options"].index(
                    selected
                )
            )

            final_answers.append(
                selected_index
            )

        st.session_state.diagnostic_answers = (
            final_answers
        )

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

    weakest = min(
        scores,
        key=scores.get
    )

    weakest_score = scores[weakest]

    st.markdown(
        f"""
        <div class="score-header">

            <div style="font-size:42px;">
                🎓
            </div>

            <h1>
                Your AI Learning Score Card
            </h1>

            <div class="score-label">
                Your current AI knowledge profile
            </div>

            <div class="score-number">
                {overall}%
            </div>

            <div class="score-label">
                Overall Score
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.subheader(
        "📚 Subject Scores"
    )

    for subject in SUBJECTS:

        score = scores[subject]

        st.markdown(
            f"**{subject}**"
        )

        st.progress(
            score / 100
        )

        st.caption(
            f"{score}%  •  {get_status(score)}"
        )

        st.write("")

    st.divider()

    st.subheader(
        "🎯 Recommended Starting Point"
    )

    st.markdown(
        f"### {weakest} — {weakest_score}%"
    )

    if weakest_score < 40:

        st.write(
            f"Build your foundation in **{weakest}** "
            "before moving into advanced topics."
        )

    elif weakest_score < 70:

        st.write(
            f"Strengthen your **{weakest}** knowledge "
            "with focused lessons and practice."
        )

    else:

        st.write(
            f"Continue developing **{weakest}** through "
            "advanced concepts and projects."
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🗺️ View Personalised Roadmap",
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

            st.session_state.diagnostic_questions = (
                create_diagnostic(level)
            )

            st.session_state.diagnostic_answers = []

            st.session_state.scores = {}

            st.session_state.roadmap = []

            st.session_state.page = "diagnostic"

            st.rerun()


# ============================================================
# ROADMAP
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
        "Your learning journey is arranged around "
        "your current knowledge profile."
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
            f"### {index + 1}. {subject}"
        )

        st.progress(
            score / 100
        )

        st.write(
            f"Current score: **{score}%**"
        )

        st.write(
            f"Priority: **{priority}**"
        )

        if score < 40:

            recommendation = (
                "Start with the fundamentals, core terminology, "
                "examples and guided practice."
            )

        elif score < 70:

            recommendation = (
                "Strengthen your understanding through "
                "intermediate concepts and practice."
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
        "🏠 Back to Home",
        use_container_width=True,
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
        use_container_width=True,
    ):

        st.session_state.page = "home"

        st.rerun()

    if st.button(
        "📊 Score Card",
        use_container_width=True,
        disabled=not bool(
            st.session_state.scores
        ),
    ):

        st.session_state.page = "score_card"

        st.rerun()

    if st.button(
        "🗺️ Roadmap",
        use_container_width=True,
        disabled=not bool(
            st.session_state.scores
        ),
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
