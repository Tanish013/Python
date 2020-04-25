import random
import json
def hangman():
    list_of_words = json.load(open("word.json"))
    word = random.choice(list_of_words)
    turns = 10
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    guessmade = ''
    while turns > 0 or guessmade != word:
        main = ''
        #print(f"Hint: {words[word]}")
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main +"_ "
            if main == word:
                print(f"You Win.The word is {word}")
                return ""
        #print(f"{main} {guessmade}")
        print(f"Guess the word {main}")
        ip = input()
        ip = ip.lower()
        if ip in validletters:
            guessmade = guessmade + ip
        else:
            print("Enter a valid character")
            ip = input()
        if ip not in word:
            turns = turns -1
            if turns == 9:
                print('9 turns left')
                print('-----------')
            elif turns == 8:
                print('8 turns left')
                print('-----------')
                print('     0     ')
            elif turns == 7:
                print('7 turns left')
                print('-----------')
                print('     0     ')
                print('     |     ')
            elif turns == 6:
                print('6 turns left')
                print('-----------')
                print('     0     ')
                print('     |     ')
                print('    /      ')
            elif turns == 5:
                print('5 turns left')
                print('-----------')
                print('     0     ')
                print('     |     ')
                print('    / \    ')
            elif turns == 4:
                print('4 turns left')
                print('-----------')
                print('   \ 0     ')
                print('     |     ')
                print('    / \    ')
            elif turns == 3:
                print('3 turns left')
                print('-----------')
                print('   \ 0 /   ')
                print('     |     ')
                print('    / \    ')
            elif turns == 2:
                print('2 turns left')
                print('-----------')
                print('   \ 0 /|  ')
                print('     |     ')
                print('    / \    ')
            elif turns == 1:
                print('1 turns left')
                print("It's the last breath. Come on you can do it")
                print('-----------')
                print('   \ 0 _|  ')
                print('     | \   ')
                print('    / \    ')
            else:
                print("All turns are over . You Lose. You let a kind man die.")
                print(f"The word was {word}")
                print('-----------')
                print('     0_|   ')
                print('    /|\    ')
                print('    / \    ')
                break
    

print("Welcome to Hangman\nPlease enter your name ")
name = input()
print("Welcome ", name )
print("-------------------")
print("try to guess the word in less than 10 attempts")
while(1):
    hangman()
    re = input("press r to replay ")
    if re == "r":
        continue
    break