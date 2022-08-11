import cogs.chance_cards_files.chance_cards_config as cc_config
from cogs.chance_cards_files.games.chance_card_game import ChanceCardGame


class CoinFlipGame(ChanceCardGame):

    def __init__(self, name=cc_config.coinflip_name, description=cc_config.coinflip_description,
                 image_directory="coin_flip_game/"):
        print("coinflipgame")
        super().__init__(name, description, image_directory)
