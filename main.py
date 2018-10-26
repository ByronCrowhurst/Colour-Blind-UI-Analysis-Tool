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
    colour_blind_adjustments(base_image, image_one, image_two, image_three)


def load_image():
    image = pygame.image.load("screen.jpg")
    image = image.convert(image)
    return image


def colour_blind_adjustments(base_image, image_one, image_two, image_three):
    protanopia_image = image_one
    deuteranomaly = image_two
    tritanomaly = image_three
    protanomaly_colour = pygame.PixelArray(protanopia_image)
    deuteranomaly_colour = pygame.PixelArray(deuteranomaly)
    tritanomaly_colour = pygame.PixelArray(tritanomaly)
    image_width, image_height = base_image.get_size()
    for x in range(0, image_width):
        for y in range(0, image_height):
            red = base_image.get_at((x, y)).r
            green = base_image.get_at((x, y)).g
            blue = base_image.get_at((x, y)).b
            proto_red, proto_green, proto_blue = protanopia_recolouring(red, green, blue)
            deuta_red, deuta_green, deuta_blue = deuternopia_recolouring(red, green, blue)
            trita_red, trita_green, trita_blue = tritanopia_recolouring(red, green, blue)
            protanomaly_colour[x, y] = (proto_blue, proto_green, proto_red)
            deuteranomaly_colour[x, y] = (deuta_blue, deuta_green, deuta_red)
            tritanomaly_colour[x, y] = (trita_blue, trita_green, trita_red)

    del protanomaly_colour
    del deuteranomaly_colour
    del tritanomaly_colour
    pygame.image.save(protanopia_image, "protoanomaly screen.PNG")
    pygame.image.save(deuteranomaly, "deuteranomaly screen.PNG")
    pygame.image.save(tritanomaly, "tritanomaly.screen.PNG")


def protanopia_recolouring(red, green, blue):
    red_channel_red_value = red * 0.56667
    red_channel_green_value = green * 0.43337
    red_channel_blue_value = blue * 0.0
    green_channel_red_value = red * 0.55883
    green_channel_green_value = green * 0.44167
    green_channel_blue_value = blue * 0.0
    blue_channel_red_value = red * 0.0
    blue_channel_green_value = green * 0.24167
    blue_channel_blue_value = blue * 0.75833
    red = red_channel_red_value + red_channel_green_value + red_channel_blue_value
    green = green_channel_red_value + green_channel_green_value + green_channel_blue_value
    blue = blue_channel_red_value + blue_channel_green_value + blue_channel_blue_value
    return red, green, blue


def deuternopia_recolouring(red, green, blue):
    red_channel_red_value = red * 0.625
    red_channel_green_value = green * 0.375
    red_channel_blue_value = blue * 0.0
    green_channel_red_value = red * 0.7
    green_channel_green_value = green * 0.3
    green_channel_blue_value = blue * 0.0
    blue_channel_red_value = red * 0.0
    blue_channel_green_value = green * 0.3
    blue_channel_blue_value = blue * 0.7
    red = red_channel_red_value + red_channel_green_value + red_channel_blue_value
    green = green_channel_red_value + green_channel_green_value + green_channel_blue_value
    blue = blue_channel_red_value + blue_channel_green_value + blue_channel_blue_value
    return red, green, blue


def tritanopia_recolouring(red, green, blue):
    red_channel_red_value = red * 0.95
    red_channel_green_value = green * 0.05
    red_channel_blue_value = blue * 0.0
    green_channel_red_value = red * 0.0
    green_channel_green_value = green * 0.43333
    green_channel_blue_value = blue * 0.56667
    blue_channel_red_value = red * 0.0
    blue_channel_green_value = green * 0.475
    blue_channel_blue_value = blue * 0.525
    red = red_channel_red_value + red_channel_green_value + red_channel_blue_value
    green = green_channel_red_value + green_channel_green_value + green_channel_blue_value
    blue = blue_channel_red_value + blue_channel_green_value + blue_channel_blue_value
    return red, green, blue


main()
