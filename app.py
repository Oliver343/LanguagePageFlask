from flask import Flask, render_template, request, flash
import json
import random

with open('questions_data.json') as f:
    questions = json.load(f)
    print("Loaded json data is: {}".format(questions))
    # Retrieving data from json file `questions_data.json`

carried_over = 0  # This is where the correct answer is stored so it can be checked even any the page is refreshed.

app = Flask(__name__)
app.secret_key = "sausage123" # Not used

@app.route('/', methods=["POST", "GET"])
def index():
    """ Runs when the main page is loaded. Generates random questions and answers. Relies on global variable nammed `carried_over` """
    global carried_over
    question_number = random.randrange(len(questions))
    wrong_answer1 = question_number
    wrong_answer2 = question_number
    wrong_answer3 = question_number
    correct_radio_button = random.randrange(0,3)
    print("Correct answer is: ", correct_radio_button)
    # The random numbers have to be generated here each time the page is loaded so they are different each time.
    while wrong_answer1 == question_number:
        wrong_answer1 = random.randrange(len(questions))
    while wrong_answer2 == question_number or wrong_answer2 == wrong_answer1:
        wrong_answer2 = random.randrange(len(questions))
    while wrong_answer3 == question_number or wrong_answer3 == wrong_answer1 or wrong_answer3 == wrong_answer2:
        wrong_answer3 = random.randrange(len(questions))
        # In these while loops, it will keep generating random numbers until
        # all the wrong answers have unique answers that dont match the correct answer.  
    user_answer = request.form.get('radio_1')
    print("Users selected answer is: ", user_answer)
    # Gets the selected answer from radio buttons (returns None if none selected)
    answer_1 = questions[str(wrong_answer1)][random.randint(3,4)]
    answer_2 = questions[str(wrong_answer2)][random.randint(3,4)]
    answer_3 = questions[str(wrong_answer3)][random.randint(3,4)]
    # Incorrect answers are asigned to all options first
    answer_list = [answer_1, answer_2, answer_3]
    answer_list[correct_radio_button] = questions[str(question_number)][random.randint(3,4)]
    # This sets the correct answer in the list using the random number generated before in 'correct_radio_button'
    
    if user_answer != None: # checks if an answer has been entered and if it is correct
        if user_answer == str(carried_over):
            flash("Correct!")
        else:
            flash("Wrong answer")
    carried_over = correct_radio_button
    return render_template('index.html', pass_question = questions[str(question_number)][0], 
    pass_sentence = questions[str(question_number)][random.randint(1,2)], pass_answer1 = answer_list[0],
    pass_answer2 = answer_list[1], pass_answer3 = answer_list[2])
    # Variables are passed to index.html



        
