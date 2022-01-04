
class QuizBrain:

    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

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

    def check_answer(self, user_answer, question_answer):
        if user_answer == question_answer:
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {question_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

