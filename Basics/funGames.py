import random
import string
from wordlist import words

# if __name__==__main__:
# dunder argument
#script1 and script2

#hangman
hangman_art={0: ("   ",
                     "   ",
                     "   "),
                 1: (" o ",
                     "   ",
                     "   "),
                 2: (" o ",
                     " | ",
                     "   "),
                 3: (" o ",
                     "/| ",
                     "   "),
                 4: (" o ",
                     "/|\\",
                     "   "),
                 5: (" o ",
                     "/|\\",
                     "/  "),
                 6: (" o ",
                     "/|\\",
                     "/ \\"),
                 }
def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))

#Python Banking program
def show_balance(balance):
    print(f"Your balance is ₹{balance:.2f}")
def deposit():
    amount=float(input("Enter a amount: "))
    if amount<0:
        print("That's not a valid amount")
        return 0
    else:
        return amount
def withdraw(balance):
    amount = float(input("Enter a amount: "))
    if amount>balance:
        print("Insufficient funds")
        return 0
    elif amount<0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

#slot machine
def spin_row():
    symbols=["🍋", "🍒", "🍑" ,"🔔" ,"💰"]
    # results=[]
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results
    return [random.choice(symbols)for symbol in range(3)]
def print_row(row):
    print(" | ".join(row))
def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        match row[0]:
            case "🍋":return bet*2
            case "🍑":return bet*3
            case "🍒":return bet*5
            case "🔔":return bet*7
            case "💰":return bet*10
            case _:return 0
    return 0


def main():
    #Bank account
    balance = 0
    is_running = True
    while is_running:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        choice = input("Enter your choice(1-4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That's not a valid option")
    print()

    #slot machine
    print("Welcome to Python Slots")
    print("Symbols:🍋 🍒 🍑 🔔 💰")
    while balance>0:
        print(f"Your current Balance: ₹{balance}")
        bet=input("Place your bet: ")
        if not bet.isdigit():
            print("Enter a valid number")
            continue
        bet=int(bet)
        if bet > balance:
            print("Insufficient funds")
            continue
        elif bet < 0:
            print("Bet must be greater than 0")
            continue
        else:
            balance-=bet
        row=spin_row()
        print("Spinning...")
        print_row(row)
        payout=get_payout(row,bet)
        if payout>0:
            print(f"You won ₹{payout}")
        else:
            print("Sorry you lost")
        balance+=payout
        play_again=input("Do you want to play again? (y/n): ")
        if play_again.lower()!='y':
            break
    print(f"Your final balance is: {balance}")

    #msg encryption
    chars=" "+string.punctuation+string.digits+string.ascii_letters
    chars=list(chars)
    key=chars.copy()
    random.shuffle(key)
    # print(f"Chars: {chars}")
    # print(f"Keys: {key}")

    #ENCRYPT
    plain_text=input("Enter a message to encrypt: ")
    cipher_text=""
    for letter in plain_text:
        index=chars.index(letter)
        cipher_text+=key[index]
    print(f"Original text: {plain_text}")
    print(f"Encrypted text: {cipher_text}")

    #DECRYPT
    cipher_text=input("Enter a message to decrypt: ")
    plain_text=""
    for letter in cipher_text:
        index=key.index(letter)
        plain_text+=chars[index]
    print(f"Encrypted text: {cipher_text}")
    print(f"Original text: {plain_text}")

    #Hangman game
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_guesses=0
    guessed_letters=set()
    is_running=True
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess=input("Enter a letter: ").lower()
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid Input")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue
        guessed_letters.add((guess))
        if guess in answer:
            print("Correct")
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
        else:
            print("Wrong")
            wrong_guesses+=1
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            is_running=False
        elif wrong_guesses>=len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOST")
            is_running = False



if __name__=='__main__':
    main()
