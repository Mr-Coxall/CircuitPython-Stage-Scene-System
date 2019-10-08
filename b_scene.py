#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: October 2019
# This file is the B scene
#   for CircuitPython and uGame

import ugame
import stage

import menu_scene

def game_loop():
    # this function is a scene

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the background to image 0 in the bank
    #   we will not change the background after initially drawing it
    background = stage.Grid(image_bank_1, 160, 120)

    # a list of sprites that will be updated every frame
    sprites = []

    # create a sprite
    #   parameters (image_bank, image # in bank, x, y)
    #alien = stage.Sprite(image_bank_1, 9, 80-8, 60-8)
    #sprites.append(alien)

    # show text on screen
    text = stage.Text(width = 29, height = 1)
    text.move(30, 110)
    text.text("B")

    # create a stage for the background to show up on
    #   and set the frame rate to 30fps
    game = stage.Stage(ugame.display, 30)
    # set the layers, items show up in order
    game.layers = [text] + sprites + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # update game logic
        if keys & ugame.K_SELECT != 0:  # Select button
            menu_scene.game_loop()


        # redraw sprite list
        game.render_sprites(sprites)
        game.tick() # wait until refresh rate finishes


if __name__ == "__main__":
    game_loop()