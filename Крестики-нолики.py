import random

# Подсчет очков
player1_score = 0
player2_score = 0

# Создаем поле для игры
board = [' ' for i in range(9)]

# Приветствие
print('Добро пожаловать в игру "Крестики-Нолики"!')
print("")
print("Правила игры: ")
print("")
print("Игроки по очереди ставят на свободные клетки поля 3x3 свои символы (крестики или нолики).")
print("Цель игры — первым составить ряд из трёх своих символов по горизонтали, вертикали или диагонали.")
print("Если все клетки заполнены, а победителя нет, объявляется ничья.")
print("Кто начнет игру первый - решит жеребьевка. Желаем удачи!")
print("")

# Имена игроков
player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
players = {'X': player1, 'O': player2}

# Игровое поле
def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

# Победные комбинации
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # горизонтальные
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # вертикальные
        [0, 4, 8], [2, 4, 6]              # диагональные
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Функция для одной игры
def play_game():
    global current_player, board
    game_running = True

    while game_running:
        print_board()
        try:
            player_name = players[current_player]
            move = int(input(f"{player_name} ({current_player}), выберите ячейку (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Пожалуйста, выберите число от 1 до 9.")
                continue
            if board[move] == ' ':
                board[move] = current_player
                if check_win(current_player):
                    print_board()
                    print(f"Поздравляем, {player_name}! Вы победили!")
                    game_running = False
                    return current_player  # Возвращаем символ победителя
                elif ' ' not in board:
                    print_board()
                    print("Ничья!")
                    game_running = False
                    return 'Draw'  # Возвращаем 'Draw' в случае ничьей
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Эта ячейка уже занята. Попробуйте снова.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число от 1 до 9.")


# Основная функция программы
def main():
    global current_player, board, player1_score, player2_score, game_count

    while True:
        # Сбрасываем игровое поле
        board = [' ' for _ in range(9)]

        # Жеребьёвка перед началом игры
        print("\nПроводим жеребьёвку, чтобы определить, кто ходит первым...")
        current_player = random.choice(['X', 'O'])
        print(f"По результатам жеребьёвки первым ходит {players[current_player]} ({current_player}).")

        # Запускаем игру
        result = play_game()

        # Обновляем счет в зависимости от результата
        if result == 'X':
            player1_score += 1
        elif result == 'O':
            player2_score += 1

        # Выводим текущий счет
        print(f"{player1} (X): {player1_score}")
        print(f"{player2} (O): {player2_score}")

        # Предлагаем сыграть еще раз
        play_again = input("\nХотите сыграть ещё раз? (да/нет): ").lower()
        if play_again in ['да', 'yes', 'y', 'д']:
           continue  # Начинаем новую игру
        else:
            print("Спасибо за игру!")
            break  # Выходим из цикла и завершаем программу

# Запуск программы
main()