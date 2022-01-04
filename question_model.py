# This file is the class showing how we model the question. Each question has a text portion, and a answer
# portion. We can access this data using this class!

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer