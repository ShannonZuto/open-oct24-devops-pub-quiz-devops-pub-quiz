# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B"
    },
    {
        "question": "What is 12 X 12?",
        "options": ["A) 133", "B) 144", "C) 155", "D) 122"],
        "answer": "B"
    },
    {
        "question": "What is the name of the tallest mountain in the world?",
        "options": ["A) Everest", "B) Mount Kilimanjaro", "C) K2", "D) Ben Nevis"],
        "answer": "A"
    },
    {
        "question": "How many wives did Henry VIII have?",
        "options": ["A) 4", "B) 1", "C) 6", "D) 12"],
        "answer": "C"
    },
]

correct_answers = 0
# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
    user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison
    
    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

print(f"You got {correct_answers} out of {len(quiz_questions)} questions correct.")

# Goodbye message
print("Thanks for playing the Pub Quiz!")
