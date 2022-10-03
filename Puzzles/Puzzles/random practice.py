import os
from random import randint

def main(number_of_questions:int) -> str:
    """
    Randomly select n puzzles from all the previously completed puzzles to practice
    """
    problems = os.listdir(".")
    problems.remove("random practice.py")
    
    output = []    
    for _ in range(number_of_questions):
        if not len(problems): break # we've run out of puzzles so break out of the loop

        idx = randint(0,len(problems)-1)
        output.append(problems[idx]) # select a random puzzle
        problems.pop(idx) # remove that puzzle from problems list so we dont get it again

    return '\n'.join(output)

if __name__ == "__main__":
    print(main(3))