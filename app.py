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
    "scores": {},
    "roadmap": [],
}

for key, value in DEFAULT_STATE.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# QUESTION BANK
# ============================================================
#
# Each level contains multiple questions.
#
# During a diagnostic:
#   5 subjects
#   × 3 questions
#   = 15 questions
#
# Questions are selected randomly without duplication.
# Answer choices are also shuffled.
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
    {
        "subject": "Python",
        "level": "Beginner",
        "question": "Which keyword is used to create a conditional statement?",
        "options": ["if", "when", "check", "condition"],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Beginner",
        "question": "Which of these is a valid Python string?",
        "options": ["Hello", '"Hello"', "{Hello}", "[Hello]"],
        "answer": 1,
    },
    {
        "subject": "Python",
        "level": "Beginner",
        "question": "Which operator is used for multiplication in Python?",
        "options": ["x", "*", "%", "^"],
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
            "A way to compile Python",
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
            "Execute functions automatically",
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
        "question": "What is the purpose of a function in Python?",
        "options": [
            "To group reusable logic",
            "To permanently store files",
            "To install packages",
            "To create an operating system",
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
    {
        "subject": "Python",
        "level": "Intermediate",
        "question": "What does a tuple differ from a list mainly by?",
        "options": [
            "A tuple is immutable",
            "A tuple can only contain numbers",
            "A tuple cannot be indexed",
            "A tuple cannot contain strings",
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Intermediate",
        "question": "What is exception handling used for?",
        "options": [
            "Handling errors during program execution",
            "Making code execute twice",
            "Creating variables automatically",
            "Removing functions",
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Intermediate",
        "question": "Which keyword is commonly used to iterate over items in a sequence?",
        "options": ["loop", "for", "repeat", "iterate"],
        "answer": 1,
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
            "To prevent all memory allocation",
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
            "Disable exceptions",
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Advanced",
        "question": "Which concept allows a class to inherit behavior from another class?",
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
        "question": "What is the benefit of using a context manager with with?",
        "options": [
            "It helps manage setup and cleanup resources",
            "It automatically makes code asynchronous",
            "It prevents every possible exception",
            "It converts Python to C++",
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Advanced",
        "question": "What does *args allow in a Python function?",
        "options": [
            "An arbitrary number of positional arguments",
            "An arbitrary number of classes",
            "Only keyword arguments",
            "Only one required argument",
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Advanced",
        "question": "What does **kwargs allow a function to receive?",
        "options": [
            "An arbitrary number of keyword arguments",
            "Only positional arguments",
            "Only integers",
            "Only one dictionary",
        ],
        "answer": 0,
    },
    {
        "subject": "Python",
        "level": "Advanced",
        "question": "What is the primary purpose of a virtual environment?",
        "options": [
            "Isolate project dependencies",
            "Increase CPU speed",
            "Replace Python",
            "Automatically debug every program",
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
            "The number of features",
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
            "Average of all values",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Beginner",
        "question": "What is the probability of a certain event?",
        "options": ["0", "0.5", "1", "10"],
        "answer": 2,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Beginner",
        "question": "What is the median of 1, 3, 5?",
        "options": ["1", "3", "4", "5"],
        "answer": 1,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Beginner",
        "question": "What is the sum of 5 and 7?",
        "options": ["10", "11", "12", "13"],
        "answer": 2,
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
            "The number of features",
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
            "Count categorical variables",
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
            "Both events must have probability zero",
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
            "The number of classes",
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
            "A distribution containing only zeros",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What does a negative correlation indicate?",
        "options": [
            "As one variable tends to increase, the other tends to decrease",
            "Both variables always increase",
            "The variables are identical",
            "There is no variation",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Intermediate",
        "question": "What is a sample in statistics?",
        "options": [
            "A subset of a population",
            "The entire universe of data",
            "A mathematical constant",
            "A neural network layer",
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
            "It determines the number of rows in a dataset",
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
            "The number of neural network layers",
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
            "They eliminate the need for training data",
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
            "Dataset size",
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
            "The dimensionality of an image",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "What does a p-value help assess in hypothesis testing?",
        "options": [
            "How compatible the observed data are with a null hypothesis",
            "The size of a neural network",
            "The number of training epochs",
            "The number of features in a dataset",
        ],
        "answer": 0,
    },
    {
        "subject": "Mathematics & Statistics",
        "level": "Advanced",
        "question": "What is the purpose of a gradient descent algorithm?",
        "options": [
            "Iteratively move parameters toward lower objective values",
            "Generate labels automatically",
            "Remove all training data",
            "Increase the number of features",
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
            "Manually writing every prediction rule",
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
            "Writing documentation",
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
            "Reducing image dimensions",
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
            "Finding image edges",
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
            "To turn all problems into classification",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "What is a feature in a machine learning dataset?",
        "options": [
            "An input variable used by a model",
            "The final prediction only",
            "The model's filename",
            "The training computer",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Beginner",
        "question": "What is the target variable?",
        "options": [
            "The value a supervised model attempts to predict",
            "A database password",
            "A feature scaling method",
            "A programming language",
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
            "A model always performs perfectly",
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
            "For converting regression into clustering",
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
            "Increasing the number of classes",
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
            "Removing every numerical feature",
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
            "The number of training examples",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "What is recall?",
        "options": [
            "The proportion of actual positives correctly identified",
            "The proportion of predicted positives that are correct",
            "The number of model parameters",
            "The size of the training dataset",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Intermediate",
        "question": "Why is a test set kept separate?",
        "options": [
            "To estimate performance on unseen data after development",
            "To train the model twice",
            "To remove all features",
            "To replace the validation process",
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
            "Choosing between Python and Java",
            "Increasing storage capacity",
            "Selecting a database engine",
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
            "To make every model linear",
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
            "Removal of the validation set",
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
            "It removes the need for evaluation metrics",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "What is the main purpose of a confusion matrix?",
        "options": [
            "Summarize classification outcomes by predicted and actual classes",
            "Calculate neural network gradients",
            "Store training data",
            "Scale numerical features",
        ],
        "answer": 0,
    },
    {
        "subject": "Machine Learning",
        "level": "Advanced",
        "question": "Why should preprocessing be fitted only on training data in many workflows?",
        "options": [
            "To avoid information from evaluation data leaking into training",
            "To increase the number of labels",
            "To guarantee perfect accuracy",
            "To remove the target variable",
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
            "A file compression format",
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
            "One feature in a dataset",
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
            "Class labels only",
            "Python packages",
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
            "Removing all parameters",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What is a neuron in a neural network?",
        "options": [
            "A computational unit that transforms inputs",
            "A database record",
            "A training dataset",
            "A programming language",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Beginner",
        "question": "What does training a neural network mean?",
        "options": [
            "Adjusting its parameters using data",
            "Writing every output manually",
            "Deleting its weights",
            "Converting it into a database",
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
            "Selecting database rows",
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
            "Sorting Python lists",
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
            "Store images permanently",
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
            "Increasing the number of labels",
            "Replacing the optimizer",
            "Converting regression to classification",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What does pooling commonly do in CNNs?",
        "options": [
            "Reduce spatial dimensions while retaining useful information",
            "Increase the number of classes",
            "Generate training labels",
            "Replace the loss function",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Intermediate",
        "question": "What is a batch in neural network training?",
        "options": [
            "A subset of training examples processed together",
            "The entire model architecture",
            "A single neuron",
            "The final prediction",
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
            "Neural networks cannot use activation functions",
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
            "Replace every convolution with pooling",
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
            "Converts classification into clustering",
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
            "They guarantee perfect predictions",
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
            "Measure model accuracy",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "Why can an excessively large learning rate be problematic?",
        "options": [
            "Updates may overshoot useful parameter values and prevent stable optimization",
            "It always reduces dataset size",
            "It removes all model parameters",
            "It guarantees underfitting",
        ],
        "answer": 0,
    },
    {
        "subject": "Deep Learning",
        "level": "Advanced",
        "question": "What is transfer learning?",
        "options": [
            "Using knowledge from a pretrained model for another task",
            "Moving a model between databases",
            "Copying labels into the test set",
            "Changing Python versions",
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
            "A model's database",
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
            "Text based on its learned patterns and instructions",
            "Only numerical spreadsheets",
            "Only computer hardware",
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
        "level": "Beginner",
        "question": "Which type of content can Generative AI create?",
        "options": [
            "Text, images, audio, or other content",
            "Only spreadsheets",
            "Only passwords",
            "Only computer processors",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Beginner",
        "question": "What is an AI model?",
        "options": [
            "A learned computational system that can process inputs and produce outputs",
            "Only a physical robot",
            "A spreadsheet",
            "A web browser",
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
            "Neural network layers",
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
            "A Python exception",
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
            "Rapid Automated Grading",
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
            "It replaces all neural networks",
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
            "The number of GPUs",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "What is prompt engineering?",
        "options": [
            "Designing instructions to guide an AI model toward useful outputs",
            "Training a GPU",
            "Creating a database",
            "Replacing model parameters manually",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Intermediate",
        "question": "Why are embeddings useful in retrieval systems?",
        "options": [
            "They allow information to be compared using vector similarity",
            "They guarantee factual accuracy",
            "They remove all documents",
            "They replace the language model",
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
            "The model only processes one token in total",
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
            "They directly produce human-readable answers",
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
        "question": "What is a hallucination in an LLM?",
        "options": [
            "A generated response that presents unsupported or incorrect information",
            "A GPU hardware failure",
            "A training dataset format",
            "A tokenization algorithm",
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
            "It determines the number of users",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "What is a key limitation of RAG?",
        "options": [
            "Poor retrieval can lead to poor or irrelevant context for generation",
            "RAG cannot use documents",
            "RAG always requires model retraining",
            "RAG only works with numerical data",
        ],
        "answer": 0,
    },
    {
        "subject": "Generative AI",
        "level": "Advanced",
        "question": "What is a vector database commonly used for in GenAI applications?",
        "options": [
            "Storing and searching vector representations efficiently",
            "Training GPUs",
            "Replacing all language models",
            "Generating HTML automatically",
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
    else:
        return "Strong"


def prepare_question(question):
    """
    Make a fresh copy of a question and randomize
    its answer choices without losing the correct answer.
    """

    option_pairs = []

    for index, option in enumerate(question["options"]):
        option_pairs.append(
            (
                option,
                index == question["answer"]
            )
        )

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

    return {
        "subject": question["subject"],
        "level": question["level"],
        "question": question["question"],
        "options": new_options,
        "answer": new_answer,
    }


def create_diagnostic(level):
    """
    Create exactly 15 unique questions:
        3 Python
        3 Mathematics & Statistics
        3 Machine Learning
        3 Deep Learning
        3 Generative AI

    Questions are randomly selected from the chosen
    difficulty level.
    """

    selected_questions = []

    for subject in SUBJECTS:

        available_questions = [
            question
            for question in QUESTION_BANK
            if question["subject"] == subject
            and question["level"] == level
        ]

        # Safety check
        if len(available_questions) < 3:
            raise ValueError(
                f"Not enough questions available for {subject} "
                f"at {level} level."
            )

        # random.sample guarantees no duplicate question
        # within this diagnostic.
        selected = random.sample(
            available_questions,
            3
        )

        for question in selected:
            selected_questions.append(
                prepare_question(question)
            )

    # Randomize order of the 15 questions.
    random.shuffle(selected_questions)

    return selected_questions


def calculate_scores():

    scores = {
        subject: 0
        for subject in SUBJECTS
    }

    totals = {
        subject: 0
        for subject in SUBJECTS
    }

    for question, selected_answer in zip(
        st.session_state.diagnostic_questions,
        st.session_state.diagnostic_answers
    ):

        subject = question["subject"]

        totals[subject] += 1

        if selected_answer == question["answer"]:
            scores[subject] += 1

    final_scores = {}

    for subject in SUBJECTS:

        if totals[subject] > 0:

            final_scores[subject] = round(
                (
                    scores[subject]
                    / totals[subject]
                )
                * 100
            )

        else:

            final_scores[subject] = 0

    return final_scores


def create_roadmap(scores):

    sorted_subjects = sorted(
        scores.items(),
        key=lambda item: item[1]
    )

    roadmap = []

    for position, item in enumerate(sorted_subjects):

        subject = item[0]
        score = item[1]

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
        "<h1 style='text-align:center; margin-bottom:4px;'>"
        "AI StudyMate"
        "</h1>",
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
        ],
        index=[
            "Beginner",
            "Intermediate",
            "Advanced",
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
    # START
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

        # Create a completely new diagnostic.
        st.session_state.diagnostic_questions = (
            create_diagnostic(level)
        )

        st.session_state.diagnostic_answers = []

        st.session_state.scores = {}

        st.session_state.roadmap = []

        st.session_state.page = "diagnostic"

        st.rerun()


# ============================================================
# DIAGNOSTIC PAGE
# ============================================================

def diagnostic_page():

    questions = st.session_state.diagnostic_questions

    if not questions:

        st.session_state.page = "home"

        st.rerun()

        return

    total_questions = len(questions)

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.title("🧠 AI Knowledge Diagnostic")

    learner_name = st.session_state.profile.get(
        "name",
        "Learner"
    )

    learner_level = st.session_state.profile.get(
        "level",
        "Beginner"
    )

    st.write(
        f"Hello **{learner_name}**!"
    )

    st.write(
        "Answer all 15 questions based on your current "
        "knowledge. Your answers will be evaluated only "
        "after you submit the diagnostic."
    )

    st.info(
        f"Current AI level: **{learner_level}**"
    )

    # --------------------------------------------------------
    # PROGRESS
    # --------------------------------------------------------

    st.progress(0.0)

    st.caption(
        "15 questions • 3 questions from each learning area"
    )

    st.divider()

    # --------------------------------------------------------
    # ANSWERS
    # --------------------------------------------------------

    answers = {}

    # --------------------------------------------------------
    # ALL 15 QUESTIONS
    # --------------------------------------------------------

    for index, question in enumerate(questions):

        question_number = index + 1

        # IMPORTANT:
        # We deliberately DO NOT display the subject here.
        # The learner sees only Question 1, Question 2, etc.

        st.markdown(
            f"### Question {question_number}"
        )

        st.write(
            question["question"]
        )

        selected_answer = st.radio(
            "Select one answer:",
            question["options"],
            key=f"diagnostic_question_{index}",
            index=None,
        )

        answers[index] = selected_answer

        if question_number < total_questions:
            st.divider()

    # --------------------------------------------------------
    # SUBMIT SECTION
    # --------------------------------------------------------

    st.divider()

    st.subheader("🎯 Ready to submit?")

    st.write(
        "Review your answers and submit the diagnostic. "
        "Your personalised score card will be generated "
        "after submission."
    )

    if st.button(
        "🎯 Submit Diagnostic",
        use_container_width=True,
        type="primary"
    ):

        # ----------------------------------------------------
        # FIND UNANSWERED QUESTIONS
        # ----------------------------------------------------

        unanswered = [
            index + 1
            for index, answer in answers.items()
            if answer is None
        ]

        if unanswered:

            question_numbers = ", ".join(
                str(number)
                for number in unanswered
            )

            st.warning(
                f"Please answer question(s): "
                f"{question_numbers}"
            )

            return

        # ----------------------------------------------------
        # CONVERT SELECTED OPTIONS TO ANSWER INDEXES
        # ----------------------------------------------------

        final_answers = []

        for index, question in enumerate(questions):

            selected_answer = answers[index]

            selected_answer_index = (
                question["options"].index(
                    selected_answer
                )
            )

            final_answers.append(
                selected_answer_index
            )

        st.session_state.diagnostic_answers = (
            final_answers
        )

        # ----------------------------------------------------
        # CALCULATE SCORE
        # ----------------------------------------------------

        scores = calculate_scores()

        st.session_state.scores = scores

        # ----------------------------------------------------
        # CREATE ROADMAP
        # ----------------------------------------------------

        st.session_state.roadmap = create_roadmap(
            scores
        )

        # ----------------------------------------------------
        # MOVE TO SCORE CARD
        # ----------------------------------------------------

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
    # OVERALL SCORE
    # --------------------------------------------------------

    overall_score = round(
        sum(scores.values())
        / len(scores)
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
        "<p>Your current AI knowledge profile</p>"
        "</div>",
        unsafe_allow_html=True
    )

    st.divider()

    # --------------------------------------------------------
    # OVERALL SCORE
    # --------------------------------------------------------

    st.markdown(
        "<p style='text-align:center; font-size:18px;'>"
        "Overall Score"
        "</p>",
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

        score = scores.get(
            subject,
            0
        )

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

    st.subheader(
        "🎯 Recommended Starting Point"
    )

    st.markdown(
        f"### {weakest_subject} — {weakest_score}%"
    )

    if weakest_score < 40:

        st.write(
            f"Build your foundation in "
            f"**{weakest_subject}** before moving "
            "into more advanced topics."
        )

    elif weakest_score < 70:

        st.write(
            f"Strengthen your **{weakest_subject}** "
            "skills through focused lessons and practice."
        )

    else:

        st.write(
            f"You have a strong foundation in "
            f"**{weakest_subject}**. Continue with "
            "advanced practice and projects."
        )

    # --------------------------------------------------------
    # LEARNER PROFILE
    # --------------------------------------------------------

    st.divider()

    st.subheader(
        "👤 Your Learning Profile"
    )

    profile = st.session_state.profile

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "AI Level",
            profile.get(
                "level",
                "Beginner"
            )
        )

        st.metric(
            "Daily Study Time",
            profile.get(
                "study_time",
                "30 minutes"
            )
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
    # BUTTONS
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

    st.title(
        "🗺️ Your Personalised AI Roadmap"
    )

    st.write(
        "AI StudyMate has arranged your learning journey "
        "from areas that need the most attention to areas "
        "where you already have stronger knowledge."
    )

    st.divider()

    roadmap = st.session_state.roadmap

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

        if score < 40:

            recommendation = (
                "Start with the fundamentals. Focus on "
                "core concepts, terminology, examples, "
                "and guided practice."
            )

        elif score < 70:

            recommendation = (
                "Strengthen your understanding through "
                "intermediate concepts, worked examples, "
                "and practice."
            )

        else:

            recommendation = (
                "Continue toward advanced concepts, "
                "projects, and application-based practice."
            )

        st.info(
            recommendation
        )

        st.divider()

    # --------------------------------------------------------
    # NEXT STEP
    # --------------------------------------------------------

    st.subheader(
        "🚀 Your Next Step"
    )

    if roadmap:

        first_subject = roadmap[0]["subject"]

        st.write(
            f"Start your personalised learning journey "
            f"with **{first_subject}**."
        )

    st.write(
        "The next stage of AI StudyMate will provide "
        "adaptive lessons, practice tasks, mastery "
        "tracking, and performance-based recommendations."
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

    st.divider()

    st.caption(
        "Discover what you know. Identify your gaps. "
        "Follow a personalised AI learning journey."
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
