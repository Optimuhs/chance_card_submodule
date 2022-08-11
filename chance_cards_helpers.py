import random

import disnake
from PIL import Image

import cogs.chance_cards_files.chance_cards_config as cc_config


class ChanceCardEmbedGenerator:

    @staticmethod
    async def create_start_image(master, player):
        ready_template = Image.open("cogs/chance_cards_files/images/templates/ready.jpg")
        ready = ready_template.copy()
        print(ready.size)

        player_name = str(player.id)
        player_file = "cogs/chance_cards_files/images/created/" + player_name + ".jpg"
        await player.display_avatar.save(player_file)
        player_img = Image.open(player_file)
        player_img = player_img.resize((220, 220))
        print(player_img.size)

        master_name = str(master.id)
        master_file = "cogs/chance_cards_files/images/created/" + master_name + ".jpg"
        await master.display_avatar.save(master_file)
        master_img = Image.open(master_file)
        master_img = master_img.resize((220, 220))
        print(master_img.size)

        ready.paste(master_img, (100, 220))
        ready.paste(player_img, (640, 220))
        ready_image = "cogs/chance_cards_files/images/created/" + master_name + player_name + ".jpg"
        ready.save(ready_image)

        return disnake.File(ready_image, filename="ready.jpg")

    @staticmethod
    async def send_start_image(inter, gamemaster, player):
        print(gamemaster)
        print(player)

        emb = disnake.Embed(title="WANNA PLAY " + player.display_name + "?")
        emb.set_author(name=gamemaster.display_name, icon_url=gamemaster.display_avatar)
        f = await ChanceCardEmbedGenerator.create_start_image(gamemaster, player)
        emb.set_image(url="attachment://ready.jpg")
        await inter.channel.send(player.mention, file=f, embed=emb)

    @staticmethod
    async def send_thinking_image(inter, gamemaster, player):
        gif = random.choice(cc_config.thinking_gifs)
        thinking_gif = disnake.File(gif, filename="thinking.gif")
        await inter.channel.send(player.mention, file=thinking_gif)
