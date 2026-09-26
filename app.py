import streamlit as st

st.set_page_config(
    page_title="AI StudyMate",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "started" not in st.session_state:
    st.session_state.started = False

if "profile" not in st.session_state:
    st.session_state.profile = {}

if "diagnostic_completed" not in st.session_state:
    st.session_state.diagnostic_completed = False

if "topic_scores" not in st.session_state:
    st.session_state.topic_scores = {}

if "current_topic" not in st.session_state:
    st.session_state.current_topic = None

if "tutor_started" not in st.session_state:
    st.session_state.tutor_started = False

if "mastery" not in st.session_state:
    st.session_state.mastery = "Not Started"

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "mastery_points" not in st.session_state:
    st.session_state.mastery_points = 0

if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Easy"

if "last_feedback" not in st.session_state:
    st.session_state.last_feedback = ""


# -----------------------------
# ADAPTIVE LESSONS
# -----------------------------
lessons = {

    "AI Fundamentals": {
        "title": "Understanding Artificial Intelligence",

        "easy": """
Artificial Intelligence (AI) is the field of creating computer systems
that can perform tasks that normally require human intelligence.

Examples include:
- Understanding language
- Recognizing objects in images
- Making predictions
- Recommending content

Think of AI as a system that receives information,
processes it, and produces an intelligent output.
""",

        "medium": """
AI systems can be designed to recognize patterns, make predictions,
understand language and support decision-making.

For example, an image recognition system can receive an image,
process its visual patterns and predict what objects are present.

The important idea is that AI systems use information to produce
useful outputs for a particular task.
""",

        "hard": """
Modern AI systems can learn complex patterns from large amounts of data.

For example, an image classification model can learn relationships
between visual features and labels during training.

A key distinction is that AI is a broad field, while machine learning
is one approach used to build AI systems.
""",

        "questions": {
            "Easy": "In your own words, what is Artificial Intelligence?",
            "Medium": "Give one example of an AI system and explain what information it receives and what output it produces.",
            "Hard": "Explain the relationship between Artificial Intelligence and Machine Learning."
        },

        "keywords": {
            "Easy": ["computer", "machine", "intelligence", "human", "task"],
            "Medium": ["input", "output", "image", "language", "prediction", "data"],
            "Hard": ["ai", "artificial intelligence", "machine learning", "learning", "data"]
        }
    },

    "Python": {
        "title": "Python for AI",

        "easy": """
Python is one of the most commonly used programming languages in AI.

Important Python concepts include:
- Variables
- Data types
- Conditions
- Loops
- Functions
- Lists and dictionaries

Example:

x = 10

Here, x is a variable containing the value 10.
""",

        "medium": """
Python is widely used in AI because it has a simple syntax
and a large ecosystem of libraries.

Common AI and data libraries include:
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

Python allows developers to work with data, build models
and create AI applications efficiently.
""",

        "hard": """
Python is especially useful for AI development because it provides
libraries and frameworks for different stages of the machine learning
workflow.

For example, data can be prepared with Pandas and NumPy,
models can be trained with Scikit-learn,
and neural networks can be developed using deep-learning frameworks.

This ecosystem reduces the amount of low-level code developers need
to write when building AI systems.
""",

        "questions": {
            "Easy": "Why is Python useful when learning Artificial Intelligence?",
            "Medium": "Name two Python libraries commonly used in AI and explain what they are useful for.",
            "Hard": "Explain how Python's ecosystem supports different stages of an AI development workflow."
        },

        "keywords": {
            "Easy": ["simple", "easy", "ai", "library", "libraries", "programming"],
            "Medium": ["numpy", "pandas", "scikit", "matplotlib", "data", "model"],
            "Hard": ["data", "prepare", "model", "train", "library", "framework", "workflow"]
        }
    },

    "Machine Learning": {
        "title": "Introduction to Machine Learning",

        "easy": """
Machine Learning (ML) is a branch of AI where computers learn
patterns from data.

For example, instead of manually programming a system to recognize cats,
we can provide many examples of images containing cats.

The model learns patterns from those examples and can then
make predictions on new data.
""",

        "medium": """
Machine learning uses data to train models that can make predictions
or decisions.

In supervised learning, the training examples contain labels.

For example, a model can learn from images labelled "cat" and "dog"
and later predict the label of a new image.
""",

        "hard": """
A machine learning model learns a relationship between input features
and a target output from training data.

In supervised learning, labelled examples are used during training.
The trained model can then generalize its learned patterns
to previously unseen data.

The quality and representativeness of the training data
can strongly affect model performance.
""",

        "questions": {
            "Easy": "What does a machine learning model learn from?",
            "Medium": "What is supervised learning? Give a simple example.",
            "Hard": "Why is the quality of training data important for a machine learning model?"
        },

        "keywords": {
            "Easy": ["data", "examples", "patterns", "training"],
            "Medium": ["label", "labelled", "data", "training", "prediction"],
            "Hard": ["data", "quality", "training", "representative", "performance", "model"]
        }
    },

    "Generative AI": {
        "title": "Understanding Generative AI",

        "easy": """
Generative AI refers to AI systems that can create new content.

They can generate:
- Text
- Images
- Audio
- Video
- Code

Large Language Models (LLMs) are an important example of Generative AI.
""",

        "medium": """
Generative AI models learn patterns from existing data
and can use those learned patterns to generate new content.

For example, a language model can generate text based on
a user's prompt.

Generative AI is different from a system that only classifies
or labels existing information.
""",

        "hard": """
Generative AI models learn statistical patterns from large datasets
and use those patterns to produce new outputs.

Large Language Models generate text by predicting likely tokens
based on the context provided to them.

The quality of the generated output depends on factors such as
the model, training data, prompt and context.
""",

        "questions": {
            "Easy": "What makes Generative AI different from a system that only classifies information?",
            "Medium": "How can a Generative AI system create new text from a user prompt?",
            "Hard": "What role do training data, prompts and context play in Generative AI output?"
        },

        "keywords": {
            "Easy": ["create", "generate", "new", "content", "text", "image"],
            "Medium": ["prompt", "generate", "data", "patterns", "text"],
            "Hard": ["training", "prompt", "context", "model", "data", "output"]
        }
    },

    "RAG": {
        "title": "Understanding RAG",

        "easy": """
RAG stands for Retrieval-Augmented Generation.

A RAG system retrieves relevant information from a knowledge source
and provides that information to a language model before generating
an answer.

Simple flow:

Question → Retrieve information → Generate answer
""",

        "medium": """
RAG combines information retrieval with text generation.

When a user asks a question, the system first searches
a knowledge source for relevant information.

That retrieved information is then provided as context
to the language model so it can generate a more informed answer.
""",

        "hard": """
Retrieval-Augmented Generation helps language models use
external knowledge during response generation.

A typical RAG pipeline retrieves relevant documents,
selects useful context and provides that context to a language model.

This approach can help applications answer questions using
domain-specific or updated information contained in the knowledge base.
""",

        "questions": {
            "Easy": "What is the main purpose of retrieving information in a RAG system?",
            "Medium": "How does retrieved information help a language model answer a question?",
            "Hard": "Why can RAG be useful when building an AI application that needs domain-specific information?"
        },

        "keywords": {
            "Easy": ["information", "context", "knowledge", "answer", "relevant"],
            "Medium": ["retrieve", "context", "information", "question", "answer"],
            "Hard": ["knowledge", "domain", "information", "documents", "context", "updated"]
        }
    },

    "AI Agents": {
        "title": "Introduction to AI Agents",

        "easy": """
An AI agent is a system designed to perceive information
and take actions toward a goal.

A simple agent workflow can be:

Observe → Think → Act → Observe again

For example, an AI agent could receive a user's goal,
decide what steps are needed, use available tools,
and then return the result.
""",

        "medium": """
AI agents can combine reasoning, planning and tool usage
to accomplish a goal.

Instead of only generating a response,
an agent can decide which actions are required,
use available tools and evaluate the results.
""",

        "hard": """
An AI agent can be viewed as a system that receives observations,
maintains relevant context, decides what action to take,
uses available tools and evaluates the resulting information.

This allows an agent to perform multi-step tasks rather than
simply producing a single response to a prompt.
""",

        "questions": {
            "Easy": "What is one important difference between an AI agent and a simple chatbot?",
            "Medium": "Why might an AI agent need tools when completing a task?",
            "Hard": "Describe how an AI agent could complete a multi-step task using observations, decisions and tools."
        },

        "keywords": {
            "Easy": ["action", "goal", "tools", "steps", "act"],
            "Medium": ["tools", "action", "goal", "task", "steps"],
            "Hard": ["observe", "observation", "decision", "action", "tools", "steps", "goal"]
        }
    }
}


# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def get_difficulty():
    return st.session_state.difficulty


def calculate_answer_score(answer, keywords):
    answer_lower = answer.lower()

    matched = 0

    for keyword in keywords:
        if keyword.lower() in answer_lower:
            matched += 1

    total = len(keywords)

    if total == 0:
        return 0

    return matched / total


def adapt_tutor(score):
    """
    Adapt difficulty based on learner performance.
    """

    if score >= 0.40:
        if st.session_state.difficulty == "Easy":
            st.session_state.difficulty = "Medium"
        elif st.session_state.difficulty == "Medium":
            st.session_state.difficulty = "Hard"

        st.session_state.mastery_points += 10

        if st.session_state.mastery_points >= 20:
            st.session_state.mastery = "Improving"
        else:
            st.session_state.mastery = "Practice"

        return "correct"

    elif score > 0:
        st.session_state.mastery = "Needs Practice"
        st.session_state.mastery_points += 3

        return "partial"

    else:
        if st.session_state.difficulty == "Hard":
            st.session_state.difficulty = "Medium"
        elif st.session_state.difficulty == "Medium":
            st.session_state.difficulty = "Easy"

        st.session_state.mastery = "Needs Review"

        return "weak"


# -----------------------------
# HEADER
# -----------------------------
st.title("🤖 AI StudyMate")
st.caption("Your Personalized AI Tutor for Learning AI")


# -----------------------------
# TUTOR SCREEN
# -----------------------------
if st.session_state.tutor_started:

    topic = st.session_state.current_topic

    if topic not in lessons:
        st.error("No lesson is available for this topic.")
        st.stop()

    lesson = lessons[topic]
    difficulty = get_difficulty()

    st.success(
        f"🎯 Personalized lesson: **{topic}**"
    )

    st.info(
        f"🧠 Adaptive Difficulty: **{difficulty}**"
    )

    st.header(f"📚 {lesson['title']}")

    st.write(
        lesson[difficulty.lower()]
    )

    st.divider()

    st.subheader("🧠 Adaptive Check")

    st.write(
        lesson["questions"][difficulty]
    )

    answer = st.text_area(
        "Write your answer in your own words:",
        height=150,
        placeholder="Type your answer here..."
    )

    if st.button("✅ Check My Understanding"):

        if not answer.strip():

            st.warning(
                "Please write an answer before checking."
            )

        else:

            keywords = lesson["keywords"][difficulty]

            score = calculate_answer_score(
                answer,
                keywords
            )

            result = adapt_tutor(score)

            st.session_state.attempts += 1

            if result == "correct":

                st.success(
                    "🎉 Good job! Your answer demonstrates "
                    "understanding of the key concept."
                )

                st.write("### 🌟 Adaptive Tutor Feedback")

                st.write(
                    "You performed well, so the tutor is increasing "
                    "the difficulty of your next activity."
                )

                st.write(
                    f"**Next difficulty:** {st.session_state.difficulty}"
                )

            elif result == "partial":

                st.info(
                    "👍 You're on the right track."
                )

                st.write("### 💡 Tutor Hint")

                st.write(
                    "Your answer contains part of the expected concept. "
                    "Review the lesson and try to include the main idea "
                    "more clearly."
                )

                st.write(
                    f"**Current difficulty:** {st.session_state.difficulty}"
                )

            else:

                st.error(
                    "Let's review this concept once more."
                )

                st.write("### 💡 Tutor Support")

                st.write(
                    "The tutor has reduced the difficulty to help "
                    "you strengthen the fundamentals."
                )

                st.write(
                    f"**New difficulty:** {st.session_state.difficulty}"
                )

    st.divider()

    st.subheader("📈 Your Learning Progress")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Attempts",
            st.session_state.attempts
        )

    with col2:
        st.metric(
            "Mastery Points",
            st.session_state.mastery_points
        )

    with col3:
        st.metric(
            "Difficulty",
            st.session_state.difficulty
        )

    if st.session_state.mastery == "Improving":

        st.success(
            "🟢 Mastery Status: Improving"
        )

    elif st.session_state.mastery == "Needs Practice":

        st.warning(
            "🟡 Mastery Status: Needs Practice"
        )

    elif st.session_state.mastery == "Needs Review":

        st.error(
            "🔴 Mastery Status: Needs Review"
        )

    else:

        st.info(
            "🔵 Mastery Status: Start your first activity"
        )

    st.divider()

    if st.button("🔄 Continue Adaptive Learning"):

        st.rerun()

    if st.button("⬅️ Back to Personalized Path"):

        st.session_state.tutor_started = False

        st.rerun()

    st.stop()


# -----------------------------
# WELCOME SCREEN
# -----------------------------
if not st.session_state.started:

    st.subheader(
        "Learn AI at your own pace."
    )

    st.write(
        "AI StudyMate first understands what you already know, "
        "then adapts the learning experience based on your performance."
    )

    st.write("### What your AI tutor will do")

    st.write("🔎 Assess your current knowledge")
    st.write("🎯 Identify your weakest topics")
    st.write("🛣️ Create a personalized learning path")
    st.write("🤖 Teach concepts step by step")
    st.write("📈 Adapt difficulty based on your performance")

    if st.button("🚀 Start Learning"):

        st.session_state.started = True

        st.rerun()

    st.stop()


# -----------------------------
# PROFILE
# -----------------------------
if not st.session_state.profile:

    st.header("👤 Tell Me About Yourself")

    name = st.text_input(
        "Your Name"
    )

    level = st.selectbox(
        "Current AI Experience",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    goal = st.selectbox(
        "What do you want to achieve?",
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

    if st.button("Continue →"):

        if not name.strip():

            st.warning(
                "Please enter your name."
            )

        else:

            st.session_state.profile = {
                "name": name,
                "level": level,
                "goal": goal,
                "study_time": study_time
            }

            st.rerun()

    st.stop()


# -----------------------------
# DIAGNOSTIC TEST
# -----------------------------
if not st.session_state.diagnostic_completed:

    st.header("🧠 AI Knowledge Diagnostic")

    st.write(
        f"Hi **{st.session_state.profile['name']}**! "
        "Let's quickly understand what you already know."
    )

    st.write(
        "There are 10 questions. Answer honestly — "
        "the goal is to personalize your learning path."
    )

    questions = [

        (
            "AI Fundamentals",
            "What does AI stand for?",
            [
                "Artificial Intelligence",
                "Automated Internet",
                "Advanced Information",
                "Artificial Interface"
            ],
            "Artificial Intelligence"
        ),

        (
            "AI Fundamentals",
            "Which is an example of AI?",
            [
                "A calculator",
                "A system recognizing objects in images",
                "A light bulb",
                "A keyboard"
            ],
            "A system recognizing objects in images"
        ),

        (
            "Python",
            "Which symbol is commonly used to write a comment in Python?",
            [
                "//",
                "#",
                "<!--",
                "**"
            ],
            "#"
        ),

        (
            "Python",
            "Which Python data type represents True or False?",
            [
                "String",
                "Integer",
                "Boolean",
                "List"
            ],
            "Boolean"
        ),

        (
            "Machine Learning",
            "What is supervised learning?",
            [
                "Learning without data",
                "Learning from labelled examples",
                "Only writing rules manually",
                "Deleting incorrect data"
            ],
            "Learning from labelled examples"
        ),

        (
            "Machine Learning",
            "What is a training dataset?",
            [
                "Data used to teach a model",
                "A programming language",
                "A computer",
                "A user interface"
            ],
            "Data used to teach a model"
        ),

        (
            "Generative AI",
            "What can a generative AI model do?",
            [
                "Only classify data",
                "Generate new content",
                "Only store files",
                "Only calculate numbers"
            ],
            "Generate new content"
        ),

        (
            "Generative AI",
            "What does LLM stand for?",
            [
                "Large Language Model",
                "Long Learning Machine",
                "Logical Language Method",
                "Large Logic Machine"
            ],
            "Large Language Model"
        ),

        (
            "RAG",
            "What does RAG stand for?",
            [
                "Retrieval-Augmented Generation",
                "Random AI Generation",
                "Rapid Automated Guidance",
                "Retrieved AI Graph"
            ],
            "Retrieval-Augmented Generation"
        ),

        (
            "AI Agents",
            "What are AI agents designed to do?",
            [
                "Only answer fixed questions",
                "Perceive information and take actions toward a goal",
                "Only store data",
                "Only generate images"
            ],
            "Perceive information and take actions toward a goal"
        )
    ]

    answers = []

    for i, (
        topic,
        question,
        options,
        correct
    ) in enumerate(questions):

        st.subheader(
            f"Question {i + 1}"
        )

        answer = st.radio(
            question,
            options,
            key=f"question_{i}"
        )

        answers.append(
            (topic, answer, correct)
        )

    if st.button(
        "📊 Generate My Personalized Path"
    ):

        topic_scores = {}

        for topic, answer, correct in answers:

            if topic not in topic_scores:

                topic_scores[topic] = {
                    "correct": 0,
                    "total": 0
                }

            topic_scores[topic]["total"] += 1

            if answer == correct:

                topic_scores[topic]["correct"] += 1

        for topic in topic_scores:

            correct = topic_scores[topic]["correct"]

            total = topic_scores[topic]["total"]

            topic_scores[topic]["percentage"] = int(
                correct / total * 100
            )

        st.session_state.topic_scores = topic_scores

        st.session_state.diagnostic_completed = True

        st.rerun()

    st.stop()


# -----------------------------
# PERSONALIZED PATH
# -----------------------------
st.header(
    "🛣️ Your Personalized Learning Path"
)

st.write(
    f"Based on your diagnostic assessment, "
    f"here is the learning path created for "
    f"**{st.session_state.profile['name']}**."
)

scores = st.session_state.topic_scores

ordered_topics = sorted(
    scores.keys(),
    key=lambda topic: scores[topic]["percentage"]
)

for position, topic in enumerate(
    ordered_topics,
    start=1
):

    percentage = scores[topic]["percentage"]

    if percentage >= 80:

        status = "🟢 Strong"

    elif percentage >= 50:

        status = "🟡 Practice More"

    else:

        status = "🔴 Priority"

    st.write(
        f"**{position}. {topic}** — "
        f"{percentage}% — {status}"
    )

    st.progress(
        percentage / 100
    )

weakest_topic = ordered_topics[0]

st.session_state.current_topic = weakest_topic

st.divider()

st.subheader(
    "🎯 Your Recommended Focus"
)

st.info(
    f"Your tutor recommends starting with "
    f"**{weakest_topic}** because this is currently "
    "your weakest area."
)

st.write(
    "The tutor will automatically adjust the difficulty "
    "of your learning activities based on your answers."
)

if st.button(
    "🤖 Start My Adaptive Lesson"
):

    st.session_state.tutor_started = True

    st.rerun()
