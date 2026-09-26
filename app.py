import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AI StudyMate",
    page_icon="AI",
    layout="wide"
)

# ============================================================
# SESSION STATE
# ============================================================

defaults = {
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

for key, value in defaults.items():
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
# Each subject has Basic, Intermediate and Advanced questions.
# The student's selected level determines which questions are used.
# ============================================================

QUESTION_BANK = {

    "Python": {

        "Basic": [
            {
                "question": "Which symbol is used to write a comment in Python?",
                "options": ["//", "#", "/* */", "<!-- -->"],
                "answer": "#",
                "explanation": "In Python, the # symbol is used to write a single-line comment."
            },
            {
                "question": "Which of the following is a Python data type?",
                "options": ["Integer", "Browser", "Website", "Folder"],
                "answer": "Integer",
                "explanation": "Integer (int) is a built-in Python data type used for whole numbers."
            },
            {
                "question": "Which function is commonly used to display output in Python?",
                "options": ["show()", "display()", "print()", "output()"],
                "answer": "print()",
                "explanation": "The print() function displays text or values in the Python output."
            }
        ],

        "Intermediate": [
            {
                "question": "Which Python data structure stores data as key-value pairs?",
                "options": ["List", "Tuple", "Dictionary", "Set"],
                "answer": "Dictionary",
                "explanation": "A Python dictionary stores information as key-value pairs."
            },
            {
                "question": "What does a Python function allow you to do?",
                "options": [
                    "Only print text",
                    "Reuse a block of code",
                    "Delete Python",
                    "Create an operating system"
                ],
                "answer": "Reuse a block of code",
                "explanation": "Functions group reusable logic so it can be called multiple times."
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["function", "define", "def", "func"],
                "answer": "def",
                "explanation": "Python uses the def keyword to define a function."
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
                "explanation": "NumPy provides efficient numerical operations and multidimensional arrays."
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
                "explanation": "Pandas provides powerful structures and tools for working with tabular and structured data."
            },
            {
                "question": "Why is vectorization useful in Python numerical computing?",
                "options": [
                    "It avoids using variables",
                    "It allows efficient operations on arrays",
                    "It removes all loops from Python",
                    "It converts Python into Java"
                ],
                "answer": "It allows efficient operations on arrays",
                "explanation": "Vectorized operations can perform calculations on entire arrays efficiently."
            }
        ]
    },


    "Mathematics & Statistics": {

        "Basic": [
            {
                "question": "What is the mean of 2, 4 and 6?",
                "options": ["2", "4", "6", "12"],
                "answer": "4",
                "explanation": "The mean is (2 + 4 + 6) / 3 = 4."
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
                "explanation": "Probability describes how likely an event is to occur."
            },
            {
                "question": "Which of these is a mathematical operation?",
                "options": ["Addition", "Browser", "Database", "Keyboard"],
                "answer": "Addition",
                "explanation": "Addition is one of the basic arithmetic operations."
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
                "explanation": "Standard deviation measures how spread out values are around their mean."
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
                "explanation": "A vector can represent a quantity using an ordered collection of components."
            },
            {
                "question": "If the probability of an event is 0, what does it mean?",
                "options": [
                    "The event is certain",
                    "The event is impossible",
                    "The event is likely",
                    "The event is random but guaranteed"
                ],
                "answer": "The event is impossible",
                "explanation": "A probability of 0 represents an impossible event."
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
                "explanation": "Gradients indicate how a function changes and are used by optimization algorithms such as gradient descent."
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
                "explanation": "Covariance indicates the direction in which two variables tend to vary together."
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
                "explanation": "A loss function quantifies the difference between predictions and target values."
            }
        ]
    },


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
                "explanation": "Machine learning allows systems to learn patterns from data and use them to make predictions or decisions."
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
                "explanation": "Training data is used by a machine learning algorithm to learn patterns."
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
                "explanation": "Supervised learning uses examples where the desired target or label is known."
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
                "explanation": "Overfitting happens when a model learns the training data too closely and fails to generalize."
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
                "explanation": "Classification predicts a category or class, such as spam or not spam."
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
                "explanation": "The test set provides unseen examples for evaluating model performance."
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
                "explanation": "Feature engineering involves creating useful representations of input data for machine learning."
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
                "explanation": "Cross-validation evaluates a model across different train-validation splits to estimate generalization."
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
                "explanation": "Regularization adds constraints or penalties that can reduce overfitting."
            }
        ]
    },


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
                "explanation": "Neural networks are machine learning models made of interconnected computational units."
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
                "explanation": "A neuron receives inputs, applies weights and an activation function, and produces an output."
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
                "explanation": "An epoch represents one complete pass through the training dataset during training."
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
                "explanation": "Activation functions allow neural networks to model complex non-linear relationships."
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
                "explanation": "Backpropagation calculates gradients of the loss with respect to model parameters."
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
                "explanation": "The learning rate controls how large each optimization step is."
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
                "explanation": "CNNs use convolution operations to detect local spatial patterns in images."
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
                "explanation": "Attention lets models assign different importance to different parts of an input sequence."
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
                "explanation": "Transformers use attention mechanisms as a central component for processing sequences."
            }
        ]
    },


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
                "explanation": "Generative AI can create new text, images, audio, code and other forms of content."
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
                "explanation": "LLM stands for Large Language Model."
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
                "explanation": "A prompt provides instructions or context to a generative AI model."
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
                "explanation": "Language models process text as tokens, which can represent words, parts of words or other text units."
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
                "explanation": "Embeddings represent information such as text as numerical vectors that capture useful relationships."
            },
            {
                "question": "What is the purpose of context in an LLM prompt?",
                "options": [
                    "Provide relevant information for generating a response",
                    "Delete the model",
                    "Increase the computer screen size",
                    "Remove all instructions"
                ],
                "answer": "Provide relevant information for generating a response",
                "explanation": "Context gives the model additional information that can guide its response."
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
                "explanation": "RAG combines information retrieval with generation so a model can use relevant external information."
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
                "explanation": "Embeddings allow systems to compare semantic similarity between queries and stored information."
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
                "explanation": "Fine-tuning updates a pretrained model using task- or domain-specific data."
            }
        ]
    }
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_difficulty_from_level(level):
    """Convert learner profile level to question difficulty."""

    mapping = {
        "Complete Beginner": "Basic",
        "Intermediate": "Intermediate",
        "Advanced": "Advanced"
    }

    return mapping.get(level, "Basic")


def build_diagnostic_questions(level):
    """
    Create exactly 15 questions:
    3 questions from each of the 5 subjects
    at the learner's selected difficulty.
    """

    difficulty = get_difficulty_from_level(level)

    questions = []

    for subject in SUBJECTS:
        subject_questions = QUESTION_BANK[subject][difficulty]

        for question in subject_questions:
            q = question.copy()
            q["subject"] = subject
            q["difficulty"] = difficulty
            questions.append(q)

    return questions


def calculate_scores():
    """Calculate score for each subject."""

    scores = {}

    for subject in SUBJECTS:

        subject_answers = [
            answer
            for answer in st.session_state.answers
            if answer["subject"] == subject
        ]

        if len(subject_answers) == 0:
            scores[subject] = None
        else:
            correct = sum(
                1 for answer in subject_answers
                if answer["correct"]
            )

            scores[subject] = round(
                (correct / len(subject_answers)) * 100
            )

    return scores


def score_status(score):

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

    if not assessed:
        return []

    # Weakest subject first
    ordered = sorted(
        assessed.items(),
        key=lambda x: x[1]
    )

    roadmap = []

    for index, (subject, score) in enumerate(ordered, start=1):

        if score < 40:
            recommendation = "Build the fundamentals"
        elif score < 70:
            recommendation = "Practice core concepts"
        elif score < 100:
            recommendation = "Strengthen intermediate concepts"
        else:
            recommendation = "Ready for advanced learning"

        roadmap.append({
            "step": index,
            "subject": subject,
            "score": score,
            "recommendation": recommendation
        })

    return roadmap


def reset_diagnostic():

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

    st.markdown("Personalised AI Tutor")

    st.divider()

    if st.button("Home", use_container_width=True):
        st.session_state.page = "home"

    if st.button("AI Diagnostic", use_container_width=True):

        if st.session_state.profile:
            st.session_state.page = "diagnostic"

        else:
            st.warning("Please complete your profile first.")

    if st.button("Knowledge Map", use_container_width=True):

        if st.session_state.diagnostic_complete:
            st.session_state.page = "knowledge_map"

        else:
            st.warning("Complete the diagnostic first.")

    if st.button("My Roadmap", use_container_width=True):

        if st.session_state.diagnostic_complete:
            st.session_state.page = "roadmap"

        else:
            st.warning("Complete the diagnostic first.")


# ============================================================
# HOME
# ============================================================

if st.session_state.page == "home":

    st.title("AI StudyMate")

    st.subheader("Personalised AI Tutor for Learning AI")

    st.write(
        "Tell us about yourself. AI StudyMate will use your current "
        "level to create the right diagnostic experience for you."
    )

    st.divider()

    st.markdown("### Learner Profile")

    with st.form("profile_form"):

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

        submitted = st.form_submit_button(
            "Start AI Journey",
            use_container_width=True
        )

    if submitted:

        if not name.strip():

            st.error("Please enter your name.")

        else:

            st.session_state.profile = {
                "name": name.strip(),
                "level": level,
                "goal": goal,
                "study_time": study_time
            }

            # Build questions according to selected level
            st.session_state.questions = build_diagnostic_questions(level)

            reset_diagnostic()

            # reset_diagnostic clears questions, so build again
            st.session_state.questions = build_diagnostic_questions(level)

            st.session_state.page = "diagnostic"

            st.rerun()


# ============================================================
# DIAGNOSTIC
# ============================================================

elif st.session_state.page == "diagnostic":

    if not st.session_state.profile:

        st.warning("Please complete your learner profile first.")

        if st.button("Go to Home"):
            st.session_state.page = "home"
            st.rerun()

    else:

        profile = st.session_state.profile

        questions = st.session_state.questions

        current_index = st.session_state.current_question

        # ----------------------------------------------------
        # Diagnostic Complete
        # ----------------------------------------------------

        if st.session_state.diagnostic_complete:

            st.success("Diagnostic completed successfully!")

            st.session_state.domain_scores = calculate_scores()

            st.session_state.roadmap = create_roadmap(
                st.session_state.domain_scores
            )

            st.markdown("## Your Diagnostic Summary")

            st.write(
                f"Well done, **{profile['name']}**. "
                "Your personalised knowledge map is ready."
            )

            if st.button(
                "View My Knowledge Map",
                use_container_width=True
            ):

                st.session_state.page = "knowledge_map"
                st.rerun()

        else:

            difficulty = get_difficulty_from_level(
                profile["level"]
            )

            total_questions = len(questions)

            # Progress
            progress = current_index / total_questions

            st.progress(progress)

            st.caption(
                f"Question {current_index + 1} of {total_questions}"
            )

            st.markdown("## AI Diagnostic Assessment")

            st.write(
                f"Level selected: **{profile['level']}**"
            )

            st.write(
                f"Question difficulty: **{difficulty}**"
            )

            st.divider()

            question_data = questions[current_index]

            subject = question_data["subject"]

            st.markdown(
                f"### {subject}"
            )

            st.caption(
                f"{difficulty} level"
            )

            st.markdown(
                f"### {question_data['question']}"
            )

            # ------------------------------------------------
            # If answer has NOT been submitted
            # ------------------------------------------------

            if not st.session_state.answer_submitted:

                selected = st.radio(
                    "Select your answer:",
                    question_data["options"],
                    key=f"question_{current_index}"
                )

                if st.button(
                    "Check Answer",
                    use_container_width=True
                ):

                    is_correct = (
                        selected == question_data["answer"]
                    )

                    st.session_state.answers.append({
                        "question_number": current_index + 1,
                        "subject": subject,
                        "difficulty": difficulty,
                        "selected": selected,
                        "correct_answer": question_data["answer"],
                        "correct": is_correct
                    })

                    st.session_state.last_answer_correct = is_correct

                    st.session_state.answer_submitted = True

                    st.rerun()

            # ------------------------------------------------
            # Show answer and explanation
            # ------------------------------------------------

            else:

                if st.session_state.last_answer_correct:

                    st.success("Correct!")

                else:

                    st.error("Incorrect.")

                st.markdown(
                    f"**Correct Answer:** "
                    f"{question_data['answer']}"
                )

                st.info(
                    f"**Explanation:** "
                    f"{question_data['explanation']}"
                )

                # Current subject score
                subject_answers = [
                    answer
                    for answer in st.session_state.answers
                    if answer["subject"] == subject
                ]

                subject_correct = sum(
                    1
                    for answer in subject_answers
                    if answer["correct"]
                )

                subject_score = round(
                    subject_correct /
                    len(subject_answers) * 100
                )

                st.caption(
                    f"{subject} diagnostic progress: "
                    f"{subject_score}%"
                )

                if st.button(
                    "Next Question",
                    use_container_width=True
                ):

                    st.session_state.current_question += 1

                    st.session_state.answer_submitted = False

                    st.session_state.last_answer_correct = None

                    if (
                        st.session_state.current_question
                        >= len(st.session_state.questions)
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

        st.warning("Complete the diagnostic first.")

    else:

        st.title("Your AI Knowledge Map")

        st.write(
            "This map shows your performance in the diagnostic assessment."
        )

        st.divider()

        scores = st.session_state.domain_scores

        for subject in SUBJECTS:

            score = scores.get(subject)

            if score is None:

                st.markdown(
                    f"### {subject}"
                )

                st.info("Not Assessed")

            else:

                status = score_status(score)

                st.markdown(
                    f"### {subject}"
                )

                st.progress(score / 100)

                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "Diagnostic Score",
                        f"{score}%"
                    )

                with col2:
                    st.metric(
                        "Status",
                        status
                    )

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

            weakest_score = assessed[weakest_subject]

            st.markdown("## Recommended Starting Point")

            st.success(
                f"**{weakest_subject}** — {weakest_score}%"
            )

            st.write(
                "Based on your diagnostic performance, "
                f"we recommend starting with **{weakest_subject}** "
                "and strengthening the areas where you need the "
                "most practice."
            )

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

        st.warning("Complete the diagnostic first.")

    else:

        st.title("My Personalised AI Roadmap")

        st.write(
            "Your roadmap is generated from your diagnostic results."
        )

        st.divider()

        roadmap = st.session_state.roadmap

        if not roadmap:

            st.info(
                "No assessed subjects are available yet."
            )

        else:

            for item in roadmap:

                st.markdown(
                    f"## {item['step']}. {item['subject']}"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Diagnostic Score",
                        f"{item['score']}%"
                    )

                with col2:

                    st.write(
                        f"**Status:** "
                        f"{score_status(item['score'])}"
                    )

                st.write(
                    f"**Recommendation:** "
                    f"{item['recommendation']}"
                )

                if item["score"] < 40:

                    st.warning(
                        "Start with the fundamentals of this subject."
                    )

                elif item["score"] < 70:

                    st.info(
                        "Practice the core concepts before moving ahead."
                    )

                elif item["score"] < 100:

                    st.info(
                        "Strengthen your understanding with intermediate practice."
                    )

                else:

                    st.success(
                        "Strong diagnostic performance. "
                        "You can move toward advanced topics."
                    )

                st.divider()

        st.markdown("## Next Step")

        st.write(
            "The next stage of AI StudyMate will use this knowledge "
            "map to provide personalised lessons, practice questions "
            "and adaptive AI tutoring."
        )

        if st.button(
            "Back to Knowledge Map",
            use_container_width=True
        ):

            st.session_state.page = "knowledge_map"

            st.rerun()
