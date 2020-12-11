import string
from words import choose_word
from images import IMAGES

# End of helper code
# ------------------


def get_hint(secret_word,letters_guessed):
    import random
    letter_not_guessed=[]
    for i in secret_word:
        if i not in letters_guessed:
            if i not in letter_not_guessed:
                letter_not_guessed.append(i)
    return random.choice(letter_not_guessed)


def ifValid(user_input):
    if len(user_input) != 1:
        return False

    if not user_input.isalpha():
        return False

    # True humne tab hi return kiya hai jab
    # user_input ki length 1 hai aur woh character hai
    return True

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    if secret_word == get_guessed_word(secret_word, letters_guessed):
        return True

    return False

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1

    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string
    letters_left = string.ascii_lowercase
    for i in letters_guessed:
        letters_left=letters_left.replace(i,"")

    return letters_left

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Hangman game yeh start karta hai:
    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai
    * Har round mei user se ek letter guess karne ko bolte hai
    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi
    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai
    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print ""


    '''total_live:-hamane max of max jo life user ko deni hai
        choice_chose_img:- list of index for the IMAGES which is we are importing
        frome another file

        Here we are giving the dificulty level to user for make the game intrusting.'''
    total_live=8
    remaining_live=8
    choice_choose_img=[0,1,2,3,4,5,6,7]

    print "App game ko kis level par khelna chahte hai?\n(a)\n(b)\n(c)"
    level=raw_input("Enter your choice for level(a,b or c) ")
    if level=="b":
        total_live=remaining_live=6
        choice_choose_img=[1,2,3,4,6,7]
    elif level=="c":
        total_live=remaining_live=4
        choice_choose_img=[1,3,5,7]
    else:
        if level != "a":
            print "Apne wrong level choose kiya hai.\nGame basic level se start ho raha hai__"
    letters_guessed = []

    hints=2

    while(remaining_live>0):
        available_letters = get_available_letters(letters_guessed)
        print "Available letters: " + available_letters

        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()

        if not ifValid(letter) and letter != "hint":
            print "invalid input"
            continue
        if letter == 'hint' and hints>0:
            print "Your hint for next word is "+get_hint(secret_word,letters_guessed)
            hints-=1
            continue
        elif letter == 'hint' and hints==0:
            print "you already used your all hints for this word"
            continue
        if letter in secret_word:
            letters_guessed.append(letter)
            print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
            print ""

            if is_word_guessed(secret_word, letters_guessed):
                print " * * Congratulations, you won! * * "
                print ""
                break

        else:
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            letters_guessed.append(letter)
            print ""
            print IMAGES[choice_choose_img[total_live-remaining_live]]
            remaining_live-=1
        print "sorry you lose the game, the word was - "+secret_word
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
