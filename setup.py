import beggar
import toot

game = beggar.new_hands()
beggar.save_cards("beggar.game", game)

toot.toot("Player 1 and player 2 are each dealt 26 cards.")

