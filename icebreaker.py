import random
import openpyxl

# Save the excel file questions in a list

workbook = openpyxl.load_workbook("icebreaker_questions.xlsx")
sheet = workbook.worksheets[0]
questions_list = []

for row in sheet:
    question = row[0].value
    questions_list.append(question)

questions_length = len(questions_list)



print(questions_length)