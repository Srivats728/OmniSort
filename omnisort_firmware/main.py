{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import board\
from kmk.kmk_keyboard import KMKKeyboard\
from kmk.keys import KC\
from kmk.scanners import DiodeOrientation\
from kmk.modules.encoder import EncoderHandler\
from kmk.extensions.RGB import RGB\
\
keyboard = KMKKeyboard()\
\
keyboard.col_pins = (board.D3, board.D6, board.D9)\
keyboard.row_pins = (board.D0, board.D1, board.D2)\
keyboard.diode_orientation = DiodeOrientation.COL2ROW\
\
encoder_handler = EncoderHandler()\
encoder_handler.pins = ((board.D7, board.D8, None, False),)\
encoder_handler.map = [ ((KC.VOLD, KC.VOLU),) ]\
keyboard.modules.append(encoder_handler)\
\
rgb = RGB(pixel_pin=board.D10, num_pixels=8, val_limit=100, hue_default=200, sat_default=255, val_default=100)\
keyboard.extensions.append(rgb)\
\
keyboard.keymap = [\
    [\
        KC.N1, KC.N2, KC.N3,\
        KC.N4, KC.N5, KC.N6,\
        KC.N7, KC.N8, KC.MUTE\
    ]\
]\
\
if __name__ == '__main__':\
    keyboard.go()}