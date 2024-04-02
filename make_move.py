import beggar
import toot

game = beggar.load_cards("beggar.game")
player, cards = beggar.make_move(game)
beggar.save_cards("beggar.game", game)

toot.toot(beggar.as_toot(player, cards))
