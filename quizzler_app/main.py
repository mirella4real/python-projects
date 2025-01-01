from question_model import Question # type: ignore
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests
import html

question_bank = []

def call_api(api_url, parameters=None):
    if parameters != None:
        response = requests.get(url=api_url, params=parameters)
    else:
        response = requests.get(url=api_url)
    response.raise_for_status()
    return response.json()

def create_question_bank():
    parameters = {
        "amount": 10,
        "type": "boolean"
    }
    data = call_api("https://opentdb.com/api.php", parameters)

    for question in data["results"]:
        question_bank.append(Question(html.unescape(question['question']), question['correct_answer']))
    return True

def init():
    if create_question_bank() == True:
        my_quiz_brain = QuizBrain(question_bank)
        my_quiz_ui = QuizInterface(my_quiz_brain)
  
init()
