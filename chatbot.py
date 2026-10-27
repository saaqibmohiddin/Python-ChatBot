
import streamlit as st
from datetime import datetime
import random
import re

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="PyTalk - Python Learning Assistant",
    page_icon="🤖",
    layout="centered"
)

# ==========================================
# CHATBOT KNOWLEDGE BASE
# ==========================================

def get_response(user):
    question = user.lower().strip()
    question = re.sub(r"[?!.,]", "", question)
    question = re.sub(r"\s+", " ", question)

    # Greetings
    greetings = [
        "hi", "hello", "hey", "hai",
        "good morning", "good afternoon",
        "good evening"
    ]

    if question in greetings or any(
        question.startswith(g + " ") for g in greetings
    ):
        return "Hello! 👋 Welcome to PyTalk. What would you like to learn today?"

    if "how are you" in question:
        return "I'm doing great! 😊 Ready to help you learn Python and technology."

    if "your name" in question or "who are you" in question:
        return "I'm PyTalk, your personal Python learning chatbot. 🤖"

    if "who created you" in question:
        return "I was developed using Python and Streamlit."

    if question in ["bye", "goodbye", "see you"]:
        return "Goodbye! Keep learning and coding. See you again! 👋"

    # Help
    if "help" in question or "what can you do" in question:
        return """
### 🤖 PyTalk can help you with:

- Python fundamentals
- Python data types and operators
- Functions and OOP
- Python programming examples
- Artificial Intelligence
- Machine Learning
- Deep Learning
- HTML, CSS and JavaScript
- SQL and databases
- Basic programming interview preparation

Try asking: **What is Python?**
"""

    # Python fundamentals
    if "what is python" in question or question == "python":
        return """
### 🐍 What is Python?

Python is a high-level, interpreted, general-purpose programming language.

**Features:**
1. Easy to learn and read.
2. Simple syntax.
3. Supports object-oriented programming.
4. Large collection of libraries.
5. Cross-platform compatibility.

**Applications:**
- Artificial Intelligence
- Machine Learning
- Web development
- Data science
- Automation

**Example:**
```python
print("Hello, World!")
```
"""

    if "features of python" in question:
        return """
### Features of Python

1. Simple and readable syntax.
2. Interpreted language.
3. Dynamically typed.
4. Object-oriented.
5. Portable.
6. Open source.
7. Large standard library.
"""

    if "advantages of python" in question:
        return """
### Advantages of Python

1. Easy to learn.
2. Faster development.
3. Large community support.
4. Many libraries and frameworks.
5. Useful in AI, ML and automation.
"""

    if "disadvantages of python" in question:
        return """
### Disadvantages of Python

1. Can be slower than compiled languages.
2. Can consume more memory in some applications.
3. Not the first choice for every mobile application.
4. Dynamic typing can allow errors to appear at runtime.
"""

    # Data types
    if "data types" in question:
        return """
### Python Data Types

| Type | Example |
|---|---|
| int | 10 |
| float | 10.5 |
| str | "Hello" |
| bool | True |
| list | [1, 2, 3] |
| tuple | (1, 2, 3) |
| set | {1, 2, 3} |
| dict | {"name": "Sam"} |

Example:
```python
name = "Python"
age = 25
price = 99.5
is_active = True

print(type(name))
```
"""

    if "list and tuple" in question or "difference between list and tuple" in question:
        return """
### List vs Tuple

**List**
- Uses square brackets `[]`.
- Mutable: values can be changed.
- Example: `numbers = [10, 20, 30]`

**Tuple**
- Uses parentheses `()`.
- Immutable: values cannot be changed.
- Example: `numbers = (10, 20, 30)`
"""

    if "dictionary" in question or "dict in python" in question:
        return """
### Python Dictionary

A dictionary stores information as key-value pairs.

Example:
```python
student = {
    "name": "Alex",
    "age": 21,
    "course": "Python"
}

print(student["name"])
```
"""

    if "set in python" in question:
        return """
### Python Set

A set stores unique elements and does not maintain a guaranteed order.

Example:
```python
numbers = {10, 20, 20, 30}
print(numbers)
```
"""

    # Functions and OOP
    if "function" in question:
        return """
### Python Functions

A function is a reusable block of code.

Example:
```python
def greet(name):
    print("Hello", name)

greet("Alex")
```

The `def` keyword defines a function.
"""

    if "oop" in question or "object oriented" in question:
        return """
### Object-Oriented Programming (OOP)

OOP organizes programs using classes and objects.

Four major principles:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

Example:
```python
class Student:
    def greet(self):
        print("Hello Student")

s = Student()
s.greet()
```
"""

    if "class and object" in question:
        return """
### Class and Object

A **class** is a blueprint.

An **object** is an instance of a class.

Example:
```python
class Car:
    brand = "Toyota"

car1 = Car()
print(car1.brand)
```
"""

    if "exception handling" in question:
        return """
### Exception Handling

Exception handling prevents a program from stopping unexpectedly when an error occurs.

Example:
```python
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Enter a valid number")
```
"""

    # Python programs
    if "even or odd" in question:
        return """
### Program: Even or Odd

```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```
"""

    if "prime number" in question:
        return """
### Program: Prime Number

```python
number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")
```
"""

    if "factorial" in question:
        return """
### Program: Factorial

```python
number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("Factorial:", factorial)
```
"""

    if "fibonacci" in question:
        return """
### Program: Fibonacci Series

```python
a, b = 0, 1

for i in range(10):
    print(a)
    a, b = b, a + b
```
"""

    if "palindrome" in question:
        return """
### Program: Palindrome

```python
word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
```
"""

    if "reverse a string" in question:
        return """
### Program: Reverse a String

```python
text = input("Enter text: ")
reverse = text[::-1]

print(reverse)
```
"""

    if "armstrong" in question:
        return """
### Program: Armstrong Number

```python
number = int(input("Enter a number: "))
digits = str(number)

total = sum(int(d) ** len(digits) for d in digits)

if total == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
```
"""

    # AI and technology
    if "artificial intelligence" in question or "what is ai" in question:
        return """
### Artificial Intelligence (AI)

AI is a field of computer science that develops systems capable of performing tasks that normally require human intelligence.

**Examples:**
1. Voice assistants.
2. Chatbots.
3. Image recognition.
4. Recommendation systems.
5. Self-driving technology.
"""

    if "machine learning" in question:
        return """
### Machine Learning (ML)

Machine Learning is a branch of AI that enables computers to learn patterns from data.

**Types:**
1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning

**Libraries:** Scikit-learn, TensorFlow and PyTorch.
"""

    if "deep learning" in question:
        return """
### Deep Learning

Deep Learning is a subset of Machine Learning that uses multi-layered neural networks.

Applications:
- Image recognition
- Speech recognition
- Natural Language Processing
- Autonomous systems
"""

    if "natural language processing" in question or "what is nlp" in question:
        return """
### Natural Language Processing (NLP)

NLP helps computers understand, process and generate human language.

Applications:
- Chatbots
- Language translation
- Sentiment analysis
- Speech recognition
"""

    if "generative ai" in question:
        return """
### Generative AI

Generative AI creates new content such as text, images, audio and code.

Examples include AI writing assistants, image generators and coding assistants.
"""

    # Web and database technologies
    if "what is html" in question:
        return "HTML stands for HyperText Markup Language. It structures content on web pages."

    if "what is css" in question:
        return "CSS stands for Cascading Style Sheets. It controls the appearance and layout of web pages."

    if "javascript" in question:
        return "JavaScript is a programming language used to create interactive web applications."

    if "what is sql" in question:
        return "SQL stands for Structured Query Language. It is used to manage and query relational databases."

    if "what is database" in question:
        return "A database is an organized collection of information that can be stored, managed and retrieved."

    if "what is api" in question:
        return "API stands for Application Programming Interface. It allows different software applications to communicate."

    if "what is streamlit" in question:
        return "Streamlit is a Python framework for building interactive web applications, especially for data and AI projects."

    if "what is github" in question:
        return "GitHub is a platform for hosting code, managing repositories and collaborating on software projects."

    # Time and date
    if "time" in question or "date" in question:
        return "Current date and time: " + datetime.now().strftime("%d-%m-%Y %I:%M %p")

    # Fallback
    return """
I don't have a predefined answer for that question yet.

Try one of these topics:

- What is Python?
- Explain Python data types.
- What is OOP?
- Write a prime number program.
- What is Artificial Intelligence?
- Explain Machine Learning.
- What is SQL?

Use the Learning Topics section to explore more.
"""


# ==========================================
# QUIZ QUESTIONS
# ==========================================

QUIZ_QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "answer": "Tuple"
    },
    {
        "question": "What is the output of print(2 ** 3)?",
        "options": ["6", "8", "9", "5"],
        "answer": "8"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },
    {
        "question": "Which library is commonly used for data analysis?",
        "options": ["Pandas", "Turtle", "Random", "OS"],
        "answer": "Pandas"
    }
]


# ==========================================
# SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! 👋 Welcome to PyTalk. How can I help you today?",
            "time": datetime.now().strftime("%I:%M %p")
        }
    ]

if "quiz_question" not in st.session_state:
    st.session_state.quiz_question = 0

if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0

if "quiz_answered" not in st.session_state:
    st.session_state.quiz_answered = False

if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False


# ==========================================
# MAIN HEADER
# ==========================================

st.title("🤖 PyTalk")
st.subheader("Your Personal Python Learning Assistant")

st.write(
    "Learn Python, explore AI concepts, "
    "practice programming and test your knowledge."
)

st.divider()


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:
    st.title("🚀 PyTalk Menu")

    st.write("Explore your learning assistant.")

    st.subheader("📚 Learning Topics")

    topics = [
        "What is Python?",
        "Explain Python data types",
        "What is OOP?",
        "What is Artificial Intelligence?",
        "Explain Machine Learning",
        "What is Deep Learning?",
        "What is SQL?"
    ]

    for topic in topics:
        if st.button(topic, use_container_width=True):
            st.session_state.messages.append({
                "role": "user",
                "content": topic,
                "time": datetime.now().strftime("%I:%M %p")
            })

            st.session_state.messages.append({
                "role": "assistant",
                "content": get_response(topic),
                "time": datetime.now().strftime("%I:%M %p")
            })

            st.rerun()

    st.divider()

    st.subheader("📥 Chat Export")

    chat_text = ""

    for message in st.session_state.messages:
        chat_text += (
            f"{message['time']} - "
            f"{message['role'].upper()}: "
            f"{message['content']}\n\n"
        )

    st.download_button(
        label="Download Chat History",
        data=chat_text,
        file_name="pytalk_chat_history.txt",
        mime="text/plain",
        use_container_width=True
    )

    st.divider()

    st.caption("Built with Python and Streamlit")


# ==========================================
# CHAT CONTROLS
# ==========================================

col1, col2 = st.columns(2)

with col1:
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! Welcome to PyTalk. How can I help you today?",
                "time": datetime.now().strftime("%I:%M %p")
            }
        ]
        st.rerun()

with col2:
    if st.button("🎓 Start Python Quiz", use_container_width=True):
        st.session_state.quiz_started = True
        st.session_state.quiz_question = 0
        st.session_state.quiz_score = 0
        st.session_state.quiz_answered = False
        st.rerun()


# ==========================================
# CHAT DISPLAY
# ==========================================

st.subheader("💬 Chat with PyTalk")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        st.caption(message["time"])


# ==========================================
# CHAT INPUT
# ==========================================

user_input = st.chat_input("Ask PyTalk a question...")

if user_input:
    now = datetime.now().strftime("%I:%M %p")

    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "time": now
    })

    response = get_response(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response,
        "time": datetime.now().strftime("%I:%M %p")
    })

    st.rerun()


# ==========================================
# PYTHON QUIZ
# ==========================================

if st.session_state.quiz_started:

    st.divider()
    st.subheader("🎓 Python Knowledge Quiz")

    total = len(QUIZ_QUESTIONS)
    current = st.session_state.quiz_question

    if current < total:

        question = QUIZ_QUESTIONS[current]

        st.progress(current / total)

        st.write(f"Question {current + 1} of {total}")

        st.markdown(f"### {question['question']}")

        selected = st.radio(
            "Choose your answer:",
            question["options"],
            key=f"quiz_option_{current}"
        )

        if not st.session_state.quiz_answered:

            if st.button("Submit Answer"):
                if selected == question["answer"]:
                    st.session_state.quiz_score += 1
                    st.success("Correct answer! 🎉")
                else:
                    st.error(
                        f"Incorrect. Correct answer: "
                        f"{question['answer']}"
                    )

                st.session_state.quiz_answered = True
                st.rerun()

        else:
            if st.button("Next Question"):
                st.session_state.quiz_question += 1
                st.session_state.quiz_answered = False
                st.rerun()

    else:
        st.progress(1.0)

        st.success("Quiz completed!")

        st.metric(
            "Your Score",
            f"{st.session_state.quiz_score}/{total}"
        )

        if st.session_state.quiz_score == total:
            st.balloons()
            st.write("Excellent! You answered every question correctly.")
        else:
            st.write("Good effort! Keep practicing Python.")

        if st.button("Restart Quiz"):
            st.session_state.quiz_question = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_answered = False
            st.rerun()


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "🤖 PyTalk | Built with Python and Streamlit"
)

st.caption(
    "Note: PyTalk uses predefined, rule-based responses. "
    "It is a learning demonstration, not a general-purpose AI model."
)
