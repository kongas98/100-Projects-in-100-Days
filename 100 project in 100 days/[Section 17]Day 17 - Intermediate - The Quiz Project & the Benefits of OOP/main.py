from question_model import Question  # Import the Question class from question_model module
from data import question_data  # Import the question data from data module
from quiz_brain import QuizBrain  # Import the QuizBrain class from quiz_brain module

# Initialize an empty list to store the question objects
question_bank = []

# Loop through each question in the question_data list
for question in question_data:
    # Create a new Question object with the question text and answer
    new_question = Question(question["text"], question["answer"])
    # Add the new Question object to the question_bank list
    question_bank.append(new_question)

# Create a QuizBrain object with the question_bank list
quiz = QuizBrain(question_bank)

# Loop through the quiz questions as long as there are still questions left
while quiz.still_has_questions():
    # Ask the next question in the quiz
    quiz.next_question()
    print("\n\n")  # Print new lines for better readability

# Check the final score and provide feedback to the user
if quiz.score == len(question_bank):
    print(f"Wow!!! You did TERRIFIC!! YOU GOT ALL {len(question_bank)} QUESTIONS RIGHT!")
elif quiz.score >= (len(question_bank) / 2) and quiz.score < len(question_bank):
    print("Nice job!!! You managed to get most of the questions correct!! Congrats!!")
else:
    print("Well... That could have gone better. Better luck next time!")
