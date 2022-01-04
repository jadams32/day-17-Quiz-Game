# Today's project with 100 days of code, is a quiz game. Built using object-oriented programing, I am tasked to create a
# game using my own created classes. Poke around and play with the game a bit!

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    new_question = Question(item["text"], item["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()