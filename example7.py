import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camelia"]

chosen_word= random.choice(word_list)
print(chosen_word)


game_over=False

corrected_word=[]
lives=6

while not game_over:
    
    guess=input("Guess a letter : ")

    

    display=" "

    for letter in chosen_word:
        if letter==guess:
            corrected_word.append(guess)
            display+=letter
        elif letter in corrected_word:
             display += letter 
        else:
            display+=" _ "

    print(display)

    if "_" not in display:
        game_over=True
        print("you won")

    
    if guess not in chosen_word:
        lives-=1
        print(f"****you have:{lives}/6 lives***********")
        if lives==0:
            game_over=True
            print("you lose")
    else:
        print(f"****you have:{lives}/6 lives***********")

    print(stages[lives])









        

