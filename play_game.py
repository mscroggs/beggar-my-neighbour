import beggar

game = beggar.new_hands()

print(game)

while len(game[2]) > 0 and len(game[3]) > 0:
    player, cards = beggar.make_move(game)
    print(len(game[2]), len(game[3]), beggar.describe(player, cards))
