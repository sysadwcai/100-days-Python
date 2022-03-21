from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = '#375362'

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):  # quiz_brain: QuizBrain (data type)
        self.quiz = Quiz_Brain  #call the quiz_brain class
        self.window = Tk()
        self.window.title('quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280, #get the question text wrap into nextline
            text='questions',
            fill=THEME_COLOR,
            font=('Ariel', 20, 'italic')
        )
        self.canvas.grid(row=1, coloumn=0, columnspan=2, pady=50)  # padding for y coordinate
        
        self.score_text = Label(text=f'Score: 0', fg='white', bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)
        
        true_img = PhotoImage(file='images/true.png')  # no need for self.true_img (only call once here)
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=2)
        
        false_img = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
   def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_question():
            self.score_text.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text={q_text})
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state='disable')
            self.false_button.config(state='disable')
            
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))
    
    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.get_next_question)
        
        
    
                                   
        
