# Today's project with 100 days of code, is a quiz game. Built using object-oriented programing, I am tasked to create a
# game using my own created classes. Poke around and play with the game a bit!

# Importing classes and data from other files
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Empty list for the question bank.
question_bank = []

# This for loop puts all the questions into the question bank as instances.
for item in question_data:
    new_question = Question(item["question"], item["correct_answer"])
    question_bank.append(new_question)

# Initializing the quiz instance
quiz = QuizBrain(question_bank)

# Main Quiz while loop, while we still have questions to be answered the quiz continues.
while quiz.still_have_questions():

    # This simply calls the next question to the quiz from the Class QuizBrain
    quiz.next_question()

# Print Game ending texts and show user the final score.
print("You have completed the Quiz.")
print(f"Your Final score was {quiz.score}/{quiz.question_number}!")
