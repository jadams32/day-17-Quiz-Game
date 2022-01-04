# This is the main logic for our quiz. It contains the QuizBrain class and all the methods used to play the game.
class QuizBrain:

    # Here the init method initializes the users score, question number, and question list.
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    # This method brings in a question from the list and asks the user for answer.
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {current_question.text}(True/False):")
        self.check_answer(user_answer, current_question.answer)

    def still_have_questions(self):
        """Returns True if there are questions left to answer, false otherwise."""
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    # This method checks if the users answer was correct or not and adds to their score, displaying correct or not
    # and total score.
    def check_answer(self, user_answer, question_answer):
        if user_answer == question_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {question_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
