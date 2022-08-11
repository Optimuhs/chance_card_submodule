from db.db_connection import DbConnection


class DbChanceCards(DbConnection):

    # ******************************************************************************************************************
    # *****************************************   DB TABLES   **********************************************************
    # ******************************************************************************************************************

    def create_tables(self):
        #   BOUNTY_LOG

        bounty_log = """CREATE TABLE IF NOT EXISTS bounty_log
                                   (id INTEGER PRIMARY KEY,
                                   timestamp VARCHAR(255) NOT NULL,
                                   gamemaster_id VARCHAR(255),
                                   player_id VARCHAR(255),
                                   admin_id VARCHAR(255),
                                   event_type VARCHAR(255) NOT NULL,
                                   amount INTEGER, 
                                   item  VARCHAR(255),
                                   message VARCHAR(255) )
                                   """
        self.create_tables_q.append(bounty_log)

        bounties = """CREATE TABLE IF NOT EXISTS bounties
                                    (id INTEGER PRIMARY KEY,
                                    guild_id INTEGER NOT NULL, 
                                    bounty_name VARCHAR(255) NOT NULL, 
                                    bounty_description  VARCHAR(255),  
                                    is_prize INTEGER NOT NULL, 
                                    is_penalty INTEGER NOT NULL, 
                                    bounty_action_type VARCHAR(255) NOT NULL, 
                                    bounty_images  VARCHAR(255), 
                                    remove_after_use   INTEGER NOT NULL, 
                                    multiplier INTEGER NOT NULL,
                                    bounty_level  INTEGER NOT NULL,
                                    token   VARCHAR(255), 
                                    amount  INTEGER NOT NULL,
                                    item_id  VARCHAR(255), 
                                    role_id  VARCHAR(255), 
                                    alternative_role   VARCHAR(255), 
                                    alternative_item   VARCHAR(255), 
                                    reroll INTEGER,
                                    alternative INTEGER                                   
                                    )
                                    """
        self.create_tables_q.append(bounties)

        try:

            for t in self.create_tables_q:
                self.db.execute(t)
                print("CREATED CHANCE CARDS TABLES")
        except Error as e:
            print(e)
            print("ERROR CREATING CHANCE CARDS TABLES")

    # ******************************************************************************************************************
    # *****************************************   GETTERS & SETTERS   **************************************************
    # ******************************************************************************************************************

    async def create_new_bounty(self, bounty):
        print(" method not implemented yet")
        return False

    async def remove_bounty(self, bounty):
        print(" method not implemented yet")
        return False

    async def update_bounty(self, bounty):
        print(" method not implemented yet")
        return False
