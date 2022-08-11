from cogs.chance_cards_files.bounties.chance_card_bounty import ChanceCardBounty


class Mee6SauceBounty(ChanceCardBounty):

    def __init__(self, bounty_name, bounty_description, is_prize, is_penalty,
                 bounty_action_type="get or lose discord sauce",
                 bounty_images=None, remove_after_use=True, multiplier=1, bounty_level=2,
                 amount=69):
        super().__init__(bounty_name, bounty_description, is_prize, is_penalty, bounty_action_type,
                         bounty_images, remove_after_use, multiplier, bounty_level)
        self.amount = amount

    async def dispense_bounty(self, player):
        # what should happen when someone wins discord sauce
        # the bot can not use mee6's commands so cannot give sauce to the player
        # the gamemaster has to do it manually, he will get a private message with the exact command to copy paste

        print("dispense bounty - mee6 sauce - method not implemented yet")
        return False
