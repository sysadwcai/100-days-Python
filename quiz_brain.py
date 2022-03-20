import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
#         if self.question_number < len(self.question_list):
#             return True
#         return False
    
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f'Q.{self.question_number}: {q_text}'
#         user_answer = input(f"Q: {self.question_number}{q_text} (True/False):")
#         self.check_answer(user_answer, current_question.answer)
        
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            score += 1
            return True
            #print("You got it right!"
        else:
            return False
            #print("That's wrong.")
#         print(f"The correct answer is: {correct_answer}")
#         print(f"Your current score is: {score}/{self.question_number}.")
#         print('\n')
         
            
