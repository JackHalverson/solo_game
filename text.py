import time

class text_speed():
    def print_normal(text: str, delay=0.05):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def print_slow(text, delay=.2):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

class text_color():
    def red(text: str):
        return "\033[91m{}\033[00m".format(text)
    def green(text: str):
        return "\033[92m{}\033[00m".format(text)
    def yellow(text: str):
        return "\033[93m{}\033[00m".format(text)
    def blue(text: str):
        return "\033[94m{}\033[00m".format(text)
    def purple(text: str):
        return "\033[95m{}\033[00m".format(text)
    def cyan(text: str):
        return "\033[96m{}\033[00m".format(text)
    def white(text: str):
        return "\033[97m{}\033[00m".format(text)

class text_effects():
    def bold(text, delay=0.1):
        return "\033[1m{}\033[00m".format(text)
    def italic(text, delay=0.1):
        return "\033[3m{}\033[00m".format(text)


