import os
import abc

class Question:
    def __init__(self, str_question, points):
        self.str_question = str_question
        self.points = points
    
    def __str__(self):
        return self.str_question

    def read_questions(self, file_name):
        with open(file_name, "r") as file_handler:
            self.list_lines = file_handler.readlines()

    def create_questions(self):
        for index, value in self.list_lines:
            if index == 0 index // 6 == 0:
                return self.list_lines

def SingleAnswerQuestion(Question, str_question, points, single_answer):
    super().__init__(self, str_question, points)
    self.single_answer = single_answer

def MultipleAnswerQuestion(Question):
    pass

test = Question("What is your question?", 10)

print(test)



