from question_model import Question # type: ignore
from quiz_brain import QuizBrain
from ui import QuizInterface
import requests
import html

CORRECT = "Correct!"
WRONG = "Wrong answer."
YOUR_CURRENT_SCORE = "Your current score is"
OUT_OF = "out of"
CORRECT_ANSWER = "The correct answer was:"
END_MESSAGE = "You've completed the quiz!"
FINAL_SCORE = "Your final score was:"
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

def run_quiz(my_quiz_brain, question):
    print("\n")
    response = input(f"Q.{question.number}: {question.text} (True or False): ").lower()
    is_correct = my_quiz_brain.is_correct_answer(question, response)
    if is_correct == True:
        print(CORRECT) 
    else:
        print(WRONG)
    print(f"{CORRECT_ANSWER} {question.answer}.")
    print(f"{YOUR_CURRENT_SCORE} {my_quiz_brain.get_score()} {OUT_OF} {question.number}")
    

def end_quiz(my_quiz_brain):
    print("\n")
    print(f"{END_MESSAGE}")
    print(f"{FINAL_SCORE} {my_quiz_brain.get_score()}/{my_quiz_brain.get_total_questions()}\n")

def init():
    if create_question_bank() == True:
        my_quiz_brain = QuizBrain(question_bank)
        my_quiz_ui = QuizInterface()
        can_run_quiz = my_quiz_brain.has_questions_left()
        # while can_run_quiz == True:
        #     question = my_quiz_brain.next_question()
        #     run_quiz(my_quiz_brain, question)
        #     can_run_quiz = my_quiz_brain.has_questions_left()
        # end_quiz(my_quiz_brain)

init()
