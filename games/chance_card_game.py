from abc import ABC, abstractmethod

import cogs.chance_cards_files.chance_cards_config as cc_config


class ChanceCardGame(ABC):

    def __init__(self, game_name=None, game_description=None,
                 image_directory: str = cc_config.shared_image_directory_name):
        self.game_name = game_name
        self.game_description = game_description
        self.image_directory = image_directory

    async def get_game_image_directory_path(self, gamemaster: str = cc_config.shared_image_directory_name):
        path = cc_config.base_image_path + \
               gamemaster + \
               cc_config.game_image_dir + \
               self.image_directory

    async def get_images(self, image_type: str = None, include_shared=True, include_gamemaster_specific=True,
                         gamemaster_name: str = None, gamemaster_moods_exclude: list = None):
        print(" method not implemented yet")
        return False

    @abstractmethod
    async def play(self, inter, gamemaster, player):
        # todo
        print(" method not implemented yet")
        return False

    @abstractmethod
    async def send_game_selected_image(self, inter, gamemaster, player):
        # todo
        print(" method not implemented yet")
        return False

    @abstractmethod
    async def send_game_rules_image(self, inter, gamemaster, player):
        # todo
        print(" method not implemented yet")
        return False

    @abstractmethod
    async def send_game_result_image(self, inter, gamemaster, player):
        # todo
        print(" method not implemented yet")
        return False

    @abstractmethod
    async def send_you_lose_image(self, inter, gamemaster, player):
        # todo
        print(" method not implemented yet")
        return False

    @abstractmethod
    async def send_you_win_image(self, inter, gamemaster, player):
        # todo
        print(" method not implemented yet")
        return False
