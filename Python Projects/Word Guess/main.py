import random

word_lists = {
    4: ['abba', 'cafe', 'deaf', 'idea', 'jazz', 'kite', 'lens', 'moon', 'navy', 'opal', 'park', 'quiz', 'rock', 'song', 'tape', 'user', 'vibe', 'wave', 'zone'],
    5: ['apple', 'beach', 'chess', 'dream', 'emily', 'flute', 'grape', 'happy', 'igloo', 'jumpy', 'karma', 'lemon', 'music', 'novel', 'oasis', 'peach', 'queen', 'radio', 'sunny'],
    6: ['banana', 'coffee', 'dragon', 'flower', 'guitar', 'honest', 'island', 'jungle', 'knight', 'lemon', 'marble', 'number', 'orange', 'pencil', 'rocket', 'silver', 'turtle', 'unique', 'violet']
}

def generate_word(length: int) -> str:
    words = word_lists[length]
    return random.choice(words)

def count_common_letters(secret_word: str, guess: str) -> int:
    common_letters = 0
    for i in range(len(secret_word)):
        if secret_word[i] in guess:
            common_letters += 1
    return common_letters

def has_repeated_letters(word) -> bool:
    return len(word) != len(set(word))

def play_game():
    length = int(input("Enter the length of the word (4, 5, or 6): "))
    if length not in word_lists:
        print("Invalid word length!")
        return
    
    secret_word = input("choose word: ")
    if has_repeated_letters(secret_word):
        print("Repeated letters used!")
        return
    computer_word = generate_word(length)
    if has_repeated_letters(computer_word):
        print("Repeated letters used!")
        return
    
    attempts = 0
    while True:
        attempts += 1
        print(f"Attempt {attempts}:")
        
        # Human's turn
        human_guess = input(f"Your guess ({length}-letter word): ")
        if len(human_guess) != length:
 print(f"Invalid guess! Please enter a {length}-letter word.")
            continue
        
        human_common_letters = count_common_letters(computer_word, human_guess)
        print(f"Your guess: common letters:", human_common_letters)
        if human_guess == computer_word:
            print(f"Congratulations! You guessed the computer's word in {attempts} attempts.")
            break
        
        
        computer_guess = generate_word(length)
        computer_common_letters = count_common_letters(secret_word, computer_guess)
        print(f"Computer's guess: {computer_guess}, common letters:", computer_common_letters)
        if computer_guess == secret_word:
            print(f"The computer guessed your word in {attempts} attempts. You lose!")
            break
play_game()
