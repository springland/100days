
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
class QuizGame:

    def __init__(self):
        questions_list = [ Question(x["text"] , x["answer"]) for x in question_data]
        self.questionBank = QuizBrain(questions_list)

    def run(self):
        while(self.questionBank.still_has_questions()):
            question = self.questionBank.nextQuestion()
            ans = input(f"{question.text} (True/False)")
            if ans.lower() == question.getAnswer().lower():
                print("Correct")
            else:
                print("Incorrect")



game = QuizGame()
game.run()


