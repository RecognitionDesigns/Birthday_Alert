#!/usr/bin/env python3

import anki_vector
import time
from math import ceil
from anki_vector.util import degrees
from decimal import Decimal, ROUND_DOWN, ROUND_UP
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def rainbow_eyes():
    for i in range(10):
        for j in range(100):
            robot.behavior.set_eye_color(hue=j/100.0, saturation=0.99)
            time.sleep(0.005)

def make_text_image(text_to_draw, x, y, font=None):
    dimensions = (184, 96)
    text_image = Image.new('RGBA', dimensions, (0, 0, 0, 255))
    dc = ImageDraw.Draw(text_image)
    dc.text((x, y), text_to_draw, fill=(0, 255, 0, 255), font=font)
    return text_image

try:
    font_file = ImageFont.truetype("/Users/Colin/VectorSdk/Fonts/lcd.ttf", 40)
except IOError:
    try:
        font_file = ImageFont.truetype("Fonts/arial.ttf", 37)
    except IOError:
        pass

with anki_vector.AsyncRobot('0050169f') as robot:
    robot.behavior.set_head_angle(degrees(30.0))
    robot.behavior.set_lift_height(0.0)

    text_to_draw = """  Happy 
Birthday!!!"""
    face_image = make_text_image(text_to_draw, 20, 5, font_file)
    #args = anki_vector.util.parse_command_args()
    
    robot.behavior.say_text("Today is your birthday, Happy Birthday Human")
    rainbow_eyes()
   # time.sleep(1)

    

    print("Display image on Vector's face...")
        
    robot.behavior.say_text("Happy Birthday to you. Happy Birthday to you. Happy Birthday dear Human. Happy Birthday to you", True, 1.1)
    screen_data = anki_vector.screen.convert_image_to_screen_data(face_image)
    robot.screen.set_screen_with_image_data(screen_data, 20.0, interrupt_running=True)
    time.sleep(2)
    
with anki_vector.Robot('0050169f') as robot:
    robot.behavior.set_head_angle(degrees(30.0))
    robot.behavior.set_lift_height(0.0)
    time.sleep(3)
    robot.audio.stream_wav_file("/Users/Colin/VectorSdk/Sounds/party_horn.wav", 50)
    robot.anim.play_animation_trigger('GreetAfterLongTime')
    time.sleep(1)