## █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀▄ █▀▀ █ █ █▀▀ █   █▀█ █▀█ █▀▀ █▀▄   ▄▀█ █▄ █ █▀▄   █▀█ █▀█ █▀█ █▀▄ █ █ █▀▀ █▀▀ █▀▄   █▄▄ █▄█   █▄ █ █ █▀▀ █▄▀   █▄▄ █ █▀ █▀ █▀▀ ▀█▀
## █▄█ █▀█ █ ▀ █ ██▄   █▄▀ ██▄ ▀▄▀ ██▄ █▄▄ █▄█ █▀▀ ██▄ █▄▀   █▀█ █ ▀█ █▄▀   █▀▀ █▀▄ █▄█ █▄▀ █▄█ █▄▄ ██▄ █▄▀   █▄█  █    █ ▀█ █ █▄▄ █ █   █▄█ █ ▄█ ▄█ ██▄  █

import os
import sys
import time

def big_text_print(text: str, row: int = -1, colour = ''):
    if row not in range(1, 6):
        return 'Error: Row invalid'
    if text == '':
        return ''
    else:
        row -= 1
    big_text = {
        # letters
        'a': [
            '█████',
            '█▀▄ █',
            '█ ▀ █',
            '▄▄█▄▄',
            '▀▀▀▀▀'],
        'b': [
            '█████',
            '▄ ▄ ▀',
            '█ ▄ ▀',
            '▄▄▄▄█',
            '▀▀▀▀▀'],
        'c': [
            '█████',
            ' ▄▄▄ ',
            ' ███▀',
            '▄▄▄▄▄',
            '▀▀▀▀▀'],
        'd': [
            '█████',
            '▄ ▄▄▀',
            '█ ██ ',
            '▄▄▄▄█',
            '▀▀▀▀▀'],
        'e': [
            '█████',
            '▄ ▄▄ ',
            '█ ▄█▀',
            '▄▄▄▄▄',
            '▀▀▀▀▀'],
        'f': [
            '█████',
            '▄ ▄▄ ',
            '█ ▄██',
            '▄▄▄██',
            '▀▀▀▀▀'],
        'g': [
            '█████',
            ' ▄▄▄▄',
            ' ██▄ ',
            '▄▄▄▄▄',
            '▀▀▀▀▀'],
        'h': [
            '███',
            ' █ ',
            ' ▄ ',
            '▄█▄',
            '▀▀▀'],
        'i': [
            '███',
            '▄ ▄',
            '█ █',
            '▄▄▄',
            '▀▀▀'],
        'j': [
            '█████',
            '██▄ ▄',
            ' ▄█ █',
            '▄▄▄██',
            '▀▀▀▀▀'],
        'k': [
            '█████',
            '▄ █ ▄',
            '█ ▄▀█',
            '▄▄█▄▄',
            '▀▀▀▀▀'],
        'l': [
            '█████',
            '▄ ▄██',
            '█ ██▀',
            '▄▄▄▄▄',
            '▀▀▀▀▀'],
        'm': [
            '███████',
            '▄ ▀█▀ ▄',
            '█ █▄█ █',
            '▄▄▄█▄▄▄',
            '▀▀▀▀▀▀▀'],
        'n': [
            '███████',
            '▄ ▀█▄ ▄',
            '█ █▄▀ █',
            '▄▄▄██▄▄',
            '▀▀▀▀▀▀▀'],
        'o': [
            '████',
            ' ▄▄ ',
            ' ██ ',
            '▄▄▄▄',
            '▀▀▀▀'],
        'p': [
            '█████',
            '▄ ▄▄ ',
            '█ ▄▄▄',
            '▄▄▄██',
            '▀▀▀▀▀'],
        'q': [
            '█████',
            ' ▄▄▄ ',
            ' ██▀ ',
            '▄▄▄▄▄',
            '▀▀▀▀▀'],
        'r': [
            '█████',
            '▄ ▄▄▀',
            '█ ▄ ▄',
            '▄▄█▄▄',
            '▀▀▀▀▀'],
        's': [
            '█████',
            ' ▄▄▄▄',
            '▄▄▄▄ ',
            '▄▄▄▄▄',
            '▀▀▀▀▀'],
        't': [
            '█████',
            ' ▄ ▄ ',
            '██ ██',
            '█▄▄▄█',
            '▀▀▀▀▀'],
        'u': [
            '██████',
            '▄ ██ ▄',
            '█ ██ █',
            '█▄▄▄▄█',
            '▀▀▀▀▀▀'],
        'v': [
            '█████',
            '▄ █ ▄',
            '█▄▀▄█',
            '██▄██',
            '▀▀▀▀▀'],
        'w': [
            '█████████',
            '▄ █▀▀▀█ ▄',
            '█ █ █ █ █',
            '█▄▄▄█▄▄▄█',
            '▀▀▀▀▀▀▀▀▀'],
        'x': [
            '█████',
            '▄ ▀ ▄',
            '█▀ ▀█',
            '▄▄█▄▄',
            '▀▀▀▀▀'],
        'y': [
            '█████',
            '▄ █ ▄',
            '█▄ ▄█',
            '█▄▄▄█',
            '▀▀▀▀▀'],
        'z': [
            '█████',
            ' ▄▄ ▄',
            '█▀▄█▀',
            '▄▄▄▄▄',
            '▀▀▀▀▀'],
        # numbers
        '0': [
            '████',
            ' ▄▄ ',
            ' ██ ',
            '▄▄▄▄',
            '▀▀▀▀'],
        '1': [
            '███',
            '▀ █',
            '█ █',
            '▄▄▄',
            '▀▀▀'],
        '2': [
            '████',
            '▀▄▄▀',
            '█▀▄█',
            '▄▄▄▄',
            '▀▀▀▀'],
        '3': [
            '████',
            '▄▄▄ ',
            '█▄▄ ',
            '▄▄▄▄',
            '▀▀▀▀'],
        '4': [
            '████',
            ' █ █',
            '▄▄ █',
            '█▄▄▄',
            '▀▀▀▀'],
        '5': [
            '████',
            ' ▄▄▄',
            '▄▄▄ ',
            '▄▄▄▄',
            '▀▀▀▀'],
        '6': [
            '████',
            ' ▄▄▄',
            ' ▄▄ ',
            '▄▄▄▄',
            '▀▀▀▀'],
        '7': [
            '████',
            '▄▄▄ ',
            '██ █',
            '█▄██',
            '▀▀▀▀'],
        '8': [
            '████',
            '▀▄▄▀',
            '▀▄▄▀',
            '█▄▄█',
            '▀▀▀▀'],
        '9': [
            '████',
            ' ▄▄ ',
            '▄▄▄ ',
            '▄▄▄▄',
            '▀▀▀▀'],
        # special characters
        ' ': [
            '█',
            '█',
            '█',
            '█',
            '▀'],
        ':': [
            '███',
            '█▀█',
            '███',
            '█▄█',
            '▀▀▀'],
        '.': [
            '██',
            '██',
            '██',
            '▄█',
            '▀▀'],
        '?': [
            '█████',
            '▀▄▄▀█',
            '██▄██',
            '██▄██',
            '▀▀▀▀▀'],
        '|': [
            '██▀██',
            '██ ██',
            '██ ██',
            '██ ██',
            '▀▀▀▀▀']
    }
    text = text.lower()
    if row == 4:
        yeet = '▀'
    else:
        yeet = '█'
    return_string = colour + yeet
    # split text to account for the colours 
    for letter in text:
        try:
            return_string += big_text[letter][row] + yeet
        except KeyError:
            if row == 0:
                return f'Error: symbol/letter not implemented: {letter}'
            else:
                return ''
    return return_string


def medium_text_print(text: str, row: int = -1, colour = ''):
    if row not in range(1, 3):
        return 'Error: Row invalid'
    if text == '':
        return ''
    else:
        row -= 1
    medium_text = {
        # letters
        'a':[
            '▄▀█',
            '█▀█'
        ],
        'b':[
            '█▄▄',
            '█▄█'
        ],
        'c':[
            '█▀▀',
            '█▄▄'
        ],
        'd':[
            '█▀▄',
            '█▄▀'
        ],
        'e':[
            '█▀▀',
            '██▄'
        ],
        'f':[
            '█▀▀',
            '█▀ '
        ],
        'g':[
            '█▀▀',
            '█▄█'
        ],
        'h':[
            '█ █',
            '█▀█'
        ],
        'i':[
            '█',
            '█'
        ],
        'j':[
            '  █',
            '█▄█'
        ],
        'k':[
            '█▄▀',
            '█ █'
        ],
        'l':[
            '█  ',
            '█▄▄'
        ],
        'm':[
            '█▀▄▀█',
            '█ ▀ █'
        ],
        'n':[
            '█▄ █',
            '█ ▀█'
        ],
        'o':[
            '█▀█',
            '█▄█'
        ],
        'p':[
            '█▀█',
            '█▀▀'
        ],
        'q':[
            '█▀█',
            '▀▀█'
        ],
        'r':[
            '█▀█',
            '█▀▄'
        ],
        's':[
            '█▀',
            '▄█'
        ],
        't':[
            '▀█▀',
            ' █ '
        ],
        'u':[
            '█ █',
            '█▄█'
        ],
        'v':[
            '█ █',
            '▀▄▀'
        ],
        'w':[
            '█ █ █',
            '▀▄▀▄▀'
        ],
        'x':[
            '▀▄▀',
            '█ █'
        ],
        'y':[
            '█▄█',
            ' █ '
        ],
        'z':[
            '▀█',
            '█▄'
        ],
        # numbers
        '0': [
            '█▀█',
            '█▄█'
        ],
        '1':[
            '▄█',
            ' █'
        ],
        '2': [
            '▀█',
            '█▄'
        ],
        '3': [
            '\033[4m▀\033[0m█',
            '▄█'
        ],
        '4': [
            '█ █',
            '▀▀█'
        ],
        '5':[
            '█▀',   
            '▄█'
        ],
        '6': [
            '█▄▄',
            '█▄█'
        ],
        '7': [
            '▀▀█',
            '  █'
        ],
        '8': [
            '█\033[4m▀\033[0m█',
            '█▄█'
        ],
        '9': [
            '█▀█',
            '▀▀█'
        ],

        # special characters
        ' ':[
            ' ',
            ' '
        ],
        '.':[
            ' ',
            '▄'
        ],
        ':':[
            '▄',
            '▄'
        ],
        '?':[
            '▀█',
            ' ▄'
        ],
        '<':[
            '▄█▀',
            '▀█▄'
        ],
        '>':[
            '▀█▄',
            '▄█▀'
        ],
        '/':[
            ' ▄▀',
            '▄▀ '
        ],
        '(':[
            '▄▀',
            '▀▄'
        ],
        ')':[
            '▀▄',
            '▄▀'
        ],
        '[':[
            '█▀',
            '█▄'
        ],
        ']':[
            '▀█',
            '▄█'
        ],
        '!':[
            '█',
            '▄'
        ],
        "'":[
            '▀',
            ' '
        ],
        '🍗':[
            f"{medium_text_print('hunger')}",
            f"{medium_text_print('hunger')}"
        ],
        '💎':[
            f"{medium_text_print('hunger')}",
            f"{medium_text_print('hunger')}"
        ],
        '💰':[
            f"{medium_text_print('gold')}",
            f"{medium_text_print('gold')}"
        ],
    } 
    text = text.lower()  
    return_string = f"{colour}"
    for i in range(len(text)):
        try:
            return_string += medium_text[text[i]][row] + ' '
        except KeyError:
            if row == 0:
                return f'Error: symbol/letter not implemented: {text[i]}'
            else:
                return ''
    return return_string

def test():
    import os
    os.system('cls')
    while True:
        test_text = input('>>> ')
        os.system('cls')
        print(f"""
{big_text_print(test_text, 1)}
{big_text_print(test_text, 2)}      
{big_text_print(test_text, 3)}
{big_text_print(test_text, 4)}
{big_text_print(test_text, 5)}   
   
{medium_text_print(test_text, 1)}
{medium_text_print(test_text, 2)}
""")
        
def text_print(text):
    if type(text) == str:
        for i in range(len(text)):
            print(text[0:i+1],end='\r') 
            if '.' in text and text[i] == '.' and i != len(text)-1:
                time.sleep(.5)
            elif text[i] == '!' or text[i] == '?' and i != len(text)-1:
                time.sleep(.2)
            else:
                time.sleep(.0100) 
        print(text)
    elif type(text) == list or type(text) == tuple:
        MaxTextLen = 0
        for i in range(len(text)):
            if MaxTextLen < len(text[i]):
                MaxTextLen = len(text[i])
        for i in range(MaxTextLen):
            for b in range(len(text)):
                try:
                    print(text[b][0:i+1],end='\n')
                except IndexError:
                    print('', end = '\n')
            time.sleep(.0100) 
            if i != MaxTextLen-1:
                for x in range(len(text)): #go back
                    sys.stdout.write("\033[F")
    time.sleep(.25)     
    
    
def medium_text_period_print(text):
    original_text = text
    text = [medium_text_print(text, 1, True), medium_text_print(text, 2, True)]
    for i in range(len(text)):
        text[i] = text[i].split(',') 
    # do the printing
    for i in range(len(text[0])):
        for b in range(len(text)):
            try:
                print(' '.join(text[b][0:i+1]))
            except IndexError:
                print('', end = '\n')
        try:
            try:
                if '.' in original_text and original_text[i] == '.' and i != len(text)-1:
                    time.sleep(.5)
                elif original_text[i] == '!' or original_text[i] == '?' and i != len(text)-1:
                    time.sleep(.2)
                else:
                    time.sleep(.01) 
            except IndexError:
                assert AttributeError
        except AttributeError:
            time.sleep(.03) 
        if i != len(text[0])-1:
            for x in range(len(text)): #go back
                sys.stdout.write("\033[F")
    time.sleep(.25) 
    
    
def get_screensize(vertical = False):
    import os 
    _raw = str(os.get_terminal_size())
    accepted_list = [',']
    _raw = ''.join([char for char in _raw if (char.isdigit() or char in accepted_list) ])
    if vertical:
        screensize = int(_raw.split(',')[1])
    else:
        screensize = int(_raw.split(',')[0])
    return screensize

def go_back(back = get_screensize(True)+4):
    for _ in range(back):
        sys.stdout.write("\033[F")
        
    
def clearConsole(): 
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

# class for battle output
class rolling_instance_text:
    
    def __init__(self, _text: str, _delay: int = 0):
        self.text = _text
        self.done = False
        self.delay =_delay
        self.creation_instance = int(time.time()*1000)
        self.setup_max_instance()
    
    def setup_max_instance(self):
        #from run_game import Settings, get_global_settings
        #self.settings: Settings = get_global_settings()
        self.text_time_length = [0]*len(self.text)
        for i, symbol in enumerate(self.text):
            #print(self.text[0:i+1],end='\r') 
            if '.' in self.text and symbol == '.' and i != len(self.text)-1:
                self.text_time_length[i] += self.text_time_length[i-1] + 500
            elif symbol == '!' or symbol == '?' and i != len(self.text)-1:
                self.text_time_length[i] += self.text_time_length[i-1] + 200
            else:
                self.text_time_length[i] += self.text_time_length[i-1] + 10 #self.settings.speed
        self.max_instance = max(self.text_time_length) + 10
        
    def set_start_instance(self):
        self.start_instance = int(time.time()*1000) - 10 + self.delay #self.settings.speed
        
    def refresh_instance(self):
        while True:
            try:
                self.instance = int(time.time()*1000) - self.start_instance
                return False
            except AttributeError:
                self.set_start_instance()
            except AssertionError:
                return True
    def __str__(self):
        if self.is_done():  
            return f"{self.text}"  
        if self.refresh_instance():
            return ""
        for i in range(len(self.text_time_length)-1):
            if self.text_time_length[i] <= self.instance and self.text_time_length[i+1] >= self.instance:
                return f"{self.text[0:i+1]}"
        return f"{self.text}"
    
    def __repr__(self):
        return self.__str__()
    
    def is_done(self):
        if self.done == False and self.max_instance <= self.refresh_instance():
            self.done = True
        else:
            self.done = False
        return self.done
    
if __name__ == '__main__':
    test_text1 = rolling_instance_text('this is a test to see how... yes how... how well this works i guess lmao!!!?!?!?!??!!')
    test_text2 = rolling_instance_text('this is a test to see how... yes how... how well this works i guess lmao!!!?!?!?!??!!', 2000)
    while True:
        print(test_text1)
        print(test_text2)
        if test_text1.is_done() and test_text2.is_done():
            time.sleep(1)
            break
        go_back(2)
        