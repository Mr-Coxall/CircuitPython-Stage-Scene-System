#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: October 2019
# This file is the starting point for menu scene system
#   for CircuitPython and uGame

import splash_scene


def main():
    # goes to the first game scene
    splash_scene.game_loop()

if __name__ == "__main__":
    main()