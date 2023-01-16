import time
import sys
import os
import shutil
import msvcrt 

from text_generation import *

"""
NOTE: unless specified all methods have a best and worst case complexity of O(1)
"""

# functions which help the intergration of graphics

def keyboard_wait():
    keypressed = msvcrt.getch()
    # TODO
    return 

def clearConsole():
    """
    a short program that clears the console of any unwanted output text
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)  
    
    
def get_screensize(vertical = False):
    """_summary_
    gets the dimentions of the terminal 
    Args:
        vertical (bool, optional): whether the size is vertical or horizontal. Defaults to False.

    Returns:
        int: count of whatever direction 
        
    COMPLEXITY: O(n), n = len(_raw)
    """
    try:
        _raw = str(os.get_terminal_size())
    except:
        _raw = str(shutil.get_terminal_size()) #using shutil instead of os will work and not give OSError.
    accepted_list = [',']
    _raw = ''.join([char for char in _raw if (char.isdigit() or char in accepted_list) ])
    if vertical:
        screensize = int(_raw.split(',')[1])
    else:
        screensize = int(_raw.split(',')[0])
    return screensize   
    
def console_print(_text: str, test = False):
    text_print(_text, test)
    time_sleep(1.5, test)
    go_back(1)
    print(" "*get_screensize())

def go_back(back = get_screensize(True)+4, **kwargs):
    """_summary_
    goes back 1 line vertically in the console
    Args:
        back (int, optional): how many lines to go back. Defaults to get_screensize(True).
    """
    try:
        _print = kwargs['_print']
    except KeyError:
        _print = True
    screensize = get_screensize()
    for line in range(back):
        if _print:
            print(" "*screensize, end = "")
        sys.stdout.write("\033[F")
    
def text_print(text, test = False):
    """_summary_

    printing helper function that goes brrrrrr

    Args:
        text (_type_): text being printed to console
        test (bool, optional): whether . Defaults to False.
        
    COMPLEXITY = O(n), n = len(text)
    """
    if type(text) == str:
        for i in range(len(text)):
            print(text[i],end='') 
            if '.' in text and text[i] == '.' and i != len(text)-1:
                time_sleep(.5, test)
            elif text[i] == '!' or text[i] == '?' and i != len(text)-1:
                time_sleep(.2, test)
            else:
                time_sleep(.0100, test) 
        print(text)
    time_sleep(.25, test)
    
def time_sleep(amount, test = False):
    if test:
        if amount > .1:
            time.sleep(amount/200)
    else:
        time.sleep(amount)
    
    
