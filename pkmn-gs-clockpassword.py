#!/usr/bin/env python3
# coding=utf-8
# Pokémon Gold/Silver Clock Reset Password Generator
# Version 0.3
# Copyright 2011 woddfellow2 | http://wlair.us.to/
# Python 2.7 "port" also copyright 2015 Wyatt Ward.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# TODO:
# - Command-line options

import sys

# Collect player character name, trainer ID number, and amount of held money,
# also error handling:
name = input("Enter name of player character (case-sensitive; use { for PK and } for MN):\n> ")  # fixed raw_input -> input
if len(name) > 7:
    sys.stderr.write("ER001: Name must be only 7 characters long.\n")
    exit()
if name == "":
    sys.stderr.write("ER005: Name must not be blank.\n")
    exit()
try:
    trainerid = int(input("Enter ID number:\n> "))  # fixed raw_input -> input
except ValueError:
    sys.stderr.write("ER006: Trainer ID given was blank or not a number.\n")
    exit()
# FIX: range check corrected
if not (0 <= trainerid <= 65535):
    sys.stderr.write("ER002: Trainer ID must be a 5-digit number from 00000 to 65536.\n")
    exit()
try:
    money = int(input("Enter amount of held money:\n> "))  # fixed raw_input -> input
except ValueError:
    sys.stderr.write("ER007: Amount of held money given was blank or not a number.\n")
    exit()
# FIX: range check corrected
if not (0 <= money <= 999999):
    sys.stderr.write("ER003: Amount of money must be a 0- to 6-digit number.\n")
    exit()

# Name
# Translate first 5 characters of name into values:
name_chars = { "A": 128, "B": 129, "C": 130, "D": 131, "E": 132, "F": 133,
               "G": 134, "H": 135, "I": 136, "J": 137, "K": 138, "L": 139,
               "M": 140, "N": 141, "O": 142, "P": 143, "Q": 144, "R": 145,
               "S": 146, "T": 147, "U": 148, "V": 149, "W": 150, "X": 151,
               "Y": 152, "Z": 153, "(": 154, ")": 155, ":": 156, ";": 157,
               "[": 158, "]": 159, "a": 160, "b": 161, "c": 162, "d": 163,
               "e": 164, "f": 165, "g": 166, "h": 167, "i": 168, "j": 169,
               "k": 170, "l": 171, "m": 172, "n": 173, "o": 174, "p": 175,
               "q": 176, "r": 177, "s": 178, "t": 179, "u": 180, "v": 181,
               "w": 182, "x": 183, "y": 184, "z": 185, "{": 225, "}": 226,
               "-": 227, "?": 230, "!": 231, ".": 232, "*": 241, "/": 243,
               ",": 244, " ": 0 }

# FIX: wrapped in try/except to prevent NameError on invalid chars
try:
    for k, v in name_chars.items():
        if name[0] == k:
            name_char1 = v
        if len(name) >= 2:
            if name[1] == k:
                name_char2 = v
        if len(name) >= 3:
            if name[2] == k:
                name_char3 = v
        if len(name) >= 4:
            if name[3] == k:
                name_char4 = v
        if len(name) >= 5:
            if name[4] == k:
                name_char5 = v
except NameError:
    sys.stderr.write("ER004: Name given contains one or more invalid characters.\n")
    exit()

try:
    if len(name) == 1:
        name_total = name_char1
    if len(name) == 2:
        name_total = name_char1 + name_char2
    if len(name) == 3:
        name_total = name_char1 + name_char2 + name_char3
    if len(name) == 4:
        name_total = name_char1 + name_char2 + name_char3 + name_char4
    if len(name) >= 5:
        name_total = name_char1 + name_char2 + name_char3 + name_char4 + name_char5

    if len(name) < 5:
        name_total += 80
except NameError:
    sys.stderr.write("ER004: Name given contains one or more invalid characters.\n")
    exit()

# Money
# FIXED integer division
money_byte1 = money // 65536
money_byte2 = (money // 256) % 256
money_byte3 = money % 256
money_total = money_byte1 + money_byte2 + money_byte3

# Trainer ID
# FIXED integer division
trainerid_byte1 = trainerid // 256
trainerid_byte2 = trainerid % 256
trainerid_total = trainerid_byte1 + trainerid_byte2

# Password
password = name_total + money_total + trainerid_total

# Output result
print()  # Newline to make it look better
print("%s/%s, %d units of currency" % (name, str(trainerid).zfill(5), money))
print("Password:", str(password).zfill(5))
