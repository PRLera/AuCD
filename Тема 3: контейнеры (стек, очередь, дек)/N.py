from collections import deque

player1 = deque(map(int, input().split()))
player2 = deque(map(int, input().split()))

moves = 0

while player1 and player2 and moves < 10 ** 6:
    card1 = player1.popleft()
    card2 = player2.popleft()
    moves += 1

    # Определяем победителя
    # 0 побеждает 9, иначе большая карта побеждает
    if card1 == 0 and card2 == 9:
        winner = 1
    elif card2 == 0 and card1 == 9:
        winner = 2
    elif card1 > card2:
        winner = 1
    else:
        winner = 2

    # Победитель забирает карты (сначала первого, потом второго)
    if winner == 1:
        player1.append(card1)
        player1.append(card2)
    else:
        player2.append(card1)
        player2.append(card2)

# Вывод результата
if not player1:
    print('second', moves)
elif not player2:
    print('first', moves)
else:
    print('botva')