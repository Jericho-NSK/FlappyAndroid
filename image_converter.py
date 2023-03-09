"""
Converter for RGBA .png files with resizing to pygame.Surface, PIL.Image or bytecode.
Anywhere use PIL for resizing.
Quality is much better than standard resizing by pygame.transform.
Useful for pet projects with graphics.
Originals .png files must be in 'images/originals' folder
Could create new RGBA .png file in 'images' folder.
"""

import os
from io import BytesIO

import PIL.Image
import pygame


def convert(filename: str,
            width: int | float | None = None,
            height: int | float | None = None,
            square: bool = True,
            new_file: bool = True,
            for_pygame: bool = True,
            ) -> pygame.Surface | PIL.Image.Image | bytes:
    """
    Convert to the image with new size to bytecode WITH OR WITHOUT creating a new file
    """

    image = PIL.Image.open(os.path.join(os.getcwd(), 'images', 'originals', f'original_{filename}.png'), mode='r')

    if square and (width and not height):
        height = width
    elif square and (height and not width):
        width = height
    elif width and not height:
        height = width * image.size[1] / image.size[0]
    elif height and not width:
        width = height * image.size[0] / image.size[1]
    elif not width and not height:
        width = image.size[0]
        height = image.size[1]

    image = image.resize(
        (
            int(width),
            int(height)
        )
    )

    bytes_image = BytesIO()
    image.save(bytes_image, format='PNG')
    bytes_image = bytes_image.getvalue()

    if new_file:
        with open(os.path.join(os.getcwd(), 'images', f'{filename}.png'), 'wb') as file:
            file.write(bytes_image)
        if for_pygame:
            pygame_image = pygame.image.load(os.path.join(os.getcwd(), 'images', f'{filename}.png'))
            pygame_image.convert_alpha()
            return pygame_image
        else:
            pil_image = PIL.Image.open(os.path.join(os.getcwd(), 'images', f'{filename}.png'), mode='r')
            return pil_image
    else:
        return bytes_image

# image = PIL.Image.open(os.path.join(os.getcwd(), 'images', f'{filename}.png').reduce(5)  # Уменьшение в 5 раз
