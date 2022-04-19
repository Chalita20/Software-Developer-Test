import string
import random

def randomLetter():
    letter = []
    for i in range(4):
        letter.append(random.choice(string.ascii_letters))
    return letter
def check_guess(answer, random_answer):
    n=0
    for ra in random_answer:
        if ra in answer:
            n+=1
    return n

def check_position(answer,random_answer):
    n=[]
    for i in range(4):
        if answer[i] == random_answer[i]:
            n.append(i)
    return n
answer = randomLetter()
number = 1
kn={}

while True:

    random_s = randomLetter()
    #check_guess
    n_guess = check_guess(answer,random_s)
    #check_position
    n_position = check_position(answer,random_s)

    kn[number] = {'answer':answer, 'randomLetter':random_s, 'n_guess':n_guess, 'n_position':n_position}

    number+=1

    if n_position == 4:
        break
