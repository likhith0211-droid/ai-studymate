import random
import streamlit as st


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
# GLOBAL CSS
# =========================================================

st.markdown(
    """
    <style>

    /* ---------- GLOBAL ---------- */

    .stApp {
        background: #ffffff;
        color: #344454;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 0.5rem;
        padding-bottom: 3rem;
    }

    header[data-testid="stHeader"] {
        background: white;
    }

    footer {
        visibility: hidden;
    }

    /* Hide Streamlit default decoration */
    [data-testid="stDecoration"] {
        display: none;
    }

    /* ---------- HEADER ---------- */

    .ai-header {
        height: 72px;
        border-bottom: 1px solid #e8edf2;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 8px;
        margin-bottom: 10px;
    }

    .ai-brand {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .ai-logo {
        width: 44px;
        height: 44px;
        object-fit: contain;
        border-radius: 8px;
    }

    .ai-brand-name {
        font-size: 27px;
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
        width: 42px;
        height: 42px;
        border: 1px solid #e2e8ee;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
    }

    /* ---------- HERO ---------- */

    .hero-section {
        min-height: 470px;
        display: flex;
        align-items: center;
        padding: 55px 0 35px 0;
    }

    .hero-left {
        padding: 25px 20px 25px 0;
    }

    .hero-title {
        font-size: 58px;
        line-height: 1.04;
        font-weight: 800;
        letter-spacing: -2px;
        color: #344454;
        margin-bottom: 22px;
    }

    .hero-title span {
        color: #344454;
    }

    .hero-subtitle {
        font-size: 20px;
        line-height: 1.55;
        color: #637282;
        max-width: 570px;
        margin-bottom: 22px;
    }

    .hero-highlight {
        font-size: 16px;
        line-height: 1.6;
        color: #637282;
        max-width: 570px;
        padding: 17px 20px;
        background: #f5f9fc;
        border-left: 4px solid #19b889;
        border-radius: 8px;
    }

    .hero-highlight strong {
        color: #344454;
    }

    /* ---------- VISUAL ---------- */

    .learning-visual {
        position: relative;
        height: 430px;
        width: 100%;
        min-width: 450px;
    }

    .visual-main-circle {
        position: absolute;
        width: 260px;
        height: 260px;
        border-radius: 50%;
        background: #eaf4ff;
        left: 50%;
        top: 70px;
        transform: translateX(-50%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 105px;
        box-shadow: 0 18px 45px rgba(52, 68, 84, 0.10);
    }

    .visual-small {
        position: absolute;
        width: 82px;
        height: 82px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 38px;
        box-shadow: 0 10px 30px rgba(52, 68, 84, 0.12);
    }

    .visual-one {
        background: #e9f8f2;
        left: 8%;
        top: 55px;
    }

    .visual-two {
        background: #fff4df;
        right: 7%;
        top: 105px;
    }

    .visual-three {
        background: #f0ebff;
        right: 12%;
        bottom: 45px;
    }

    .floating-card {
        position: absolute;
        padding: 13px 18px;
        border-radius: 12px;
        background: white;
        box-shadow: 0 10px 30px rgba(52, 68, 84, 0.13);
        font-size: 14px;
        font-weight: 700;
        color: #344454;
    }

    .card-ai {
        left: 2%;
        bottom: 72px;
    }

    .card-progress {
        right: 0;
        top: 35px;
    }

    .card-python {
        left: 25%;
        bottom: 5px;
    }

    /* ---------- PROFILE ---------- */

    .profile-section {
        margin-top: 25px;
        padding: 38px;
        background: #f8fafc;
        border-radius: 20px;
        border: 1px solid #e9eef3;
    }

    .profile-title {
        font-size: 28px;
        font-weight: 750;
        color: #344454;
        margin-bottom: 8px;
    }

    .profile-description {
        color: #687786;
        font-size: 16px;
        margin-bottom: 28px;
    }

    /* ---------- FOUNDATION ---------- */

    .foundation-section {
        text-align: center;
        padding: 65px 0 25px 0;
    }

    .foundation-title {
        font-size: 32px;
        font-weight: 800;
        color: #344454;
        margin-bottom: 10px;
    }

    .foundation-description {
        color: #687786;
        font-size: 17px;
        margin-bottom: 30px;
    }

    .foundation-card {
        background: white;
        border: 1px solid #e5ebf0;
        border-radius: 15px;
        padding: 24px 10px;
        min-height: 125px;
        box-shadow: 0 5px 18px rgba(52, 68, 84, 0.05);
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

    /* ---------- BUTTONS ---------- */

    .stButton > button {
        border-radius: 8px;
        min-height: 44px;
        font-weight: 700;
        border: 1px solid #344454;
    }

    /* ---------- DIAGNOSTIC ---------- */

    .diagnostic-header {
        padding: 30px 0 20px 0;
    }

    .diagnostic-title {
        font-size: 38px;
        font-weight: 800;
        color: #344454;
    }

    .diagnostic-subtitle {
        color: #687786;
        font-size: 16px;
        margin-top: 8px;
    }

    .question-card {
        background: #ffffff;
        border: 1px solid #e2e8ee;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 4px 15px rgba(52, 68, 84, 0.04);
    }

    .question-number {
        font-size: 13px;
        font-weight: 700;
        color: #19a879;
        margin-bottom: 8px;
    }

    .question-text {
        font-size: 17px;
        font-weight: 700;
        line-height: 1.45;
        color: #344454;
    }

    /* ---------- SCORE CARD ---------- */

    .score-header {
        text-align: center;
        background: #f5f9fc;
        border-radius: 20px;
        padding: 35px 20px;
        margin-bottom: 30px;
    }

    .score-header-title {
        font-size: 28px;
        font-weight: 800;
        color: #344454;
    }

    .overall-score {
        font-size: 58px;
        font-weight: 800;
        color: #19a879;
        margin: 12px 0;
    }

    .score-subtitle {
        color: #687786;
    }

    .subject-card {
        border: 1px solid #e3e9ee;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
        background: white;
    }

    .subject-name {
        font-size: 18px;
        font-weight: 750;
        color: #344454;
        margin-bottom: 10px;
    }

    .score-number {
        font-size: 24px;
        font-weight: 800;
        color: #344454;
    }

    .recommendation {
        margin-top: 25px;
        background: #f0faf6;
        border: 1px solid #ccefe1;
        border-radius: 15px;
        padding: 25px;
    }

    .recommendation-title {
        font-size: 20px;
        font-weight: 800;
        color: #344454;
        margin-bottom: 8px;
    }

    /* ---------- ROADMAP ---------- */

    .roadmap-card {
        border: 1px solid #e2e8ee;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
        background: white;
    }

    .roadmap-number {
        width: 34px;
        height: 34px;
        border-radius: 50%;
        background: #344454;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .roadmap-title {
        font-size: 19px;
        font-weight: 800;
        color: #344454;
    }

    .roadmap-text {
        color: #687786;
        margin-top: 7px;
        line-height: 1.5;
    }

    /* ---------- MOBILE ---------- */

    @media (max-width: 800px) {

        .hero-section {
            min-height: auto;
        }

        .hero-title {
            font-size: 43px;
        }

        .learning-visual {
            min-width: 0;
            margin-top: 20px;
        }

        .visual-main-circle {
            width: 210px;
            height: 210px;
        }

        .profile-section {
            padding: 22px;
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

LOGO_URL = (
    "https://raw.githubusercontent.com/"
    "likhith0211-droid/ai-studymate/main/"
    "0f6577fe444ba6b1365cd00394ee581e.jpg"
)


# =========================================================
# QUESTION BANK
#
# Format:
# question, options, correct_index
#
# There are separate questions for each level.
# We randomly choose 3 from each subject.
# Therefore 15 questions are shown at once.
# =========================================================

QUESTION_BANK = {

    "Beginner": {

        "Python": [
            ("Which symbol is commonly used to start a comment in Python?",
             ["//", "#", "<!--", "/*"], 1),

            ("Which of these is a Python data type?",
             ["Boolean", "Markup", "Selector", "Element"], 0),

            ("What does len([10, 20, 30]) return?",
             ["2", "3", "4", "30"], 1),

            ("Which keyword is used to define a function in Python?",
             ["function", "func", "def", "define"], 2),

            ("Which structure stores multiple ordered values in Python?",
             ["list", "condition", "module", "operator"], 0),

            ("What value represents a logical true condition in Python?",
             ["TRUE", "True", "trueValue", "Yes"], 1),
        ],

        "Mathematics & Statistics": [
            ("What is the mean of 2, 4 and 6?",
             ["2", "4", "6", "12"], 1),

            ("What is the probability of getting heads from a fair coin?",
             ["0", "0.25", "0.5", "1"], 2),

            ("Which measure represents the middle value of an ordered dataset?",
             ["Mean", "Median", "Range", "Variance"], 1),

            ("What is 5 squared?",
             ["10", "15", "20", "25"], 3),

            ("What does a larger standard deviation generally indicate?",
             ["Less variation", "More variation", "No data", "More samples only"], 1),

            ("Which operation is represented by 3 × 4?",
             ["Addition", "Subtraction", "Multiplication", "Division"], 2),
        ],

        "Machine Learning": [
            ("What is machine learning mainly used for?",
             ["Learning patterns from data", "Replacing electricity", "Writing HTML only", "Managing files only"], 0),

            ("What is a training dataset?",
             ["Data used to train a model", "Only final predictions", "A programming language", "A database password"], 0),

            ("Which is an example of supervised learning?",
             ["Learning from labelled examples", "Random guessing", "Compressing a file", "Drawing a chart manually"], 0),

            ("What is a model in machine learning?",
             ["A learned representation used to make predictions", "A computer monitor", "A spreadsheet only", "A keyboard layout"], 0),

            ("Which task is classification?",
             ["Predicting whether an email is spam", "Predicting tomorrow's exact temperature", "Sorting files alphabetically", "Adding two numbers"], 0),

            ("What is a feature?",
             ["An input variable used by a model", "The final prediction only", "A model password", "A programming error"], 0),
        ],

        "Deep Learning": [
            ("What is a neural network inspired by?",
             ["Networks of biological neurons", "Computer keyboards", "Databases", "Web browsers"], 0),

            ("What is a neuron in a neural network?",
             ["A computational unit", "A file type", "A database table", "A web page"], 0),

            ("What is an activation function used for?",
             ["Introducing non-linearity", "Storing files", "Creating passwords", "Installing Python"], 0),

            ("What does a neural network learn during training?",
             ["Parameters or weights", "Monitor brightness", "File names", "Keyboard shortcuts"], 0),

            ("What is an epoch?",
             ["One complete pass through the training data", "A single neuron", "A dataset column", "A programming language"], 0),

            ("What is a loss function used for?",
             ["Measuring prediction error", "Drawing neural networks", "Creating folders", "Loading images only"], 0),
        ],

        "Generative AI": [
            ("What is Generative AI designed to do?",
             ["Generate new content", "Only store databases", "Only sort files", "Only calculate averages"], 0),

            ("What does LLM stand for?",
             ["Large Language Model", "Linear Learning Machine", "Language Logic Module", "Large Logic Memory"], 0),

            ("What can an LLM generate?",
             ["Text", "Only electricity", "Only database tables", "Only images"], 0),

            ("What is a prompt?",
             ["An instruction or input given to an AI model", "A computer cable", "A database", "A Python package"], 0),

            ("What are tokens used for in language models?",
             ["Representing pieces of text", "Storing electricity", "Connecting monitors", "Creating folders"], 0),

            ("What is an AI chatbot?",
             ["A system designed to interact through conversation", "A graphics card", "A database server only", "A spreadsheet formula"], 0),
        ],
    },


    "Intermediate": {

        "Python": [
            ("What does a list comprehension primarily provide?",
             ["A concise way to create lists", "A way to compile Python", "A database connection", "A replacement for classes"], 0),

            ("What is the main difference between a list and a tuple?",
             ["Lists are mutable while tuples are immutable", "Tuples always contain strings", "Lists cannot contain numbers", "There is no difference"], 0),

            ("What does a Python dictionary store?",
             ["Key-value pairs", "Only ordered numbers", "Only functions", "Only Boolean values"], 0),

            ("What does *args allow a function to receive?",
             ["A variable number of positional arguments", "Only one keyword argument", "Only strings", "Only lists"], 0),

            ("What is the purpose of exception handling?",
             ["Handling runtime errors gracefully", "Making code execute twice", "Deleting variables", "Increasing screen resolution"], 0),

            ("What does a class primarily define?",
             ["A blueprint for creating objects", "A database connection only", "A loop", "A file extension"], 0),
        ],

        "Mathematics & Statistics": [
            ("What does variance measure?",
             ["The average squared deviation from the mean", "The middle observation", "The number of samples", "The maximum value only"], 0),

            ("What does correlation measure?",
             ["The strength and direction of association between variables", "The number of rows", "The median only", "The sample size only"], 0),

            ("What is a probability distribution?",
             ["A description of possible outcomes and their probabilities", "A programming loop", "A neural network layer", "A database schema"], 0),

            ("What does a derivative describe?",
             ["A rate of change", "A probability only", "A sample count", "A matrix dimension"], 0),

            ("What is a matrix?",
             ["A rectangular arrangement of values", "A probability distribution only", "A Python loop", "A neural network optimizer"], 0),

            ("What is the purpose of normalization in many ML workflows?",
             ["Putting features onto comparable scales", "Removing all rows", "Changing labels randomly", "Deleting outliers automatically"], 0),
        ],

        "Machine Learning": [
            ("What is overfitting?",
             ["When a model learns training data too specifically and generalizes poorly", "When a model has no parameters", "When data is missing", "When training is impossible"], 0),

            ("Why is a validation set commonly used?",
             ["To evaluate choices during model development", "To permanently store passwords", "To replace training data entirely", "To increase file size"], 0),

            ("What is precision?",
             ["The fraction of predicted positives that are actually positive", "The fraction of all samples that are positive", "The number of features", "The training duration"], 0),

            ("What is recall?",
             ["The fraction of actual positives that are correctly identified", "The number of negative samples", "The model size", "The number of training epochs"], 0),

            ("What does feature engineering involve?",
             ["Creating or transforming useful input variables", "Deleting the target variable", "Changing the programming language", "Removing the model"], 0),

            ("What is unsupervised learning?",
             ["Learning patterns from data without target labels", "Learning only from labelled data", "Learning without any data", "Learning only from reinforcement signals"], 0),
        ],

        "Deep Learning": [
            ("What is backpropagation used for?",
             ["Computing gradients to update neural network parameters", "Creating datasets", "Compressing images", "Choosing usernames"], 0),

            ("What does a learning rate control?",
             ["The step size of parameter updates", "The number of classes", "The dataset size", "The image resolution"], 0),

            ("Why are CNNs commonly useful for images?",
             ["They can learn spatial patterns using convolutional filters", "They only process text", "They require no training", "They remove all image information"], 0),

            ("What is dropout used for?",
             ["Reducing over-reliance on particular neurons during training", "Increasing the number of labels", "Creating datasets", "Removing the loss function"], 0),

            ("What does an optimizer do?",
             ["Updates model parameters to reduce the loss", "Creates the training labels", "Displays graphs only", "Stores images"], 0),

            ("What is a batch?",
             ["A subset of training examples processed together", "A neural network output", "A type of activation function", "A programming language"], 0),
        ],

        "Generative AI": [
            ("What is an embedding?",
             ["A numerical representation of information in a vector space", "A database password", "A Python loop", "A model license"], 0),

            ("What is RAG designed to combine?",
             ["Retrieval of relevant information with generation", "Two programming languages", "Two databases only", "Image compression and audio"], 0),

            ("Why are tokens important in LLMs?",
             ["They are the units processed by the language model", "They determine monitor size", "They replace GPUs", "They store user passwords"], 0),

            ("What does context window refer to?",
             ["The amount of input context a model can consider", "The size of a computer screen", "The model's training budget", "The number of GPUs"], 0),

            ("What is prompt engineering?",
             ["Designing inputs to guide model behavior", "Training a GPU", "Writing operating systems", "Compressing datasets"], 0),

            ("What is fine-tuning?",
             ["Further training a pretrained model on a targeted dataset", "Deleting the pretrained model", "Changing the GPU", "Removing tokens"], 0),
        ],
    },


    "Advanced": {

        "Python": [
            ("What is the key benefit of a generator compared with constructing a complete list?",
             ["It can produce values lazily and reduce memory usage", "It always runs faster", "It stores every value twice", "It removes the need for iteration"], 0),

            ("What does a Python decorator generally allow you to do?",
             ["Modify or extend callable behavior without changing its core definition", "Convert Python into C", "Delete a class", "Prevent all exceptions"], 0),

            ("Why can mutable default arguments cause unexpected behavior in Python functions?",
             ["The default object is created once and reused across calls", "Python copies it on every call", "Mutable objects cannot be passed to functions", "Defaults are always global variables"], 0),

            ("What is the purpose of __init__ in a typical Python class?",
             ["Initialize a newly created object's state", "Destroy the object", "Compile the class", "Import external modules"], 0),

            ("What is the primary role of an iterator's __next__ method?",
             ["Return the next available value or raise StopIteration", "Create a new class", "Sort a list", "Open a database"], 0),

            ("Why is vectorized NumPy computation often faster than explicit Python loops?",
             ["Many operations execute in optimized compiled numerical code", "Python loops are always parallel", "NumPy removes numerical operations", "NumPy stores no data"], 0),
        ],

        "Mathematics & Statistics": [
            ("Why is the gradient important in gradient-based optimization?",
             ["It indicates the direction of steepest local increase of a differentiable function", "It directly gives the global minimum", "It is always a probability", "It represents dataset size"], 0),

            ("What does covariance indicate?",
             ["How two variables vary together", "The exact causal effect of one variable", "The number of observations", "The median of both variables"], 0),

            ("Why can correlation not by itself establish causation?",
             ["Association can arise from confounding or other relationships without a causal mechanism", "Correlation only works on text", "Correlation is always zero", "Causation requires no data"], 0),

            ("What does an eigenvector represent for a matrix transformation?",
             ["A direction whose orientation is preserved up to scaling", "A guaranteed zero vector", "A probability distribution", "A dataset label"], 0),

            ("What is the purpose of a loss landscape in optimization?",
             ["It describes how the objective value changes across parameter values", "It stores training examples", "It replaces the optimizer", "It determines GPU memory"], 0),

            ("Why can standardization help gradient-based models?",
             ["Features on comparable scales can make optimization better conditioned", "It guarantees zero training error", "It removes the need for data", "It guarantees no overfitting"], 0),
        ],

        "Machine Learning": [
            ("Why does regularization often improve generalization?",
             ["It constrains model complexity and can reduce fitting to noise", "It always increases training accuracy", "It removes the training set", "It guarantees perfect predictions"], 0),

            ("What is data leakage?",
             ["Information unavailable at prediction time accidentally influences model training", "A missing dataset file", "A slow GPU", "A model with too few layers"], 0),

            ("Why can accuracy be misleading on a highly imbalanced dataset?",
             ["A model can achieve high accuracy by mostly predicting the majority class", "Accuracy cannot be calculated on classification", "Imbalanced data always gives 50% accuracy", "Accuracy measures regression only"], 0),

            ("What is cross-validation primarily used for?",
             ["Estimating model performance across multiple train-validation splits", "Increasing the number of labels", "Removing all features", "Replacing the test set permanently"], 0),

            ("What is the bias-variance tradeoff about?",
             ["Balancing systematic error from overly simple assumptions against sensitivity to training data", "Balancing CPU and RAM", "Choosing between Python and Java", "Selecting image resolution"], 0),

            ("Why should a final test set normally remain untouched during model selection?",
             ["Repeated use can leak information and make its estimate optimistic", "The test set cannot contain labels", "It is always smaller than training data", "Models cannot be evaluated twice"], 0),
        ],

        "Deep Learning": [
            ("Why can deep networks suffer from vanishing gradients?",
             ["Repeated multiplication through layers can make gradients become extremely small", "The dataset becomes empty", "The GPU stops storing weights", "The loss becomes a probability"], 0),

            ("What is the role of attention in Transformer architectures?",
             ["It lets representations weight relationships among tokens based on their relevance", "It removes all tokens", "It replaces the training data", "It guarantees factual outputs"], 0),

            ("Why are residual connections useful in deep networks?",
             ["They provide shorter paths for information and gradients through layers", "They eliminate all parameters", "They guarantee no overfitting", "They remove activation functions"], 0),

            ("What does batch normalization generally do?",
             ["Normalizes intermediate activations using batch statistics during training", "Removes all network layers", "Guarantees zero loss", "Creates labels automatically"], 0),

            ("Why can increasing model depth sometimes hurt performance?",
             ["Optimization difficulties and degradation can arise despite increased representational capacity", "More layers always reduce available data", "Deep networks cannot use gradients", "Depth prevents training completely"], 0),

            ("What is the main purpose of an attention mask in autoregressive language modeling?",
             ["Preventing a token from using information from future positions", "Removing all punctuation", "Increasing vocabulary size", "Changing the optimizer"], 0),
        ],

        "Generative AI": [
            ("Why can retrieval improve a generative AI system's factual grounding?",
             ["The model can condition generation on relevant external information", "Retrieval guarantees every answer is correct", "It eliminates the language model", "It prevents all hallucinations automatically"], 0),

            ("What is a key limitation of embeddings?",
             ["Similarity in vector space does not guarantee exact semantic or factual equivalence", "Embeddings can only represent numbers", "Embeddings cannot be stored", "Embeddings always contain the original document verbatim"], 0),

            ("Why can a larger context window still fail to produce a correct answer?",
             ["More available context does not guarantee correct retrieval, reasoning, or interpretation", "Context windows contain no text", "Large context prevents generation", "The model stops using tokens"], 0),

            ("What is the purpose of chunking in a RAG pipeline?",
             ["Breaking source material into retrievable units that can be indexed and retrieved", "Encrypting documents", "Training the GPU", "Deleting metadata"], 0),

            ("Why might fine-tuning be inappropriate when the main problem is access to changing factual information?",
             ["Fine-tuning does not inherently provide continuously updated external knowledge", "Fine-tuning cannot change model behavior", "Fine-tuning only works on images", "Fine-tuning removes the context window"], 0),

            ("What is temperature commonly used to control in text generation?",
             ["The randomness of token selection", "The GPU temperature", "The context-window size", "The embedding dimension"], 0),
        ],
    }
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
    else:
        return "Strong"


def make_diagnostic(level):
    """
    Select exactly 3 unique questions from each subject.
    Total = 15 questions.
    """

    selected = []

    for subject in SUBJECTS:

        bank = QUESTION_BANK[level][subject]

        # Randomly select 3 different questions.
        chosen = random.sample(bank, 3)

        for question, options, correct_index in chosen:
            selected.append({
                "subject": subject,
                "question": question,
                "options": options,
                "correct": correct_index
            })

    # Shuffle the complete 15-question test
    random.shuffle(selected)

    return selected


def calculate_scores():
    scores = {}

    for subject in SUBJECTS:

        subject_questions = [
            q for q in st.session_state.diagnostic_questions
            if q["subject"] == subject
        ]

        correct = 0

        for q_index, q in enumerate(st.session_state.diagnostic_questions):

            if q["subject"] != subject:
                continue

            answer = st.session_state.diagnostic_answers.get(q_index)

            if answer == q["correct"]:
                correct += 1

        total = len(subject_questions)

        if total > 0:
            scores[subject] = round((correct / total) * 100)
        else:
            scores[subject] = 0

    st.session_state.scores = scores

    if scores:
        st.session_state.overall_score = round(
            sum(scores.values()) / len(scores)
        )
    else:
        st.session_state.overall_score = 0


def start_diagnostic():
    level = st.session_state.profile["level"]

    st.session_state.diagnostic_questions = make_diagnostic(level)
    st.session_state.diagnostic_answers = {}

    st.session_state.page = "diagnostic"


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
                    alt="AI Learn logo"
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
        unsafe_allow_html=True
    )


# =========================================================
# HOME PAGE
# =========================================================

def home_page():

    render_header()

    # ---------------- HERO ----------------

    col1, col2 = st.columns([1.05, 0.95])

    with col1:

        st.markdown(
            """
            <div class="hero-section">

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

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="learning-visual">

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
            unsafe_allow_html=True
        )

    st.divider()

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

    st.write("")

    name = st.text_input(
        "Your Name",
        placeholder="Enter your name"
    )

    col1, col2 = st.columns(2)

    with col1:

        level = st.selectbox(
            "Current AI Level",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

    with col2:

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

    start_col1, start_col2, start_col3 = st.columns([1, 2, 1])

    with start_col2:

        start = st.button(
            "🚀 Start AI Journey",
            type="primary",
            use_container_width=True
        )

    if start:

        if not name.strip():

            st.warning("Please enter your name first.")

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
        unsafe_allow_html=True
    )

    foundation_cols = st.columns(5)

    foundations = [
        ("🐍", "Python"),
        ("📐", "Mathematics & Statistics"),
        ("🤖", "Machine Learning"),
        ("🧠", "Deep Learning"),
        ("✨", "Generative AI")
    ]

    for col, (icon, name_) in zip(foundation_cols, foundations):

        with col:

            st.markdown(
                f"""
                <div class="foundation-card">

                    <div class="foundation-icon">
                        {icon}
                    </div>

                    <div class="foundation-name">
                        {name_}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# DIAGNOSTIC PAGE
# =========================================================

def diagnostic_page():

    render_header()

    profile = st.session_state.profile

    st.markdown(
        f"""
        <div class="diagnostic-header">

            <div class="diagnostic-title">
                AI Diagnostic Assessment
            </div>

            <div class="diagnostic-subtitle">
                Hi {profile.get("name", "Learner")} 👋
                Answer all 15 questions to help AI Learn
                understand your current knowledge.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.info(
        f"Level selected: {profile.get('level', 'Beginner')} • "
        "3 questions from each of the 5 AI foundations."
    )

    questions = st.session_state.diagnostic_questions

    if not questions:

        st.error("No diagnostic questions found. Please return to Home.")

        if st.button("Go to Home"):
            st.session_state.page = "home"
            st.rerun()

        return

    # IMPORTANT:
    # Form prevents Streamlit from rerunning the page
    # after every radio selection.
    with st.form("diagnostic_form"):

        for index, q in enumerate(questions):

            st.markdown(
                f"""
                <div class="question-card">

                    <div class="question-number">
                        QUESTION {index + 1} OF 15
                    </div>

                    <div class="question-text">
                        {q["question"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            # No subject/topic is displayed here.
            answer = st.radio(
                "Select your answer:",
                q["options"],
                index=None,
                key=f"diagnostic_q_{index}",
                label_visibility="collapsed"
            )

            st.write("")

        submitted = st.form_submit_button(
            "✅ Submit Diagnostic",
            type="primary",
            use_container_width=True
        )

    if submitted:

        unanswered = []

        answers = {}

        for index, q in enumerate(questions):

            answer = st.session_state.get(
                f"diagnostic_q_{index}"
            )

            if answer is None:
                unanswered.append(index + 1)

            else:
                answers[index] = q["options"].index(answer)

        if unanswered:

            st.warning(
                "Please answer all 15 questions before submitting. "
                f"Missing question(s): {', '.join(map(str, unanswered))}"
            )

        else:

            # Store answers silently.
            st.session_state.diagnostic_answers = answers

            # Calculate scores only now.
            calculate_scores()

            # Move directly to Score Card.
            st.session_state.page = "score"

            st.rerun()


# =========================================================
# SCORE CARD
# =========================================================

def score_card_page():

    render_header()

    scores = st.session_state.scores
    overall = st.session_state.overall_score

    if not scores:

        st.warning("Please complete the diagnostic first.")

        if st.button("Go to Home"):

            st.session_state.page = "home"
            st.rerun()

        return

    st.markdown(
        f"""
        <div class="score-header">

            <div class="score-header-title">
                🎓 YOUR AI LEARNING SCORE CARD
            </div>

            <div class="overall-score">
                {overall}%
            </div>

            <div class="score-subtitle">
                Your current AI knowledge profile
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- SUBJECT SCORES ----------------

    for subject in SUBJECTS:

        score = scores.get(subject, 0)
        status = status_for_score(score)

        st.markdown(
            f"""
            <div class="subject-card">

                <div class="subject-name">
                    {subject}
                </div>

                <div class="score-number">
                    {score}%
                </div>

                <div style="
                    margin-top:10px;
                    height:10px;
                    background:#e9eef2;
                    border-radius:20px;
                    overflow:hidden;
                ">

                    <div style="
                        width:{score}%;
                        height:100%;
                        background:#19b889;
                        border-radius:20px;
                    "></div>

                </div>

                <div style="
                    margin-top:8px;
                    color:#687786;
                    font-size:14px;
                ">
                    Status: <strong>{status}</strong>
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------------- RECOMMENDATION ----------------

    weakest_subject = min(
        scores,
        key=scores.get
    )

    weakest_score = scores[weakest_subject]

    st.markdown(
        f"""
        <div class="recommendation">

            <div class="recommendation-title">
                🎯 Recommended Starting Point
            </div>

            <div style="
                font-size:24px;
                font-weight:800;
                color:#344454;
                margin-bottom:8px;
            ">
                {weakest_subject} — {weakest_score}%
            </div>

            <div style="
                color:#687786;
                line-height:1.5;
            ">
                AI Learn will prioritise this area in your
                personalised learning journey before moving
                you toward more advanced topics.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🗺️ View My Personalised Roadmap",
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

            level = st.session_state.profile.get(
                "level",
                "Beginner"
            )

            st.session_state.diagnostic_questions = make_diagnostic(
                level
            )

            st.session_state.diagnostic_answers = {}

            st.session_state.page = "diagnostic"

            st.rerun()


# =========================================================
# ROADMAP
# =========================================================

def roadmap_page():

    render_header()

    scores = st.session_state.scores

    if not scores:

        st.warning("Complete your diagnostic first.")

        return

    st.markdown(
        """
        <div class="diagnostic-header">

            <div class="diagnostic-title">
                🗺️ Your Personalised AI Roadmap
            </div>

            <div class="diagnostic-subtitle">
                Your roadmap starts with the areas that need
                the most attention and gradually moves upward.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    ordered_subjects = sorted(
        SUBJECTS,
        key=lambda subject: scores.get(subject, 0)
    )

    descriptions = {

        "Python":
            "Build programming fundamentals, data structures, functions, OOP, NumPy and Pandas.",

        "Mathematics & Statistics":
            "Strengthen statistics, probability, linear algebra, calculus and gradients.",

        "Machine Learning":
            "Learn supervised learning, unsupervised learning, preprocessing, evaluation and model improvement.",

        "Deep Learning":
            "Progress through neural networks, backpropagation, CNNs, sequence models and Transformers.",

        "Generative AI":
            "Learn LLMs, tokens, embeddings, prompting, RAG, fine-tuning concepts and modern generative AI."
    }

    for number, subject in enumerate(
        ordered_subjects,
        start=1
    ):

        score = scores.get(subject, 0)

        st.markdown(
            f"""
            <div class="roadmap-card">

                <div class="roadmap-number">
                    {number}
                </div>

                <div class="roadmap-title">
                    {subject}
                </div>

                <div class="roadmap-text">
                    Current score: <strong>{score}%</strong>
                    <br><br>
                    {descriptions[subject]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    if st.button(
        "← Back to Score Card",
        use_container_width=True
    ):

        st.session_state.page = "score"
        st.rerun()


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

with st.sidebar:

    st.markdown(
        """
        ## 🎓 AI Learn

        Your personalised AI learning journey.
        """
    )

    if st.button(
        "🏠 Home",
        use_container_width=True
    ):

        st.session_state.page = "home"
        st.rerun()

    if st.session_state.scores:

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
