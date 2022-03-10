from flask import Flask, render_template, request, flash
import json
import random

with open('questions_data.json') as f:
    questions = json.load(f)
    print("Loaded json data is: {}".format(questions))
    # Retrieving data from json file

carried_over = 0

app = Flask(__name__)
app.secret_key = "sausage123" # Not used

@app.route('/', methods=["POST", "GET"])
def index():
    global carried_over
    question_number = random.randrange(len(questions))
    correct_radio_button = random.randrange(0,3)
    print("Correct answer is: ", correct_radio_button)
    # The random numbers have to be generated here each time the page is loaded so they are different each time.
    user_answer = request.form.get('radio_1')
    print("Users selected answer is: ", user_answer)
    # Gets the selected answer from radio buttons (returns None if none selected)
    answer_1 = "Wrong answer 1"
    answer_2 = "Wrong answer 2"
    answer_3 = "Wrong answer 3"
    # Incorrect answers are asigned to all options first
    answer_list = [answer_1, answer_2, answer_3]
    answer_list[correct_radio_button] = questions[str(question_number)][3]
    # This sets the correct answer in the list using the random number generated before in 'correct_radio_button'
    
    if user_answer != None: # checks if an answer has been entered and if it is correct
        if user_answer == str(carried_over):
            flash("Correct!")
        else:
            flash("Wrong answer")
    carried_over = correct_radio_button
    return render_template('index.html', pass_question = questions[str(question_number)][0], 
    pass_sentence = questions[str(question_number)][1], pass_answer1 = answer_list[0],
    pass_answer2 = answer_list[1], pass_answer3 = answer_list[2])
    # Variables are passed to index.html



        
