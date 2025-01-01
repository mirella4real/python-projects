class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.correct_answers = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        question.number = self.question_number
        return question
    
    def has_questions_left(self):
        """Returns true if there are any questions left"""
        return self.question_number < len(self.question_list)
    
    def check_answer(self, response:str) -> bool:
        question = self.question_list[self.question_number - 1]
        if question.answer.lower() == response:
            self.correct_answers += 1
            return True
        else:
            return False

    def get_score(self):
        return self.correct_answers
    
    def get_total_questions(self):
        return len(self.question_list)