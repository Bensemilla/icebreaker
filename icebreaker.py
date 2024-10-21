import random
import openpyxl
from tkinter import *

# Save the excel file questions in a list

workbook = openpyxl.load_workbook("icebreaker_questions.xlsx")
sheet = workbook.worksheets[0]
questions_list = []

for row in sheet:
    question = row[0].value
    questions_list.append(question)

questions_length = len(questions_list)


#Define function to retrieve random question

def random_question():
    question_num = random.randint(0, (questions_length - 1))
    return(questions_list[question_num])


# Create and define root GUI window, label and button

root_window = Tk()
root_window.title("Icebreaker questions")
root_window.geometry('350x200')

lbl = Label(root_window, text = "Get an icebreaker question by clicking the button!")
lbl.grid()

def clicked():
    lbl.configure(text = random_question())

btn = Button(root_window, text = "Click me!", fg = "green", command = clicked)
btn.grid(column = 0, row = 4)

root_window.mainloop()

