from cogs.chance_cards_files.bounties.chance_card_bounty import ChanceCardBounty


class Mee6ItemBounty(ChanceCardBounty):

    def __init__(self, bounty_name, bounty_description, is_prize, is_penalty,
                 bounty_action_type="get or lose mee6 items, nugbucks or Nergberks",
                 bounty_images=None, remove_after_use=True, multiplier=1, bounty_level=2,
                 amount=1, item_id=None):
        super().__init__(bounty_name, bounty_description, is_prize, is_penalty, bounty_action_type,
                         bounty_images, remove_after_use, multiplier, bounty_level)
        self.item_id = item_id
        self.amount = amount

    async def dispense_bounty(self, player):
        # what should happen when someone wins an item
        # the bot can not use mee6's commands so cannot give the item to the player
        # the gamemaster has to do it manually, he will get a private message with the exact command to copy paste
        # what to do if player can't receive the item or doesn't have (enough of) it to be taken away

        print("dispense bounty - mee6 item - method not implemented yet")
        return False
