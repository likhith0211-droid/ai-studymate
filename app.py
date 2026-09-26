import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI StudyMate",
    page_icon="AI",
    layout="wide"
)


# ============================================================
# SESSION STATE
# ============================================================

DEFAULTS = {
    "page": "home",
    "profile": {},
    "questions": [],
    "current_question": 0,
    "answers": [],
    "answer_submitted": False,
    "last_answer_correct": None,
    "diagnostic_complete": False,
    "domain_scores": {},
    "roadmap": []
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


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
# QUESTION BANK
# ============================================================
#
# 5 subjects
# 3 questions per subject
# 3 difficulty levels
#
# Complete Beginner -> Basic
# Intermediate      -> Intermediate
# Advanced           -> Advanced
#
# Total diagnostic questions = 15
# ============================================================

QUESTION_BANK = {

    # ========================================================
    # PYTHON
    # ========================================================

    "Python": {

        "Basic": [

            {
                "question": "Which function is commonly used to display output in Python?",
                "options": [
                    "show()",
                    "display()",
                    "print()",
                    "output()"
                ],
                "answer": "print()",
                "explanation": (
                    "The print() function is commonly used to display "
                    "text or values in Python."
                )
            },

            {
                "question": "Which symbol is used to write a comment in Python?",
                "options": [
                    "//",
                    "#",
                    "/* */",
                    "<!-- -->"
                ],
                "answer": "#",
                "explanation": (
                    "In Python, the # symbol is used to write a "
                    "single-line comment."
                )
            },

            {
                "question": "Which of the following is a Python data type?",
                "options": [
                    "Integer",
                    "Browser",
                    "Website",
                    "Folder"
                ],
                "answer": "Integer",
                "explanation": (
                    "Integer, or int, is a built-in Python data type "
                    "used to represent whole numbers."
                )
            }
        ],

        "Intermediate": [

            {
                "question": "Which Python data structure stores data as key-value pairs?",
                "options": [
                    "List",
                    "Tuple",
                    "Dictionary",
                    "Set"
                ],
                "answer": "Dictionary",
                "explanation": (
                    "A Python dictionary stores information using "
                    "key-value pairs."
                )
            },

            {
                "question": "Which keyword is used to define a function in Python?",
                "options": [
                    "function",
                    "define",
                    "def",
                    "func"
                ],
                "answer": "def",
                "explanation": (
                    "Python uses the def keyword to define a function."
                )
            },

            {
                "question": "What is the main purpose of a Python function?",
                "options": [
                    "To reuse a block of code",
                    "To delete Python",
                    "To create hardware",
                    "To shut down the computer"
                ],
                "answer": "To reuse a block of code",
                "explanation": (
                    "Functions allow us to group code into reusable "
                    "blocks that can be called when needed."
                )
            }
        ],

        "Advanced": [

            {
                "question": "What is the main purpose of NumPy in AI and machine learning?",
                "options": [
                    "Building web pages",
                    "Numerical and array-based computation",
                    "Sending emails",
                    "Managing passwords"
                ],
                "answer": "Numerical and array-based computation",
                "explanation": (
                    "NumPy provides efficient numerical operations "
                    "and multidimensional arrays."
                )
            },

            {
                "question": "What is the primary purpose of Pandas?",
                "options": [
                    "Data manipulation and analysis",
                    "Creating neural networks only",
                    "Designing websites",
                    "Managing computer hardware"
                ],
                "answer": "Data manipulation and analysis",
                "explanation": (
                    "Pandas provides tools and data structures for "
                    "working with structured and tabular data."
                )
            },

            {
                "question": "Why is vectorization useful in numerical computing?",
                "options": [
                    "It avoids using variables",
                    "It allows efficient operations on arrays",
                    "It converts Python into Java",
                    "It removes all data"
                ],
                "answer": "It allows efficient operations on arrays",
                "explanation": (
                    "Vectorized operations allow calculations to be "
                    "performed efficiently across arrays."
                )
            }
        ]
    },


    # ========================================================
    # MATHEMATICS & STATISTICS
    # ========================================================

    "Mathematics & Statistics": {

        "Basic": [

            {
                "question": "What is the mean of 2, 4 and 6?",
                "options": [
                    "2",
                    "4",
                    "6",
                    "12"
                ],
                "answer": "4",
                "explanation": (
                    "The mean is calculated as "
                    "(2 + 4 + 6) / 3 = 4."
                )
            },

            {
                "question": "What does probability measure?",
                "options": [
                    "The likelihood of an event",
                    "The size of a computer",
                    "The speed of a program",
                    "The number of files"
                ],
                "answer": "The likelihood of an event",
                "explanation": (
                    "Probability describes how likely an event is "
                    "to occur."
                )
            },

            {
                "question": "Which of these is a mathematical operation?",
                "options": [
                    "Addition",
                    "Browser",
                    "Database",
                    "Keyboard"
                ],
                "answer": "Addition",
                "explanation": (
                    "Addition is one of the basic arithmetic operations."
                )
            }
        ],

        "Intermediate": [

            {
                "question": "What does standard deviation measure?",
                "options": [
                    "Data spread around the mean",
                    "The number of columns",
                    "The maximum value only",
                    "The number of samples only"
                ],
                "answer": "Data spread around the mean",
                "explanation": (
                    "Standard deviation measures how spread out values "
                    "are around their mean."
                )
            },

            {
                "question": "What is a vector in linear algebra?",
                "options": [
                    "A quantity represented by components",
                    "Only a single number",
                    "A programming language",
                    "A database table"
                ],
                "answer": "A quantity represented by components",
                "explanation": (
                    "A vector can represent a quantity using an "
                    "ordered collection of components."
                )
            },

            {
                "question": "If the probability of an event is 0, what does it mean?",
                "options": [
                    "The event is certain",
                    "The event is impossible",
                    "The event is likely",
                    "The event is guaranteed"
                ],
                "answer": "The event is impossible",
                "explanation": (
                    "A probability of 0 represents an impossible event."
                )
            }
        ],

        "Advanced": [

            {
                "question": "Why are gradients important in machine learning?",
                "options": [
                    "They help optimize model parameters",
                    "They store datasets",
                    "They create HTML pages",
                    "They replace all training data"
                ],
                "answer": "They help optimize model parameters",
                "explanation": (
                    "Gradients indicate how a function changes and are "
                    "used by optimization algorithms such as gradient descent."
                )
            },

            {
                "question": "What does covariance describe?",
                "options": [
                    "How two variables change together",
                    "The maximum of one variable",
                    "The number of rows",
                    "The size of a neural network"
                ],
                "answer": "How two variables change together",
                "explanation": (
                    "Covariance indicates the direction in which "
                    "two variables tend to vary together."
                )
            },

            {
                "question": "What is the purpose of a loss function in machine learning?",
                "options": [
                    "Measure prediction error",
                    "Store the model",
                    "Create a dataset",
                    "Display a graph only"
                ],
                "answer": "Measure prediction error",
                "explanation": (
                    "A loss function measures the difference between "
                    "a model's predictions and the target values."
                )
            }
        ]
    },


    # ========================================================
    # MACHINE LEARNING
    # ========================================================

    "Machine Learning": {

        "Basic": [

            {
                "question": "What is machine learning?",
                "options": [
                    "A way for computers to learn patterns from data",
                    "A type of keyboard",
                    "A web browser",
                    "A file format"
                ],
                "answer": "A way for computers to learn patterns from data",
                "explanation": (
                    "Machine learning allows systems to learn patterns "
                    "from data and use them for predictions or decisions."
                )
            },

            {
                "question": "What is a training dataset?",
                "options": [
                    "Data used to train a model",
                    "A computer monitor",
                    "A programming language",
                    "A web page"
                ],
                "answer": "Data used to train a model",
                "explanation": (
                    "Training data is used by a machine learning "
                    "algorithm to learn patterns."
                )
            },

            {
                "question": "Which is an example of supervised learning?",
                "options": [
                    "Learning from labelled examples",
                    "Deleting data",
                    "Drawing a website",
                    "Compressing a file"
                ],
                "answer": "Learning from labelled examples",
                "explanation": (
                    "Supervised learning uses examples where the "
                    "desired target or label is known."
                )
            }
        ],

        "Intermediate": [

            {
                "question": "What is overfitting?",
                "options": [
                    "A model performs well on training data but poorly on unseen data",
                    "A model has no parameters",
                    "A dataset contains no rows",
                    "A computer runs out of electricity"
                ],
                "answer": "A model performs well on training data but poorly on unseen data",
                "explanation": (
                    "Overfitting happens when a model learns the "
                    "training data too closely and fails to generalize."
                )
            },

            {
                "question": "Which task is an example of classification?",
                "options": [
                    "Predicting whether an email is spam",
                    "Predicting house price",
                    "Calculating an average",
                    "Sorting file names"
                ],
                "answer": "Predicting whether an email is spam",
                "explanation": (
                    "Classification predicts a category or class, "
                    "such as spam or not spam."
                )
            },

            {
                "question": "Why do we split data into training and testing sets?",
                "options": [
                    "To evaluate how well the model generalizes",
                    "To make the computer faster",
                    "To remove all data",
                    "To avoid using features"
                ],
                "answer": "To evaluate how well the model generalizes",
                "explanation": (
                    "The test set contains unseen examples that help "
                    "evaluate model performance."
                )
            }
        ],

        "Advanced": [

            {
                "question": "What is feature engineering?",
                "options": [
                    "Creating or transforming input features to improve a model",
                    "Building computer hardware",
                    "Deleting the target variable",
                    "Writing only documentation"
                ],
                "answer": "Creating or transforming input features to improve a model",
                "explanation": (
                    "Feature engineering involves creating useful "
                    "representations of input data for machine learning."
                )
            },

            {
                "question": "What is the purpose of cross-validation?",
                "options": [
                    "Estimate model performance across multiple data splits",
                    "Create a neural network",
                    "Remove all features",
                    "Convert Python to C++"
                ],
                "answer": "Estimate model performance across multiple data splits",
                "explanation": (
                    "Cross-validation evaluates a model using different "
                    "train-validation splits."
                )
            },

            {
                "question": "What does regularization attempt to reduce?",
                "options": [
                    "Overfitting",
                    "Training data",
                    "Number of classes",
                    "Input features always"
                ],
                "answer": "Overfitting",
                "explanation": (
                    "Regularization adds constraints or penalties that "
                    "can help reduce overfitting."
                )
            }
        ]
    },


    # ========================================================
    # DEEP LEARNING
    # ========================================================

    "Deep Learning": {

        "Basic": [

            {
                "question": "What is a neural network?",
                "options": [
                    "A model inspired by interconnected neurons",
                    "A database",
                    "A web browser",
                    "A computer cable"
                ],
                "answer": "A model inspired by interconnected neurons",
                "explanation": (
                    "Neural networks are machine learning models "
                    "made of interconnected computational units."
                )
            },

            {
                "question": "What is a neuron in a neural network?",
                "options": [
                    "A computational unit",
                    "A dataset",
                    "A programming language",
                    "A file"
                ],
                "answer": "A computational unit",
                "explanation": (
                    "A neuron receives inputs, applies weights and "
                    "an activation function, and produces an output."
                )
            },

            {
                "question": "What is an epoch?",
                "options": [
                    "One complete pass through the training data",
                    "A type of dataset",
                    "A programming language",
                    "A hardware component"
                ],
                "answer": "One complete pass through the training data",
                "explanation": (
                    "An epoch represents one complete pass through "
                    "the training dataset."
                )
            }
        ],

        "Intermediate": [

            {
                "question": "What is an activation function used for?",
                "options": [
                    "Introducing non-linearity into a neural network",
                    "Storing datasets",
                    "Creating web pages",
                    "Removing all weights"
                ],
                "answer": "Introducing non-linearity into a neural network",
                "explanation": (
                    "Activation functions allow neural networks to "
                    "model complex non-linear relationships."
                )
            },

            {
                "question": "What is backpropagation used for?",
                "options": [
                    "Computing gradients for updating weights",
                    "Collecting datasets",
                    "Creating labels",
                    "Deploying a website"
                ],
                "answer": "Computing gradients for updating weights",
                "explanation": (
                    "Backpropagation calculates gradients of the loss "
                    "with respect to model parameters."
                )
            },

            {
                "question": "What does a learning rate control?",
                "options": [
                    "The size of parameter updates during optimization",
                    "The number of datasets",
                    "The number of classes only",
                    "The size of the computer screen"
                ],
                "answer": "The size of parameter updates during optimization",
                "explanation": (
                    "The learning rate controls how large each "
                    "optimization step is."
                )
            }
        ],

        "Advanced": [

            {
                "question": "Why are convolutional neural networks useful for images?",
                "options": [
                    "They can learn spatial patterns using convolutional filters",
                    "They only process text",
                    "They do not use parameters",
                    "They replace all datasets"
                ],
                "answer": "They can learn spatial patterns using convolutional filters",
                "explanation": (
                    "CNNs use convolution operations to detect "
                    "local spatial patterns in images."
                )
            },

            {
                "question": "What problem does attention help solve in sequence models?",
                "options": [
                    "It allows the model to focus on relevant parts of the input",
                    "It removes all input data",
                    "It converts images into databases",
                    "It eliminates training"
                ],
                "answer": "It allows the model to focus on relevant parts of the input",
                "explanation": (
                    "Attention allows a model to assign different "
                    "importance to different parts of an input."
                )
            },

            {
                "question": "What is a Transformer primarily based on?",
                "options": [
                    "Self-attention mechanisms",
                    "Only convolution",
                    "File compression",
                    "Database indexing"
                ],
                "answer": "Self-attention mechanisms",
                "explanation": (
                    "Transformers use attention mechanisms as a "
                    "central component for processing sequences."
                )
            }
        ]
    },


    # ========================================================
    # GENERATIVE AI
    # ========================================================

    "Generative AI": {

        "Basic": [

            {
                "question": "What does Generative AI do?",
                "options": [
                    "Generates new content",
                    "Only stores files",
                    "Only calculates averages",
                    "Only manages networks"
                ],
                "answer": "Generates new content",
                "explanation": (
                    "Generative AI can create new text, images, "
                    "audio, code and other forms of content."
                )
            },

            {
                "question": "What does LLM stand for?",
                "options": [
                    "Large Language Model",
                    "Local Learning Machine",
                    "Long Logic Method",
                    "Language Learning Memory"
                ],
                "answer": "Large Language Model",
                "explanation": (
                    "LLM stands for Large Language Model."
                )
            },

            {
                "question": "What is a prompt?",
                "options": [
                    "Instructions or input given to an AI model",
                    "A computer keyboard",
                    "A database",
                    "A programming language"
                ],
                "answer": "Instructions or input given to an AI model",
                "explanation": (
                    "A prompt provides instructions or context "
                    "to a generative AI model."
                )
            }
        ],

        "Intermediate": [

            {
                "question": "What is a token in an LLM?",
                "options": [
                    "A unit of text processed by the model",
                    "A computer password",
                    "A database table",
                    "A neural network layer only"
                ],
                "answer": "A unit of text processed by the model",
                "explanation": (
                    "Language models process text as tokens, which "
                    "can represent words, parts of words or other units."
                )
            },

            {
                "question": "What is an embedding?",
                "options": [
                    "A numerical representation of information",
                    "A database password",
                    "A web page",
                    "A programming loop"
                ],
                "answer": "A numerical representation of information",
                "explanation": (
                    "Embeddings represent information such as text "
                    "as numerical vectors."
                )
            },

            {
                "question": "What is the purpose of context in an LLM prompt?",
                "options": [
                    "Provide relevant information for generating a response",
                    "Delete the model",
                    "Increase screen size",
                    "Remove all instructions"
                ],
                "answer": "Provide relevant information for generating a response",
                "explanation": (
                    "Context gives the model additional information "
                    "that can guide its response."
                )
            }
        ],

        "Advanced": [

            {
                "question": "What is Retrieval-Augmented Generation (RAG)?",
                "options": [
                    "Retrieving relevant information before generating an answer",
                    "Training a computer from scratch every time",
                    "Compressing a language model",
                    "Removing the model's context"
                ],
                "answer": "Retrieving relevant information before generating an answer",
                "explanation": (
                    "RAG combines information retrieval with generation "
                    "so a model can use relevant external information."
                )
            },

            {
                "question": "Why are embeddings useful in RAG systems?",
                "options": [
                    "They help represent and retrieve semantically related information",
                    "They replace all language models",
                    "They remove documents",
                    "They create computer hardware"
                ],
                "answer": "They help represent and retrieve semantically related information",
                "explanation": (
                    "Embeddings allow systems to compare semantic "
                    "similarity between queries and stored information."
                )
            },

            {
                "question": "What is the main purpose of fine-tuning a language model?",
                "options": [
                    "Adapt a pretrained model to a specific task or domain",
                    "Delete the pretrained model",
                    "Increase monitor resolution",
                    "Remove all training data"
                ],
                "answer": "Adapt a pretrained model to a specific task or domain",
                "explanation": (
                    "Fine-tuning updates a pretrained model using "
                    "task- or domain-specific data."
                )
            }
        ]
    }
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_difficulty(level):
    """Convert learner level into question difficulty."""

    mapping = {
        "Complete Beginner": "Basic",
        "Intermediate": "Intermediate",
        "Advanced": "Advanced"
    }

    return mapping[level]


def build_questions(level):
    """
    Build the 15-question diagnostic.

    The learner's selected level determines
    the difficulty of ALL questions.
    """

    difficulty = get_difficulty(level)

    questions = []

    for subject in SUBJECTS:

        for question in QUESTION_BANK[subject][difficulty]:

            question_copy = question.copy()

            question_copy["subject"] = subject
            question_copy["difficulty"] = difficulty

            questions.append(question_copy)

    return questions


def calculate_scores():

    scores = {}

    for subject in SUBJECTS:

        subject_answers = [
            answer
            for answer in st.session_state.answers
            if answer["subject"] == subject
        ]

        if not subject_answers:

            scores[subject] = None

        else:

            correct_answers = sum(
                answer["correct"]
                for answer in subject_answers
            )

            scores[subject] = round(
                correct_answers /
                len(subject_answers) *
                100
            )

    return scores


def get_status(score):

    if score is None:
        return "Not Assessed"

    if score < 40:
        return "Needs Foundation"

    if score < 70:
        return "Developing"

    if score < 100:
        return "Intermediate"

    return "Strong"


def create_roadmap(scores):

    assessed = {
        subject: score
        for subject, score in scores.items()
        if score is not None
    }

    ordered = sorted(
        assessed.items(),
        key=lambda item: item[1]
    )

    roadmap = []

    for number, (subject, score) in enumerate(
        ordered,
        start=1
    ):

        if score < 40:

            recommendation = (
                "Start with the fundamentals of this subject."
            )

        elif score < 70:

            recommendation = (
                "Practice the core concepts before progressing."
            )

        elif score < 100:

            recommendation = (
                "Strengthen your understanding with more practice."
            )

        else:

            recommendation = (
                "Strong diagnostic performance. "
                "You can move toward advanced topics."
            )

        roadmap.append({
            "number": number,
            "subject": subject,
            "score": score,
            "recommendation": recommendation
        })

    return roadmap


def reset_diagnostic_state():

    st.session_state.questions = []
    st.session_state.current_question = 0
    st.session_state.answers = []
    st.session_state.answer_submitted = False
    st.session_state.last_answer_correct = None
    st.session_state.diagnostic_complete = False
    st.session_state.domain_scores = {}
    st.session_state.roadmap = []


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## AI StudyMate")

    st.caption("Personalised AI Tutor")

    st.divider()

    if st.button(
        "Home",
        use_container_width=True
    ):

        st.session_state.page = "home"
        st.rerun()

    if st.button(
        "AI Diagnostic",
        use_container_width=True
    ):

        if st.session_state.profile:

            st.session_state.page = "diagnostic"
            st.rerun()

        else:

            st.warning(
                "Please complete your profile first."
            )

    if st.button(
        "Knowledge Map",
        use_container_width=True
    ):

        if st.session_state.diagnostic_complete:

            st.session_state.page = "knowledge_map"
            st.rerun()

        else:

            st.warning(
                "Complete the diagnostic first."
            )

    if st.button(
        "My Roadmap",
        use_container_width=True
    ):

        if st.session_state.diagnostic_complete:

            st.session_state.page = "roadmap"
            st.rerun()

        else:

            st.warning(
                "Complete the diagnostic first."
            )


# ============================================================
# HOME PAGE
# ============================================================

if st.session_state.page == "home":

    st.title("AI StudyMate")

    st.subheader(
        "Personalised AI Tutor for Learning AI"
    )

    st.write(
        "Tell us about your current experience and learning goal. "
        "Your selected level will determine the difficulty of your "
        "initial diagnostic assessment."
    )

    st.divider()

    st.markdown("### Learner Profile")

    with st.form("learner_profile"):

        name = st.text_input(
            "Your Name",
            placeholder="Enter your name"
        )

        level = st.selectbox(
            "What is your current AI level?",
            [
                "Complete Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

        goal = st.selectbox(
            "What is your main learning goal?",
            [
                "Learn AI fundamentals",
                "Build AI projects",
                "Prepare for an AI job",
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

        start = st.form_submit_button(
            "Start AI Journey",
            use_container_width=True
        )

    if start:

        if not name.strip():

            st.error(
                "Please enter your name."
            )

        else:

            st.session_state.profile = {
                "name": name.strip(),
                "level": level,
                "goal": goal,
                "study_time": study_time
            }

            reset_diagnostic_state()

            st.session_state.questions = build_questions(
                level
            )

            st.session_state.page = "diagnostic"

            st.rerun()


# ============================================================
# DIAGNOSTIC PAGE
# ============================================================

elif st.session_state.page == "diagnostic":

    if not st.session_state.profile:

        st.warning(
            "Please complete your learner profile first."
        )

        if st.button("Go to Home"):

            st.session_state.page = "home"
            st.rerun()

    else:

        profile = st.session_state.profile

        # ----------------------------------------------------
        # COMPLETED
        # ----------------------------------------------------

        if st.session_state.diagnostic_complete:

            st.title("Diagnostic Complete")

            st.success(
                f"Well done, {profile['name']}! "
                "Your diagnostic assessment is complete."
            )

            st.write(
                "We have assessed your current knowledge "
                "across the five AI learning domains."
            )

            if st.button(
                "View My Knowledge Map",
                use_container_width=True
            ):

                st.session_state.page = "knowledge_map"
                st.rerun()

        else:

            questions = st.session_state.questions

            current_index = (
                st.session_state.current_question
            )

            total_questions = len(questions)

            current_question = questions[current_index]

            difficulty = current_question["difficulty"]

            subject = current_question["subject"]

            # ------------------------------------------------
            # HEADER
            # ------------------------------------------------

            st.title("AI Diagnostic Assessment")

            st.write(
                f"Welcome, **{profile['name']}**."
            )

            st.write(
                f"Your selected level: **{profile['level']}**"
            )

            st.write(
                f"Diagnostic difficulty: **{difficulty}**"
            )

            # ------------------------------------------------
            # PROGRESS
            # ------------------------------------------------

            progress = current_index / total_questions

            st.progress(progress)

            st.caption(
                f"Question {current_index + 1} of "
                f"{total_questions}"
            )

            st.divider()

            # ------------------------------------------------
            # SUBJECT
            # ------------------------------------------------

            st.markdown(
                f"### {subject}"
            )

            st.caption(
                f"{difficulty} level question"
            )

            # ------------------------------------------------
            # QUESTION
            # ------------------------------------------------

            st.markdown(
                f"## {current_question['question']}"
            )

            st.write("")

            # =================================================
            # BEFORE ANSWER
            # =================================================

            if not st.session_state.answer_submitted:

                # IMPORTANT:
                # index=None means NO option is selected
                # when the question first appears.

                selected = st.radio(
                    "Select your answer:",
                    current_question["options"],
                    index=None,
                    key=f"answer_{current_index}"
                )

                st.write("")

                if st.button(
                    "Check Answer",
                    use_container_width=True
                ):

                    if selected is None:

                        st.warning(
                            "Please select an answer before continuing."
                        )

                    else:

                        is_correct = (
                            selected ==
                            current_question["answer"]
                        )

                        st.session_state.answers.append({

                            "question_number":
                                current_index + 1,

                            "subject":
                                subject,

                            "difficulty":
                                difficulty,

                            "selected":
                                selected,

                            "correct_answer":
                                current_question["answer"],

                            "correct":
                                is_correct
                        })

                        st.session_state.last_answer_correct = (
                            is_correct
                        )

                        st.session_state.answer_submitted = True

                        st.rerun()

            # =================================================
            # AFTER ANSWER
            # =================================================

            else:

                if st.session_state.last_answer_correct:

                    st.success(
                        "Correct!"
                    )

                else:

                    st.error(
                        "Incorrect."
                    )

                st.markdown(
                    "### Correct Answer"
                )

                st.write(
                    current_question["answer"]
                )

                st.info(
                    current_question["explanation"]
                )

                # --------------------------------------------
                # SUBJECT PROGRESS
                # --------------------------------------------

                subject_answers = [
                    answer
                    for answer in st.session_state.answers
                    if answer["subject"] == subject
                ]

                subject_correct = sum(
                    answer["correct"]
                    for answer in subject_answers
                )

                subject_score = round(
                    subject_correct /
                    len(subject_answers) *
                    100
                )

                st.caption(
                    f"{subject} progress: "
                    f"{subject_score}%"
                )

                st.write("")

                # --------------------------------------------
                # NEXT QUESTION
                # --------------------------------------------

                if st.button(
                    "Next Question",
                    use_container_width=True
                ):

                    st.session_state.current_question += 1

                    st.session_state.answer_submitted = False

                    st.session_state.last_answer_correct = None

                    # ----------------------------------------
                    # CHECK WHETHER ALL QUESTIONS ARE DONE
                    # ----------------------------------------

                    if (
                        st.session_state.current_question
                        >= total_questions
                    ):

                        st.session_state.diagnostic_complete = True

                        st.session_state.domain_scores = (
                            calculate_scores()
                        )

                        st.session_state.roadmap = (
                            create_roadmap(
                                st.session_state.domain_scores
                            )
                        )

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

        st.title("Your AI Knowledge Map")

        st.write(
            "Your scores are based on your diagnostic performance."
        )

        st.divider()

        scores = st.session_state.domain_scores

        for subject in SUBJECTS:

            score = scores.get(subject)

            st.markdown(
                f"### {subject}"
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

                    st.metric(
                        "Knowledge Score",
                        f"{score}%"
                    )

                with col2:

                    st.metric(
                        "Status",
                        get_status(score)
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
                    f"Your diagnostic indicates that you should "
                    f"build a strong foundation in {weakest_subject}."
                )

            elif weakest_score < 70:

                st.write(
                    f"You have some understanding of "
                    f"{weakest_subject}, but additional practice "
                    "will help strengthen your foundation."
                )

            elif weakest_score < 100:

                st.write(
                    f"You have a good foundation in "
                    f"{weakest_subject}. More practice can help "
                    "you progress further."
                )

            else:

                st.write(
                    f"You demonstrated strong performance in "
                    f"{weakest_subject}."
                )

        st.write("")

        if st.button(
            "View My Personalised Roadmap",
            use_container_width=True
        ):

            st.session_state.page = "roadmap"

            st.rerun()


# ============================================================
# ROADMAP
# ============================================================

elif st.session_state.page == "roadmap":

    if not st.session_state.diagnostic_complete:

        st.warning(
            "Complete the diagnostic first."
        )

    else:

        st.title(
            "My Personalised AI Roadmap"
        )

        st.write(
            "Your roadmap is based on your diagnostic results."
        )

        st.divider()

        scores = st.session_state.domain_scores

        # ----------------------------------------------------
        # SHOW ALL SUBJECTS
        # ----------------------------------------------------

        for subject in SUBJECTS:

            score = scores.get(subject)

            st.markdown(
                f"## {subject}"
            )

            if score is None:

                st.info(
                    "Not Assessed"
                )

                st.caption(
                    "Complete an assessment to determine "
                    "your starting level."
                )

            else:

                st.progress(
                    score / 100
                )

                st.write(
                    f"**Score:** {score}%"
                )

                st.write(
                    f"**Status:** {get_status(score)}"
                )

                if score < 40:

                    st.warning(
                        "Start with the fundamentals."
                    )

                elif score < 70:

                    st.info(
                        "Practice core concepts."
                    )

                elif score < 100:

                    st.info(
                        "Strengthen your intermediate knowledge."
                    )

                else:

                    st.success(
                        "Strong performance. "
                        "You can move toward advanced topics."
                    )

            st.divider()

        # ----------------------------------------------------
        # NEXT STAGE
        # ----------------------------------------------------

        st.markdown(
            "## Next Step"
        )

        st.write(
            "The next version of AI StudyMate will use this "
            "knowledge map to provide personalised lessons, "
            "practice questions and adaptive AI tutoring."
        )

        if st.button(
            "Back to Knowledge Map",
            use_container_width=True
        ):

            st.session_state.page = "knowledge_map"

            st.rerun()
