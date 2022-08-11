import glob

import cogs.chance_cards_files.chance_cards_config as cc_config


class ChanceCardImages():

    async def list_images_in_directory(self, directory_path, exclude=None):
        print(glob.glob(directory_path))

    async def get_shared_images(self, image_type_path: str = None, gamemaster_moods_exclude: list = None):
        directory_path = cc_config.base_image_path + cc_config.shared_image_directory_name + image_type_path

        images = await self.list_images_in_directory(directory_path, gamemaster_moods_exclude)
        return images

    async def get_gamemaster_images(self, image_type_path: str = None, gamemaster_moods_exclude: list = None):
        print('methode nog niet geimplementeerd')

        directory_path = cc_config.base_image_path + cc_config.shared_image_directory_name + image_type_path

        images = await self.list_images_in_directory(image_type_path, gamemaster_moods_exclude)
        return images

    async def get_images(self, image_type_path: str = None, include_shared=True, include_gamemaster_specific=True,
                         gamemaster_name: str = None, gamemaster_moods_exclude: list = None):
        print('methode nog niet geimplementeerd')

        if include_shared == True:
            # get images from shared directory
            shared_images = await self.get_shared_images(image_type_path, gamemaster_moods_exclude)
