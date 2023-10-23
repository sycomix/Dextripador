#!/usr/bin/python3
#-*- coding: utf-8 -*-

######################################################
#   Dextripador
#   File: utils.py
#   Version: 0.7
######################################################

VERSION = 0.7

COMMAND_FLAG = False
VERBOSE_1 = False
VERBOSE_2 = False
VERBOSE_3 = False

credits = '''

██████╗ ███████╗██╗  ██╗████████╗██████╗ ██╗██████╗  █████╗ ██████╗  ██████╗ ██████╗ 
██╔══██╗██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
██║  ██║█████╗   ╚███╔╝    ██║   ██████╔╝██║██████╔╝███████║██║  ██║██║   ██║██████╔╝
██║  ██║██╔══╝   ██╔██╗    ██║   ██╔══██╗██║██╔═══╝ ██╔══██║██║  ██║██║   ██║██╔══██╗
██████╔╝███████╗██╔╝ ██╗   ██║   ██║  ██║██║██║     ██║  ██║██████╔╝╚██████╔╝██║  ██║
╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                          Version %0.1f                                                           
                                                                                     
Dextripador is a tool aimed to provide parsing of odex files and internal dex files,
with the possibility to extract these latter.

This tool is part of a research made by UC3M COSEC Lab & IMDEA Networks.

Programmers & Ideas:
    
    - Eduardo Blazquez
    - Julien Gamba
    
https://androidobservatory.com
''' % (VERSION)

def SET_COMMAND_FLAG(BOOLEAN):
    global COMMAND_FLAG
    COMMAND_FLAG = BOOLEAN

def SET_VERBOSE1(BOOLEAN):
    global VERBOSE_1
    VERBOSE_1 = BOOLEAN

def SET_VERBOSE2(BOOLEAN):
    global VERBOSE_2
    VERBOSE_2 = BOOLEAN

def SET_VERBOSE3(BOOLEAN):
    global VERBOSE_3
    VERBOSE_3 = BOOLEAN

class Printer():

    def print(self):
        global COMMAND_FLAG
        if COMMAND_FLAG:
            print(self)

    def verbose1(self):
        global COMMAND_FLAG
        global VERBOSE_1
        if COMMAND_FLAG and VERBOSE_1:
            print(self)

    def verbose2(self):
        global COMMAND_FLAG
        global VERBOSE_2
        if COMMAND_FLAG and VERBOSE_2:
            print(self)

    def verbose3(self):
        global COMMAND_FLAG
        global VERBOSE_3

        if COMMAND_FLAG and VERBOSE_3:
            print(self)