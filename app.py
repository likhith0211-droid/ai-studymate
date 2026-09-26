import streamlit as st


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
    "roadmap": []
}

for key, value in DEFAULTS.items():

    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# QUESTION BANK
# ============================================================

QUESTION_BANK = {

    "Python": {

        "Basic": [
            {
                "question": "Which symbol is used to write a comment in Python?",
                "options": ["//", "#", "/*", "--"],
                "answer": "#"
            },
            {
                "question": "Which of these is a Python data type?",
                "options": ["Integer", "Boolean", "Both Integer and Boolean", "Character only"],
                "answer": "Both Integer and Boolean"
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["function", "def", "fun", "define"],
                "answer": "def"
            }
        ],

        "Intermediate": [
            {
                "question": "What is the output type of range(5) in Python?",
                "options": ["List", "Range object", "Tuple", "Set"],
                "answer": "Range object"
            },
            {
                "question": "Which Python data structure stores key-value pairs?",
                "options": ["List", "Tuple", "Dictionary", "Set"],
                "answer": "Dictionary"
            },
            {
                "question": "What does a Python class primarily define?",
                "options": [
                    "A database",
                    "A blueprint for objects",
                    "A loop",
                    "A file"
                ],
                "answer": "A blueprint for objects"
            }
        ],

        "Advanced": [
            {
                "question": "What is a Python decorator commonly used for?",
                "options": [
                    "Modifying or extending function behavior",
                    "Creating databases",
                    "Installing Python",
                    "Deleting variables"
                ],
                "answer": "Modifying or extending function behavior"
            },
            {
                "question": "What does list comprehension provide?",
                "options": [
                    "A concise way to create lists",
                    "A database engine",
                    "A debugging tool",
                    "A package manager"
                ],
                "answer": "A concise way to create lists"
            },
            {
                "question": "What is the main purpose of a generator in Python?",
                "options": [
                    "To produce values lazily",
                    "To create classes",
                    "To compile Python",
                    "To install libraries"
                ],
                "answer": "To produce values lazily"
            }
        ]
    },


    "Mathematics & Statistics": {

        "Basic": [
            {
                "question": "What is the mean of 2, 4 and 6?",
                "options": ["2", "4", "6", "12"],
                "answer": "4"
            },
            {
                "question": "What is probability used to measure?",
                "options": [
                    "The likelihood of an event",
                    "The size of a dataset",
                    "The number of variables",
                    "The speed of a computer"
                ],
                "answer": "The likelihood of an event"
            },
            {
                "question": "What does the x-axis represent in a basic graph?",
                "options": [
                    "Horizontal values",
                    "Vertical values",
                    "Only percentages",
                    "Only categories"
                ],
                "answer": "Horizontal values"
            }
        ],

        "Intermediate": [
            {
                "question": "What does standard deviation measure?",
                "options": [
                    "Data spread",
                    "Dataset size",
                    "Number of columns",
                    "Model accuracy only"
                ],
                "answer": "Data spread"
            },
            {
                "question": "What is the median?",
                "options": [
                    "The middle value when data is ordered",
                    "The largest value",
                    "The smallest value",
                    "The average of all values always"
                ],
                "answer": "The middle value when data is ordered"
            },
            {
                "question": "What does correlation measure?",
                "options": [
                    "Relationship between variables",
                    "Number of observations",
                    "CPU usage",
                    "File size"
                ],
                "answer": "Relationship between variables"
            }
        ],

        "Advanced": [
            {
                "question": "What does a gradient represent mathematically?",
                "options": [
                    "Direction and rate of greatest increase",
                    "Only the average",
                    "Only the variance",
                    "Number of samples"
                ],
                "answer": "Direction and rate of greatest increase"
            },
            {
                "question": "What is a derivative primarily used to describe?",
                "options": [
                    "Rate of change",
                    "Number of classes",
                    "Dataset size",
                    "Probability only"
                ],
                "answer": "Rate of change"
            },
            {
                "question": "In probability, what does conditional probability describe?",
                "options": [
                    "Probability of an event given another event",
                    "Probability of nothing happening",
                    "Only independent events",
                    "Dataset size"
                ],
                "answer": "Probability of an event given another event"
            }
        ]
    },


    "Machine Learning": {

        "Basic": [
            {
                "question": "What is machine learning?",
                "options": [
                    "A way for computers to learn patterns from data",
                    "A programming language",
                    "A type of database",
                    "A computer operating system"
                ],
                "answer": "A way for computers to learn patterns from data"
            },
            {
                "question": "What is a training dataset?",
                "options": [
                    "Data used to teach a model",
                    "Data used only for storage",
                    "A programming language",
                    "A visualization"
                ],
                "answer": "Data used to teach a model"
            },
            {
                "question": "Which is an example of supervised learning?",
                "options": [
                    "Learning from labelled examples",
                    "Learning without any data",
                    "Deleting data",
                    "Sorting files"
                ],
                "answer": "Learning from labelled examples"
            }
        ],

        "Intermediate": [
            {
                "question": "What is overfitting?",
                "options": [
                    "When a model learns training data too closely",
                    "When a model has no data",
                    "When a model is always correct",
                    "When a dataset is deleted"
                ],
                "answer": "When a model learns training data too closely"
            },
            {
                "question": "Which metric is commonly used for classification?",
                "options": [
                    "Accuracy",
                    "File size",
                    "CPU speed",
                    "Memory capacity"
                ],
                "answer": "Accuracy"
            },
            {
                "question": "What is feature engineering?",
                "options": [
                    "Creating or transforming useful input features",
                    "Deleting the model",
                    "Creating a database",
                    "Installing Python"
                ],
                "answer": "Creating or transforming useful input features"
            }
        ],

        "Advanced": [
            {
                "question": "What is regularization used for?",
                "options": [
                    "Reducing overfitting",
                    "Increasing dataset size only",
                    "Deleting features automatically",
                    "Increasing file size"
                ],
                "answer": "Reducing overfitting"
            },
            {
                "question": "What is cross-validation commonly used for?",
                "options": [
                    "Estimating model performance",
                    "Writing Python comments",
                    "Creating neural networks only",
                    "Compressing datasets"
                ],
                "answer": "Estimating model performance"
            },
            {
                "question": "What is the purpose of a loss function?",
                "options": [
                    "Measure how far predictions are from desired outputs",
                    "Store training data",
                    "Create a user interface",
                    "Install libraries"
                ],
                "answer": "Measure how far predictions are from desired outputs"
            }
        ]
    },


    "Deep Learning": {

        "Basic": [
            {
                "question": "What is a neural network?",
                "options": [
                    "A model inspired by connected neurons",
                    "A database",
                    "A programming language",
                    "A web browser"
                ],
                "answer": "A model inspired by connected neurons"
            },
            {
                "question": "What is an activation function?",
                "options": [
                    "A function that introduces non-linearity",
                    "A database function",
                    "A file format",
                    "A programming editor"
                ],
                "answer": "A function that introduces non-linearity"
            },
            {
                "question": "What is a neural network trained using?",
                "options": [
                    "Data",
                    "Only text files",
                    "Only images",
                    "No examples"
                ],
                "answer": "Data"
            }
        ],

        "Intermediate": [
            {
                "question": "What is backpropagation?",
                "options": [
                    "A method for calculating gradients through a network",
                    "A data storage system",
                    "A database query",
                    "A visualization technique"
                ],
                "answer": "A method for calculating gradients through a network"
            },
            {
                "question": "What is a CNN commonly used for?",
                "options": [
                    "Image-related tasks",
                    "Database management",
                    "File compression",
                    "Operating systems"
                ],
                "answer": "Image-related tasks"
            },
            {
                "question": "What is an optimizer used for?",
                "options": [
                    "Updating model parameters during training",
                    "Creating datasets",
                    "Displaying charts",
                    "Saving images"
                ],
                "answer": "Updating model parameters during training"
            }
        ],

        "Advanced": [
            {
                "question": "What problem can batch normalization help with?",
                "options": [
                    "Training stability and optimization",
                    "Database indexing",
                    "File compression",
                    "Network security"
                ],
                "answer": "Training stability and optimization"
            },
            {
                "question": "What is an attention mechanism used for?",
                "options": [
                    "Allowing models to focus on relevant parts of input",
                    "Deleting data",
                    "Compressing files",
                    "Creating databases"
                ],
                "answer": "Allowing models to focus on relevant parts of input"
            },
            {
                "question": "Transformers primarily rely on which mechanism?",
                "options": [
                    "Self-attention",
                    "Decision trees",
                    "K-means",
                    "Linear regression"
                ],
                "answer": "Self-attention"
            }
        ]
    },


    "Generative AI": {

        "Basic": [
            {
                "question": "What does Generative AI do?",
                "options": [
                    "Generates new content",
                    "Only stores data",
                    "Only sorts files",
                    "Only calculates averages"
                ],
                "answer": "Generates new content"
            },
            {
                "question": "What does LLM stand for?",
                "options": [
                    "Large Language Model",
                    "Long Learning Machine",
                    "Large Logic Machine",
                    "Language Learning Method"
                ],
                "answer": "Large Language Model"
            },
            {
                "question": "What is a prompt?",
                "options": [
                    "An instruction or input given to an AI model",
                    "A database",
                    "A programming language",
                    "A hardware component"
                ],
                "answer": "An instruction or input given to an AI model"
            }
        ],

        "Intermediate": [
            {
                "question": "What are embeddings?",
                "options": [
                    "Numerical representations of information",
                    "Images only",
                    "Databases",
                    "Programming languages"
                ],
                "answer": "Numerical representations of information"
            },
            {
                "question": "What does RAG stand for?",
                "options": [
                    "Retrieval-Augmented Generation",
                    "Random AI Generation",
                    "Rapid Application Generation",
                    "Retrieval AI Graph"
                ],
                "answer": "Retrieval-Augmented Generation"
            },
            {
                "question": "Why is context important for an LLM?",
                "options": [
                    "It provides information relevant to the response",
                    "It increases screen size",
                    "It replaces Python",
                    "It stores the operating system"
                ],
                "answer": "It provides information relevant to the response"
            }
        ],

        "Advanced": [
            {
                "question": "What is fine-tuning?",
                "options": [
                    "Further training a pretrained model on specific data",
                    "Deleting a model",
                    "Creating a database",
                    "Changing a screen"
                ],
                "answer": "Further training a pretrained model on specific data"
            },
            {
                "question": "What is a vector database commonly used for in RAG?",
                "options": [
                    "Storing and retrieving vector embeddings",
                    "Running Python programs",
                    "Creating images",
                    "Managing operating systems"
                ],
                "answer": "Storing and retrieving vector embeddings"
            },
            {
                "question": "What is hallucination in generative AI?",
                "options": [
                    "When a model produces unsupported or incorrect information",
                    "When a model becomes faster",
                    "When a model stores a file",
                    "When a model shuts down"
                ],
                "answer": "When a model produces unsupported or incorrect information"
            }
        ]
    }
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_difficulty(level):

    if level == "Complete Beginner":
        return "Basic"

    if level == "Intermediate":
        return "Intermediate"

    return "Advanced"


def build_questions(level):

    difficulty = get_difficulty(level)

    questions = []

    for subject in SUBJECTS:

        subject_questions = QUESTION_BANK[
            subject
        ][difficulty]

        for question in subject_questions:

            questions.append(
                {
                    "subject": subject,
                    "difficulty": difficulty,
                    "question": question["question"],
                    "options": question["options"],
                    "answer": question["answer"]
                }
            )

    return questions


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

        if len(subject_questions) > 0:

            score = round(
                (correct / len(subject_questions)) * 100
            )

            scores[subject] = score

        else:

            scores[subject] = None

    return scores


def get_status(score):

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

    return ordered


def reset_diagnostic():

    st.session_state.questions = []
    st.session_state.current_question = 0
    st.session_state.answers = []
    st.session_state.diagnostic_complete = False
    st.session_state.domain_scores = {}
    st.session_state.roadmap = []


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
        "AI StudyMate first understands what you already know, "
        "then builds a learning path around your knowledge, "
        "goal and learning level."
    )

    st.divider()

    st.markdown("## 👤 Tell us about yourself")

    with st.form("profile_form"):

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

            reset_diagnostic()

            st.session_state.questions = build_questions(
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

        if st.button("Go to Home"):

            st.session_state.page = "home"
            st.rerun()

    elif st.session_state.diagnostic_complete:

        st.success(
            "Your diagnostic is complete!"
        )

        st.title("Diagnostic Completed")

        st.write(
            "Your answers have been analysed. "
            "Open Knowledge Map to see your results."
        )

        if st.button(
            "View Knowledge Map",
            use_container_width=True
        ):

            st.session_state.page = "knowledge_map"
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

        question_number = current_index + 1

        st.title("🧠 AI Knowledge Diagnostic")

        st.write(
            f"Question {question_number} of "
            f"{total_questions}"
        )

        st.progress(
            question_number / total_questions
        )

        st.divider()

        st.markdown(
            f"### {current_question['subject']}"
        )

        st.caption(
            f"Difficulty: {current_question['difficulty']}"
        )

        st.markdown(
            f"## {current_question['question']}"
        )

        selected = st.radio(
            "Select your answer:",
            current_question["options"],
            index=None,
            key=f"question_{current_index}"
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

                # Store answer silently.
                # No correct/incorrect feedback is shown
                # during the diagnostic.

                st.session_state.questions[
                    current_index
                ]["selected"] = selected

                st.session_state.answers.append(
                    selected
                )

                if (
                    current_index
                    < total_questions - 1
                ):

                    st.session_state.current_question += 1

                else:

                    scores = calculate_scores()

                    st.session_state.domain_scores = scores

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

        st.title("Your AI Knowledge Map")

        st.write(
            "Your scores are based on your performance "
            "in the diagnostic assessment."
        )

        st.divider()

        scores = st.session_state.domain_scores

        for subject in SUBJECTS:

            # IMPORTANT:
            # Get the score for this specific subject.

            score = scores.get(subject)

            # ------------------------------------------------
            # COURSE / SUBJECT NAME
            # ------------------------------------------------

            st.markdown(
                f"<h2 style='margin-bottom: 5px;'>{subject}</h2>",
                unsafe_allow_html=True
            )

            # ------------------------------------------------
            # NOT ASSESSED
            # ------------------------------------------------

            if score is None:

                st.info("Not Assessed")

            # ------------------------------------------------
            # ASSESSED
            # ------------------------------------------------

            else:

                st.progress(
                    score / 100
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.markdown(
                        "<div style='font-size: 15px; "
                        "font-weight: 600;'>Knowledge Score</div>",
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"<div style='font-size: 20px; "
                        f"font-weight: 500;'>{score}%</div>",
                        unsafe_allow_html=True
                    )

                with col2:

                    st.markdown(
                        "<div style='font-size: 15px; "
                        "font-weight: 600;'>Status</div>",
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"<div style='font-size: 20px; "
                        f"font-weight: 500;'>{get_status(score)}</div>",
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
                f"{weakest_subject} — {weakest_score}%"
            )

            if weakest_score < 40:

                st.write(
                    f"Your diagnostic indicates that you should "
                    f"build a strong foundation in "
                    f"{weakest_subject}."
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

    st.title("📚 My Personalised AI Roadmap")

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

        profile = st.session_state.profile

        if profile:

            st.write(
                f"Great work, **{profile['name']}**."
            )

            st.write(
                f"Your roadmap is based on your current level "
                f"(**{profile['level']}**), your goal "
                f"(**{profile['goal']}**), and your diagnostic "
                f"performance."
            )

        st.divider()

        st.markdown(
            "## Your Learning Order"
        )

        roadmap = st.session_state.roadmap

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
                    "Start with the fundamentals and build "
                    "your foundation through guided lessons "
                    "and beginner practice."
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
                    "toward advanced topics and projects."
                )

            st.divider()

        st.markdown(
            "## 🎯 Next Stage"
        )

        st.write(
            "AI StudyMate will use your diagnostic results "
            "to personalise your lessons, practice questions, "
            "difficulty and learning pace."
        )
