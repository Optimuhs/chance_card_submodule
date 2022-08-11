from cogs.chance_cards_files.bounties.chance_card_bounty import ChanceCardBounty


class CryptoBounty(ChanceCardBounty):

    def __init__(self, bounty_name, bounty_description, is_prize=True, is_penalty=False,
                 bounty_action_type="get crypto",
                 bounty_images=None, remove_after_use=True, multiplier=1, bounty_level=3,
                 token="eth", amount=0.1):
        super().__init__(bounty_name, bounty_description, is_prize, is_penalty, bounty_action_type,
                         bounty_images, remove_after_use, multiplier, bounty_level)
        self.token = token
        self.amount = amount

    async def dispense_bounty(self, player):
        # what should happen when someone wins a crypto bounty

        print("dispense bounty - crypto - method not implemented yet")
        return False
