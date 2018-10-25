import pygame
import sys
from pygame.locals import *
"""
Byron Crowhurst
"""

def main():
    pygame.init()
    base_image = load_image()
    image_one = load_image()
    image_two = load_image()
    image_three = load_image()
    anomalous_trichromacy(base_image, image_one, image_two, image_three)


def load_image():
    image = pygame.image.load("screen.jpg")
    image = image.convert(image)
    return image


def anomalous_trichromacy(base_image, image_one, image_two, image_three):
    protanomaly = image_one
    deuteranomaly = image_two
    tritanomaly = image_three
    protanomaly_colour = pygame.PixelArray(protanomaly)
    deuteranomaly_colour = pygame.PixelArray(deuteranomaly)
    tritanomaly_colour = pygame.PixelArray(tritanomaly)
    image_width, image_height = base_image.get_size()
    for x in range(0, image_width):
        for y in range(0, image_height):
            red = base_image.get_at((x, y)).r
            green = base_image.get_at((x, y)).g
            blue = base_image.get_at((x, y)).b
            proto_red = (red*0.15)
            deuter_green = (green*0.15)
            trit_blue = (blue*0.15)
            protanomaly_colour[x, y] = (proto_red, green, blue)
            deuteranomaly_colour[x, y] = (red, deuter_green, blue)
            tritanomaly_colour[x, y] = (red, green, trit_blue)

    del protanomaly_colour
    del deuteranomaly_colour
    del tritanomaly_colour
    pygame.image.save(protanomaly, "protoanomaly screen.PNG")
    pygame.image.save(deuteranomaly, "deuteranomaly screen.PNG")
    pygame.image.save(tritanomaly, "tritanomaly.screen.PNG")


main()
