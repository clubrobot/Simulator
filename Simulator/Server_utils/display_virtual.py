#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Server_utils.Components_virtual import SerialTalksComponent
from common.serialutils import *
from math import *
import time

SET_EEPROM_DEFAULT_MESSAGE_OPCODE = 0x09
SET_SPEED_MATRIX_OPCODE = 0x0A
SET_EEPROM_CHAR_LEDMATRIX_OPCODE = 0x0B
SET_EEPROM_CHAR_IPDISPLAY_OPCODE = 0x0C
SET_MATRIX_MESSAGE_OPCODE = 0x0D
SET_IPDISPLAY_MESSAGE_OPCODE = 0x0E
CLEAR_IPDISPLAY_MESSAGE_OPCODE = 0x0F
SET_IPDISPLAY_UNIQUE_MESSAGE_OPCODE = 0x10

SLIDE_MODE = 0
ANIMATION_MODE = 1
RIGHT_ROTATION_MODE = 2
LEFT_ROTATION_MODE = 3
UPSIDEDOWN_MODE = 4


class Display(SerialTalksComponent):

    def __init__(self, parent):
        SerialTalksComponent.__init__(self, "display")
        self.add_method(SET_MATRIX_MESSAGE_OPCODE,   self.set_message)
        self.add_method(SET_SPEED_MATRIX_OPCODE, self.set_speed)
        self.add_method(SET_EEPROM_DEFAULT_MESSAGE_OPCODE,
                        self.set_default_message)
        self.add_method(SET_EEPROM_CHAR_LEDMATRIX_OPCODE,
                        self.upload_char_pattern)

        self.add_method(SET_IPDISPLAY_UNIQUE_MESSAGE_OPCODE,
                        self.set_message)
        self.add_method(SET_IPDISPLAY_MESSAGE_OPCODE, self.set_multi_message)
        self.add_method(SET_EEPROM_CHAR_IPDISPLAY_OPCODE,
                        self.upload_char_pattern)
        self.add_method(CLEAR_IPDISPLAY_MESSAGE_OPCODE,
                        self.clear_messages)

        self.robot = parent
        self.parent = parent.parent

    def set_message(self, message, mode=None, speed=None):
        pass

    def set_speed(self, speed, a=0):  # `speed` in milliseconds
        pass

    def set_multi_message(self, message):
        pass

    def set_default_message(self, message, mode, speed):
        pass

    def upload_char_pattern(self, char, pattern):
        pass

    def clear_messages(self):
        pass

    def compute(self):
        pass
