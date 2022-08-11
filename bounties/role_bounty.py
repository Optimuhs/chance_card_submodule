from cogs.chance_cards_files.bounties.chance_card_bounty import ChanceCardBounty


class RoleBounty(ChanceCardBounty):

    def __init__(self, bounty_name, bounty_description, is_prize, is_penalty,
                 bounty_action_type="get or lose role",
                 bounty_images=None, remove_after_use=True, multiplier=1, bounty_level=2,
                 role_id=None, alternative_role=None, alternative_item=None, reroll=False, alternative=0):
        super().__init__(bounty_name, bounty_description, is_prize, is_penalty, bounty_action_type,
                         bounty_images, remove_after_use, multiplier, bounty_level)
        self.role_id = role_id
        self.alternative_role = alternative_role
        self.alternative_item = alternative_item
        self.reroll = reroll
        self.alternative = alternative

    async def dispense_bounty(self, player):
        # bot gives or removes role to/from player
        # what should happen when the user already has the role so can't get it a second time
        # --> if reroll = true --> pick another random bounty
        # --> if alternative_item  & alternative = 1  --> give an item instead (that can be used to get the role at a later time)
        # --> if alternative_role & alternative = 1 --> give alternative role instead
        # --> if alternative_item  & alternative = -1 --> remove alternative item instead
        # --> if alternative_role  & alternative = -1 --> remove alternative role instead
        # what should happen when the user doesn't have the role so it can't be taken away
        # --> if reroll = true --> pick another random bounty
        # --> if alternative_item  & alternative = 1 --> give alternative item instead
        # --> if alternative_role  & alternative = 1 --> give alternative role instead
        # --> if alternative_item  & alternative = -1 --> remove alternative item instead
        # --> if alternative_role  & alternative = -1 --> remove alternative role instead

        print("dispense bounty - role - method not implemented yet")
        return False
