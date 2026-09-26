import streamlit as st
import random
from pathlib import Path


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Learn",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background: #ffffff;
    }

    .main .block-container {
        max-width: 1180px;
        padding-top: 0.5rem;
        padding-bottom: 3rem;
    }

    html {
        scroll-behavior: smooth;
    }

    /* Hide Streamlit chrome */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    /* ---------- TOP NAV ---------- */

    .top-nav {
        width: 100%;
        height: 76px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid #edf0f2;
        margin-bottom: 30px;
    }

    .brand-area {
        display: flex;
        align-items: center;
        gap: 11px;
    }

    .brand-logo {
        width: 43px;
        height: 43px;
        object-fit: contain;
        border-radius: 10px;
    }

    .brand-name {
        font-size: 27px;
        font-weight: 700;
        color: #263746;
        letter-spacing: -0.5px;
    }

    .brand-name span {
        color: #10b981;
    }

    .nav-actions {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .nav-gift {
        width: 42px;
        height: 42px;
        border: 1px solid #e5e9ed;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 19px;
    }

    .nav-login {
        border: 1px solid #344454;
        border-radius: 8px;
        padding: 11px 27px;
        color: #344454;
        font-weight: 600;
        font-size: 15px;
    }

    .nav-join {
        background: #344454;
        color: white;
        border-radius: 8px;
        padding: 12px 23px;
        font-weight: 700;
        font-size: 15px;
    }

    /* ---------- HERO ---------- */

    .hero-section {
        min-height: 450px;
        display: flex;
        align-items: center;
        padding: 30px 0 50px 0;
    }

    .hero-left {
        padding-right: 30px;
    }

    .hero-title {
        font-size: 58px;
        line-height: 1.06;
        font-weight: 750;
        color: #344454;
        letter-spacing: -2px;
        margin-bottom: 24px;
    }

    .hero-title span {
        color: #10b981;
    }

    .hero-subtitle {
        font-size: 20px;
        line-height: 1.55;
        color: #5d6975;
        max-width: 610px;
        margin-bottom: 20px;
    }

    .hero-highlight {
        background: #f3fbf8;
        border-left: 4px solid #10b981;
        padding: 17px 20px;
        border-radius: 8px;
        color: #4c5965;
        font-size: 15px;
        line-height: 1.6;
        max-width: 620px;
    }

    .hero-highlight strong {
        color: #344454;
    }

    /* ---------- VISUAL ---------- */

    .learning-visual {
        position: relative;
        height: 390px;
        width: 100%;
    }

    .visual-circle {
        position: absolute;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        font-size: 48px;
        box-shadow: 0 12px 35px rgba(44, 62, 80, 0.10);
    }

    .circle-one {
        width: 190px;
        height: 190px;
        background: #e5f3ff;
        left: 45px;
        top: 30px;
    }

    .circle-two {
        width: 145px;
        height: 145px;
        background: #eafaf3;
        right: 45px;
        top: 10px;
    }

    .circle-three {
        width: 155px;
        height: 155px;
        background: #fff4dd;
        left: 115px;
        bottom: 20px;
    }

    .circle-four {
        width: 125px;
        height: 125px;
        background: #f0ebff;
        right: 75px;
        bottom: 20px;
    }

    .floating-card {
        position: absolute;
        background: white;
        border: 1px solid #e9edf0;
        border-radius: 12px;
        padding: 11px 16px;
        box-shadow: 0 8px 25px rgba(44, 62, 80, 0.10);
        font-size: 13px;
        font-weight: 700;
        color: #344454;
    }

    .card-ai {
        left: 15px;
        top: 235px;
    }

    .card-progress {
        right: 0;
        top: 190px;
    }

    .card-python {
        left: 80px;
        bottom: 0;
    }

    /* ---------- PROFILE ---------- */

    .profile-section {
        background: #f8fafb;
        border-radius: 18px;
        padding: 34px 38px 38px 38px;
        margin-top: 10px;
        border: 1px solid #edf0f2;
    }

    .profile-title {
        font-size: 28px;
        font-weight: 750;
        color: #344454;
        margin-bottom: 8px;
    }

    .profile-description {
        color: #687580;
        font-size: 16px;
        margin-bottom: 25px;
    }

    /* ---------- SUBJECTS ---------- */

    .foundations-section {
        padding: 55px 0 25px 0;
        text-align: center;
    }

    .foundations-title {
        font-size: 31px;
        font-weight: 750;
        color: #344454;
        margin-bottom: 8px;
    }

    .foundations-subtitle {
        color: #687580;
        font-size: 16px;
        margin-bottom: 30px;
    }

    .subject-card {
        background: white;
        border: 1px solid #e8ecef;
        border-radius: 13px;
        padding: 24px 15px;
        text-align: center;
        min-height: 125px;
        box-shadow: 0 4px 15px rgba(44, 62, 80, 0.04);
    }

    .subject-icon {
        font-size: 30px;
        margin-bottom: 9px;
    }

    .subject-name {
        font-size: 14px;
        font-weight: 700;
        color: #344454;
    }

    /* ---------- PAGE TITLES ---------- */

    .page-title {
        font-size: 38px;
        font-weight: 750;
        color: #344454;
        margin-bottom: 5px;
    }

    .page-subtitle {
        color: #687580;
        font-size: 16px;
        margin-bottom: 28px;
    }

    /* ---------- QUESTION CARDS ---------- */

    .question-card {
        background: #ffffff;
        border: 1px solid #e7ebee;
        border-radius: 14px;
        padding: 20px 22px;
        margin-bottom: 18px;
        box-shadow: 0 3px 12px rgba(44, 62, 80, 0.04);
    }

    .question-number {
        color: #10a978;
        font-size: 13px;
        font-weight: 750;
        margin-bottom: 8px;
    }

    .question-text {
        color: #293946;
        font-size: 17px;
        font-weight: 650;
        line-height: 1.5;
        margin-bottom: 15px;
    }

    /* ---------- SCORE CARD ---------- */

    .score-header {
        background: linear-gradient(135deg, #f0fbf7, #f8fbff);
        border: 1px solid #e1eee9;
        border-radius: 18px;
        padding: 35px;
        text-align: center;
        margin-bottom: 30px;
    }

    .score-header-title {
        font-size: 29px;
        font-weight: 750;
        color: #344454;
    }

    .overall-score {
        font-size: 58px;
        font-weight: 800;
        color: #10a978;
        margin: 10px 0;
    }

    .score-description {
        color: #687580;
        font-size: 15px;
    }

    .score-card {
        background: white;
        border: 1px solid #e7ebee;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 15px;
    }

    .score-topic {
        font-size: 17px;
        font-weight: 750;
        color: #344454;
        margin-bottom: 9px;
    }

    .score-status {
        color: #687580;
        font-size: 13px;
        margin-top: 8px;
    }

    .recommendation {
        background: #f3fbf8;
        border: 1px solid #d7eee6;
        border-radius: 14px;
        padding: 25px;
        margin-top: 25px;
        margin-bottom: 25px;
    }

    .recommendation-title {
        color: #344454;
        font-size: 20px;
        font-weight: 750;
        margin-bottom: 8px;
    }

    /* ---------- ROADMAP ---------- */

    .roadmap-card {
        background: white;
        border: 1px solid #e7ebee;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 15px;
    }

    .roadmap-number {
        display: inline-flex;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        align-items: center;
        justify-content: center;
        background: #eaf8f3;
        color: #0c9b6e;
        font-weight: 800;
        margin-right: 10px;
    }

    .roadmap-name {
        color: #344454;
        font-size: 18px;
        font-weight: 750;
    }

    .roadmap-description {
        color: #687580;
        margin-top: 9px;
        line-height: 1.5;
    }

    /* ---------- BUTTONS ---------- */

    .stButton > button {
        border-radius: 8px;
        min-height: 45px;
        font-weight: 700;
    }

    /* ---------- MOBILE ---------- */

    @media (max-width: 800px) {

        .hero-title {
            font-size: 43px;
        }

        .hero-section {
            padding-top: 10px;
        }

        .learning-visual {
            margin-top: 30px;
            transform: scale(0.9);
        }

        .profile-section {
            padding: 25px;
        }

        .nav-login,
        .nav-join {
            display: none;
        }

        .main .block-container {
            padding-left: 18px;
            padding-right: 18px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# CONSTANTS
# =========================================================

SUBJECTS = [
    "Python",
    "Mathematics & Statistics",
    "Machine Learning",
    "Deep Learning",
    "Generative AI"
]

SUBJECT_ICONS = {
    "Python": "🐍",
    "Mathematics & Statistics": "📐",
    "Machine Learning": "🤖",
    "Deep Learning": "🧠",
    "Generative AI": "✨"
}


# =========================================================
# LOGO
# =========================================================

def get_logo_path():
    """
    Looks for the recommended AI Learn logo filename first.
    Also supports the filename of the image you originally uploaded.
    """

    possible_files = [
        "ailearn_logo.jpg",
        "0f6577fe444ba6b1365cd00394ee581e.jpg"
    ]

    for filename in possible_files:
        path = Path(filename)
        if path.exists():
            return str(path)

    return None


# =========================================================
# QUESTION BANK
#
# Each question has:
# subject
# difficulty
# question
# options
# answer
#
# The subject is stored internally but NEVER displayed
# during the diagnostic.
# =========================================================

QUESTION_BANK = {

    "Python": {

        "Beginner": [
            {
                "question": "Which symbol is used to start a comment in Python?",
                "options": ["//", "#", "/*", "--"],
                "answer": "#"
            },
            {
                "question": "Which Python data type stores True or False?",
                "options": ["String", "Boolean", "Float", "List"],
                "answer": "Boolean"
            },
            {
                "question": "Which function is commonly used to display output in Python?",
                "options": ["show()", "display()", "print()", "output()"],
                "answer": "print()"
            },
            {
                "question": "Which of these is a Python list?",
                "options": ["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "<1, 2, 3>"],
                "answer": "[1, 2, 3]"
            },
            {
                "question": "What does len([10, 20, 30]) return?",
                "options": ["2", "3", "30", "10"],
                "answer": "3"
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["function", "define", "def", "func"],
                "answer": "def"
            },
            {
                "question": "Which operator is used for exponentiation in Python?",
                "options": ["^", "**", "//", "^^"],
                "answer": "**"
            },
            {
                "question": "Which value represents the absence of a value in Python?",
                "options": ["None", "Empty", "NullValue", "Void"],
                "answer": "None"
            }
        ],

        "Intermediate": [
            {
                "question": "What is the output of: len({1, 1, 2, 3})?",
                "options": ["4", "3", "2", "1"],
                "answer": "3"
            },
            {
                "question": "Which Python structure is best suited for key-value pairs?",
                "options": ["List", "Tuple", "Dictionary", "Set"],
                "answer": "Dictionary"
            },
            {
                "question": "What does a list comprehension primarily provide?",
                "options": [
                    "A compact way to create lists",
                    "A way to define classes",
                    "Automatic database storage",
                    "Memory allocation"
                ],
                "answer": "A compact way to create lists"
            },
            {
                "question": "What is the main purpose of try/except?",
                "options": [
                    "Loop through data",
                    "Handle exceptions",
                    "Create functions",
                    "Define variables"
                ],
                "answer": "Handle exceptions"
            },
            {
                "question": "What does *args allow a function to receive?",
                "options": [
                    "Multiple positional arguments",
                    "Only one argument",
                    "Only keyword arguments",
                    "A class"
                ],
                "answer": "Multiple positional arguments"
            },
            {
                "question": "Which library is primarily used for numerical arrays in Python?",
                "options": ["NumPy", "Flask", "BeautifulSoup", "Requests"],
                "answer": "NumPy"
            },
            {
                "question": "Which Pandas object represents a two-dimensional table?",
                "options": ["Array", "Series", "DataFrame", "Matrix"],
                "answer": "DataFrame"
            },
            {
                "question": "What is inheritance in Python OOP?",
                "options": [
                    "A child class acquiring behavior from another class",
                    "Copying a variable",
                    "Deleting an object",
                    "Converting a list"
                ],
                "answer": "A child class acquiring behavior from another class"
            }
        ],

        "Advanced": [
            {
                "question": "What does a Python generator primarily provide?",
                "options": [
                    "Lazy iteration over values",
                    "Automatic multithreading",
                    "Database indexing",
                    "Static typing"
                ],
                "answer": "Lazy iteration over values"
            },
            {
                "question": "Why is a tuple generally safer than a list for immutable records?",
                "options": [
                    "Tuples cannot be modified after creation",
                    "Tuples always use less memory",
                    "Tuples automatically sort data",
                    "Tuples support only numbers"
                ],
                "answer": "Tuples cannot be modified after creation"
            },
            {
                "question": "What is the primary purpose of a Python decorator?",
                "options": [
                    "Modify or extend function behavior",
                    "Create database tables",
                    "Compile Python to machine code",
                    "Remove variables"
                ],
                "answer": "Modify or extend function behavior"
            },
            {
                "question": "What does the `with` statement commonly help manage?",
                "options": [
                    "Resources and context management",
                    "Neural networks",
                    "List sorting only",
                    "Package installation"
                ],
                "answer": "Resources and context management"
            },
            {
                "question": "What problem can shallow copying create with nested mutable objects?",
                "options": [
                    "Nested objects may still be shared",
                    "The program becomes statically typed",
                    "All values become strings",
                    "Functions stop executing"
                ],
                "answer": "Nested objects may still be shared"
            },
            {
                "question": "What is the typical time complexity of dictionary key lookup in Python on average?",
                "options": ["O(1)", "O(n)", "O(n²)", "O(log n)"],
                "answer": "O(1)"
            },
            {
                "question": "What does `__init__` normally represent in a Python class?",
                "options": [
                    "An initializer called when an instance is created",
                    "A destructor",
                    "A module importer",
                    "A static compiler"
                ],
                "answer": "An initializer called when an instance is created"
            },
            {
                "question": "What is duck typing in Python?",
                "options": [
                    "Behavior matters more than explicit declared type",
                    "Only duck objects can be stored",
                    "Variables must have fixed types",
                    "Classes cannot inherit"
                ],
                "answer": "Behavior matters more than explicit declared type"
            }
        ]
    },


    "Mathematics & Statistics": {

        "Beginner": [
            {
                "question": "What is the mean of 2, 4 and 6?",
                "options": ["3", "4", "5", "6"],
                "answer": "4"
            },
            {
                "question": "What is the probability of getting heads from a fair coin?",
                "options": ["0", "0.25", "0.5", "1"],
                "answer": "0.5"
            },
            {
                "question": "Which value represents the middle of an ordered dataset?",
                "options": ["Mean", "Median", "Variance", "Range"],
                "answer": "Median"
            },
            {
                "question": "What is 5 × 5?",
                "options": ["10", "20", "25", "30"],
                "answer": "25"
            },
            {
                "question": "What does a vector commonly represent in machine learning?",
                "options": [
                    "A collection of numerical features",
                    "Only an image",
                    "A database",
                    "A programming language"
                ],
                "answer": "A collection of numerical features"
            },
            {
                "question": "What is the range of 3, 7, 10?",
                "options": ["3", "7", "10", "7"],
                "answer": "7"
            },
            {
                "question": "What is 10% of 200?",
                "options": ["10", "20", "30", "40"],
                "answer": "20"
            },
            {
                "question": "If a fair die is rolled, how many possible outcomes are there?",
                "options": ["4", "5", "6", "8"],
                "answer": "6"
            }
        ],

        "Intermediate": [
            {
                "question": "What does variance measure?",
                "options": [
                    "Spread of values around the mean",
                    "The largest value only",
                    "The number of samples",
                    "The median"
                ],
                "answer": "Spread of values around the mean"
            },
            {
                "question": "What does standard deviation represent?",
                "options": [
                    "A measure of dispersion",
                    "The sample count",
                    "The maximum value",
                    "The median"
                ],
                "answer": "A measure of dispersion"
            },
            {
                "question": "What is the derivative of x²?",
                "options": ["x", "2x", "x²", "2"],
                "answer": "2x"
            },
            {
                "question": "What does correlation measure?",
                "options": [
                    "Strength and direction of linear association",
                    "Causation only",
                    "Sample size",
                    "Classification accuracy"
                ],
                "answer": "Strength and direction of linear association"
            },
            {
                "question": "What is the probability of an event that is certain?",
                "options": ["0", "0.25", "0.5", "1"],
                "answer": "1"
            },
            {
                "question": "What does a matrix contain?",
                "options": [
                    "Rows and columns of values",
                    "Only one value",
                    "Only text",
                    "Functions only"
                ],
                "answer": "Rows and columns of values"
            },
            {
                "question": "What does a negative correlation indicate?",
                "options": [
                    "Variables tend to move in opposite directions",
                    "Variables are always identical",
                    "There is no relationship",
                    "Both variables are constant"
                ],
                "answer": "Variables tend to move in opposite directions"
            },
            {
                "question": "Why are features sometimes standardized before machine learning?",
                "options": [
                    "To put numerical features on comparable scales",
                    "To delete all outliers",
                    "To create labels",
                    "To increase dataset size"
                ],
                "answer": "To put numerical features on comparable scales"
            }
        ],

        "Advanced": [
            {
                "question": "What does the gradient represent for a scalar-valued function?",
                "options": [
                    "The vector of partial derivatives",
                    "Only the function value",
                    "The dataset size",
                    "The class label"
                ],
                "answer": "The vector of partial derivatives"
            },
            {
                "question": "What does Bayes' theorem update?",
                "options": [
                    "A probability using prior information and evidence",
                    "A neural network layer",
                    "A dataset size",
                    "A feature name"
                ],
                "answer": "A probability using prior information and evidence"
            },
            {
                "question": "What is an eigenvector associated with a matrix?",
                "options": [
                    "A vector whose direction is preserved under the transformation",
                    "A random vector",
                    "A scalar probability",
                    "A dataset row"
                ],
                "answer": "A vector whose direction is preserved under the transformation"
            },
            {
                "question": "What is the purpose of a Hessian matrix in optimization?",
                "options": [
                    "It contains second-order partial derivatives",
                    "It stores labels",
                    "It calculates accuracy only",
                    "It removes missing data"
                ],
                "answer": "It contains second-order partial derivatives"
            },
            {
                "question": "What does covariance describe?",
                "options": [
                    "How two variables vary together",
                    "The mean of one variable",
                    "The number of classes",
                    "The maximum probability"
                ],
                "answer": "How two variables vary together"
            },
            {
                "question": "What is the central limit theorem broadly concerned with?",
                "options": [
                    "The distribution of sample means",
                    "Neural network depth",
                    "Database indexing",
                    "Python execution"
                ],
                "answer": "The distribution of sample means"
            },
            {
                "question": "What does convexity provide in many optimization problems?",
                "options": [
                    "A structure where local minima can also be global minima",
                    "Automatic feature engineering",
                    "Guaranteed zero training error",
                    "More training data"
                ],
                "answer": "A structure where local minima can also be global minima"
            },
            {
                "question": "Why is log loss commonly used for probabilistic classification?",
                "options": [
                    "It penalizes confident incorrect probability predictions",
                    "It always ignores probabilities",
                    "It measures dataset size",
                    "It removes all outliers"
                ],
                "answer": "It penalizes confident incorrect probability predictions"
            }
        ]
    },


    "Machine Learning": {

        "Beginner": [
            {
                "question": "What is supervised learning?",
                "options": [
                    "Learning from labelled examples",
                    "Learning without data",
                    "Only clustering",
                    "Manual programming of every prediction"
                ],
                "answer": "Learning from labelled examples"
            },
            {
                "question": "What is a training dataset used for?",
                "options": [
                    "Teaching a machine learning model",
                    "Only displaying results",
                    "Deleting features",
                    "Deploying a website"
                ],
                "answer": "Teaching a machine learning model"
            },
            {
                "question": "Which task predicts a continuous numerical value?",
                "options": ["Regression", "Classification", "Clustering", "Tokenization"],
                "answer": "Regression"
            },
            {
                "question": "Which task predicts categories such as spam or not spam?",
                "options": ["Regression", "Classification", "Clustering", "Normalization"],
                "answer": "Classification"
            },
            {
                "question": "What is a feature?",
                "options": [
                    "An input variable used by a model",
                    "The final prediction",
                    "A programming language",
                    "A database server"
                ],
                "answer": "An input variable used by a model"
            },
            {
                "question": "What is a model in machine learning?",
                "options": [
                    "A learned mathematical pattern used for prediction",
                    "Only a dataset",
                    "A web browser",
                    "A text editor"
                ],
                "answer": "A learned mathematical pattern used for prediction"
            },
            {
                "question": "What is clustering?",
                "options": [
                    "Grouping similar data points",
                    "Predicting labelled classes only",
                    "Writing Python comments",
                    "Sorting source code"
                ],
                "answer": "Grouping similar data points"
            },
            {
                "question": "Why is test data used?",
                "options": [
                    "To evaluate performance on unseen data",
                    "To train every parameter",
                    "To increase labels",
                    "To create features"
                ],
                "answer": "To evaluate performance on unseen data"
            }
        ],

        "Intermediate": [
            {
                "question": "What is overfitting?",
                "options": [
                    "A model learns training data too closely and generalizes poorly",
                    "A model cannot learn anything",
                    "A dataset has no labels",
                    "A model has too few features"
                ],
                "answer": "A model learns training data too closely and generalizes poorly"
            },
            {
                "question": "Why do we split data into training and validation sets?",
                "options": [
                    "To evaluate and tune models before final testing",
                    "To remove all features",
                    "To increase the number of labels",
                    "To avoid using data"
                ],
                "answer": "To evaluate and tune models before final testing"
            },
            {
                "question": "What does precision measure?",
                "options": [
                    "The fraction of predicted positives that are actually positive",
                    "The fraction of all negatives",
                    "The training time",
                    "The number of features"
                ],
                "answer": "The fraction of predicted positives that are actually positive"
            },
            {
                "question": "What does recall measure?",
                "options": [
                    "The fraction of actual positives that are found",
                    "The number of training rows",
                    "The number of model parameters",
                    "The feature scale"
                ],
                "answer": "The fraction of actual positives that are found"
            },
            {
                "question": "What is cross-validation used for?",
                "options": [
                    "Estimating model performance across different data splits",
                    "Creating neural networks",
                    "Removing labels",
                    "Writing SQL queries"
                ],
                "answer": "Estimating model performance across different data splits"
            },
            {
                "question": "What is feature engineering?",
                "options": [
                    "Creating or transforming useful input features",
                    "Deleting the target variable",
                    "Deploying a model",
                    "Writing documentation"
                ],
                "answer": "Creating or transforming useful input features"
            },
            {
                "question": "What does regularization generally do?",
                "options": [
                    "Penalizes model complexity to reduce overfitting",
                    "Always increases model complexity",
                    "Deletes the dataset",
                    "Guarantees perfect accuracy"
                ],
                "answer": "Penalizes model complexity to reduce overfitting"
            },
            {
                "question": "What is an epoch in iterative model training?",
                "options": [
                    "One complete pass through the training data",
                    "One feature",
                    "One prediction",
                    "One test example"
                ],
                "answer": "One complete pass through the training data"
            }
        ],

        "Advanced": [
            {
                "question": "Why can accuracy be misleading for highly imbalanced classification data?",
                "options": [
                    "A model can achieve high accuracy by mostly predicting the majority class",
                    "Accuracy cannot be calculated",
                    "Accuracy always equals recall",
                    "Class imbalance increases the number of features"
                ],
                "answer": "A model can achieve high accuracy by mostly predicting the majority class"
            },
            {
                "question": "What is the bias-variance tradeoff?",
                "options": [
                    "Balancing underfitting from high bias against sensitivity to data from high variance",
                    "Choosing Python over R",
                    "Balancing labels and features",
                    "Selecting training hardware"
                ],
                "answer": "Balancing underfitting from high bias against sensitivity to data from high variance"
            },
            {
                "question": "What does gradient descent optimize?",
                "options": [
                    "A model's parameters by moving toward lower loss",
                    "The dataset size",
                    "The number of labels",
                    "The number of classes only"
                ],
                "answer": "A model's parameters by moving toward lower loss"
            },
            {
                "question": "What is data leakage?",
                "options": [
                    "Information unavailable at prediction time influences training",
                    "A file is accidentally deleted",
                    "A model has too few parameters",
                    "A dataset contains numerical features"
                ],
                "answer": "Information unavailable at prediction time influences training"
            },
            {
                "question": "Why is the test set ideally used only at the end?",
                "options": [
                    "Repeated use can indirectly tune the model to the test data",
                    "Test data cannot contain numbers",
                    "The model cannot predict on test data",
                    "Testing always changes the labels"
                ],
                "answer": "Repeated use can indirectly tune the model to the test data"
            },
            {
                "question": "What is the purpose of an ROC curve?",
                "options": [
                    "To examine classification performance across thresholds",
                    "To visualize neural network layers",
                    "To store features",
                    "To tokenize text"
                ],
                "answer": "To examine classification performance across thresholds"
            },
            {
                "question": "What does PCA primarily attempt to do?",
                "options": [
                    "Represent data using fewer dimensions while preserving important variation",
                    "Add more labels",
                    "Increase every feature",
                    "Train only decision trees"
                ],
                "answer": "Represent data using fewer dimensions while preserving important variation"
            },
            {
                "question": "Why can feature scaling matter for distance-based algorithms?",
                "options": [
                    "Large-scale features can dominate distance calculations",
                    "Distance algorithms cannot use numbers",
                    "Scaling removes the target",
                    "Scaling always increases accuracy"
                ],
                "answer": "Large-scale features can dominate distance calculations"
            }
        ]
    },


    "Deep Learning": {

        "Beginner": [
            {
                "question": "What is an artificial neuron inspired by?",
                "options": [
                    "A simplified model of biological neurons",
                    "A database table",
                    "A sorting algorithm",
                    "A web server"
                ],
                "answer": "A simplified model of biological neurons"
            },
            {
                "question": "What is a neural network made of?",
                "options": [
                    "Connected computational layers",
                    "Only databases",
                    "Only images",
                    "Web pages"
                ],
                "answer": "Connected computational layers"
            },
            {
                "question": "What is an activation function used for?",
                "options": [
                    "Introducing non-linearity",
                    "Storing datasets",
                    "Deleting parameters",
                    "Creating labels"
                ],
                "answer": "Introducing non-linearity"
            },
            {
                "question": "What is a loss function?",
                "options": [
                    "A measure of prediction error",
                    "A database",
                    "A Python package",
                    "A data type"
                ],
                "answer": "A measure of prediction error"
            },
            {
                "question": "What does training a neural network change?",
                "options": [
                    "Model parameters such as weights",
                    "The programming language",
                    "The dataset file format",
                    "The computer monitor"
                ],
                "answer": "Model parameters such as weights"
            },
            {
                "question": "What is an input layer?",
                "options": [
                    "The layer receiving input features",
                    "The final prediction only",
                    "The optimizer",
                    "The loss function"
                ],
                "answer": "The layer receiving input features"
            },
            {
                "question": "What is an output layer?",
                "options": [
                    "The layer producing the model's final output",
                    "The training dataset",
                    "The input file",
                    "The optimizer"
                ],
                "answer": "The layer producing the model's final output"
            },
            {
                "question": "What does an epoch mean in neural network training?",
                "options": [
                    "One complete pass through the training dataset",
                    "One neuron",
                    "One prediction",
                    "One hidden layer"
                ],
                "answer": "One complete pass through the training dataset"
            }
        ],

        "Intermediate": [
            {
                "question": "What is backpropagation used for?",
                "options": [
                    "Computing gradients for updating model parameters",
                    "Loading images",
                    "Creating labels",
                    "Deploying APIs"
                ],
                "answer": "Computing gradients for updating model parameters"
            },
            {
                "question": "What does ReLU output for a negative input?",
                "options": ["The input itself", "Zero", "One", "The square"],
                "answer": "Zero"
            },
            {
                "question": "What is dropout used for?",
                "options": [
                    "Reducing overfitting by randomly disabling units during training",
                    "Increasing dataset size",
                    "Removing all layers",
                    "Creating labels"
                ],
                "answer": "Reducing overfitting by randomly disabling units during training"
            },
            {
                "question": "What is a CNN especially useful for?",
                "options": [
                    "Spatial patterns such as those in images",
                    "Only tabular sorting",
                    "Database indexing",
                    "Text file compression"
                ],
                "answer": "Spatial patterns such as those in images"
            },
            {
                "question": "What is a batch in neural network training?",
                "options": [
                    "A subset of training examples processed together",
                    "The entire model",
                    "One parameter",
                    "A loss function"
                ],
                "answer": "A subset of training examples processed together"
            },
            {
                "question": "What does learning rate control?",
                "options": [
                    "The step size used when updating parameters",
                    "The number of labels",
                    "The dataset format",
                    "The number of classes"
                ],
                "answer": "The step size used when updating parameters"
            },
            {
                "question": "What is an RNN designed to handle especially well?",
                "options": [
                    "Sequential or time-dependent information",
                    "Only static images",
                    "Database tables",
                    "Operating systems"
                ],
                "answer": "Sequential or time-dependent information"
            },
            {
                "question": "Why are hidden layers called hidden?",
                "options": [
                    "They are intermediate layers between input and output",
                    "They cannot contain parameters",
                    "They are encrypted",
                    "They are never trained"
                ],
                "answer": "They are intermediate layers between input and output"
            }
        ],

        "Advanced": [
            {
                "question": "Why can very deep networks suffer from vanishing gradients?",
                "options": [
                    "Gradients can become extremely small as they propagate backward",
                    "The dataset becomes smaller",
                    "The model loses all labels",
                    "The optimizer stops existing"
                ],
                "answer": "Gradients can become extremely small as they propagate backward"
            },
            {
                "question": "What problem do residual connections help address?",
                "options": [
                    "Training very deep networks by improving gradient flow",
                    "Removing all parameters",
                    "Reducing dataset size",
                    "Creating class labels"
                ],
                "answer": "Training very deep networks by improving gradient flow"
            },
            {
                "question": "What is batch normalization intended to help with?",
                "options": [
                    "Stabilizing and accelerating neural network training",
                    "Creating test labels",
                    "Deleting features",
                    "Converting images to text"
                ],
                "answer": "Stabilizing and accelerating neural network training"
            },
            {
                "question": "What is attention designed to allow a model to do?",
                "options": [
                    "Weight the importance of different parts of an input",
                    "Delete all input tokens",
                    "Remove neural network layers",
                    "Guarantee correct predictions"
                ],
                "answer": "Weight the importance of different parts of an input"
            },
            {
                "question": "What is the main idea of transfer learning?",
                "options": [
                    "Reuse knowledge from a pretrained model for another task",
                    "Train without data",
                    "Delete pretrained parameters",
                    "Avoid evaluation"
                ],
                "answer": "Reuse knowledge from a pretrained model for another task"
            },
            {
                "question": "Why are GPUs useful for deep learning?",
                "options": [
                    "They can efficiently perform large amounts of parallel numerical computation",
                    "They eliminate the need for data",
                    "They automatically label datasets",
                    "They guarantee model accuracy"
                ],
                "answer": "They can efficiently perform large amounts of parallel numerical computation"
            },
            {
                "question": "What is an embedding in modern deep learning systems?",
                "options": [
                    "A learned numerical representation of an item",
                    "A training label only",
                    "A hardware component",
                    "A loss function"
                ],
                "answer": "A learned numerical representation of an item"
            },
            {
                "question": "What does softmax commonly produce for multiclass classification?",
                "options": [
                    "A probability distribution across classes",
                    "Only one raw integer",
                    "A binary image",
                    "A feature database"
                ],
                "answer": "A probability distribution across classes"
            }
        ]
    },


    "Generative AI": {

        "Beginner": [
            {
                "question": "What does Generative AI primarily do?",
                "options": [
                    "Generate new content from learned patterns",
                    "Only store files",
                    "Only sort numbers",
                    "Only display websites"
                ],
                "answer": "Generate new content from learned patterns"
            },
            {
                "question": "What does LLM stand for?",
                "options": [
                    "Large Language Model",
                    "Long Learning Machine",
                    "Logical Language Method",
                    "Large Logic Memory"
                ],
                "answer": "Large Language Model"
            },
            {
                "question": "What is a prompt?",
                "options": [
                    "An instruction or input given to an AI model",
                    "A database",
                    "A neural network layer",
                    "A programming language"
                ],
                "answer": "An instruction or input given to an AI model"
            },
            {
                "question": "What is a token in an LLM?",
                "options": [
                    "A unit of text processed by the model",
                    "A hardware chip",
                    "A database row",
                    "A web page"
                ],
                "answer": "A unit of text processed by the model"
            },
            {
                "question": "What is an AI chatbot?",
                "options": [
                    "A system that interacts with users using natural language",
                    "A database server",
                    "A compiler",
                    "A spreadsheet"
                ],
                "answer": "A system that interacts with users using natural language"
            },
            {
                "question": "What does RAG stand for?",
                "options": [
                    "Retrieval-Augmented Generation",
                    "Random AI Generation",
                    "Rapid Answer Generator",
                    "Retrieval Analysis Graph"
                ],
                "answer": "Retrieval-Augmented Generation"
            },
            {
                "question": "What is an embedding?",
                "options": [
                    "A numerical representation used to capture semantic relationships",
                    "A password",
                    "A database password",
                    "A file extension"
                ],
                "answer": "A numerical representation used to capture semantic relationships"
            },
            {
                "question": "What is multimodal AI?",
                "options": [
                    "AI that can work with multiple types of data such as text and images",
                    "AI that only handles text",
                    "AI without training data",
                    "AI that only uses numbers"
                ],
                "answer": "AI that can work with multiple types of data such as text and images"
            }
        ],

        "Intermediate": [
            {
                "question": "Why is context important when using an LLM?",
                "options": [
                    "It gives the model relevant information for generating a response",
                    "It increases monitor resolution",
                    "It removes the model",
                    "It replaces all training"
                ],
                "answer": "It gives the model relevant information for generating a response"
            },
            {
                "question": "What is the main purpose of RAG?",
                "options": [
                    "Retrieve relevant external information before generating an answer",
                    "Train a model from scratch every time",
                    "Remove all documents",
                    "Generate random answers"
                ],
                "answer": "Retrieve relevant external information before generating an answer"
            },
            {
                "question": "What is prompt engineering?",
                "options": [
                    "Designing instructions to guide model behavior",
                    "Building GPU hardware",
                    "Creating database indexes",
                    "Compressing images"
                ],
                "answer": "Designing instructions to guide model behavior"
            },
            {
                "question": "What does temperature generally influence in text generation?",
                "options": [
                    "The randomness of token selection",
                    "The model's number of layers",
                    "The dataset size",
                    "The GPU memory"
                ],
                "answer": "The randomness of token selection"
            },
            {
                "question": "What is fine-tuning?",
                "options": [
                    "Further training a pretrained model on task-specific data",
                    "Deleting model weights",
                    "Changing the monitor",
                    "Writing prompts only"
                ],
                "answer": "Further training a pretrained model on task-specific data"
            },
            {
                "question": "Why are embeddings useful in semantic search?",
                "options": [
                    "Similar meanings can be represented by nearby vectors",
                    "They eliminate the need for documents",
                    "They only store passwords",
                    "They guarantee factual answers"
                ],
                "answer": "Similar meanings can be represented by nearby vectors"
            },
            {
                "question": "What is hallucination in Generative AI?",
                "options": [
                    "A generated response containing unsupported or false information",
                    "A model shutdown",
                    "A database failure",
                    "A GPU error"
                ],
                "answer": "A generated response containing unsupported or false information"
            },
            {
                "question": "What is a vector database commonly used for in RAG systems?",
                "options": [
                    "Efficient similarity search over embeddings",
                    "Rendering web pages",
                    "Training CPUs",
                    "Creating passwords"
                ],
                "answer": "Efficient similarity search over embeddings"
            }
        ],

        "Advanced": [
            {
                "question": "Why does retrieval quality strongly affect a RAG system?",
                "options": [
                    "Poor retrieved context can lead to poor grounded generation",
                    "Retrieval only changes the UI",
                    "Generation ignores retrieved information",
                    "Retrieval automatically fixes every hallucination"
                ],
                "answer": "Poor retrieved context can lead to poor grounded generation"
            },
            {
                "question": "What is a context window?",
                "options": [
                    "The amount of input/output context a model can process within its limit",
                    "The model's GPU size",
                    "The number of databases",
                    "The number of users"
                ],
                "answer": "The amount of input/output context a model can process within its limit"
            },
            {
                "question": "What is instruction tuning?",
                "options": [
                    "Training a model to better follow natural-language instructions",
                    "Increasing GPU clock speed",
                    "Removing training data",
                    "Converting text into images"
                ],
                "answer": "Training a model to better follow natural-language instructions"
            },
            {
                "question": "What is the role of an embedding model in a RAG pipeline?",
                "options": [
                    "Convert text or other content into vectors for similarity search",
                    "Generate the final answer directly",
                    "Deploy the application",
                    "Train the database"
                ],
                "answer": "Convert text or other content into vectors for similarity search"
            },
            {
                "question": "What is retrieval-augmented generation attempting to improve?",
                "options": [
                    "Grounding generation in relevant external information",
                    "GPU temperature",
                    "Python execution speed",
                    "Database storage capacity"
                ],
                "answer": "Grounding generation in relevant external information"
            },
            {
                "question": "Why can chunking strategy matter in document retrieval?",
                "options": [
                    "Poor chunks can separate important context or retrieve irrelevant text",
                    "Chunking changes GPU architecture",
                    "Chunking eliminates embeddings",
                    "Chunking guarantees perfect answers"
                ],
                "answer": "Poor chunks can separate important context or retrieve irrelevant text"
            },
            {
                "question": "What does temperature near zero generally encourage in many text-generation APIs?",
                "options": [
                    "More deterministic token selection",
                    "Maximum randomness",
                    "Longer context windows",
                    "More training epochs"
                ],
                "answer": "More deterministic token selection"
            },
            {
                "question": "Why can fine-tuning be different from RAG?",
                "options": [
                    "Fine-tuning changes model parameters while RAG supplies retrieved context at inference",
                    "RAG always changes model weights",
                    "Fine-tuning never uses data",
                    "They are exactly the same process"
                ],
                "answer": "Fine-tuning changes model parameters while RAG supplies retrieved context at inference"
            }
        ]
    }
}


# =========================================================
# SESSION STATE
# =========================================================

DEFAULT_STATE = {
    "page": "home",
    "profile": {},
    "diagnostic_questions": [],
    "answers": {},
    "scores": {},
    "diagnostic_complete": False
}

for key, value in DEFAULT_STATE.items():
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
    else:
        return "Strong"


def create_diagnostic(level):
    """
    Select exactly 3 DIFFERENT questions from each subject.

    Because sampling happens independently for every subject,
    there are exactly 15 questions total.
    """

    selected = []

    for subject in SUBJECTS:

        available = QUESTION_BANK[subject][level]

        chosen = random.sample(
            available,
            3
        )

        for question in chosen:

            selected.append({
                "subject": subject,
                "difficulty": level,
                "question": question["question"],
                "options": random.sample(
                    question["options"],
                    len(question["options"])
                ),
                "answer": question["answer"]
            })

    # Shuffle all 15 questions so subjects are mixed.
    random.shuffle(selected)

    return selected


def calculate_scores():

    subject_correct = {
        subject: 0
        for subject in SUBJECTS
    }

    subject_total = {
        subject: 0
        for subject in SUBJECTS
    }

    for index, question in enumerate(
        st.session_state.diagnostic_questions
    ):

        subject = question["subject"]

        subject_total[subject] += 1

        user_answer = st.session_state.answers.get(
            f"q_{index}"
        )

        if user_answer == question["answer"]:
            subject_correct[subject] += 1

    scores = {}

    for subject in SUBJECTS:

        if subject_total[subject] == 0:
            scores[subject] = 0
        else:
            scores[subject] = round(
                (
                    subject_correct[subject]
                    /
                    subject_total[subject]
                )
                * 100
            )

    return scores


def start_diagnostic():

    level = st.session_state.profile["level"]

    st.session_state.diagnostic_questions = create_diagnostic(level)

    st.session_state.answers = {}

    st.session_state.scores = {}

    st.session_state.diagnostic_complete = False

    st.session_state.page = "diagnostic"


def get_recommendation():

    if not st.session_state.scores:
        return SUBJECTS[0], 0

    weakest = min(
        st.session_state.scores,
        key=st.session_state.scores.get
    )

    return weakest, st.session_state.scores[weakest]


# =========================================================
# TOP NAVIGATION
# =========================================================

def show_nav():

    logo_path = get_logo_path()

    logo_html = ""

    if logo_path:
        try:
            import base64

            with open(logo_path, "rb") as f:
                encoded = base64.b64encode(
                    f.read()
                ).decode()

            logo_html = f"""
                <img
                    src="data:image/jpeg;base64,{encoded}"
                    class="brand-logo"
                />
            """

        except Exception:
            logo_html = "🎓"

    else:
        logo_html = "🎓"

    st.markdown(
        f"""
        <div class="top-nav">

            <div class="brand-area">

                {logo_html}

                <div class="brand-name">
                    AI <span>Learn</span>
                </div>

            </div>

            <div class="nav-actions">

                <div class="nav-gift">
                    🎁
                </div>

                <div class="nav-login">
                    Log in
                </div>

                <div class="nav-join">
                    Join for free
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# HOME PAGE
# =========================================================

def home_page():

    show_nav()

    # ---------------- HERO ----------------

    col1, col2 = st.columns(
        [1.05, 0.95],
        gap="large"
    )

    with col1:

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
            unsafe_allow_html=True
        )

    with col2:

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
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "Your Name",
            value=st.session_state.profile.get(
                "name",
                ""
            ),
            placeholder="Enter your name"
        )

    with col2:

        level = st.selectbox(
            "Current AI Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ],
            index=[
                "Beginner",
                "Intermediate",
                "Advanced"
            ].index(
                st.session_state.profile.get(
                    "level",
                    "Beginner"
                )
            )
        )

    col3, col4 = st.columns(2)

    with col3:

        goal = st.selectbox(
            "What is your main goal?",
            [
                "Learn AI fundamentals",
                "Build AI projects",
                "Prepare for a job",
                "Learn Generative AI",
                "Learn AI Agents"
            ]
        )

    with col4:

        study_time = st.selectbox(
            "How much time can you study daily?",
            [
                "15 minutes",
                "30 minutes",
                "1 hour",
                "2+ hours"
            ]
        )

    st.write("")

    start_col1, start_col2, start_col3 = st.columns(
        [1, 2, 1]
    )

    with start_col2:

        if st.button(
            "🚀 Start AI Journey",
            use_container_width=True,
            type="primary"
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
                    "study_time": study_time
                }

                start_diagnostic()

                st.rerun()

    # ---------------- FOUNDATIONS ----------------

    st.markdown(
        """
        <div class="foundations-section">

            <div class="foundations-title">
                One journey. Five AI foundations.
            </div>

            <div class="foundations-subtitle">
                Learn the foundations needed to understand,
                build and work with modern AI.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    cols = st.columns(5)

    for index, subject in enumerate(SUBJECTS):

        with cols[index]:

            st.markdown(
                f"""
                <div class="subject-card">

                    <div class="subject-icon">
                        {SUBJECT_ICONS[subject]}
                    </div>

                    <div class="subject-name">
                        {subject}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# DIAGNOSTIC PAGE
# =========================================================

def diagnostic_page():

    show_nav()

    st.markdown(
        """
        <div class="page-title">
            AI Knowledge Assessment
        </div>

        <div class="page-subtitle">
            Answer all 15 questions. Your answers will be
            evaluated after you submit the assessment.
        </div>
        """,
        unsafe_allow_html=True
    )

    level = st.session_state.profile.get(
        "level",
        "Beginner"
    )

    st.info(
        f"Assessment level: **{level}**  •  "
        f"15 questions  •  3 questions from each AI foundation"
    )

    questions = st.session_state.diagnostic_questions

    if not questions:
        st.error(
            "No diagnostic questions found."
        )

        if st.button("Return Home"):
            st.session_state.page = "home"
            st.rerun()

        return

    # -----------------------------------------------------
    # ALL 15 QUESTIONS AT ONCE
    # -----------------------------------------------------

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
            unsafe_allow_html=True
        )

        selected = st.radio(
            "Choose your answer:",
            question["options"],
            index=None,
            key=f"q_{index}",
            label_visibility="collapsed"
        )

        st.write("")

    st.divider()

    # -----------------------------------------------------
    # SUBMIT
    # -----------------------------------------------------

    unanswered = []

    for index in range(15):

        answer = st.session_state.get(
            f"q_{index}"
        )

        if answer is None:
            unanswered.append(index + 1)

    submit_col1, submit_col2, submit_col3 = st.columns(
        [1, 2, 1]
    )

    with submit_col2:

        if st.button(
            "✅ Submit Diagnostic",
            use_container_width=True,
            type="primary"
        ):

            if unanswered:

                st.warning(
                    f"Please answer all questions before submitting. "
                    f"Unanswered questions: {', '.join(map(str, unanswered))}"
                )

            else:

                # Store answers silently.
                st.session_state.answers = {
                    f"q_{index}":
                    st.session_state.get(
                        f"q_{index}"
                    )
                    for index in range(15)
                }

                st.session_state.scores = calculate_scores()

                st.session_state.diagnostic_complete = True

                st.session_state.page = "score"

                st.rerun()


# =========================================================
# SCORE CARD
# =========================================================

def score_card_page():

    show_nav()

    if not st.session_state.diagnostic_complete:

        st.session_state.page = "home"

        st.rerun()

        return

    scores = st.session_state.scores

    overall = round(
        sum(scores.values())
        /
        len(scores)
    )

    st.markdown(
        f"""
        <div class="score-header">

            <div class="score-header-title">
                🎓 YOUR AI LEARNING SCORE CARD
            </div>

            <div class="overall-score">
                {overall}%
            </div>

            <div class="score-description">
                Your current AI knowledge profile
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # -----------------------------------------------------
    # SUBJECT SCORES
    # -----------------------------------------------------

    for subject in SUBJECTS:

        score = scores.get(
            subject,
            0
        )

        status = status_for_score(
            score
        )

        st.markdown(
            f"""
            <div class="score-card">

                <div class="score-topic">
                    {SUBJECT_ICONS[subject]}
                    &nbsp; {subject}
                </div>

                <div style="
                    background:#edf1f3;
                    height:12px;
                    border-radius:10px;
                    overflow:hidden;
                ">

                    <div style="
                        width:{score}%;
                        height:100%;
                        background:#10b981;
                        border-radius:10px;
                    ">
                    </div>

                </div>

                <div class="score-status">
                    <strong>{score}%</strong>
                    &nbsp; • &nbsp;
                    Status: {status}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # -----------------------------------------------------
    # RECOMMENDATION
    # -----------------------------------------------------

    weakest_subject, weakest_score = get_recommendation()

    st.markdown(
        f"""
        <div class="recommendation">

            <div class="recommendation-title">
                🎯 Recommended Starting Point
            </div>

            <div style="
                font-size:21px;
                font-weight:750;
                color:#10a978;
                margin-bottom:8px;
            ">
                {weakest_subject} — {weakest_score}%
            </div>

            <div style="
                color:#687580;
                line-height:1.6;
            ">
                Build your foundation here before moving
                to more advanced topics. Your personalised
                roadmap will prioritise the areas where
                you need the most development.
            </div>

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

            start_diagnostic()

            st.rerun()


# =========================================================
# PERSONALIZED ROADMAP
# =========================================================

def roadmap_page():

    show_nav()

    st.markdown(
        """
        <div class="page-title">
            🗺️ Your Personalised AI Roadmap
        </div>

        <div class="page-subtitle">
            Your learning order is based on the knowledge
            profile from your diagnostic.
        </div>
        """,
        unsafe_allow_html=True
    )

    sorted_subjects = sorted(
        SUBJECTS,
        key=lambda subject:
        st.session_state.scores.get(
            subject,
            0
        )
    )

    for index, subject in enumerate(
        sorted_subjects,
        start=1
    ):

        score = st.session_state.scores.get(
            subject,
            0
        )

        status = status_for_score(
            score
        )

        if score < 40:

            description = (
                "Start with the fundamentals and build "
                "a strong foundation through guided lessons "
                "and practice."
            )

        elif score < 70:

            description = (
                "Strengthen your current understanding with "
                "targeted practice and progressively harder tasks."
            )

        elif score < 100:

            description = (
                "You have a solid foundation. Continue with "
                "intermediate concepts and practical projects."
            )

        else:

            description = (
                "Your diagnostic indicates strong understanding. "
                "Move toward advanced concepts and projects."
            )

        st.markdown(
            f"""
            <div class="roadmap-card">

                <div>

                    <span class="roadmap-number">
                        {index}
                    </span>

                    <span class="roadmap-name">
                        {SUBJECT_ICONS[subject]}
                        &nbsp; {subject}
                    </span>

                </div>

                <div class="roadmap-description">

                    Current score:
                    <strong>{score}%</strong>
                    &nbsp; • &nbsp;
                    {status}

                    <br><br>

                    {description}

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    if st.button(
        "🏠 Back to Home",
        use_container_width=True
    ):

        st.session_state.page = "home"

        st.rerun()


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

with st.sidebar:

    st.markdown(
        "### 🎓 AI Learn"
    )

    st.caption(
        "Personalised AI learning"
    )

    if st.button(
        "🏠 Home",
        use_container_width=True
    ):

        st.session_state.page = "home"

        st.rerun()

    if st.session_state.diagnostic_complete:

        if st.button(
            "📊 Score Card",
            use_container_width=True
        ):

            st.session_state.page = "score"

            st.rerun()

        if st.button(
            "🗺️ Roadmap",
            use_container_width=True
        ):

            st.session_state.page = "roadmap"

            st.rerun()


# =========================================================
# PAGE ROUTING
# =========================================================

if st.session_state.page == "home":

    home_page()

elif st.session_state.page == "diagnostic":

    diagnostic_page()

elif st.session_state.page == "score":

    score_card_page()

elif st.session_state.page == "roadmap":

    roadmap_page()

else:

    st.session_state.page = "home"

    home_page()
