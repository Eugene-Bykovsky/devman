# Описание кода

## Функция play
```
def play(word): # объявляется функцию play c параметром word (загаданное слово)
    attempt = 6 # инициализируется переменная attempt со значение 6 (количество попыток)
    guess, guess_wrong = [], [] # инициализируются 2 пустых списка(списки угаданных/неугаданных букв
    letters = [] # инициализируется пустой список(список текущего состояния букв)
    for i in word: # проходим по каждой букве в загаданном слове
        i = None if i != ' ' else i # если буква не пробел то в i = None, иначе i == ' '
        letters.append(i) # добавляем i в список letters
    while attempt > 0: # код в теле цикла выполняется пока attempt(попытки) > 0 
        print_game(guess_wrong, word, letters) # функция выводит текущее состояние игры
        if None not in letters: # если в словаре letters нет None выводится сообщение You win!
            print('> You win!') # выводится сообщение You win!
            break # и цикл прерывается
        user_letter = get_letter(attempt, guess) # вызов функции, которая запрашивает у пользователя букву
        if user_letter is not None: # проверка ввода корректной буквы
            for i in range(len(word)): # проходим циклом по каждой  букве в слове
                if user_letter == word[i]: # если такая буква в слове есть
                    letters[i] = user_letter # буква вставляется в соответствующее место в слове
            guess.append(user_letter) # буква вставляется в список guess
            if user_letter not in letters: # если буквы нет списке letters значит она не угалана
                guess_wrong.append(user_letter) # буква вставляется в список  guess_wrong(в список неправильных букв)
                attempt -= 1 # уменьшается количество попыток
    else: # если цикл завершается без break (то есть игрок не угадал слово)
        print_game(guess_wrong, word, letters) # (выводится состояние игры)
        print('> You lose...') # выводится сообщение вы проиграли 
        print(f'> Answer: {word.capitalize()}') # выводится правильное слово с большой буквы
```