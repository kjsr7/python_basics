#!/usr/bin/python

class que:
    def __init__(self, question, ans):
        self.question  = question
        self.ans = ans

questions = [ "what is the color of apple \na)red \nb) green\nc)yellow\n",
                "what is the highest award in CS \na)Nobel prize \nb)Turing Award\nc)Bharat Ratna\n",
                "Which is the largest desert \na)thar \nb)sahara \nc)Mysore\n"]


queobjects = [que(questions[0],"a") , que(questions[1],"b"), que(questions[2],"c")];

def run_test(queobjects):
    score = 0;
    for q in queobjects:
        ans = input(q.question)
        if ans == q.ans:
            score+=1

    print("you got " + str(score) + "/" + str(3) + " correct")

run_test(queobjects)


