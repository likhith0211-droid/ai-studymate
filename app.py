import streamlit as st
import random

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI StudyMate",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded",
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
    "diagnostic_index": 0,
    "scores": {},
    "roadmap": [],
}

for key, value in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# QUESTION BANK
# ============================================================
# Each question has:
# subject
# level
# question
# options
# answer -> correct option index
#
# The diagnostic uses 3 randomly selected questions per subject.
# ============================================================

QUESTION_BANK = [

    # ========================================================
    # PYTHON - BEGINNER
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
        "question": "Which function is commonly used to display output in Python?",
        "options": ["display()", "show()", "print()", "output()"],
        "answer": 2,
    },
    {
        "subject": "Python",
        "level": "Beginner",
        "question": "Which collection is ordered and changeable in Python?",
        "options": ["Tuple", "List", "Set", "Frozen set"],
        "answer": 1,
    },
    {
        "subject": "Python",
        "level": "Beginner",
        "question": "What is the result of 3 + 4 * 2 in Python?",
        "options": ["14", "11", "10", "9"],
        "answer": 1,
    },

    # ========================================================
    # PYTHON - INTERMEDIATE
    # ========================================================

    {
        "subject": "Python",
        "level": "Intermediate",
        "question": "What does a Python list comprehension primarily provide?",
        "options": [
            "A concise way to create lists",
            "A way to define classes",
            "A method for connecting databases",
            "A way to compile Python"
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Intermediate",
        "question": "What is the main purpose of a Python dictionary?",
        "options": [
            "Store values using key-value mappings",
            "Store only numbers",
            "Store only ordered strings",
            "Execute functions automatically"
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Intermediate",
        "question": "What does `len([10, 20, 30])` return?",
        "options": ["2", "3", "30", "60"],
        "answer": 1,
    },
    {
        "subject": "Python",
        "level": "Intermediate",
        "question": "What is the purpose of a function in Python?",
        "options": [
            "To group reusable logic",
            "To permanently store files",
            "To install packages",
            "To create an operating system"
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Intermediate",
        "question": "Which keyword is used to define a function?",
        "options": ["function", "define", "def", "func"],
        "answer": 2,
    },

    # ========================================================
    # PYTHON - ADVANCED
    # ========================================================

    {
        "subject": "Python",
        "level": "Advanced",
        "question": "What is the main purpose of a Python generator?",
        "options": [
            "To produce values lazily using iteration",
            "To automatically parallelize all code",
            "To convert Python into machine code",
            "To prevent all memory allocation"
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Advanced",
        "question": "What does a decorator generally allow you to do?",
        "options": [
            "Modify or extend function behavior",
            "Delete Python modules",
            "Convert lists into databases",
            "Disable exceptions"
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Advanced",
        "question": "Which concept allows a class to inherit behavior from another class?",
        "options": ["Encapsulation", "Inheritance", "Iteration", "Serialization"],
        "answer": 1,
    },
    {
        "subject": "Python",
        "level": "Advanced",
        "question": "What is the benefit of using a context manager with `with`?",
        "options": [
            "It helps manage setup and cleanup resources",
            "It automatically makes code asynchronous",
            "It prevents every possible exception",
            "It converts Python to C++"
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Advanced",
        "question": "What does `*args` allow in a Python function?",
        "options": [
            "An arbitrary number of positional arguments",
            "An arbitrary number of classes",
            "Only keyword arguments",
            "Only one required argument"
        ],
        "answer": 0,
    },

    # ========================================================
    # MATHEMATICS & STATISTICS - BEGINNER
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
            "The likelihood of an event",
            "The size of a dataset",
            "The average of values",
            "The number of features"
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
        "question": "What does the range of a dataset represent?",
        "options": [
            "Maximum minus minimum",
            "Mean divided by median",
            "Number of observations",
            "Average of all values"
        ],
        "answer": 0,
    },

    # ========================================================
    # MATHEMATICS & STATISTICS - INTERMEDIATE
    # ========================================================

    {
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What does variance measure?",
        "options": [
            "Spread of values around the mean",
            "The middle value",
            "The maximum value",
            "The number of features"
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What is the purpose of a correlation coefficient?",
        "options": [
            "Measure the strength and direction of a relationship",
            "Calculate a neural network layer",
            "Remove all outliers",
            "Count categorical variables"
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "If two events are independent, what is generally true?",
        "options": [
            "One event does not change the probability of the other",
            "They must always happen together",
            "Their probabilities must be equal",
            "Both events must have probability zero"
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What does standard deviation represent?",
        "options": [
            "A measure of data spread",
            "The dataset size",
            "The largest observation",
            "The number of classes"
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What is a normal distribution commonly characterized by?",
        "options": [
            "A bell-shaped symmetric distribution",
            "Only positive integer values",
            "A distribution with no mean",
            "A distribution containing only zeros"
        ],
        "answer": 0,
    },

    # ========================================================
    # MATHEMATICS & STATISTICS - ADVANCED
    # ========================================================

    {
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "Why is the gradient important in machine learning optimization?",
        "options": [
            "It indicates the direction of greatest increase of a function",
            "It directly labels training examples",
            "It removes categorical features",
            "It determines the number of rows in a dataset"
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "What does a covariance matrix describe?",
        "options": [
            "Variances and pairwise covariances among variables",
            "Only the mean of each variable",
            "Only class labels",
            "The number of neural network layers"
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "Why are eigenvectors useful in dimensionality reduction?",
        "options": [
            "They can identify important directions of variation",
            "They automatically create labels",
            "They replace every missing value",
            "They eliminate the need for training data"
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
            "Probability of a class",
            "Dataset size"
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "What is Bayes' theorem primarily used to calculate?",
        "options": [
            "A conditional probability using prior information",
            "The mean of a dataset",
            "The number of neural network neurons",
            "The dimensionality of an image"
        ],
        "answer": 0,
    },

    # ========================================================
    # MACHINE LEARNING - BEGINNER
    # ========================================================

    {
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "What is supervised learning?",
        "options": [
            "Learning from labelled examples",
            "Learning without any data",
            "Only clustering data",
            "Manually writing every prediction rule"
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "What is a training dataset used for?",
        "options": [
            "Teaching a model patterns from data",
            "Displaying the final website",
            "Deleting model parameters",
            "Writing documentation"
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "Which is an example of classification?",
        "options": [
            "Predicting whether an email is spam",
            "Predicting house price",
            "Grouping customers without labels",
            "Reducing image dimensions"
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "Which is an example of regression?",
        "options": [
            "Predicting a house price",
            "Detecting spam vs not spam",
            "Grouping similar customers",
            "Finding image edges"
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "Why do we evaluate a machine learning model?",
        "options": [
            "To measure how well it performs",
            "To increase the dataset size automatically",
            "To remove the need for training",
            "To turn all problems into classification"
        ],
        "answer": 0,
    },

    # ========================================================
    # MACHINE LEARNING - INTERMEDIATE
    # ========================================================

    {
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "What is overfitting?",
        "options": [
            "A model learns training data too specifically and generalizes poorly",
            "A model has no parameters",
            "A model has no training data",
            "A model always performs perfectly"
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "Why is a validation set useful?",
        "options": [
            "For evaluating choices during model development",
            "For permanently replacing training data",
            "For removing all features",
            "For converting regression into clustering"
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "What is feature scaling used for?",
        "options": [
            "Putting numerical features on comparable scales",
            "Adding labels to unlabeled data",
            "Deleting the target variable",
            "Increasing the number of classes"
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
            "Training only on labelled images",
            "Removing every numerical feature"
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "What is precision in classification?",
        "options": [
            "The proportion of predicted positives that are actually positive",
            "The proportion of all samples predicted correctly",
            "The proportion of actual positives detected",
            "The number of training examples"
        ],
        "answer": 0,
    },

    # ========================================================
    # MACHINE LEARNING - ADVANCED
    # ========================================================

    {
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "Why can data leakage produce misleadingly strong validation results?",
        "options": [
            "Information unavailable at prediction time has influenced model development",
            "The model has too few parameters",
            "The training dataset is always too small",
            "The model uses gradient descent"
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "What is the bias-variance tradeoff concerned with?",
        "options": [
            "Balancing underfitting and sensitivity to training data",
            "Choosing between Python and Java",
            "Increasing storage capacity",
            "Selecting a database engine"
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "Why might cross-validation be used?",
        "options": [
            "To estimate generalization performance across multiple data splits",
            "To guarantee zero test error",
            "To eliminate the target variable",
            "To make every model linear"
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "What does regularization generally encourage?",
        "options": [
            "Simpler model parameters to reduce overfitting",
            "More training labels",
            "Larger datasets automatically",
            "Removal of the validation set"
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "Why is class imbalance important in classification?",
        "options": [
            "Accuracy can hide poor performance on minority classes",
            "It always makes training impossible",
            "It guarantees overfitting",
            "It removes the need for evaluation metrics"
        ],
        "answer": 0,
    },

    # ========================================================
    # DEEP LEARNING - BEGINNER
    # ========================================================

    {
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What is a neural network?",
        "options": [
            "A model made of interconnected computational units",
            "A database table",
            "A programming language",
            "A file compression format"
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What is an activation function used for?",
        "options": [
            "Introducing nonlinear behavior into a neural network",
            "Storing datasets",
            "Deleting model weights",
            "Downloading Python"
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What is an epoch?",
        "options": [
            "One complete pass through the training dataset",
            "One feature in a dataset",
            "One neuron",
            "One test example"
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
            "Class labels only",
            "Python packages"
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What is a loss function used for?",
        "options": [
            "Measuring how far predictions are from desired outputs",
            "Increasing image resolution",
            "Creating database tables",
            "Removing all parameters"
        ],
        "answer": 0,
    },

    # ========================================================
    # DEEP LEARNING - INTERMEDIATE
    # ========================================================

    {
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What is backpropagation used for?",
        "options": [
            "Computing gradients used to update network parameters",
            "Creating training labels",
            "Compressing images",
            "Selecting database rows"
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What does a convolutional neural network commonly excel at?",
        "options": [
            "Learning spatial patterns in data such as images",
            "Managing operating system processes",
            "Writing SQL queries",
            "Sorting Python lists"
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What is the purpose of an optimizer?",
        "options": [
            "Update model parameters using information from gradients",
            "Create new labels",
            "Remove the loss function",
            "Store images permanently"
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "Why can ReLU help deep networks?",
        "options": [
            "It provides a simple nonlinear activation and can help gradient flow",
            "It removes all neurons",
            "It guarantees no overfitting",
            "It converts images into labels"
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What is dropout commonly used for?",
        "options": [
            "Reducing over-reliance on particular neurons during training",
            "Increasing the number of labels",
            "Replacing the optimizer",
            "Converting regression to classification"
        ],
        "answer": 0,
    },

    # ========================================================
    # DEEP LEARNING - ADVANCED
    # ========================================================

    {
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "Why can very deep networks suffer from vanishing gradients?",
        "options": [
            "Gradients can become extremely small as they propagate backward",
            "The dataset contains too many rows",
            "The optimizer always increases gradients",
            "Neural networks cannot use activation functions"
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "What is the key idea behind residual connections?",
        "options": [
            "Allow layers to learn a residual transformation while providing a shortcut path",
            "Remove all nonlinearities",
            "Prevent training entirely",
            "Replace every convolution with pooling"
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "What does batch normalization primarily do?",
        "options": [
            "Normalizes activations within training batches",
            "Creates new training examples",
            "Deletes network parameters",
            "Converts classification into clustering"
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "Why are attention mechanisms useful in sequence modeling?",
        "options": [
            "They allow the model to weight different parts of the input when producing an output",
            "They eliminate all parameters",
            "They only work with numerical tables",
            "They guarantee perfect predictions"
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "What is the purpose of a learning rate?",
        "options": [
            "Control the size of parameter updates during optimization",
            "Determine the number of training examples",
            "Set the number of classes automatically",
            "Measure model accuracy"
        ],
        "answer": 0,
    },

    # ========================================================
    # GENERATIVE AI - BEGINNER
    # ========================================================

    {
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What is Generative AI designed to do?",
        "options": [
            "Generate new content based on learned patterns",
            "Only store files",
            "Only calculate averages",
            "Only sort data"
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
            "Language Learning Method"
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What is a prompt?",
        "options": [
            "Instructions or input given to an AI model",
            "A model's database",
            "A hardware component",
            "A Python compiler"
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What can a text-generating AI model produce?",
        "options": [
            "Text based on its learned patterns and instructions",
            "Only numerical spreadsheets",
            "Only computer hardware",
            "Only database indexes"
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
            "A programming language"
        ],
        "answer": 0,
    },

    # ========================================================
    # GENERATIVE AI - INTERMEDIATE
    # ========================================================

    {
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "What are tokens in language models?",
        "options": [
            "Units of text processed by the model",
            "Database passwords",
            "Training computers",
            "Neural network layers"
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "What is an embedding?",
        "options": [
            "A numerical representation of information in a vector space",
            "A type of database password",
            "A hardware component",
            "A Python exception"
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "What is RAG?",
        "options": [
            "Retrieval-Augmented Generation",
            "Random AI Generation",
            "Recursive Answer Generator",
            "Rapid Automated Grading"
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "Why can RAG be useful?",
        "options": [
            "It can provide a model with relevant retrieved information",
            "It removes the need for any data",
            "It guarantees every generated answer is correct",
            "It replaces all neural networks"
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "What does temperature commonly control in text generation?",
        "options": [
            "The randomness of token selection",
            "The model's memory size",
            "The number of training examples",
            "The number of GPUs"
        ],
        "answer": 0,
    },

    # ========================================================
    # GENERATIVE AI - ADVANCED
    # ========================================================

    {
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "What is the central idea of self-attention in Transformers?",
        "options": [
            "Each token can assign different importance to other tokens when forming representations",
            "Every token must be treated identically",
            "The model removes token order entirely",
            "The model only processes one token in total"
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "Why are vector embeddings useful for semantic search?",
        "options": [
            "Semantically related items can be represented near each other in vector space",
            "They guarantee factual correctness",
            "They eliminate the need for documents",
            "They directly produce human-readable answers"
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
            "Replacing tokenization"
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "What is a hallucination in an LLM?",
        "options": [
            "A generated response that presents unsupported or incorrect information",
            "A GPU hardware failure",
            "A training dataset format",
            "A tokenization algorithm"
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "Why does context-window size matter for an LLM application?",
        "options": [
            "It limits how much input context the model can process in one interaction",
            "It determines the model's physical memory chip",
            "It guarantees factual accuracy",
            "It determines the number of users"
        ],
        "answer": 0,
    },
]


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_status(score):
    """Return a learner-friendly status based on score."""

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
    Create exactly 3 random questions for each subject
    based on the learner's selected level.
    """

    selected_questions = []

    for subject in SUBJECTS:

        available = [
            q
            for q in QUESTION_BANK
            if q["subject"] == subject
            and q["level"] == level
        ]

        selected = random.sample(
            available,
            min(3, len(available))
        )

        # Randomize answer choices while preserving correct answer.
        for question in selected:

            original_options = question["options"]
            original_answer = question["answer"]

            option_pairs = [
                (option, index == original_answer)
                for index, option in enumerate(original_options)
            ]

            random.shuffle(option_pairs)

            new_options = [
                item[0]
                for item in option_pairs
            ]

            new_answer = next(
                index
                for index, item in enumerate(option_pairs)
                if item[1]
            )

            selected_questions.append(
                {
                    "subject": question["subject"],
                    "level": question["level"],
                    "question": question["question"],
                    "options": new_options,
                    "answer": new_answer,
                }
            )

    random.shuffle(selected_questions)

    return selected_questions


def calculate_scores():

    scores = {}

    for subject in SUBJECTS:

        subject_questions = [
            q
            for q in st.session_state.diagnostic_questions
            if q["subject"] == subject
        ]

        correct = 0

        for question, selected_answer in zip(
            st.session_state.diagnostic_questions,
            st.session_state.diagnostic_answers
        ):

            if (
                question["subject"] == subject
                and selected_answer == question["answer"]
            ):
                correct += 1

        if subject_questions:
            score = round(
                (correct / len(subject_questions)) * 100
            )
        else:
            score = 0

        scores[subject] = score

    return scores


def create_roadmap(scores):

    sorted_subjects = sorted(
        scores.items(),
        key=lambda item: item[1]
    )

    roadmap = []

    for position, (subject, score) in enumerate(sorted_subjects):

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
# HOME PAGE
# ============================================================

def home_page():

    # --------------------------------------------------------
    # HERO
    # --------------------------------------------------------

    st.markdown(
        "<div style='text-align:center; font-size:58px;'>🎓</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1 style='text-align:center; margin-bottom:4px;'>AI StudyMate</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center; font-size:20px; margin-top:0;'>"
        "Personalised AI Tutor for Learning AI"
        "</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center; font-size:16px;'>"
        "Learn AI through a personalised learning journey "
        "designed around your current knowledge and goals."
        "</p>",
        unsafe_allow_html=True
    )

    st.divider()

    # --------------------------------------------------------
    # PROFILE
    # --------------------------------------------------------

    st.subheader("👤 Tell us about yourself")

    name = st.text_input(
        "Your Name",
        value=st.session_state.profile.get("name", ""),
        placeholder="Enter your name"
    )

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

    # --------------------------------------------------------
    # START BUTTON
    # --------------------------------------------------------

    if st.button(
        "🚀 Start AI Journey",
        use_container_width=True,
        type="primary"
    ):

        if not name.strip():

            st.warning(
                "Please enter your name before starting."
            )
            return

        st.session_state.profile = {
            "name": name.strip(),
            "level": level,
            "goal": goal,
            "study_time": study_time,
        }

        # Create fresh diagnostic
        st.session_state.diagnostic_questions = (
            create_diagnostic(level)
        )

        st.session_state.diagnostic_answers = []

        st.session_state.diagnostic_index = 0

        st.session_state.scores = {}

        st.session_state.roadmap = []

        st.session_state.page = "diagnostic"

        st.rerun()


# ============================================================
# DIAGNOSTIC PAGE
# ============================================================

def diagnostic_page():

    questions = st.session_state.diagnostic_questions

    total_questions = len(questions)

    current_index = st.session_state.diagnostic_index

    # Safety check
    if not questions:

        st.session_state.page = "home"
        st.rerun()
        return

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.title("🧠 AI Knowledge Diagnostic")

    st.write(
        f"Hello **{st.session_state.profile.get('name', 'Learner')}**!"
    )

    st.write(
        "This diagnostic will help AI StudyMate understand "
        "your current knowledge and create your personalised roadmap."
    )

    st.info(
        f"Your selected level: **{st.session_state.profile.get('level', 'Beginner')}**"
    )

    # --------------------------------------------------------
    # PROGRESS
    # --------------------------------------------------------

    progress = current_index / total_questions

    st.progress(progress)

    st.caption(
        f"Question {current_index + 1} of {total_questions}"
    )

    # --------------------------------------------------------
    # CURRENT QUESTION
    # --------------------------------------------------------

    current_question = questions[current_index]

    st.markdown(
        f"### {current_question['subject']}"
    )

    st.markdown(
        f"**{current_question['question']}**"
    )

    # --------------------------------------------------------
    # ANSWER
    # --------------------------------------------------------

    answer = st.radio(
        "Select your answer:",
        current_question["options"],
        key=f"diagnostic_answer_{current_index}",
        index=None,
    )

    st.write("")

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    if st.button(
        "Next Question →",
        use_container_width=True,
        type="primary"
    ):

        if answer is None:

            st.warning(
                "Please select an answer before continuing."
            )

            return

        selected_answer_index = (
            current_question["options"].index(answer)
        )

        st.session_state.diagnostic_answers.append(
            selected_answer_index
        )

        # ----------------------------------------------------
        # MORE QUESTIONS
        # ----------------------------------------------------

        if current_index < total_questions - 1:

            st.session_state.diagnostic_index += 1

            st.rerun()

        # ----------------------------------------------------
        # DIAGNOSTIC COMPLETE
        # ----------------------------------------------------

        else:

            scores = calculate_scores()

            st.session_state.scores = scores

            st.session_state.roadmap = create_roadmap(
                scores
            )

            st.session_state.page = "score_card"

            st.rerun()


# ============================================================
# SCORE CARD PAGE
# ============================================================

def score_card_page():

    scores = st.session_state.scores

    if not scores:

        st.session_state.page = "home"
        st.rerun()
        return

    # --------------------------------------------------------
    # CALCULATE OVERALL
    # --------------------------------------------------------

    overall_score = round(
        sum(scores.values()) / len(scores)
    )

    weakest_subject = min(
        scores,
        key=scores.get
    )

    weakest_score = scores[weakest_subject]

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.markdown(
        "<div style='text-align:center;'>"
        "<div style='font-size:48px;'>🎓</div>"
        "<h1>Your AI Learning Score Card</h1>"
        "<p>Here is your current AI knowledge profile.</p>"
        "</div>",
        unsafe_allow_html=True
    )

    st.divider()

    # --------------------------------------------------------
    # OVERALL SCORE
    # --------------------------------------------------------

    st.markdown(
        "<div style='text-align:center;'>"
        "<p style='font-size:18px;'>Overall Score</p>"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<h1 style='text-align:center; font-size:64px;'>"
        f"{overall_score}%"
        f"</h1>",
        unsafe_allow_html=True
    )

    st.divider()

    # --------------------------------------------------------
    # SUBJECT SCORES
    # --------------------------------------------------------

    st.subheader("📚 Subject Scores")

    for subject in SUBJECTS:

        score = scores.get(subject, 0)

        status = get_status(score)

        st.markdown(
            f"**{subject}**"
        )

        st.progress(
            score / 100
        )

        st.caption(
            f"{score}%  •  {status}"
        )

        st.write("")

    # --------------------------------------------------------
    # RECOMMENDED STARTING POINT
    # --------------------------------------------------------

    st.divider()

    st.subheader("🎯 Recommended Starting Point")

    st.markdown(
        f"### {weakest_subject} — {weakest_score}%"
    )

    if weakest_score < 40:

        st.write(
            f"Build your foundation in **{weakest_subject}** "
            "before moving into more advanced topics."
        )

    elif weakest_score < 70:

        st.write(
            f"Strengthen your **{weakest_subject}** skills "
            "with focused lessons and practice."
        )

    else:

        st.write(
            f"You have a solid foundation in **{weakest_subject}**. "
            "Continue with targeted practice to strengthen mastery."
        )

    # --------------------------------------------------------
    # PROFILE SUMMARY
    # --------------------------------------------------------

    st.divider()

    st.subheader("👤 Your Learning Profile")

    profile = st.session_state.profile

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "AI Level",
            profile.get("level", "Beginner")
        )

        st.metric(
            "Daily Study Time",
            profile.get("study_time", "30 minutes")
        )

    with col2:

        st.metric(
            "Learning Goal",
            profile.get(
                "goal",
                "Learn AI fundamentals"
            )
        )

        st.metric(
            "Subjects Assessed",
            "5"
        )

    st.write("")

    # --------------------------------------------------------
    # ACTION BUTTONS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🗺️ View Personalised Roadmap",
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

            level = profile.get(
                "level",
                "Beginner"
            )

            st.session_state.diagnostic_questions = (
                create_diagnostic(level)
            )

            st.session_state.diagnostic_answers = []

            st.session_state.diagnostic_index = 0

            st.session_state.scores = {}

            st.session_state.roadmap = []

            st.session_state.page = "diagnostic"

            st.rerun()


# ============================================================
# ROADMAP PAGE
# ============================================================

def roadmap_page():

    scores = st.session_state.scores

    if not scores:

        st.session_state.page = "home"
        st.rerun()
        return

    st.title("🗺️ Your Personalised AI Roadmap")

    st.write(
        "AI StudyMate has ordered your learning journey "
        "from areas that need the most attention to areas "
        "where you already have stronger knowledge."
    )

    st.divider()

    roadmap = st.session_state.roadmap

    # --------------------------------------------------------
    # ROADMAP
    # --------------------------------------------------------

    for index, item in enumerate(roadmap):

        subject = item["subject"]
        score = item["score"]
        priority = item["priority"]

        st.markdown(
            f"### {index + 1}. {subject}"
        )

        st.progress(
            score / 100
        )

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"Current score: **{score}%**"
            )

        with col2:

            st.write(
                f"Priority: **{priority}**"
            )

        # ----------------------------------------------------
        # LEARNING RECOMMENDATION
        # ----------------------------------------------------

        if score < 40:

            recommendation = (
                "Start with the fundamentals. "
                "Focus on concepts, terminology, simple examples, "
                "and guided practice."
            )

        elif score < 70:

            recommendation = (
                "Build stronger understanding through intermediate "
                "concepts, worked examples, and practice questions."
            )

        else:

            recommendation = (
                "Continue toward advanced concepts, projects, "
                "and application-based practice."
            )

        st.info(
            recommendation
        )

        st.divider()

    # --------------------------------------------------------
    # NEXT STEP
    # --------------------------------------------------------

    st.subheader("🚀 Next Step")

    st.write(
        f"Your first recommended learning area is "
        f"**{roadmap[0]['subject']}**."
    )

    st.write(
        "The next version of AI StudyMate will turn this roadmap "
        "into adaptive lessons, practice tasks, and mastery tracking."
    )

    if st.button(
        "🏠 Back to Home",
        use_container_width=True
    ):

        st.session_state.page = "home"

        st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## 🎓 AI StudyMate"
    )

    st.caption(
        "Personalised AI Tutor for Learning AI"
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
        disabled=not bool(st.session_state.scores)
    ):

        st.session_state.page = "score_card"

        st.rerun()

    if st.button(
        "🗺️ Roadmap",
        use_container_width=True,
        disabled=not bool(st.session_state.scores)
    ):

        st.session_state.page = "roadmap"

        st.rerun()

    st.divider()

    st.caption(
        "AI StudyMate helps learners discover what they know, "
        "identify knowledge gaps, and follow a personalised "
        "AI learning journey."
    )


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
