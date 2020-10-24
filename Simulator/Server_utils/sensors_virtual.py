#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Server_utils.Components_virtual import SerialTalksComponent
from common.serialutils import *
from math import *
import time

# Instructions
GET_SENSOR1_OPCODE = 0x10
GET_SENSOR2_OPCODE = 0x11
GET_SENSOR3_OPCODE = 0x12
GET_SENSOR4_OPCODE = 0x13
GET_SENSOR5_OPCODE = 0x14
GET_SENSOR6_OPCODE = 0x15
GET_SENSOR7_OPCODE = 0x16
GET_SENSOR8_OPCODE = 0x17

CHECK_ERROR_OPCODE = 0X18

GET_ALL_TOPIC_OPCODE = 0x01

BYTEORDER = 'little'
ENCODING = 'utf-8'

CHAR = IntegerType(1, BYTEORDER, True)
UCHAR = IntegerType(1, BYTEORDER, False)
SHORT = IntegerType(2, BYTEORDER, True)
USHORT = IntegerType(2, BYTEORDER, False)
LONG = IntegerType(4, BYTEORDER, True)
ULONG = IntegerType(4, BYTEORDER, False)

FLOAT = FloatType('f')

STRING = StringType(ENCODING)

BYTE = UCHAR
INT = SHORT
UINT = USHORT
DOUBLE = FLOAT


class Sensors(SerialTalksComponent):
    TIMESTEP = 100
    MAX_DIST = 10000

    def __init__(self, parent):
        SerialTalksComponent.__init__(self, "SensorBoard")
        self.add_method(GET_SENSOR1_OPCODE, self.get_sensor1_range)
        self.add_method(GET_SENSOR2_OPCODE, self.get_sensor2_range)
        self.add_method(GET_SENSOR3_OPCODE, self.get_sensor3_range)
        self.add_method(GET_SENSOR4_OPCODE, self.get_sensor4_range)
        self.add_method(GET_SENSOR5_OPCODE, self.get_sensor5_range)
        self.add_method(GET_SENSOR6_OPCODE, self.get_sensor6_range)
        self.add_method(GET_SENSOR7_OPCODE, self.get_sensor7_range)
        self.add_method(GET_SENSOR8_OPCODE, self.get_sensor8_range)
        self.robot = parent
        self.parent = parent.parent

    def get_sensor1_range(self):
        return Deserializer(USHORT(self.MAX_DIST)+USHORT(self.MAX_DIST))

    def get_sensor2_range(self):
        return Deserializer(USHORT(self.MAX_DIST)+USHORT(self.MAX_DIST))

    def get_sensor3_range(self):
        return Deserializer(USHORT(self.MAX_DIST)+USHORT(self.MAX_DIST))

    def get_sensor4_range(self):
        return Deserializer(USHORT(self.MAX_DIST)+USHORT(self.MAX_DIST))

    def get_sensor5_range(self):
        return Deserializer(USHORT(self.MAX_DIST)+USHORT(self.MAX_DIST))

    def get_sensor6_range(self):
        return Deserializer(USHORT(self.MAX_DIST)+USHORT(self.MAX_DIST))

    def get_sensor7_range(self):
        return Deserializer(USHORT(self.MAX_DIST)+USHORT(self.MAX_DIST))

    def get_sensor8_range(self):
        return Deserializer(USHORT(self.MAX_DIST)+USHORT(self.MAX_DIST))

    def check_errors(self):

        return Deserializer(BYTE(0))

    def compute(self):
        pass
