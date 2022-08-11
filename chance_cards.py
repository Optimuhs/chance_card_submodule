import disnake
from disnake.ext import commands

import cogs.chance_cards_files.chance_cards_config as cc_config
from cogs.chance_cards_files.chance_cards_helpers import ChanceCardEmbedGenerator
from cogs.chance_cards_files.db_chance_cards import DbChanceCards
from cogs.chance_cards_files.games.chance_card_game import ChanceCardGame


class ChanceCardsBot(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # ******************************************************************************************************************
    # ************************************   HELP FUNCTIONS   **********************************************************
    # ******************************************************************************************************************

    async def remove_role(self, player):
        print(" method not implemented yet")
        return False

    async def choose_game(self, blacklist=[]):
        print(" method not implemented yet")
        return False

    async def choose_prize(self):
        print(" method not implemented yet")
        return False

    async def choose_penalty(self):
        print(" method not implemented yet")
        return False

    # ******************************************************************************************************************
    # ************************************   SLASH COMMANDS   **********************************************************
    # ******************************************************************************************************************

    # open chance card for specific user
    @commands.slash_command(
        name=cc_config.chance_card_command_name,
        description=cc_config.chance_card_command_description
    )
    async def open(self,
                   inter: disnake.ApplicationCommandInteraction,
                   player: disnake.User
                   ):
        print(player)

        # post start image
        await ChanceCardEmbedGenerator.send_start_image(inter, inter.user, player)

        # remove role
        await self.remove_role()

        # post thinking image
        await ChanceCardEmbedGenerator.send_thinking_image(inter, inter.user, player)

        # choose random game
        game: ChanceCardGame = await self.choose_game(inter, inter.user, player)

        # post game image
        await game.send_game_selected_image(inter, inter.user, player)

        # PLAY GAME - specific game flow to determine win or lose
        winner = await game.play(inter, inter.user, player)

        # DETERMIN PRICE OR PENALTY
        if winner:
            reward = await self.choose_prize()

        else:
            reward = await self.choose_penalty()

        # 4.1 post selecting price/penalty image

        # 4.2a select random price for winner

        # 4.2b select random penalty for loser

        # 4.3 post prize/penalty image

        # 4.4a automatically add/remove price/penalty in case of Role

    # ******************************************************************************************************************
    # ************************************   USER  COMMANDS   **********************************************************
    # ******************************************************************************************************************

    # ******************************************************************************************************************
    # ************************************   MESSAGE  COMMANDS   **********************************************************
    # ******************************************************************************************************************


def setup(bot: commands.Bot):
    #                   MAKE SURE DB TABLES ARE CREATED
    try:
        db = DbChanceCards()
        db.create_tables()
    except Exception as e:
        print(e)

    bot.add_cog(ChanceCardsBot(bot))
