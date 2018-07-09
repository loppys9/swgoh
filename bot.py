#!/usr/bin/env python

import cv2
import mss
import mss.tools
import numpy
import pytesseract

# Things to keep track of
"""
boss_health
turns_to_enrage
phase
boss_speed
boss_tenacity
current_character_stats
current_character_abilities
boss_ability_cooldowns
"""

def get_swgoh_box(sct):
    monitor = sct.monitors[1]

    left = 0
    top = monitor['height'] // 4 - 20
    width = monitor['width'] // 2
    height = (monitor['height'] // 2) + 20
    return { 'left' : left, 'top' : top, 'width': width, 'height' : height }

def get_phase(img):
    p2_red = 195
    p2_green = 180
    p2_blue = 30
    p3_red = 161
    p3_green = 66
    p3_blue = 10
    p4_green = 40

    print(img.shape)
    x = 1195
    blue = img.item(15, x, 0)
    green = img.item(15, x, 1)
    red = img.item(15, x, 2)

    print(red, green, blue)
    if green > 180:
        return 1
    elif green > 100:
        return 2
    elif green > 40:
        return 3
    else:
        return 4

def get_health(img):
    start_y = 45
    start_x = 535
    end_y = start_y + 30
    end_x = start_x + 100
    health_section = img[start_y:end_y, start_x:end_x]

    #cv2.imwrite('test_health.png', health_section)
    #health_section = cv2.imread('test_health.png', 0)
    #cv2.imshow('health', health_section)
    #cv2.waitKey()

    config = '-c tessedit_char_whitelist=0123456789.%'

    health = pytesseract.image_to_string(health_section, lang='eng', config=config)
    return float(health.replace(' ', '.')[:-1])

if __name__ == '__main__':
    with mss.mss() as sct:
        swbox = get_swgoh_box(sct)
        sct_img = sct.grab(swbox)
        mss.tools.to_png(sct_img.rgb, sct_img.size, output='misc.png')
        img = numpy.array(sct_img)
        phase = get_phase(img)
        print(phase)
        # to grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        starting_health = get_health(img)
        print(starting_health)

