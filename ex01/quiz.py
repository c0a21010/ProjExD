import datetime
import random

class Quiz:
    def __init__(self) -> None:
        self.problems = {
            "サザエの旦那の名前は?":["マスオ","ますお"],
            "カツオの妹の名前は?":["ワカメ","わかめ"],
            "タラオはカツオから見てどんな関係":["甥","おい","甥っ子","おいっこ"]
        }

        self.correct = "正解!"
        self.incorrect = "出直してこい"

    def startquiz(self):

        problem_list = list(self.problems.keys())

        random_problem = random.choice(problem_list)

        print("問題:")
        print(random_problem)

        stime = datetime.datetime.now()
        etime = datetime.datetime.now()

        while True:

            ans = input("答えるんだ:")
            if ans in self.problems[random_problem]:
                print(self.correct)
                etime = datetime.datetime.now()
                break
            else:
                print(self.incorrect)

        print(etime-stime)

def main():
    quiz = Quiz()
    quiz.startquiz()
        
if __name__ == "__main__":
    main()