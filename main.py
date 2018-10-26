import pygame
from colour_skew_values import *
"""Byron Crowhurst"""


def main():
    pygame.init()
    if check_image_exists():
        base_image = load_image()
        image_one = load_image()
        image_two = load_image()
        image_three = load_image()
        # base image is the "screen" image, the other three will have different types of colour blindness simulated.
        colour_blind_adjustments(base_image, image_one, image_two, image_three)


def load_image():
    image = pygame.image.load("screen.jpg")
    image = image.convert(image)
    return image


def check_image_exists():
    try:
        load_image()
        # if the image loads then the program executes.
    except pygame.error:
        return False
        # if the file cannot be loaded then the program quits.
    return True


def colour_blind_adjustments(base_image, image_one, image_two, image_three):
    protanopia_image = image_one
    deuteranopia_image = image_two
    tritanopia_image = image_three
    protanopia_colour = pygame.PixelArray(protanopia_image)
    deuteranopia_colour = pygame.PixelArray(deuteranopia_image)
    tritanopia_colour = pygame.PixelArray(tritanopia_image)
    # Three separate versions of the same images are grabbed to simulate each version of colour blindness.
    image_width, image_height = base_image.get_size()
    for x in range(0, image_width):
        for y in range(0, image_height):
            # Runs the pixel array & assigns RGB values & modified RGB values for colour blindness simulation.
            red = base_image.get_at((x, y)).r
            green = base_image.get_at((x, y)).g
            blue = base_image.get_at((x, y)).b
            # Base RGB values that will be modified.
            protanopia_red, protanopia_green, protanopia_blue = colour_blind_recolouring(red, green, blue, 0)
            deuteranopia_red, deuteranopia_green, deuteranopia_blue = colour_blind_recolouring(red, green, blue, 1)
            tritanopia_red, tritanopia_green, tritanopia_blue = colour_blind_recolouring(red, green, blue, 2)
            # Modified RGB values that will be reassigned to the pixel arrays.
            protanopia_colour[x, y] = (protanopia_blue, protanopia_green, protanopia_red)
            deuteranopia_colour[x, y] = (deuteranopia_blue, deuteranopia_green, deuteranopia_red)
            tritanopia_colour[x, y] = (tritanopia_blue, tritanopia_green, tritanopia_red)
    del protanopia_colour
    del deuteranopia_colour
    del tritanopia_colour
    # Delete the pixel arrays one reassigned into so that they are not being read.
    pygame.image.save(protanopia_image, "protanopia screen.PNG")
    pygame.image.save(deuteranopia_image, "deuteranopia screen.PNG")
    pygame.image.save(tritanopia_image, "tritanopia screen.PNG")
    # Output the images with modified colour values.


def get_type_to_adjust(type_number):
    if type_number == 0:
        colour_blindness_name = colour_blindness_types[0]
    elif type_number == 1:
        colour_blindness_name = colour_blindness_types[1]
    elif type_number == 2:
        colour_blindness_name = colour_blindness_types[2]
    else:
        colour_blindness_name = ""
    # Gets which type of colour blindness to adjust colours for.
    return colour_blindness_name


def colour_blind_recolouring(red, green, blue, type_number):
    colour_channels = [red, green, blue, red, green, blue, red, green, blue]
    colour_blindness_name = get_type_to_adjust(type_number)
    # Initialises RGB channel list and returns the name of the colour blindness to be adjusted.
    if colour_blindness_name == colour_blindness_types[0]:
        colours_to_skew = protanopia_dictionary
    elif colour_blindness_name == colour_blindness_types[1]:
        colours_to_skew = deuternopia_dictionary
    elif colour_blindness_name == colour_blindness_types[2]:
        colours_to_skew = tritanopia_dictionary
    else:
        colours_to_skew = {}
    # Returns dictionaries which contain the values of each different colour blindness.

    colour_list = []
    new_red = 0
    new_green = 0
    new_blue = 0
    # Initialised colours to be assigned as new colours.
    if len(colours_to_skew) > 0:
        for i in range(len(colour_skew_list)):
            new_channel_value = colour_channels[i] * colours_to_skew[colour_skew_list[i]]
            colour_list.append(new_channel_value)
            # Colour channel is assigned a value using the correct skew and is appended to a list.
        for i in range(3):
            new_red += colour_list[i]
            new_green += colour_list[i+3]
            new_blue += colour_list[i+6]
            # new colours are created from the colour list

    colour_list.clear()
    return new_red, new_green, new_blue


main()
