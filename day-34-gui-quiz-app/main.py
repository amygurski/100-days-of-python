from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizIterface

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()

question_bank = []
for result in response.json()["results"]:
    question_text = result["question"]
    question_answer = result["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizIterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
