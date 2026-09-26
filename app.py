import streamlit as st
import random

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI StudyMate",
    page_icon="🎓",
    layout="wide"
)

# ============================================================
# SUBJECTS
# ============================================================

SUBJECTS = [
    "Python",
    "Mathematics & Statistics",
    "Machine Learning",
    "Deep Learning",
    "Generative AI"
]

# ============================================================
# SESSION STATE
# ============================================================

DEFAULTS = {
    "page": "home",
    "profile": {},
    "questions": [],
    "current_question": 0,
    "answers": [],
    "diagnostic_complete": False,
    "domain_scores": {},
    "roadmap": [],
    "used_question_ids": set(),
    "attempt_number": 0
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# QUESTION BANK
# ============================================================

QUESTION_BANK = {

    # ========================================================
    # PYTHON
    # ========================================================

    "Python": {

        "Beginner": [

            {
                "id": "py_b1",
                "question": "Which symbol is used to create a comment in Python?",
                "options": ["#", "//", "/*", "--"],
                "answer": "#"
            },

            {
                "id": "py_b2",
                "question": "Which of the following is a Python data type?",
                "options": ["list", "table", "recordset", "document"],
                "answer": "list"
            },

            {
                "id": "py_b3",
                "question": "What is the output type of the expression 10 > 5?",
                "options": ["Boolean", "String", "Integer", "List"],
                "answer": "Boolean"
            },

            {
                "id": "py_b4",
                "question": "Which keyword is used to define a function in Python?",
                "options": ["def", "function", "fun", "define"],
                "answer": "def"
            },

            {
                "id": "py_b5",
                "question": "Which collection stores multiple values in an ordered and changeable form?",
                "options": ["List", "Tuple", "Set", "Dictionary"],
                "answer": "List"
            },

            {
                "id": "py_b6",
                "question": "Which function is commonly used to display output in Python?",
                "options": ["print()", "display()", "show()", "output()"],
                "answer": "print()"
            },

            {
                "id": "py_b7",
                "question": "Which operator is used for exponentiation in Python?",
                "options": ["**", "^", "//", "%%"],
                "answer": "**"
            },

            {
                "id": "py_b8",
                "question": "Which value represents the absence of a value in Python?",
                "options": ["None", "NullValue", "Empty", "Void"],
                "answer": "None"
            },

            {
                "id": "py_b9",
                "question": "Which statement is used to repeat code while a condition remains true?",
                "options": ["while", "repeat", "loop", "during"],
                "answer": "while"
            },

            {
                "id": "py_b10",
                "question": "Which brackets are used to create a Python list?",
                "options": ["[]", "{}", "()", "<>"],
                "answer": "[]"
            }
        ],

        "Intermediate": [

            {
                "id": "py_i1",
                "question": "What does a Python dictionary primarily store?",
                "options": [
                    "Key-value pairs",
                    "Only numbers",
                    "Only strings",
                    "Ordered functions"
                ],
                "answer": "Key-value pairs"
            },

            {
                "id": "py_i2",
                "question": "What does list comprehension provide?",
                "options": [
                    "A concise way to create lists",
                    "A way to define classes",
                    "Database connectivity",
                    "Exception handling"
                ],
                "answer": "A concise way to create lists"
            },

            {
                "id": "py_i3",
                "question": "What is the purpose of try/except?",
                "options": [
                    "Handle exceptions",
                    "Create loops",
                    "Define variables",
                    "Import modules"
                ],
                "answer": "Handle exceptions"
            },

            {
                "id": "py_i4",
                "question": "Which Python structure is immutable?",
                "options": ["Tuple", "List", "Dictionary", "Set"],
                "answer": "Tuple"
            },

            {
                "id": "py_i5",
                "question": "What does *args allow a function to accept?",
                "options": [
                    "Variable positional arguments",
                    "Only keyword arguments",
                    "Only integers",
                    "A single list"
                ],
                "answer": "Variable positional arguments"
            },

            {
                "id": "py_i6",
                "question": "What is the purpose of a Python virtual environment?",
                "options": [
                    "Isolate project dependencies",
                    "Increase CPU speed",
                    "Replace Python",
                    "Store databases"
                ],
                "answer": "Isolate project dependencies"
            },

            {
                "id": "py_i7",
                "question": "What does the map() function generally do?",
                "options": [
                    "Apply a function to elements of an iterable",
                    "Create a dictionary",
                    "Sort a list",
                    "Remove duplicates"
                ],
                "answer": "Apply a function to elements of an iterable"
            },

            {
                "id": "py_i8",
                "question": "What is a lambda in Python?",
                "options": [
                    "An anonymous function",
                    "A database",
                    "A loop",
                    "A package manager"
                ],
                "answer": "An anonymous function"
            },

            {
                "id": "py_i9",
                "question": "What does inheritance allow in object-oriented Python?",
                "options": [
                    "A class to derive behavior from another class",
                    "A list to become a tuple",
                    "A function to become a module",
                    "A variable to become immutable"
                ],
                "answer": "A class to derive behavior from another class"
            },

            {
                "id": "py_i10",
                "question": "Which library is primarily used for numerical arrays in Python?",
                "options": ["NumPy", "Flask", "Requests", "BeautifulSoup"],
                "answer": "NumPy"
            }
        ],

        "Advanced": [

            {
                "id": "py_a1",
                "question": "What is the key difference between a shallow copy and a deep copy?",
                "options": [
                    "A shallow copy can share nested objects, while a deep copy recursively copies them",
                    "A deep copy only copies primitive values",
                    "A shallow copy always duplicates every nested object",
                    "There is no difference"
                ],
                "answer": "A shallow copy can share nested objects, while a deep copy recursively copies them"
            },

            {
                "id": "py_a2",
                "question": "What problem can mutable default function arguments cause in Python?",
                "options": [
                    "The same mutable object can persist across function calls",
                    "The function cannot return values",
                    "The function becomes asynchronous",
                    "Python automatically deletes the argument"
                ],
                "answer": "The same mutable object can persist across function calls"
            },

            {
                "id": "py_a3",
                "question": "What is the main purpose of a generator?",
                "options": [
                    "Produce values lazily instead of storing them all at once",
                    "Create classes automatically",
                    "Compile Python to C",
                    "Encrypt variables"
                ],
                "answer": "Produce values lazily instead of storing them all at once"
            },

            {
                "id": "py_a4",
                "question": "What does the Python GIL primarily affect?",
                "options": [
                    "Execution of Python bytecode by multiple threads in the standard CPython implementation",
                    "Disk storage",
                    "Database indexing",
                    "Network routing"
                ],
                "answer": "Execution of Python bytecode by multiple threads in the standard CPython implementation"
            },

            {
                "id": "py_a5",
                "question": "What is a decorator commonly used for?",
                "options": [
                    "Modify or extend function or class behavior without changing its core definition",
                    "Create database tables",
                    "Allocate GPU memory",
                    "Convert Python into Java"
                ],
                "answer": "Modify or extend function or class behavior without changing its core definition"
            }
        ]
    },


    # ========================================================
    # MATHEMATICS & STATISTICS
    # ========================================================

    "Mathematics & Statistics": {

        "Beginner": [

            {
                "id": "math_b1",
                "question": "What is the mean of 2, 4, and 6?",
                "options": ["4", "3", "6", "12"],
                "answer": "4"
            },

            {
                "id": "math_b2",
                "question": "What does probability measure?",
                "options": [
                    "The likelihood of an event",
                    "The size of a dataset",
                    "The average value",
                    "The maximum value"
                ],
                "answer": "The likelihood of an event"
            },

            {
                "id": "math_b3",
                "question": "What is the median?",
                "options": [
                    "The middle value after sorting",
                    "The largest value",
                    "The average of all values",
                    "The smallest value"
                ],
                "answer": "The middle value after sorting"
            },

            {
                "id": "math_b4",
                "question": "What does variance measure?",
                "options": [
                    "How spread out values are",
                    "The middle value",
                    "The number of rows",
                    "The maximum value"
                ],
                "answer": "How spread out values are"
            },

            {
                "id": "math_b5",
                "question": "What is the value of 2²?",
                "options": ["4", "2", "6", "8"],
                "answer": "4"
            }
        ],

        "Intermediate": [

            {
                "id": "math_i1",
                "question": "What does standard deviation represent?",
                "options": [
                    "The typical spread of values around the mean",
                    "The number of observations",
                    "The maximum value",
                    "The median"
                ],
                "answer": "The typical spread of values around the mean"
            },

            {
                "id": "math_i2",
                "question": "What is correlation used to describe?",
                "options": [
                    "The strength and direction of association between variables",
                    "The exact causal relationship between variables",
                    "The number of observations",
                    "The median"
                ],
                "answer": "The strength and direction of association between variables"
            },

            {
                "id": "math_i3",
                "question": "What does a probability of 0 represent?",
                "options": [
                    "An impossible event",
                    "A certain event",
                    "An average event",
                    "A negative event"
                ],
                "answer": "An impossible event"
            },

            {
                "id": "math_i4",
                "question": "What does a normal distribution typically look like?",
                "options": [
                    "Bell-shaped and symmetric",
                    "Always flat",
                    "Always increasing",
                    "Random with no structure"
                ],
                "answer": "Bell-shaped and symmetric"
            },

            {
                "id": "math_i5",
                "question": "What is the purpose of a derivative?",
                "options": [
                    "Measure the rate of change",
                    "Calculate only averages",
                    "Count observations",
                    "Sort data"
                ],
                "answer": "Measure the rate of change"
            }
        ],

        "Advanced": [

            {
                "id": "math_a1",
                "question": "Why is the gradient important in machine learning optimization?",
                "options": [
                    "It indicates the direction of greatest increase of a function",
                    "It always gives the final model",
                    "It removes all noise from data",
                    "It replaces the loss function"
                ],
                "answer": "It indicates the direction of greatest increase of a function"
            },

            {
                "id": "math_a2",
                "question": "What does a covariance matrix describe?",
                "options": [
                    "Variances and pairwise covariances among variables",
                    "Only the mean of each variable",
                    "Only categorical labels",
                    "Only missing values"
                ],
                "answer": "Variances and pairwise covariances among variables"
            },

            {
                "id": "math_a3",
                "question": "What is the intuition behind Bayes' theorem?",
                "options": [
                    "Update a probability using new evidence",
                    "Remove all uncertainty",
                    "Guarantee causation",
                    "Calculate only averages"
                ],
                "answer": "Update a probability using new evidence"
            },

            {
                "id": "math_a4",
                "question": "What does an eigenvector represent in linear algebra?",
                "options": [
                    "A direction that is scaled by a matrix transformation",
                    "A guaranteed zero vector",
                    "A probability distribution",
                    "A scalar loss value"
                ],
                "answer": "A direction that is scaled by a matrix transformation"
            },

            {
                "id": "math_a5",
                "question": "Why can a high-dimensional feature space be problematic for some algorithms?",
                "options": [
                    "Distance and data sparsity can become problematic",
                    "Models automatically become perfect",
                    "All features become identical",
                    "Probability becomes zero"
                ],
                "answer": "Distance and data sparsity can become problematic"
            }
        ]
    },


    # ========================================================
    # MACHINE LEARNING
    # ========================================================

    "Machine Learning": {

        "Beginner": [

            {
                "id": "ml_b1",
                "question": "What is supervised learning?",
                "options": [
                    "Learning from labelled examples",
                    "Learning without data",
                    "Only clustering data",
                    "Manually writing every prediction"
                ],
                "answer": "Learning from labelled examples"
            },

            {
                "id": "ml_b2",
                "question": "What is a training dataset used for?",
                "options": [
                    "Teaching a model patterns from data",
                    "Only displaying results",
                    "Deleting the model",
                    "Creating hardware"
                ],
                "answer": "Teaching a model patterns from data"
            },

            {
                "id": "ml_b3",
                "question": "Which is a classification task?",
                "options": [
                    "Predicting whether an email is spam",
                    "Predicting house price",
                    "Calculating average temperature",
                    "Sorting numbers"
                ],
                "answer": "Predicting whether an email is spam"
            },

            {
                "id": "ml_b4",
                "question": "Which is a regression task?",
                "options": [
                    "Predicting house price",
                    "Detecting spam/non-spam",
                    "Grouping customers",
                    "Generating clusters"
                ],
                "answer": "Predicting house price"
            },

            {
                "id": "ml_b5",
                "question": "Why do we split data into training and testing sets?",
                "options": [
                    "To evaluate generalization on unseen data",
                    "To increase the number of features",
                    "To remove the model",
                    "To make every prediction correct"
                ],
                "answer": "To evaluate generalization on unseen data"
            }
        ],

        "Intermediate": [

            {
                "id": "ml_i1",
                "question": "What is overfitting?",
                "options": [
                    "When a model learns training data too closely and performs poorly on new data",
                    "When a model has no parameters",
                    "When data contains no features",
                    "When training is impossible"
                ],
                "answer": "When a model learns training data too closely and performs poorly on new data"
            },

            {
                "id": "ml_i2",
                "question": "What is cross-validation used for?",
                "options": [
                    "Estimate model performance across different data splits",
                    "Generate labels automatically",
                    "Replace preprocessing",
                    "Remove all features"
                ],
                "answer": "Estimate model performance across different data splits"
            },

            {
                "id": "ml_i3",
                "question": "What does feature scaling help with?",
                "options": [
                    "Putting numeric features on comparable scales",
                    "Creating labels",
                    "Deleting observations",
                    "Increasing dataset size"
                ],
                "answer": "Putting numeric features on comparable scales"
            },

            {
                "id": "ml_i4",
                "question": "What does regularization generally do?",
                "options": [
                    "Penalizes model complexity",
                    "Adds unlimited features",
                    "Guarantees zero error",
                    "Removes the training set"
                ],
                "answer": "Penalizes model complexity"
            },

            {
                "id": "ml_i5",
                "question": "What is precision in classification?",
                "options": [
                    "The fraction of predicted positives that are actually positive",
                    "The fraction of all samples that are positive",
                    "The number of training epochs",
                    "The size of the feature vector"
                ],
                "answer": "The fraction of predicted positives that are actually positive"
            }
        ],

        "Advanced": [

            {
                "id": "ml_a1",
                "question": "A model has very low training error but high validation error. What is the most likely issue?",
                "options": [
                    "Overfitting",
                    "Underfitting",
                    "Perfect generalization",
                    "Insufficient labels only"
                ],
                "answer": "Overfitting"
            },

            {
                "id": "ml_a2",
                "question": "Why can data leakage produce misleadingly strong validation results?",
                "options": [
                    "Information unavailable at prediction time leaks into training or validation",
                    "The model receives too few parameters",
                    "The dataset becomes smaller",
                    "The loss function becomes zero automatically"
                ],
                "answer": "Information unavailable at prediction time leaks into training or validation"
            },

            {
                "id": "ml_a3",
                "question": "What is the bias-variance tradeoff concerned with?",
                "options": [
                    "Balancing systematic error and sensitivity to training data",
                    "Balancing CPU and RAM",
                    "Balancing labels and features",
                    "Balancing training and deployment servers"
                ],
                "answer": "Balancing systematic error and sensitivity to training data"
            },

            {
                "id": "ml_a4",
                "question": "Why might accuracy be misleading for a highly imbalanced classification dataset?",
                "options": [
                    "A model can achieve high accuracy by mostly predicting the majority class",
                    "Accuracy ignores every prediction",
                    "Accuracy only works for regression",
                    "Accuracy always equals recall"
                ],
                "answer": "A model can achieve high accuracy by mostly predicting the majority class"
            },

            {
                "id": "ml_a5",
                "question": "What does ROC-AUC generally measure?",
                "options": [
                    "How well a classifier ranks positive examples above negative examples",
                    "The number of features",
                    "Training time",
                    "The amount of missing data"
                ],
                "answer": "How well a classifier ranks positive examples above negative examples"
            }
        ]
    },


    # ========================================================
    # DEEP LEARNING
    # ========================================================

    "Deep Learning": {

        "Beginner": [

            {
                "id": "dl_b1",
                "question": "What is an artificial neural network inspired by?",
                "options": [
                    "Networks of biological neurons",
                    "Database tables",
                    "Operating systems",
                    "Sorting algorithms"
                ],
                "answer": "Networks of biological neurons"
            },

            {
                "id": "dl_b2",
                "question": "What is an activation function used for?",
                "options": [
                    "Introduce non-linearity",
                    "Store datasets",
                    "Create labels",
                    "Download models"
                ],
                "answer": "Introduce non-linearity"
            },

            {
                "id": "dl_b3",
                "question": "What is a neural network weight?",
                "options": [
                    "A parameter learned during training",
                    "A dataset row",
                    "A class label",
                    "A file name"
                ],
                "answer": "A parameter learned during training"
            },

            {
                "id": "dl_b4",
                "question": "What is an epoch?",
                "options": [
                    "One complete pass through the training dataset",
                    "One neuron",
                    "One feature",
                    "One prediction"
                ],
                "answer": "One complete pass through the training dataset"
            },

            {
                "id": "dl_b5",
                "question": "What is a loss function?",
                "options": [
                    "A measure of prediction error",
                    "A dataset format",
                    "A neural network layer",
                    "A programming language"
                ],
                "answer": "A measure of prediction error"
            }
        ],

        "Intermediate": [

            {
                "id": "dl_i1",
                "question": "What does backpropagation compute?",
                "options": [
                    "Gradients of the loss with respect to model parameters",
                    "Only predictions",
                    "Dataset labels",
                    "File sizes"
                ],
                "answer": "Gradients of the loss with respect to model parameters"
            },

            {
                "id": "dl_i2",
                "question": "Why are CNNs effective for many image tasks?",
                "options": [
                    "They exploit local spatial patterns using convolution",
                    "They ignore spatial information",
                    "They only process text",
                    "They require no training"
                ],
                "answer": "They exploit local spatial patterns using convolution"
            },

            {
                "id": "dl_i3",
                "question": "What does dropout help reduce?",
                "options": [
                    "Overfitting",
                    "Dataset size",
                    "Number of labels",
                    "GPU memory to zero"
                ],
                "answer": "Overfitting"
            },

            {
                "id": "dl_i4",
                "question": "What is the role of an optimizer such as Adam?",
                "options": [
                    "Update model parameters using gradients",
                    "Create training labels",
                    "Store images",
                    "Measure accuracy only"
                ],
                "answer": "Update model parameters using gradients"
            },

            {
                "id": "dl_i5",
                "question": "What is vanishing gradient?",
                "options": [
                    "Gradients become extremely small during backpropagation",
                    "The dataset disappears",
                    "The model loses all layers",
                    "The optimizer stops permanently"
                ],
                "answer": "Gradients become extremely small during backpropagation"
            }
        ],

        "Advanced": [

            {
                "id": "dl_a1",
                "question": "Why can residual connections help very deep neural networks?",
                "options": [
                    "They provide shorter paths for information and gradient flow",
                    "They eliminate the need for training",
                    "They remove all parameters",
                    "They convert images into labels automatically"
                ],
                "answer": "They provide shorter paths for information and gradient flow"
            },

            {
                "id": "dl_a2",
                "question": "What is the purpose of batch normalization?",
                "options": [
                    "Normalize intermediate activations to improve training behavior",
                    "Create new labels",
                    "Remove the output layer",
                    "Replace backpropagation"
                ],
                "answer": "Normalize intermediate activations to improve training behavior"
            },

            {
                "id": "dl_a3",
                "question": "Why can softmax be used for multiclass classification?",
                "options": [
                    "It converts logits into normalized class probabilities",
                    "It removes all classes",
                    "It performs regression",
                    "It guarantees correct predictions"
                ],
                "answer": "It converts logits into normalized class probabilities"
            },

            {
                "id": "dl_a4",
                "question": "What problem can an excessively large learning rate cause?",
                "options": [
                    "Training can overshoot useful regions and fail to converge",
                    "The model always becomes perfect",
                    "The dataset becomes larger",
                    "The loss is guaranteed to be zero"
                ],
                "answer": "Training can overshoot useful regions and fail to converge"
            },

            {
                "id": "dl_a5",
                "question": "What is attention designed to help a model do?",
                "options": [
                    "Weight the relevance of different input elements when computing representations",
                    "Delete training data",
                    "Guarantee causality",
                    "Replace all neural network layers"
                ],
                "answer": "Weight the relevance of different input elements when computing representations"
            }
        ]
    },


    # ========================================================
    # GENERATIVE AI
    # ========================================================

    "Generative AI": {

        "Beginner": [

            {
                "id": "gen_b1",
                "question": "What does Generative AI primarily do?",
                "options": [
                    "Generate new content",
                    "Only store data",
                    "Only sort files",
                    "Only calculate averages"
                ],
                "answer": "Generate new content"
            },

            {
                "id": "gen_b2",
                "question": "What does LLM stand for?",
                "options": [
                    "Large Language Model",
                    "Long Learning Machine",
                    "Language Logic Module",
                    "Large Logic Machine"
                ],
                "answer": "Large Language Model"
            },

            {
                "id": "gen_b3",
                "question": "What is a prompt?",
                "options": [
                    "An instruction or input given to an AI model",
                    "A database table",
                    "A programming compiler",
                    "A neural network weight"
                ],
                "answer": "An instruction or input given to an AI model"
            },

            {
                "id": "gen_b4",
                "question": "What is an AI chatbot designed to do?",
                "options": [
                    "Interact with users using natural language",
                    "Only store passwords",
                    "Only compress files",
                    "Only run databases"
                ],
                "answer": "Interact with users using natural language"
            },

            {
                "id": "gen_b5",
                "question": "What is an embedding?",
                "options": [
                    "A numerical representation of information",
                    "A database password",
                    "A web page",
                    "A programming loop"
                ],
                "answer": "A numerical representation of information"
            }
        ],

        "Intermediate": [

            {
                "id": "gen_i1",
                "question": "What is RAG?",
                "options": [
                    "Retrieval-Augmented Generation",
                    "Random AI Generation",
                    "Recursive Answer Generation",
                    "Rapid AI Grouping"
                ],
                "answer": "Retrieval-Augmented Generation"
            },

            {
                "id": "gen_i2",
                "question": "Why are embeddings useful in semantic search?",
                "options": [
                    "They represent meaning in a numerical space",
                    "They guarantee factual answers",
                    "They remove the need for data",
                    "They replace all language models"
                ],
                "answer": "They represent meaning in a numerical space"
            },

            {
                "id": "gen_i3",
                "question": "What is tokenization?",
                "options": [
                    "Breaking text into tokens processed by a model",
                    "Encrypting a database",
                    "Training a GPU",
                    "Creating a Python package"
                ],
                "answer": "Breaking text into tokens processed by a model"
            },

            {
                "id": "gen_i4",
                "question": "What is context in an LLM interaction?",
                "options": [
                    "Information provided to help the model generate a response",
                    "The model's GPU",
                    "A database index",
                    "A Python variable"
                ],
                "answer": "Information provided to help the model generate a response"
            },

            {
                "id": "gen_i5",
                "question": "What is fine-tuning?",
                "options": [
                    "Further training a pretrained model on a specific dataset or task",
                    "Deleting a model",
                    "Only changing the UI",
                    "Increasing internet speed"
                ],
                "answer": "Further training a pretrained model on a specific dataset or task"
            }
        ],

        "Advanced": [

            {
                "id": "gen_a1",
                "question": "Why can an LLM hallucinate?",
                "options": [
                    "It can generate plausible text without having a guaranteed mechanism for factual verification",
                    "It always has access to every database",
                    "It only outputs stored sentences",
                    "It cannot generate new text"
                ],
                "answer": "It can generate plausible text without having a guaranteed mechanism for factual verification"
            },

            {
                "id": "gen_a2",
                "question": "What is the key idea behind transformer self-attention?",
                "options": [
                    "Each token can assign different importance to other tokens when forming representations",
                    "Every token is processed independently with no interaction",
                    "Only the first token is used",
                    "The model removes positional information completely"
                ],
                "answer": "Each token can assign different importance to other tokens when forming representations"
            },

            {
                "id": "gen_a3",
                "question": "Why does RAG often improve factual grounding?",
                "options": [
                    "The model can condition generation on retrieved external information",
                    "It permanently changes the model weights",
                    "It guarantees every retrieved document is correct",
                    "It removes the need for prompts"
                ],
                "answer": "The model can condition generation on retrieved external information"
            },

            {
                "id": "gen_a4",
                "question": "What is temperature commonly used for in text generation?",
                "options": [
                    "Control the randomness of token selection",
                    "Increase model parameter count",
                    "Change the training dataset",
                    "Reduce context length to zero"
                ],
                "answer": "Control the randomness of token selection"
            },

            {
                "id": "gen_a5",
                "question": "What is the main purpose of a system prompt?",
                "options": [
                    "Provide high-level instructions that guide model behavior",
                    "Store model weights",
                    "Train the model from scratch",
                    "Create a database"
                ],
                "answer": "Provide high-level instructions that guide model behavior"
            }
        ]
    }
}


# ============================================================
# STATUS
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


# ============================================================
# CREATE DIAGNOSTIC
# ============================================================

def create_new_diagnostic(level):

    selected_questions = []

    for subject in SUBJECTS:

        available = QUESTION_BANK[subject][level]

        unused = [
            q for q in available
            if q["id"] not in st.session_state.used_question_ids
        ]

        if len(unused) >= 3:
            chosen = random.sample(unused, 3)
        else:
            chosen = random.sample(available, 3)

        for question in chosen:

            st.session_state.used_question_ids.add(
                question["id"]
            )

            question_copy = question.copy()

            question_copy["subject"] = subject

            shuffled_options = question_copy["options"].copy()

            random.shuffle(shuffled_options)

            question_copy["options"] = shuffled_options
            question_copy["selected"] = None

            selected_questions.append(question_copy)

    random.shuffle(selected_questions)

    st.session_state.questions = selected_questions
    st.session_state.current_question = 0
    st.session_state.answers = []
    st.session_state.diagnostic_complete = False
    st.session_state.domain_scores = {}
    st.session_state.roadmap = []
    st.session_state.attempt_number += 1


# ============================================================
# CALCULATE SCORES
# ============================================================

def calculate_scores():

    scores = {}

    for subject in SUBJECTS:

        subject_questions = [
            q for q in st.session_state.questions
            if q["subject"] == subject
        ]

        correct = 0

        for question in subject_questions:

            if question["selected"] == question["answer"]:
                correct += 1

        if len(subject_questions) > 0:

            score = round(
                (correct / len(subject_questions)) * 100
            )

        else:
            score = 0

        scores[subject] = score

    return scores


# ============================================================
# CREATE ROADMAP
# ============================================================

def create_roadmap(scores):

    sorted_subjects = sorted(
        scores.items(),
        key=lambda x: x[1]
    )

    roadmap = []

    for subject, score in sorted_subjects:

        roadmap.append(
            {
                "subject": subject,
                "score": score,
                "status": get_status(score)
            }
        )

    return roadmap


# ============================================================
# HOME PAGE
# ============================================================

def home_page():

    # --------------------------------------------------------
    # HERO SECTION
    # --------------------------------------------------------

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:45px 10px 30px 10px;
        ">

            <div style="
                font-size:56px;
                margin-bottom:10px;
            ">
                🎓
            </div>

            <h1 style="
                font-size:42px;
                margin:0;
                padding:0;
            ">
                AI StudyMate
            </h1>

            <p style="
                font-size:20px;
                margin-top:10px;
                margin-bottom:8px;
            ">
                Personalised AI Tutor for Learning AI
            </p>

            <p style="
                font-size:16px;
                margin-top:0;
            ">
                Learn AI through a personalised learning journey
                designed around your current knowledge and goals.
            </p>

        </div>
        """,
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
        )
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

    # --------------------------------------------------------
    # START BUTTON
    # --------------------------------------------------------

    if st.button(
        "🚀 Start AI Journey",
        use_container_width=True
    ):

        st.session_state.profile = {
            "name": name,
            "level": level,
            "goal": goal,
            "study_time": study_time
        }

        # Start a fresh diagnostic
        st.session_state.used_question_ids = set()

        create_new_diagnostic(level)

        st.session_state.page = "diagnostic"

        st.rerun()


# ============================================================
# DIAGNOSTIC PAGE
# ============================================================

def diagnostic_page():

    questions = st.session_state.questions

    if not questions:

        st.session_state.page = "home"

        st.rerun()

    current_index = st.session_state.current_question

    current_question = questions[current_index]

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    st.title("🧠 AI Diagnostic")

    st.write(
        f"Level selected: "
        f"**{st.session_state.profile.get('level', 'Beginner')}**"
    )

    st.caption(
        f"Question {current_index + 1} "
        f"of {len(questions)}"
    )

    progress_value = (
        (current_index + 1) /
        len(questions)
    )

    st.progress(progress_value)

    st.divider()

    # --------------------------------------------------------
    # QUESTION
    # --------------------------------------------------------

    st.subheader(
        current_question["question"]
    )

    selected = st.radio(
        "Choose one answer:",
        current_question["options"],
        index=None,
        key=f"question_{current_index}"
    )

    st.write("")

    # --------------------------------------------------------
    # NEXT BUTTON
    # --------------------------------------------------------

    if st.button(
        "Next Question →",
        use_container_width=True,
        disabled=selected is None
    ):

        # Save answer silently
        current_question["selected"] = selected

        st.session_state.answers.append(
            selected
        )

        # More questions remain
        if current_index + 1 < len(questions):

            st.session_state.current_question += 1

            st.rerun()

        # Diagnostic finished
        else:

            scores = calculate_scores()

            st.session_state.domain_scores = scores

            st.session_state.roadmap = create_roadmap(
                scores
            )

            st.session_state.diagnostic_complete = True

            st.session_state.page = "score_card"

            st.rerun()


# ============================================================
# SCORE CARD PAGE
# ============================================================

def score_card_page():

    scores = st.session_state.domain_scores

    if not scores:

        st.session_state.page = "home"

        st.rerun()

    # --------------------------------------------------------
    # OVERALL SCORE
    # --------------------------------------------------------

    valid_scores = list(scores.values())

    overall_score = round(
        sum(valid_scores) /
        len(valid_scores)
    )

    # --------------------------------------------------------
    # WEAKEST SUBJECT
    # --------------------------------------------------------

    weakest_subject = min(
        scores,
        key=scores.get
    )

    weakest_score = scores[
        weakest_subject
    ]

    # --------------------------------------------------------
    # SCORE CARD HEADER
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div style="
            text-align:center;
            padding:35px 20px;
            border-radius:18px;
            border:1px solid rgba(128,128,128,0.25);
            margin-bottom:30px;
        ">

            <div style="
                font-size:32px;
                font-weight:700;
            ">
                🎓 YOUR AI LEARNING SCORE CARD
            </div>

            <div style="
                font-size:16px;
                margin-top:8px;
            ">
                Your current AI knowledge profile
            </div>

            <div style="
                font-size:52px;
                font-weight:700;
                margin-top:15px;
            ">
                {overall_score}%
            </div>

            <div style="
                font-size:15px;
            ">
                Overall Score
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # SUBJECT PERFORMANCE
    # --------------------------------------------------------

    st.subheader("📊 Subject Performance")

    for subject in SUBJECTS:

        score = scores.get(
            subject,
            0
        )

        status = get_status(score)

        st.markdown(
            f"""
            <div style="
                margin-top:20px;
                margin-bottom:15px;
            ">

                <div style="
                    font-size:20px;
                    font-weight:600;
                ">
                    {subject}
                </div>

                <div style="
                    font-size:15px;
                    margin-top:5px;
                ">
                    {score}%
                </div>

                <div style="
                    width:100%;
                    height:12px;
                    background:#e5e7eb;
                    border-radius:10px;
                    margin-top:8px;
                    overflow:hidden;
                ">

                    <div style="
                        width:{score}%;
                        height:100%;
                        background:#4f46e5;
                        border-radius:10px;
                    ">
                    </div>

                </div>

                <div style="
                    font-size:14px;
                    margin-top:6px;
                ">
                    Status: <b>{status}</b>
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # RECOMMENDED STARTING POINT
    # --------------------------------------------------------

    st.divider()

    st.markdown(
        """
        <div style="
            font-size:24px;
            font-weight:700;
            margin-top:15px;
            margin-bottom:12px;
        ">
            🎯 Recommended Starting Point
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div style="
            border:1px solid rgba(128,128,128,0.25);
            padding:22px;
            border-radius:14px;
            margin-bottom:20px;
        ">

            <div style="
                font-size:24px;
                font-weight:700;
            ">
                {weakest_subject} — {weakest_score}%
            </div>

            <div style="
                font-size:16px;
                margin-top:10px;
            ">
                Build your foundation here before moving
                to more advanced topics.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # ACTION BUTTONS
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🗺️ View My Personalised Roadmap",
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

            create_new_diagnostic(level)

            st.session_state.page = "diagnostic"

            st.rerun()


# ============================================================
# PERSONALIZED ROADMAP
# ============================================================

def roadmap_page():

    st.title("🗺️ Your Personalised Roadmap")

    st.write(
        "Your learning journey is arranged from the areas "
        "that currently need the most improvement."
    )

    st.divider()

    for index, item in enumerate(
        st.session_state.roadmap,
        start=1
    ):

        subject = item["subject"]

        score = item["score"]

        status = item["status"]

        st.markdown(
            f"""
            <div style="
                padding:20px;
                border:1px solid rgba(128,128,128,0.25);
                border-radius:14px;
                margin-bottom:15px;
            ">

                <div style="
                    font-size:22px;
                    font-weight:700;
                ">
                    {index}. {subject}
                </div>

                <div style="
                    font-size:16px;
                    margin-top:7px;
                ">
                    Current Score: <b>{score}%</b>
                </div>

                <div style="
                    font-size:15px;
                    margin-top:5px;
                ">
                    Status: <b>{status}</b>
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

        st.session_state.page = "score_card"

        st.rerun()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:24px;
            font-weight:700;
            padding:10px;
        ">
            🎓 AI StudyMate
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    if st.session_state.diagnostic_complete:

        if st.button(
            "📊 Score Card",
            use_container_width=True
        ):

            st.session_state.page = "score_card"

            st.rerun()

        if st.button(
            "🗺️ Personalised Roadmap",
            use_container_width=True
        ):

            st.session_state.page = "roadmap"

            st.rerun()

    if st.button(
        "🏠 Home",
        use_container_width=True
    ):

        st.session_state.page = "home"

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
