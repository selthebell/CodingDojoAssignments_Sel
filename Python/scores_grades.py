import random
#random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...
def scores_grades():
    print "Scores and Grades"
    for index in range(10):
        random_num = random.randint(60,100)
        score=random_num
        #Score: 60 - 69; Grade - D Score: 70 - 79; Grade - C Score: 80 - 89; Grade - B Score: 90 - 100; Grade - A
        if score >= 90:
            print "Score is ",score,"Your Grade is A"
        elif score >= 80 and score <= 89:
            print "Score is ",score,"Your Grade is B"
        elif score >= 70 and score <= 79:
            print "Score is ",score,"Your Grade is C"
        elif score >= 60 and score <= 69:
            print "Score is ",score,"Your Grade is D"
        else:
            print "You Failed"
scores_grades()
