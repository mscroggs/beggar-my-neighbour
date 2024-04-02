import beggar
import toot

game = beggar.new_hands()
beggar.save_cards("beggar.game", game)

toot.toot(f"{beggar.pemoji(0)} and {beggar.pemoji(1)} are each dealt 26 cards.")

