from abc import ABC, abstractmethod

from cogs.chance_cards_files.db_chance_cards import DbChanceCards


class ChanceCardBounty(ABC):
    def __init__(self, bounty_name, bounty_description, is_prize, is_penalty, bounty_action_type, bounty_images=None,
                 remove_after_use=True, multiplier=1, bounty_level=2):
        self.is_prize = is_prize  # given to someone who wins
        self.is_penalty = is_penalty  # given to someone who loses
        self.bounty_name = bounty_name
        self.bounty_description = bounty_description
        self.bounty_action_type = bounty_action_type  # add role, remove role, custom action, gamemaster manual
        self.bounty_images = bounty_images  # array of paths to images to use for this bounty
        self.remove_after_use = remove_after_use  # true for a one-time bounty that is removed from the list after it is picked. false for bountys that stay in the list untill removed
        self.multiplier = multiplier  # nr of times this bounty is added to the random pick-list
        self.bounty_id = self.create_id()  # auto-generate unique id
        self.bounty_level = bounty_level  # 0 = very undesirable, 1 = undesirable,  2 = average, 3 = desirable, 4 = very desirable

    def create_id(self):
        print("create_id - method not implemented yet")
        return False

    async def create_bounty(self):
        print(" method not implemented yet")

        db = DbChanceCards()
        return await db.create_new_bounty(self)

    async def remove_bounty(self):
        print(" method not implemented yet")
        db = DbChanceCards()
        return await db.remove_bounty(self)

    async def update_bounty(self):
        print(" method not implemented yet")
        db = DbChanceCards()
        return await db.update_bounty(self)

    async def add_bounty_image(self, image):
        print(" method not implemented yet")
        return False

    async def remove_bounty_image(self, image):
        print(" method not implemented yet")
        return False

    async def return_bounty_images_overview(self):
        print(" method not implemented yet")
        return False

    async def get_random_bounty_image(self, gamemaster, player):
        print(" method not implemented yet")
        return False

    @staticmethod
    async def get_rewards_picklist():
        print(" method not implemented yet")
        return False

    @staticmethod
    async def pick_random_reward(blacklist=None, exclude_levels=None, force_levels=None):
        print(" method not implemented yet")
        return False

    @staticmethod
    async def get_penalty_picklist():
        print(" method not implemented yet")
        return False

    @staticmethod
    async def pick_random_penalty(blacklist=None, exclude_levels=None, force_levels=None):
        print(" method not implemented yet")
        return False

    @abstractmethod
    async def dispense_bounty(self, player):
        print(" method not implemented yet")
        return False

    async def return_bounty_details_image(self):
        print(" method not implemented yet")
        return False

    @staticmethod
    async def create_all_bounties_overview_image():
        print(" method not implemented yet")
        return False

    @staticmethod
    async def create_bounty_statistics_image(timespan="all"):
        print(" method not implemented yet")
        return False

    @staticmethod
    async def get_bounty_log(timespan="all", type="all"):
        print(" method not implemented yet")
        return False

    async def log_bounty_event(self, type, gamemaster=None, player=None, admin=None, message=""):
        print(" method not implemented yet")
        return False
