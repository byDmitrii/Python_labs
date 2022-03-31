
chess_board = [[0 for i in range(8)] for j in range(8)]
solutions = 0

# устанавливаем ферзя в клетку ij
def set_queen(i,j):
    for x in range(8):
        # горизонталь
        chess_board[x][j] += 1
        # вертикаль
        chess_board[i][x] += 1
        # для заполнения диагоналей, сначала проверяем существует ли клетка с таким индексом
        if 0 <= i+j-x < 8:
            chess_board[i+j-x][x] += 1
        if 0 <= i-j+x <8:
            chess_board[i-j+x][x] += 1
    # -1 - обозначение ферзя в клетке
    chess_board[i][j] = -1

def delete_quenn(i,j):
    for x in range(8):
        # освобождаем горизонталь
        chess_board[x][j] -= 1
        # освобождаем вертикаль
        chess_board[i][x] -= 1
        # освобождаем диагонали
        if 0 <= i+j-x < 8:
            chess_board[i+j-x][x] -= 1
        if 0 <= i-j+x <8:
            chess_board[i-j+x][x] -= 1
    # убираем ферзя
    chess_board[i][j] = 0

# функция для эстетичного вывода
def output_answers():
    global solutions
    solutions += 1
    temp_alphabet = 'abcdefgh'
    answer = []
    for i in range(8):
        for j in range(8):
            if chess_board[i][j] == -1:
                answer.append(temp_alphabet[j]+str(i+1))
    print('  '.join(answer))

# рекурсивная функция, находит решения i-ой строки
def solve(i):
    # ищем пустую клетку в строке
    for j in range(8):
        if chess_board[i][j] == 0:
            # если нашли ставим туда ферзя
            set_queen(i,j)
            # если мы находимся в последней строке - выводим ответ, иначе пожнимаеся на строку выше
            if i == 7:
                output_answers()
            else:
                solve(i+1)
            delete_quenn(i,j)

solve(0)
print("Всего решений = " + str(solutions))