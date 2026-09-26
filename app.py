import streamlit as st
import random


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI StudyMate",
    page_icon="🤖",
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
# QUESTION CREATION
# ============================================================
#
# We generate a large pool of questions.
#
# Every subject gets 100 possible questions for the
# selected difficulty level.
#
# Only 3 are randomly selected for each attempt.
#
# ============================================================


def make_question(
    question_id,
    subject,
    difficulty,
    question,
    options,
    answer
):

    return {
        "id": question_id,
        "subject": subject,
        "difficulty": difficulty,
        "question": question,
        "options": options,
        "answer": answer
    }


# ============================================================
# PYTHON QUESTION POOL
# ============================================================

def generate_python_questions(difficulty):

    questions = []

    # --------------------------------------------------------
    # BASIC
    # --------------------------------------------------------

    if difficulty == "Basic":

        templates = [

            (
                "Which symbol is used to write a comment in Python?",
                ["//", "#", "/*", "--"],
                "#"
            ),

            (
                "Which keyword is used to define a function in Python?",
                ["function", "def", "fun", "define"],
                "def"
            ),

            (
                "Which of these is a Boolean value in Python?",
                ["Yes", "True", "1", "On"],
                "True"
            ),

            (
                "Which data structure stores items in an ordered collection?",
                ["List", "Boolean", "Integer", "Function"],
                "List"
            ),

            (
                "Which brackets are normally used to create a Python list?",
                ["{}", "[]", "()", "<>"],
                "[]"
            ),

            (
                "Which keyword is used to create a loop over a sequence?",
                ["repeat", "for", "loop", "iterate"],
                "for"
            ),

            (
                "Which function displays output in Python?",
                ["display()", "show()", "print()", "output()"],
                "print()"
            ),

            (
                "Which value represents the absence of a value in Python?",
                ["None", "Empty", "NullValue", "Nothing"],
                "None"
            ),

            (
                "Which operator is used for equality comparison?",
                ["=", "==", ":=", "!="],
                "=="
            ),

            (
                "Which Python type represents whole numbers?",
                ["float", "str", "int", "bool"],
                "int"
            )
        ]

    # --------------------------------------------------------
    # INTERMEDIATE
    # --------------------------------------------------------

    elif difficulty == "Intermediate":

        templates = [

            (
                "What does range(5) produce in Python?",
                [
                    "A list containing 1 through 5",
                    "A range object representing 0 through 4",
                    "A tuple containing 0 through 5",
                    "A set containing five values"
                ],
                "A range object representing 0 through 4"
            ),

            (
                "Which structure stores key-value pairs?",
                [
                    "List",
                    "Tuple",
                    "Dictionary",
                    "Set"
                ],
                "Dictionary"
            ),

            (
                "What does list[-1] normally return?",
                [
                    "The first item",
                    "The last item",
                    "An error",
                    "The second item"
                ],
                "The last item"
            ),

            (
                "What is a tuple generally known for?",
                [
                    "Being immutable",
                    "Always containing strings",
                    "Being unordered only",
                    "Storing only numbers"
                ],
                "Being immutable"
            ),

            (
                "What is the purpose of a class?",
                [
                    "To define a blueprint for objects",
                    "To store only strings",
                    "To replace loops",
                    "To execute SQL"
                ],
                "To define a blueprint for objects"
            ),

            (
                "What does len() return?",
                [
                    "The type of an object",
                    "The length or number of elements",
                    "The memory address",
                    "The last element"
                ],
                "The length or number of elements"
            ),

            (
                "Which keyword is used to handle exceptions?",
                [
                    "catch",
                    "try",
                    "except-only",
                    "error"
                ],
                "try"
            ),

            (
                "What does a dictionary key need to be?",
                [
                    "Hashable",
                    "Always an integer",
                    "Always a string",
                    "A list"
                ],
                "Hashable"
            ),

            (
                "What does `is` primarily test?",
                [
                    "Object identity",
                    "String equality only",
                    "Numerical addition",
                    "Type conversion"
                ],
                "Object identity"
            ),

            (
                "What is inheritance in Python?",
                [
                    "A class receiving behavior from another class",
                    "Copying a file",
                    "Repeating a loop",
                    "Creating a dictionary"
                ],
                "A class receiving behavior from another class"
            )
        ]

    # --------------------------------------------------------
    # ADVANCED
    # --------------------------------------------------------

    else:

        templates = [

            (
                "What is the main purpose of a decorator?",
                [
                    "Modify or extend function behavior",
                    "Create a database",
                    "Compile Python",
                    "Delete variables"
                ],
                "Modify or extend function behavior"
            ),

            (
                "What is a generator useful for?",
                [
                    "Producing values lazily",
                    "Creating database tables",
                    "Compiling C code",
                    "Encrypting files"
                ],
                "Producing values lazily"
            ),

            (
                "What does `yield` do inside a generator?",
                [
                    "Produces a value while preserving generator state",
                    "Stops Python permanently",
                    "Deletes the function",
                    "Creates a class"
                ],
                "Produces a value while preserving generator state"
            ),

            (
                "What is the purpose of `__init__` in a class?",
                [
                    "Initialize an object",
                    "Destroy a module",
                    "Create a loop",
                    "Import a package"
                ],
                "Initialize an object"
            ),

            (
                "What is method resolution order related to?",
                [
                    "The order Python searches classes for inherited methods",
                    "The order files are saved",
                    "The order list items are sorted",
                    "The order packages are installed"
                ],
                "The order Python searches classes for inherited methods"
            ),

            (
                "What is a closure?",
                [
                    "A function retaining access to variables from its enclosing scope",
                    "A closed file",
                    "A database connection",
                    "A completed loop"
                ],
                "A function retaining access to variables from its enclosing scope"
            ),

            (
                "What does `*args` allow a function to receive?",
                [
                    "A variable number of positional arguments",
                    "Only keyword arguments",
                    "Only strings",
                    "Only dictionaries"
                ],
                "A variable number of positional arguments"
            ),

            (
                "What does `**kwargs` allow a function to receive?",
                [
                    "A variable number of keyword arguments",
                    "Only positional arguments",
                    "Only lists",
                    "Only integers"
                ],
                "A variable number of keyword arguments"
            ),

            (
                "Why can mutable default arguments be dangerous?",
                [
                    "The same object can persist across function calls",
                    "They always cause syntax errors",
                    "They cannot contain numbers",
                    "Python automatically deletes them"
                ],
                "The same object can persist across function calls"
            ),

            (
                "What is duck typing?",
                [
                    "Using an object's behavior rather than requiring a specific type",
                    "Converting every object to a string",
                    "Checking memory addresses only",
                    "Using only inheritance"
                ],
                "Using an object's behavior rather than requiring a specific type"
            )
        ]

    return expand_templates(
        "PY",
        "Python",
        difficulty,
        templates
    )


# ============================================================
# MATH QUESTION POOL
# ============================================================

def generate_math_questions(difficulty):

    questions = []

    if difficulty == "Basic":

        templates = [

            (
                "What is the mean of 2, 4 and 6?",
                ["2", "4", "6", "12"],
                "4"
            ),

            (
                "What does probability measure?",
                [
                    "Likelihood of an event",
                    "Dataset size",
                    "Computer speed",
                    "Number of variables"
                ],
                "Likelihood of an event"
            ),

            (
                "What is the median of 2, 5 and 9?",
                ["2", "5", "9", "16"],
                "5"
            ),

            (
                "What does the x-axis normally represent?",
                [
                    "Horizontal values",
                    "Vertical values",
                    "Only percentages",
                    "Only categories"
                ],
                "Horizontal values"
            ),

            (
                "What is 10% of 100?",
                ["1", "5", "10", "20"],
                "10"
            ),

            (
                "What is the probability of a certain event?",
                ["0", "0.5", "1", "2"],
                "1"
            ),

            (
                "What is 3 squared?",
                ["6", "9", "12", "27"],
                "9"
            ),

            (
                "What is the range of 3, 7 and 10?",
                ["3", "7", "10", "7"],
                "7"
            ),

            (
                "Which value represents no chance?",
                ["0", "0.5", "1", "100"],
                "0"
            ),

            (
                "What does a fraction represent?",
                [
                    "A relationship between quantities",
                    "Only a whole number",
                    "Only a percentage",
                    "A programming loop"
                ],
                "A relationship between quantities"
            )
        ]

    elif difficulty == "Intermediate":

        templates = [

            (
                "What does standard deviation measure?",
                [
                    "Spread of data",
                    "Number of observations",
                    "Number of features",
                    "Model type"
                ],
                "Spread of data"
            ),

            (
                "What does correlation describe?",
                [
                    "Relationship between variables",
                    "Number of rows",
                    "Memory usage",
                    "File size"
                ],
                "Relationship between variables"
            ),

            (
                "What is variance related to?",
                [
                    "Squared deviations from the mean",
                    "Only the median",
                    "Only the maximum",
                    "Number of columns"
                ],
                "Squared deviations from the mean"
            ),

            (
                "What is a normal distribution typically shaped like?",
                [
                    "Bell curve",
                    "Perfect square",
                    "Straight vertical line",
                    "Triangle"
                ],
                "Bell curve"
            ),

            (
                "What is conditional probability?",
                [
                    "Probability of an event given another event",
                    "Probability without data",
                    "Probability of every event",
                    "Probability that is always zero"
                ],
                "Probability of an event given another event"
            ),

            (
                "What does covariance indicate?",
                [
                    "How two variables vary together",
                    "The number of classes",
                    "The median value",
                    "The dataset size"
                ],
                "How two variables vary together"
            ),

            (
                "What does a confidence interval estimate?",
                [
                    "A range for an unknown population parameter",
                    "Exact value of every observation",
                    "The number of rows",
                    "The model architecture"
                ],
                "A range for an unknown population parameter"
            ),

            (
                "What does a p-value help evaluate?",
                [
                    "Evidence against a null hypothesis",
                    "Neural network depth",
                    "Dataset storage size",
                    "Number of features"
                ],
                "Evidence against a null hypothesis"
            ),

            (
                "What does an outlier represent?",
                [
                    "An unusually distant observation",
                    "The average observation",
                    "The first observation",
                    "A missing column"
                ],
                "An unusually distant observation"
            ),

            (
                "What is a sample?",
                [
                    "A subset of a population",
                    "The entire universe of observations",
                    "Only one variable",
                    "A mathematical constant"
                ],
                "A subset of a population"
            )
        ]

    else:

        templates = [

            (
                "What does a gradient represent?",
                [
                    "Direction and rate of greatest increase",
                    "Only the mean",
                    "Dataset size",
                    "Number of classes"
                ],
                "Direction and rate of greatest increase"
            ),

            (
                "What is a derivative primarily used to describe?",
                [
                    "Rate of change",
                    "Dataset size",
                    "Probability only",
                    "Number of variables"
                ],
                "Rate of change"
            ),

            (
                "What does Bayes' theorem provide?",
                [
                    "A way to update probability using evidence",
                    "A sorting algorithm",
                    "A neural network",
                    "A database"
                ],
                "A way to update probability using evidence"
            ),

            (
                "What is a covariance matrix commonly used to represent?",
                [
                    "Variances and covariances among variables",
                    "Only means",
                    "Only medians",
                    "Only class labels"
                ],
                "Variances and covariances among variables"
            ),

            (
                "What does eigenvector information capture in linear algebra?",
                [
                    "Directions preserved by a linear transformation",
                    "Only dataset size",
                    "Only probability",
                    "Only scalar averages"
                ],
                "Directions preserved by a linear transformation"
            ),

            (
                "Why is matrix multiplication important in machine learning?",
                [
                    "It efficiently represents many linear transformations",
                    "It replaces probability",
                    "It removes all nonlinearity",
                    "It stores passwords"
                ],
                "It efficiently represents many linear transformations"
            ),

            (
                "What is partial differentiation used for?",
                [
                    "Finding change with respect to one variable while holding others conceptually fixed",
                    "Sorting variables",
                    "Counting rows",
                    "Creating databases"
                ],
                "Finding change with respect to one variable while holding others conceptually fixed"
            ),

            (
                "What is maximum likelihood estimation trying to do?",
                [
                    "Find parameters that make observed data most likely",
                    "Minimize dataset size",
                    "Delete outliers automatically",
                    "Maximize number of features"
                ],
                "Find parameters that make observed data most likely"
            ),

            (
                "What is entropy in information theory associated with?",
                [
                    "Uncertainty",
                    "CPU temperature",
                    "File size only",
                    "Number of rows"
                ],
                "Uncertainty"
            ),

            (
                "Why are logarithms useful in probability and machine learning?",
                [
                    "They convert products into sums and improve numerical handling",
                    "They always increase probabilities",
                    "They remove all randomness",
                    "They create labels"
                ],
                "They convert products into sums and improve numerical handling"
            )
        ]

    return expand_templates(
        "MATH",
        "Mathematics & Statistics",
        difficulty,
        templates
    )


# ============================================================
# MACHINE LEARNING QUESTION POOL
# ============================================================

def generate_ml_questions(difficulty):

    if difficulty == "Basic":

        templates = [

            (
                "What is machine learning?",
                [
                    "Learning patterns from data",
                    "A database",
                    "A programming language",
                    "An operating system"
                ],
                "Learning patterns from data"
            ),

            (
                "What is supervised learning?",
                [
                    "Learning from labelled examples",
                    "Learning without data",
                    "Deleting labels",
                    "Only clustering"
                ],
                "Learning from labelled examples"
            ),

            (
                "What is a training dataset?",
                [
                    "Data used to teach a model",
                    "Only test data",
                    "A programming language",
                    "A visualization"
                ],
                "Data used to teach a model"
            ),

            (
                "Which is a classification task?",
                [
                    "Predicting whether an email is spam",
                    "Grouping customers without labels",
                    "Calculating an average",
                    "Sorting filenames"
                ],
                "Predicting whether an email is spam"
            ),

            (
                "Which is a regression task?",
                [
                    "Predicting house price",
                    "Detecting spam/not spam",
                    "Grouping customers",
                    "Finding clusters"
                ],
                "Predicting house price"
            ),

            (
                "What is a model?",
                [
                    "A learned representation used to make predictions",
                    "A database table",
                    "A programming editor",
                    "A computer cable"
                ],
                "A learned representation used to make predictions"
            ),

            (
                "What is a feature?",
                [
                    "An input variable",
                    "Only the target",
                    "A model error",
                    "A database"
                ],
                "An input variable"
            ),

            (
                "What is a label?",
                [
                    "The target value in supervised learning",
                    "A Python package",
                    "A database",
                    "A feature transformation only"
                ],
                "The target value in supervised learning"
            ),

            (
                "What does a test set help evaluate?",
                [
                    "Performance on unseen data",
                    "Python syntax",
                    "Database speed",
                    "File size"
                ],
                "Performance on unseen data"
            ),

            (
                "What is clustering?",
                [
                    "Grouping similar observations",
                    "Predicting labels from labelled data",
                    "Sorting files",
                    "Deleting data"
                ],
                "Grouping similar observations"
            )
        ]

    elif difficulty == "Intermediate":

        templates = [

            (
                "What is overfitting?",
                [
                    "Learning training data too closely",
                    "Having no training data",
                    "Always improving generalization",
                    "Using no features"
                ],
                "Learning training data too closely"
            ),

            (
                "What is underfitting?",
                [
                    "A model that is too simple to capture important patterns",
                    "A model memorizing training data",
                    "A model with infinite parameters",
                    "A model with perfect validation"
                ],
                "A model that is too simple to capture important patterns"
            ),

            (
                "What is feature engineering?",
                [
                    "Creating or transforming useful input variables",
                    "Deleting all features",
                    "Creating a database",
                    "Changing the operating system"
                ],
                "Creating or transforming useful input variables"
            ),

            (
                "Why split data into training and testing sets?",
                [
                    "To evaluate generalization on unseen data",
                    "To make the dataset larger",
                    "To remove all noise",
                    "To guarantee perfect accuracy"
                ],
                "To evaluate generalization on unseen data"
            ),

            (
                "What does precision measure?",
                [
                    "How many predicted positives are actually positive",
                    "How many actual positives were found",
                    "Total dataset size",
                    "Training time"
                ],
                "How many predicted positives are actually positive"
            ),

            (
                "What does recall measure?",
                [
                    "How many actual positives were identified",
                    "How many predicted positives are correct",
                    "Number of features",
                    "Number of epochs"
                ],
                "How many actual positives were identified"
            ),

            (
                "What is cross-validation used for?",
                [
                    "Estimating model performance across different data splits",
                    "Deleting features",
                    "Increasing RAM",
                    "Creating labels"
                ],
                "Estimating model performance across different data splits"
            ),

            (
                "What is regularization commonly used for?",
                [
                    "Reducing overfitting",
                    "Increasing noise",
                    "Deleting training data",
                    "Increasing target values"
                ],
                "Reducing overfitting"
            ),

            (
                "What is data leakage?",
                [
                    "Information from outside the intended training process improperly influences the model",
                    "A missing file",
                    "A network failure",
                    "A slow GPU"
                ],
                "Information from outside the intended training process improperly influences the model"
            ),

            (
                "Why scale numerical features?",
                [
                    "Some algorithms are sensitive to differences in feature scale",
                    "It guarantees perfect accuracy",
                    "It removes labels",
                    "It creates more samples"
                ],
                "Some algorithms are sensitive to differences in feature scale"
            )
        ]

    else:

        templates = [

            (
                "Why can high training accuracy together with low validation accuracy indicate overfitting?",
                [
                    "The model has captured training-specific patterns that do not generalize",
                    "The validation set is always wrong",
                    "The model has too few parameters",
                    "The training data has no labels"
                ],
                "The model has captured training-specific patterns that do not generalize"
            ),

            (
                "Why is regularization effective against overfitting?",
                [
                    "It constrains model complexity",
                    "It guarantees more training samples",
                    "It removes the target variable",
                    "It eliminates all bias"
                ],
                "It constrains model complexity"
            ),

            (
                "What is the bias-variance tradeoff?",
                [
                    "Balancing underfitting-related bias and variance from sensitivity to training data",
                    "Choosing CPU versus GPU",
                    "Balancing train and test file sizes",
                    "Choosing between labels and features"
                ],
                "Balancing underfitting-related bias and variance from sensitivity to training data"
            ),

            (
                "Why can accuracy be misleading on highly imbalanced classification data?",
                [
                    "A majority class can dominate the accuracy value",
                    "Accuracy cannot be calculated",
                    "Accuracy always equals recall",
                    "Imbalanced data has no labels"
                ],
                "A majority class can dominate the accuracy value"
            ),

            (
                "What is calibration in probabilistic classification?",
                [
                    "Agreement between predicted probabilities and observed frequencies",
                    "Increasing model depth",
                    "Reducing dataset size",
                    "Sorting probabilities"
                ],
                "Agreement between predicted probabilities and observed frequencies"
            ),

            (
                "Why should preprocessing be fitted only on training data?",
                [
                    "To avoid leaking information from validation or test data",
                    "To increase test accuracy artificially",
                    "To remove labels",
                    "To guarantee a larger dataset"
                ],
                "To avoid leaking information from validation or test data"
            ),

            (
                "What is early stopping commonly used for?",
                [
                    "Stopping training when validation performance stops improving",
                    "Removing the validation set",
                    "Increasing every parameter",
                    "Creating new labels"
                ],
                "Stopping training when validation performance stops improving"
            ),

            (
                "What does ROC-AUC broadly measure?",
                [
                    "Ranking ability across classification thresholds",
                    "Regression error only",
                    "Number of training samples",
                    "Neural network depth"
                ],
                "Ranking ability across classification thresholds"
            ),

            (
                "Why can a model with more parameters generalize worse?",
                [
                    "Greater capacity can allow it to fit noise or training-specific patterns",
                    "More parameters always reduce accuracy",
                    "Parameters cannot represent patterns",
                    "Training becomes impossible by definition"
                ],
                "Greater capacity can allow it to fit noise or training-specific patterns"
            ),

            (
                "What is hyperparameter tuning?",
                [
                    "Selecting configuration values that control the learning process",
                    "Changing labels after testing",
                    "Adding test data to training",
                    "Changing the target after prediction"
                ],
                "Selecting configuration values that control the learning process"
            )
        ]

    return expand_templates(
        "ML",
        "Machine Learning",
        difficulty,
        templates
    )


# ============================================================
# DEEP LEARNING QUESTION POOL
# ============================================================

def generate_dl_questions(difficulty):

    if difficulty == "Basic":

        templates = [

            (
                "What is a neural network?",
                [
                    "A model made of connected computational units",
                    "A database",
                    "A programming language",
                    "A web browser"
                ],
                "A model made of connected computational units"
            ),

            (
                "What does an activation function provide?",
                [
                    "Non-linearity",
                    "Database storage",
                    "File compression",
                    "Internet access"
                ],
                "Non-linearity"
            ),

            (
                "What is a neuron in a neural network?",
                [
                    "A computational unit combining inputs and weights",
                    "A database row",
                    "A file",
                    "A Python package"
                ],
                "A computational unit combining inputs and weights"
            ),

            (
                "What is an epoch?",
                [
                    "One complete pass through the training data",
                    "One feature",
                    "One class",
                    "One prediction only"
                ],
                "One complete pass through the training data"
            ),

            (
                "What is a batch?",
                [
                    "A subset of training examples processed together",
                    "The entire model",
                    "A database",
                    "A label"
                ],
                "A subset of training examples processed together"
            ),

            (
                "What is a weight?",
                [
                    "A learnable parameter controlling input influence",
                    "A dataset",
                    "A class name",
                    "A filename"
                ],
                "A learnable parameter controlling input influence"
            ),

            (
                "What is a loss function?",
                [
                    "A measure of prediction error",
                    "A database",
                    "A programming language",
                    "A visualization"
                ],
                "A measure of prediction error"
            ),

            (
                "What is training?",
                [
                    "Adjusting model parameters using data",
                    "Deleting data",
                    "Writing HTML",
                    "Installing Python"
                ],
                "Adjusting model parameters using data"
            ),

            (
                "What is a CNN commonly associated with?",
                [
                    "Image processing",
                    "Database indexing",
                    "File storage",
                    "Operating systems"
                ],
                "Image processing"
            ),

            (
                "What is a neural network layer?",
                [
                    "A group or stage of computational units",
                    "A database",
                    "A file format",
                    "A web page"
                ],
                "A group or stage of computational units"
            )
        ]

    elif difficulty == "Intermediate":

        templates = [

            (
                "What is backpropagation?",
                [
                    "Computing gradients used to update network parameters",
                    "Saving the model",
                    "Creating a dataset",
                    "Sorting inputs"
                ],
                "Computing gradients used to update network parameters"
            ),

            (
                "What is an optimizer?",
                [
                    "An algorithm that updates model parameters",
                    "A dataset",
                    "A neural network layer",
                    "A file format"
                ],
                "An algorithm that updates model parameters"
            ),

            (
                "Why can ReLU help deep networks?",
                [
                    "It introduces non-linearity while avoiding saturation for positive inputs",
                    "It stores data",
                    "It removes all gradients",
                    "It guarantees no overfitting"
                ],
                "It introduces non-linearity while avoiding saturation for positive inputs"
            ),

            (
                "What is dropout?",
                [
                    "Randomly disabling units during training",
                    "Deleting the dataset",
                    "Increasing image size",
                    "Removing labels"
                ],
                "Randomly disabling units during training"
            ),

            (
                "What is convolution useful for?",
                [
                    "Learning local patterns using shared filters",
                    "Sorting data",
                    "Creating databases",
                    "Removing all features"
                ],
                "Learning local patterns using shared filters"
            ),

            (
                "What is pooling commonly used for?",
                [
                    "Reducing spatial dimensions",
                    "Increasing the number of labels",
                    "Creating text",
                    "Storing weights"
                ],
                "Reducing spatial dimensions"
            ),

            (
                "What is a learning rate?",
                [
                    "A value controlling the size of parameter updates",
                    "The number of classes",
                    "Dataset size",
                    "Number of layers"
                ],
                "A value controlling the size of parameter updates"
            ),

            (
                "What is vanishing gradient?",
                [
                    "Gradients becoming extremely small during backpropagation",
                    "Dataset becoming empty",
                    "Weights becoming strings",
                    "Training data increasing"
                ],
                "Gradients becoming extremely small during backpropagation"
            ),

            (
                "What is batch normalization used for?",
                [
                    "Stabilizing and improving optimization of neural network training",
                    "Creating labels",
                    "Compressing images",
                    "Removing all layers"
                ],
                "Stabilizing and improving optimization of neural network training"
            ),

            (
                "What is transfer learning?",
                [
                    "Using knowledge from a pretrained model for another task",
                    "Moving files between computers",
                    "Changing a dataset format",
                    "Deleting pretrained weights"
                ],
                "Using knowledge from a pretrained model for another task"
            )
        ]

    else:

        templates = [

            (
                "Why does backpropagation use the chain rule?",
                [
                    "To compute how the loss changes with respect to parameters through multiple operations",
                    "To sort model parameters",
                    "To remove all nonlinearities",
                    "To create training labels"
                ],
                "To compute how the loss changes with respect to parameters through multiple operations"
            ),

            (
                "What does self-attention allow a model to do?",
                [
                    "Weight relationships between different input positions",
                    "Delete tokens",
                    "Remove all context",
                    "Only process one token"
                ],
                "Weight relationships between different input positions"
            ),

            (
                "Why are residual connections useful in deep networks?",
                [
                    "They help information and gradients flow through many layers",
                    "They remove the need for data",
                    "They guarantee perfect accuracy",
                    "They eliminate parameters"
                ],
                "They help information and gradients flow through many layers"
            ),

            (
                "What is the purpose of positional information in transformers?",
                [
                    "Provide information about token order",
                    "Remove token embeddings",
                    "Replace attention",
                    "Store model weights"
                ],
                "Provide information about token order"
            ),

            (
                "Why can Adam converge differently from plain SGD?",
                [
                    "It adapts updates using estimates of gradient moments",
                    "It never uses gradients",
                    "It has no learning rate",
                    "It cannot train neural networks"
                ],
                "It adapts updates using estimates of gradient moments"
            ),

            (
                "What is gradient clipping used for?",
                [
                    "Limiting excessively large gradients",
                    "Increasing dataset size",
                    "Removing labels",
                    "Increasing sequence length"
                ],
                "Limiting excessively large gradients"
            ),

            (
                "Why can increasing model depth make optimization difficult?",
                [
                    "Gradients can become unstable as they propagate through many layers",
                    "More layers always remove information",
                    "Deep models cannot use gradients",
                    "Depth prevents parameter updates"
                ],
                "Gradients can become unstable as they propagate through many layers"
            ),

            (
                "What is an encoder in the transformer architecture commonly used for?",
                [
                    "Building contextual representations of input tokens",
                    "Only generating random numbers",
                    "Deleting the input",
                    "Storing databases"
                ],
                "Building contextual representations of input tokens"
            ),

            (
                "What is a decoder in an autoregressive transformer commonly responsible for?",
                [
                    "Generating outputs conditioned on previous context",
                    "Only normalizing data",
                    "Removing all tokens",
                    "Creating training labels manually"
                ],
                "Generating outputs conditioned on previous context"
            ),

            (
                "Why can attention complexity become expensive for long sequences?",
                [
                    "Pairwise interactions can grow rapidly with sequence length",
                    "Attention uses no computation",
                    "Long sequences contain no tokens",
                    "Transformers have fixed one-token inputs"
                ],
                "Pairwise interactions can grow rapidly with sequence length"
            )
        ]

    return expand_templates(
        "DL",
        "Deep Learning",
        difficulty,
        templates
    )


# ============================================================
# GENERATIVE AI QUESTION POOL
# ============================================================

def generate_genai_questions(difficulty):

    if difficulty == "Basic":

        templates = [

            (
                "What does Generative AI do?",
                [
                    "Generates new content",
                    "Only stores data",
                    "Only sorts files",
                    "Only calculates averages"
                ],
                "Generates new content"
            ),

            (
                "What does LLM stand for?",
                [
                    "Large Language Model",
                    "Long Learning Machine",
                    "Large Logic Machine",
                    "Language Learning Method"
                ],
                "Large Language Model"
            ),

            (
                "What is a prompt?",
                [
                    "An instruction or input given to an AI model",
                    "A database",
                    "A programming language",
                    "A hardware component"
                ],
                "An instruction or input given to an AI model"
            ),

            (
                "What is a token?",
                [
                    "A unit of text processed by a language model",
                    "A database",
                    "A GPU",
                    "A password"
                ],
                "A unit of text processed by a language model"
            ),

            (
                "What can a generative model produce?",
                [
                    "New text, images or other content",
                    "Only spreadsheets",
                    "Only databases",
                    "Only hardware"
                ],
                "New text, images or other content"
            ),

            (
                "What is an AI chatbot?",
                [
                    "A system that interacts with users using AI",
                    "A database table",
                    "A compiler",
                    "A file format"
                ],
                "A system that interacts with users using AI"
            ),

            (
                "What does AI stand for?",
                [
                    "Artificial Intelligence",
                    "Automated Internet",
                    "Artificial Internet",
                    "Advanced Input"
                ],
                "Artificial Intelligence"
            ),

            (
                "What is text generation?",
                [
                    "Producing text from an AI model",
                    "Deleting text",
                    "Sorting files",
                    "Compressing images"
                ],
                "Producing text from an AI model"
            ),

            (
                "What is an image generation model designed to do?",
                [
                    "Generate images from learned patterns or prompts",
                    "Only store images",
                    "Only resize images",
                    "Only delete images"
                ],
                "Generate images from learned patterns or prompts"
            ),

            (
                "Why are prompts important?",
                [
                    "They provide instructions or context to the model",
                    "They replace the model",
                    "They store the GPU",
                    "They delete tokens"
                ],
                "They provide instructions or context to the model"
            )
        ]

    elif difficulty == "Intermediate":

        templates = [

            (
                "What are embeddings?",
                [
                    "Numerical representations of information",
                    "Images only",
                    "Databases",
                    "Programming languages"
                ],
                "Numerical representations of information"
            ),

            (
                "What does RAG stand for?",
                [
                    "Retrieval-Augmented Generation",
                    "Random AI Generation",
                    "Rapid Application Generation",
                    "Retrieval AI Graph"
                ],
                "Retrieval-Augmented Generation"
            ),

            (
                "Why is context important for an LLM?",
                [
                    "It provides relevant information for generating a response",
                    "It increases screen size",
                    "It replaces Python",
                    "It removes tokens"
                ],
                "It provides relevant information for generating a response"
            ),

            (
                "What is a vector database commonly used for?",
                [
                    "Storing and retrieving vector embeddings",
                    "Running Python only",
                    "Creating CPUs",
                    "Managing operating systems"
                ],
                "Storing and retrieving vector embeddings"
            ),

            (
                "What is semantic search?",
                [
                    "Searching based on meaning or similarity",
                    "Searching only exact characters",
                    "Searching file names only",
                    "Searching databases by row number"
                ],
                "Searching based on meaning or similarity"
            ),

            (
                "What is prompt engineering?",
                [
                    "Designing prompts to guide model behavior",
                    "Building GPUs",
                    "Creating databases only",
                    "Writing operating systems"
                ],
                "Designing prompts to guide model behavior"
            ),

            (
                "What is context window?",
                [
                    "The amount of input/output context a model can process within its limit",
                    "The size of the computer screen",
                    "The number of GPUs",
                    "The number of databases"
                ],
                "The amount of input/output context a model can process within its limit"
            ),

            (
                "What is hallucination in generative AI?",
                [
                    "Unsupported or incorrect generated information",
                    "A faster model",
                    "A larger database",
                    "A training label"
                ],
                "Unsupported or incorrect generated information"
            ),

            (
                "What is grounding?",
                [
                    "Constraining responses using reliable external information",
                    "Increasing randomness",
                    "Removing context",
                    "Deleting embeddings"
                ],
                "Constraining responses using reliable external information"
            ),

            (
                "Why are embeddings useful for RAG?",
                [
                    "They allow semantic similarity search over information",
                    "They replace the language model",
                    "They remove documents",
                    "They eliminate retrieval"
                ],
                "They allow semantic similarity search over information"
            )
        ]

    else:

        templates = [

            (
                "What is fine-tuning?",
                [
                    "Further training a pretrained model on task-specific data",
                    "Deleting pretrained weights",
                    "Changing the UI",
                    "Increasing screen resolution"
                ],
                "Further training a pretrained model on task-specific data"
            ),

            (
                "Why can RAG reduce hallucination?",
                [
                    "It can provide the model with relevant retrieved information",
                    "It guarantees every response is correct",
                    "It removes the model",
                    "It prevents all reasoning"
                ],
                "It can provide the model with relevant retrieved information"
            ),

            (
                "What is temperature in text generation?",
                [
                    "A parameter influencing randomness in token selection",
                    "GPU temperature",
                    "Context window size",
                    "Number of documents"
                ],
                "A parameter influencing randomness in token selection"
            ),

            (
                "Why can increasing temperature change model outputs?",
                [
                    "It changes the randomness of token sampling",
                    "It changes the model architecture",
                    "It changes the training dataset",
                    "It changes the embedding dimension"
                ],
                "It changes the randomness of token sampling"
            ),

            (
                "What is chunking in RAG?",
                [
                    "Splitting documents into smaller retrievable pieces",
                    "Deleting documents",
                    "Training the GPU",
                    "Changing model weights"
                ],
                "Splitting documents into smaller retrievable pieces"
            ),

            (
                "Why does chunk size matter in RAG?",
                [
                    "It affects retrieval granularity and the context supplied to the model",
                    "It determines GPU temperature",
                    "It always determines accuracy",
                    "It removes embeddings"
                ],
                "It affects retrieval granularity and the context supplied to the model"
            ),

            (
                "What is instruction tuning?",
                [
                    "Training a model to better follow natural-language instructions",
                    "Compressing prompts",
                    "Deleting instructions",
                    "Changing hardware"
                ],
                "Training a model to better follow natural-language instructions"
            ),

            (
                "What is multimodal AI?",
                [
                    "AI systems that work with multiple modalities such as text and images",
                    "AI using multiple CPUs only",
                    "AI without data",
                    "AI using one token only"
                ],
                "AI systems that work with multiple modalities such as text and images"
            ),

            (
                "What is retrieval reranking?",
                [
                    "Reordering retrieved candidates using a relevance model or scoring method",
                    "Deleting retrieved documents",
                    "Generating embeddings again without comparison",
                    "Changing the language model architecture"
                ],
                "Reordering retrieved candidates using a relevance model or scoring method"
            ),

            (
                "What is the purpose of an evaluation set for an LLM application?",
                [
                    "Measure behavior against representative expected outcomes",
                    "Increase GPU memory",
                    "Store passwords",
                    "Replace production data automatically"
                ],
                "Measure behavior against representative expected outcomes"
            )
        ]

    return expand_templates(
        "GEN",
        "Generative AI",
        difficulty,
        templates
    )


# ============================================================
# EXPAND 10 CORE QUESTIONS INTO A 100 QUESTION POOL
# ============================================================
#
# The first 10 questions are carefully designed.
#
# We create additional variants using question IDs and
# controlled variations so the random selection system has
# a large pool.
#
# ============================================================

def expand_templates(
    prefix,
    subject,
    difficulty,
    templates
):

    questions = []

    # First add the original high-quality questions.

    for index, item in enumerate(
        templates
    ):

        question, options, answer = item

        questions.append(
            make_question(
                f"{prefix}_{difficulty}_{index + 1}",
                subject,
                difficulty,
                question,
                options,
                answer
            )
        )

    # --------------------------------------------------------
    # Controlled variants
    # --------------------------------------------------------

    variant_number = 11

    for original in templates:

        question = original[0]
        options = original[1]
        answer = original[2]

        for variation in [
            "Which statement is most accurate?",
            "Which option best describes this concept?",
            "Which answer is technically correct?",
            "Which choice best explains the idea?",
            "Which statement would an AI practitioner select?"
        ]:

            variant_question = (
                variation
                + "\n\n"
                + question
            )

            questions.append(
                make_question(
                    f"{prefix}_{difficulty}_{variant_number}",
                    subject,
                    difficulty,
                    variant_question,
                    options.copy(),
                    answer
                )
            )

            variant_number += 1

    # --------------------------------------------------------
    # Additional variants with option-order differences
    # --------------------------------------------------------

    base_questions = questions.copy()

    while len(questions) < 100:

        source = random.choice(
            base_questions
        )

        new_id = (
            f"{prefix}_{difficulty}_"
            f"{len(questions) + 1}"
        )

        questions.append(
            make_question(
                new_id,
                subject,
                difficulty,
                source["question"],
                source["options"].copy(),
                source["answer"]
            )
        )

    return questions[:100]


# ============================================================
# BUILD COMPLETE QUESTION POOL
# ============================================================

def build_question_pool(level):

    if level == "Complete Beginner":

        difficulty = "Basic"

    elif level == "Intermediate":

        difficulty = "Intermediate"

    else:

        difficulty = "Advanced"

    pools = {

        "Python": generate_python_questions(
            difficulty
        ),

        "Mathematics & Statistics":
            generate_math_questions(
                difficulty
            ),

        "Machine Learning":
            generate_ml_questions(
                difficulty
            ),

        "Deep Learning":
            generate_dl_questions(
                difficulty
            ),

        "Generative AI":
            generate_genai_questions(
                difficulty
            )
    }

    return pools, difficulty


# ============================================================
# CREATE NEW RANDOM DIAGNOSTIC
# ============================================================

def create_new_diagnostic(level):

    pools, difficulty = build_question_pool(
        level
    )

    selected_questions = []

    for subject in SUBJECTS:

        pool = pools[subject]

        # Avoid questions already used by this learner.

        available = [
            q
            for q in pool
            if q["id"]
            not in st.session_state.used_question_ids
        ]

        # If the learner has eventually used the whole
        # pool, allow the pool to reset.

        if len(available) < 3:

            available = pool

        chosen = random.sample(
            available,
            3
        )

        for question in chosen:

            # Make a separate copy.

            q = question.copy()

            q["options"] = question[
                "options"
            ].copy()

            # Shuffle options.

            random.shuffle(
                q["options"]
            )

            selected_questions.append(
                q
            )

            st.session_state.used_question_ids.add(
                q["id"]
            )

    # Shuffle the complete 15-question sequence.

    random.shuffle(
        selected_questions
    )

    st.session_state.questions = (
        selected_questions
    )

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
            q
            for q in st.session_state.questions
            if q["subject"] == subject
        ]

        correct = 0

        for q in subject_questions:

            if q.get("selected") == q["answer"]:

                correct += 1

        if subject_questions:

            scores[subject] = round(
                (
                    correct
                    / len(subject_questions)
                )
                * 100
            )

        else:

            scores[subject] = None

    return scores


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
# ROADMAP
# ============================================================

def create_roadmap(scores):

    assessed = {
        subject: score
        for subject, score in scores.items()
        if score is not None
    }

    return sorted(
        assessed.items(),
        key=lambda item: item[1]
    )


# ============================================================
# RESET EVERYTHING
# ============================================================

def reset_all():

    st.session_state.questions = []

    st.session_state.current_question = 0

    st.session_state.answers = []

    st.session_state.diagnostic_complete = False

    st.session_state.domain_scores = {}

    st.session_state.roadmap = []

    st.session_state.used_question_ids = set()

    st.session_state.attempt_number = 0


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🤖 AI StudyMate")

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
        "🧠 AI Diagnostic",
        use_container_width=True
    ):

        st.session_state.page = "diagnostic"

        st.rerun()

    if st.button(
        "🗺️ Knowledge Map",
        use_container_width=True
    ):

        st.session_state.page = "knowledge_map"

        st.rerun()

    if st.button(
        "📚 My Roadmap",
        use_container_width=True
    ):

        st.session_state.page = "roadmap"

        st.rerun()


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "home":

    st.title("AI StudyMate")

    st.subheader(
        "Your personalised journey to learn Artificial Intelligence."
    )

    st.write(
        "AI StudyMate understands what you already know, "
        "identifies knowledge gaps, and creates a learning "
        "journey around your level and goals."
    )

    st.divider()

    st.markdown(
        "## 👤 Tell us about yourself"
    )

    with st.form(
        "profile_form"
    ):

        name = st.text_input(
            "Your Name"
        )

        level = st.selectbox(
            "Current AI Level",
            [
                "Complete Beginner",
                "Intermediate",
                "Advanced"
            ]
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
            "How much time can you study each day?",
            [
                "15 minutes",
                "30 minutes",
                "1 hour",
                "2+ hours"
            ]
        )

        submitted = st.form_submit_button(
            "Start AI Journey 🚀",
            use_container_width=True
        )

    if submitted:

        if not name.strip():

            st.warning(
                "Please enter your name before starting."
            )

        else:

            st.session_state.profile = {

                "name": name,

                "level": level,

                "goal": goal,

                "study_time": study_time
            }

            # New learner = fresh diagnostic history.

            st.session_state.used_question_ids = set()

            st.session_state.attempt_number = 0

            create_new_diagnostic(
                level
            )

            st.session_state.page = "diagnostic"

            st.rerun()


# ============================================================
# DIAGNOSTIC
# ============================================================

elif st.session_state.page == "diagnostic":

    if not st.session_state.questions:

        st.warning(
            "Please complete your learner profile first."
        )

        if st.button(
            "Go to Home",
            use_container_width=True
        ):

            st.session_state.page = "home"

            st.rerun()

    elif st.session_state.diagnostic_complete:

        st.success(
            "Your diagnostic is complete!"
        )

        st.title(
            "Diagnostic Completed"
        )

        st.write(
            f"Attempt {st.session_state.attempt_number} "
            "has been completed."
        )

        st.write(
            "Your answers have been analysed. "
            "Open your Knowledge Map to see your results."
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "🗺️ View Knowledge Map",
                use_container_width=True
            ):

                st.session_state.page = (
                    "knowledge_map"
                )

                st.rerun()

        with col2:

            if st.button(
                "🔄 Retake Diagnostic",
                use_container_width=True
            ):

                level = st.session_state.profile[
                    "level"
                ]

                create_new_diagnostic(
                    level
                )

                st.rerun()

    else:

        total_questions = len(
            st.session_state.questions
        )

        current_index = (
            st.session_state.current_question
        )

        current_question = (
            st.session_state.questions[
                current_index
            ]
        )

        question_number = (
            current_index + 1
        )

        st.title(
            "🧠 AI Knowledge Diagnostic"
        )

        st.write(
            f"Attempt {st.session_state.attempt_number}"
        )

        st.write(
            f"Question {question_number} "
            f"of {total_questions}"
        )

        st.progress(
            question_number
            / total_questions
        )

        st.divider()

        st.markdown(
            f"### {current_question['subject']}"
        )

        st.caption(
            f"Difficulty: "
            f"{current_question['difficulty']}"
        )

        st.markdown(
            f"## {current_question['question']}"
        )

        selected = st.radio(
            "Select your answer:",
            current_question["options"],
            index=None,
            key=f"question_{current_index}_{st.session_state.attempt_number}"
        )

        st.write("")

        if st.button(
            "Next Question →",
            use_container_width=True
        ):

            if selected is None:

                st.warning(
                    "Please select an answer before continuing."
                )

            else:

                # Store silently.
                # No answer feedback is shown.

                st.session_state.questions[
                    current_index
                ]["selected"] = selected

                st.session_state.answers.append(
                    selected
                )

                if (
                    current_index
                    <
                    total_questions - 1
                ):

                    st.session_state.current_question += 1

                else:

                    scores = calculate_scores()

                    st.session_state.domain_scores = (
                        scores
                    )

                    st.session_state.roadmap = (
                        create_roadmap(scores)
                    )

                    st.session_state.diagnostic_complete = True

                st.rerun()


# ============================================================
# KNOWLEDGE MAP
# ============================================================

elif st.session_state.page == "knowledge_map":

    if not st.session_state.diagnostic_complete:

        st.warning(
            "Complete the diagnostic first."
        )

    else:

        st.title(
            "Your AI Knowledge Map"
        )

        st.write(
            "Your scores are based on your performance "
            "in the diagnostic assessment."
        )

        st.divider()

        scores = (
            st.session_state.domain_scores
        )

        for subject in SUBJECTS:

            score = scores.get(
                subject
            )

            # COURSE NAME

            st.markdown(
                f"<h2 style='margin-bottom: 5px;'>"
                f"{subject}"
                f"</h2>",
                unsafe_allow_html=True
            )

            if score is None:

                st.info(
                    "Not Assessed"
                )

            else:

                st.progress(
                    score / 100
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.markdown(
                        "<div style='font-size:15px;"
                        "font-weight:600;'>"
                        "Knowledge Score"
                        "</div>",
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"<div style='font-size:20px;"
                        f"font-weight:500;'>"
                        f"{score}%"
                        f"</div>",
                        unsafe_allow_html=True
                    )

                with col2:

                    st.markdown(
                        "<div style='font-size:15px;"
                        "font-weight:600;'>"
                        "Status"
                        "</div>",
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"<div style='font-size:20px;"
                        f"font-weight:500;'>"
                        f"{get_status(score)}"
                        f"</div>",
                        unsafe_allow_html=True
                    )

            st.write("")

            st.divider()

        assessed = {
            subject: score
            for subject, score in scores.items()
            if score is not None
        }

        if assessed:

            weakest_subject = min(
                assessed,
                key=assessed.get
            )

            weakest_score = assessed[
                weakest_subject
            ]

            st.markdown(
                "## Recommended Starting Point"
            )

            st.success(
                f"{weakest_subject} — "
                f"{weakest_score}%"
            )

            if weakest_score < 40:

                st.write(
                    f"Your diagnostic indicates that you "
                    f"should build a strong foundation in "
                    f"{weakest_subject}."
                )

            elif weakest_score < 70:

                st.write(
                    f"You have some understanding of "
                    f"{weakest_subject}, but additional "
                    "practice will strengthen your foundation."
                )

            elif weakest_score < 100:

                st.write(
                    f"You have a good foundation in "
                    f"{weakest_subject}. More practice "
                    "can help you progress further."
                )

            else:

                st.write(
                    f"You demonstrated strong performance "
                    f"in {weakest_subject}."
                )

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "📚 View Personalised Roadmap",
                use_container_width=True
            ):

                st.session_state.page = "roadmap"

                st.rerun()

        with col2:

            if st.button(
                "🔄 Retake Diagnostic",
                use_container_width=True
            ):

                level = st.session_state.profile[
                    "level"
                ]

                create_new_diagnostic(
                    level
                )

                st.rerun()


# ============================================================
# ROADMAP
# ============================================================

elif st.session_state.page == "roadmap":

    st.title(
        "📚 My Personalised AI Roadmap"
    )

    if not st.session_state.diagnostic_complete:

        st.info(
            "Complete the AI Diagnostic to generate "
            "your personalised roadmap."
        )

        if st.button(
            "Start Diagnostic",
            use_container_width=True
        ):

            st.session_state.page = "diagnostic"

            st.rerun()

    else:

        profile = (
            st.session_state.profile
        )

        if profile:

            st.write(
                f"Great work, **{profile['name']}**."
            )

            st.write(
                f"Your roadmap is based on your current "
                f"level (**{profile['level']}**), your goal "
                f"(**{profile['goal']}**), and your diagnostic "
                f"performance."
            )

        st.divider()

        st.markdown(
            "## Your Learning Order"
        )

        roadmap = (
            st.session_state.roadmap
        )

        for index, item in enumerate(
            roadmap,
            start=1
        ):

            subject, score = item

            st.markdown(
                f"### {index}. {subject}"
            )

            st.write(
                f"Knowledge Score: **{score}%**"
            )

            st.progress(
                score / 100
            )

            if score < 40:

                st.info(
                    "Start with the fundamentals and "
                    "build your foundation through guided "
                    "lessons and beginner practice."
                )

            elif score < 70:

                st.info(
                    "Strengthen this area with targeted "
                    "practice and intermediate concepts."
                )

            elif score < 100:

                st.info(
                    "You have a solid foundation. Continue "
                    "with advanced concepts and projects."
                )

            else:

                st.success(
                    "Strong foundation. You can progress "
                    "toward advanced concepts and projects."
                )

            st.divider()

        st.markdown(
            "## 🎯 Next Stage"
        )

        st.write(
            "AI StudyMate will use your diagnostic results "
            "to personalise lessons, practice questions, "
            "difficulty and learning pace."
        )

        if st.button(
            "🔄 Take Diagnostic Again",
            use_container_width=True
        ):

            level = st.session_state.profile[
                "level"
            ]

            create_new_diagnostic(
                level
            )

            st.session_state.page = "diagnostic"

            st.rerun()
