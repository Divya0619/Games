import random
COLOURS=["R","G","B","W","Y","P"]
TRIES=10
CODE_LEN=4


def generate_code():
    code=[]
    for i in range(CODE_LEN):
        color=random.choice(COLOURS)
        code.append(color)
    #print(code)
    return code

def guess_code():
    while True:
        guess=input("Guess the colors separated by commas: ").upper().split(",")

        if len(guess)!=CODE_LEN:
            print(f"You must guess {CODE_LEN} colors!")
            continue
        for color in guess:
            if color not in COLOURS:
                print(f"Invalid color: {color}. Guess again")
                break
        else:
            break

    return guess

def check_code(guess,actual_code):
    color_counts={}
    correct_pos=0
    incorrect_pos=0

    for color in actual_code:
        if color not in color_counts:
            color_counts[color]=0
        color_counts[color]+=1
    
    for guess_color, actual_color in zip(guess,actual_code):
        if guess_color==actual_color:
            correct_pos+=1
            color_counts[guess_color]-=1

    for guess_color, actual_color in zip(guess,actual_code):
        if guess_color!=actual_color and guess_color in color_counts and color_counts[guess_color]>0:
            incorrect_pos+=1
            color_counts[guess_color]-=1
    return correct_pos,incorrect_pos

def game():
    print("The valid colors are",*COLOURS)
    code=generate_code()
    for i in range(1,TRIES+1):
        guess=guess_code()
        correct_pos,incorrect_pos=check_code(guess,code)
        if correct_pos==CODE_LEN:
            print(f"You guessed it in {i} tries!!")
            break

        print(f"Correct positions: {correct_pos} ; Incorrect positions: {incorrect_pos}")
    else:
        print(f"You failed to guess, the code was:",*code)

if __name__=="__main__":
    game()