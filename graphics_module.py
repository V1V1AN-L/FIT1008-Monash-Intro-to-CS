## █▀▀ ▄▀█ █▀▄▀█ █▀▀   █▀▄ █▀▀ █ █ █▀▀ █   █▀█ █▀█ █▀▀ █▀▄   ▄▀█ █▄ █ █▀▄   █▀█ █▀█ █▀█ █▀▄ █ █ █▀▀ █▀▀ █▀▄   █▄▄ █▄█   █▄ █ █ █▀▀ █▄▀   █▄▄ █ █▀ █▀ █▀▀ ▀█▀
## █▄█ █▀█ █ ▀ █ ██▄   █▄▀ ██▄ ▀▄▀ ██▄ █▄▄ █▄█ █▀▀ ██▄ █▄▀   █▀█ █ ▀█ █▄▀   █▀▀ █▀▄ █▄█ █▄▀ █▄█ █▄▄ ██▄ █▄▀   █▄█  █    █ ▀█ █ █▄▄ █ █   █▄█ █ ▄█ ▄█ ██▄  █
try:
    import os
except:
    pass
import shutil
import sys
import time
try:
    import msvcrt
except:
    pass

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


def medium_text_print(text: str, row: int = -1):
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
        # emojis
        '🍗':[
            f"{medium_text_print('hunger')}",
            f"{medium_text_print('hunger')}"
        ],
        '💎':[
            f"{medium_text_print('item')}",
            f"{medium_text_print('item')}"
        ],
        '💰':[
            f"{medium_text_print('gold')}",
            f"{medium_text_print('gold')}"
        ],
    } 
    text = text.lower()  
    return_string = ""
    for i in range(len(text)):
        try:
            return_string += medium_text[text[i]][row] + ' '
        except KeyError:
            if row == 0:
                return f'Error: symbol/letter not implemented: {text[i]}'
            else:
                return ''
    return return_string
        
def text_print(text):
    text_speed = .01
    if type(text) == str:
        for i in range(len(text)):
            print(text[0:i+1],end='\r') 
            if '.' in text and text[i] == '.' and i != len(text)-1:
                time.sleep(.5)
            elif text[i] == '!' or text[i] == '?' and i != len(text)-1:
                time.sleep(.2)
            else:
                time.sleep(text_speed) 
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
            time.sleep(text_speed) 
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

def time_sleep(amount, test = False):
    if test:
        if amount > .1:
            time.sleep(amount/200)
    else:
        time.sleep(amount)

def console_print(_text: str, test = False):
    text_print(_text, test)
    time_sleep(1.5, test)
    go_back(1)
    print(" "*get_screensize())

def go_back(back = get_screensize(True)+4, **kwargs):
    try:
        _print = kwargs['_print']
    except KeyError:
        _print = True
    if _print:
        if isinstance(_print, int):
            screensize = _print
        else:
            screensize = get_screensize()
        whitespace = " "*screensize
        for line in range(back):
            print(whitespace, end = "")
            sys.stdout.write("\033[F")
    else:
        for line in range(back):
            sys.stdout.write("\033[F")
            
def refresh_text_on_screen(back: int = False):
    if back:
        go_back(back)
    else:
        go_back()
    time.sleep(.005)
        
def clearConsole(): 
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
    
key_cooldown = int(time.time()*1000)
    
def update_key_cooldown():
    global key_cooldown
    if int(time.time()*1000) > key_cooldown:
        key_cooldown = int(time.time()*1000) + 150
        return True
    return False
    
special_key_mapping = {
    r"(b'\x00', b'H')":'up',
    r"(b'\x00', b'P')":'down',
    r"(b'\x00', b'K')":'left',
    r"(b'\x00', b'M')":'right',
    r"(b'\r',)":'enter',
    r"(b'\x08',)":'backspace',    
    r"(b'\x00', b'S')":'delete',    
}
    
def keyboard_wait() -> str:
    try:
        while True:
            results = []
            while msvcrt.kbhit():
                result = msvcrt.getch()
                results.append(result)
            if results != []:
                break
    except Exception as e:
        raise e
    results = tuple(results)
    if (len(results) == 2 and results[0] == b'\x00') or f"{results}" in list(special_key_mapping.keys()):
        try:
            key = f"{special_key_mapping[f'{results}']}"
        except KeyError:
            key = f"{chr(ord(results[1]))}"
    else:
        key = f"{chr(ord(results[0]))}"
    return key


def get_input(input_type = str, acceptible_range: range = range(-99999, 99999)):
    while True:
        _message = ''
        try:
            _input = input('>>> ')
            try:
                _input = input_type(_input)
            except ValueError:
                assert False
            assert _input != ''
            if (input_type == str and _input != 'None') or (input_type == int and _input in acceptible_range):
                return _input
            if _input == 'None':
                _message = "You cannot enter 'None'"
                assert False
        except AssertionError:
            go_back(1)
            print(f"{_message}")
            go_back(1)
    

# class for battle output
class RollingInstanceText:
    
    def __init__(self, _text: str, _delay: int = 0):
        self.text = _text
        self.done = False
        self.started = False
        self.delay = _delay
        self.creation_instance = int(time.time()*1000)
        self.instance = 0
        self.setup_max_instance()
    
    def setup_max_instance(self):
        text_refresh_speed = 10
        self.text_dictionary = {}
        text_time_length = [(0, "")]*len(self.text)
        for i, symbol in enumerate(self.text):
            #print(self.text[0:i+1],end='\r') 
            up_to_text = self.text[0:i+1]
            if '.' in self.text and symbol == '.' and i != len(self.text)-1:
                text_time_length[i] = (int(text_time_length[i-1][0] + 500), up_to_text)
            elif symbol == '!' or symbol == '?' and i != len(self.text)-1:
                text_time_length[i] = (int(text_time_length[i-1][0] + 200), up_to_text)
            else:
                text_time_length[i] = (int(text_time_length[i-1][0] + text_refresh_speed), up_to_text) #self.settings.speed
        for i, value in enumerate(text_time_length):
            value = value[0]
            if i == 0:
                previous_value = 0
            else:
                previous_value = text_time_length[i-1][0]
            self.text_dictionary[range(previous_value, value)] = text_time_length[i][1]
                
        self.max_instance = text_time_length[-1][0] + 10
        self.end_instance = self.max_instance + int(time.time()*1000)
        
    def set_start_instance(self):
        text_refresh_speed = 10
        self.start_instance = int(time.time()*1000) - text_refresh_speed + self.delay
        
    def refresh_instance(self):
        try:
            self.instance = int(time.time()*1000) - self.start_instance
            assert self.start_instance <= int(time.time()*1000)
            self.started = True
        except AttributeError:
            self.set_start_instance()
            pass
        except AssertionError:
            pass
        return not self.started
                
    
    def __str__(self):
        result = ""
        if self.refresh_instance(): result = ""
        elif self.is_done(): result = f"{self.text}"  
        else: result = self.get_printing_string()
        self.is_done()
        return result
    
    def has_started(self):
        return self.started
        
    def get_printing_string(self):
        for i, (compare_range, return_text) in enumerate(self.text_dictionary.items()):
            if self.instance in compare_range:
                return return_text
        return f"{self.text}"
    
    def __len__(self):
        return len(self.get_printing_string())
    
    def __repr__(self):
        return self.__str__()
    
    def is_done(self):
        self.refresh_instance()
        if self.done == False and self.max_instance <= self.instance:
            self.done = True
        else:
            self.done = False
        return self.done
    
class RollingTextList:
    
    max_len = None
    
    def __init__(self):
        self.text_list: list[RollingInstanceText] = []
        self.reset_index()
        
    def __str__(self):
        return f"{self.get_started_text()}"
    
    def __repr__(self):
        return self.__str__()
    
    def __len__(self):
        return len(self.get_started_text())
    
    def __iter__(self):
        return self.get_started_text().__iter__()
    
    def get_started_text(self):
        return [text for text in self.text_list if text.has_started()]
    
    def set_max_len(self, max_len: int):
        RollingTextList.max_len = max_len
    
    def get_max_len(self):
        return RollingTextList.max_len
    
    def all_done(self):
        for text in self.text_list:
            if not text.is_done():
                return False
        return True
        
    def append(self, text: RollingInstanceText, delay: int = False):
        if isinstance(text, str):
            if delay == True:
                text_refresh_speed = 1500
                delay = self.text_list[-1].end_instance + text_refresh_speed
            if isinstance(delay, float):
                delay = int(delay)
            elif not delay and not isinstance(delay, int):
                delay = 0
            text = RollingInstanceText(text, delay)
        assert isinstance(text, RollingInstanceText), ValueError("Expected 'text' type to be 'RollingInstanceText' or 'str'")
        self.text_list.append(text)
        self.cut_down_len()
        
    def pop(self, index: int):
        return self.text_list.pop(index)
        
    def cut_down_len(self):
        while len(self) > self.get_max_len(): 
            self.text_list.pop(0)
            self.index -= 1
            
    def reset_index(self):
        self.index = 0
            
    def get_next_text(self):
        self.cut_down_len()
        text = self.text_list[self.index]
        self.index += 1
        self.text_list.__str__()
        return text
    
    def can_continue(self) -> bool:
        return self.index < len(self)
    
    
if __name__ == '__main__':
    clearConsole()
    original_text = 'this is a test to see how... yes how... how well this works i guess lmao!!!?!?!?!??!!'
    new_text_list = [
    "Player Stats:", 
    "Attack: 21098793021", 
    "Defence: 120988034715",
    "Speed: 9874562w0gvwqsrfu",
    "Affinity: liugugr4wh",
    "Mana: iuhftwopiwqbuigvjleaq",
    "HEALTH: uyhekbjgv",
    ]
    text_list = RollingTextList()
    text_list.set_max_len(5)
    delay = 0
    for i in range(len(new_text_list)):
        text_list.append(new_text_list[i], delay)
        delay += 1500
    while True:
        print(text_list)
        for i in range(len(text_list)):
            print(text_list.get_next_text())
        text_list.reset_index()
        time.sleep(.005)
        if text_list.all_done():
            time.sleep(1)
            print('all done')
            exit()
        go_back(text_list.get_max_len())
        