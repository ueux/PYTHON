ques=("How many elements are in the periodic table?: ",
      "Which animal lays the largest eggs?: ",
      "How many bones are in the human body?: ")
options=(("A. 116","B. 117","C. 118","D. 119"),
         ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
         ("A. 206","B. 207","C. 208","D. 209"))
ans=("C","D","A")
guesses=[]
score=0
ques_no=0
for que in ques:
    print("------------------------")
    print(que)
    for option in options[ques_no]:
        print(option)
    guess=input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess==ans[ques_no]:
        score+=1
        print("Correct")
    else:
        print("Incorrect")
        print(f"{ans[ques_no]} is the correct answer")
    ques_no+=1
print("-------------------")
print("      RESULTS      ")
print("-------------------")
print("Answers: ",end="")
for an in ans:
    print(an,end=" ")
print()
print("Guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()
score=int(score/len(ques)*100)
print(f"Your score is : {score}%")