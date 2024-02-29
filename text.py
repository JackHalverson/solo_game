import time

class text_speed():
    def print_normal(text, delay=0.1):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
    
    def print_slow(text, delay=.3):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

class text_color():
    def red(text):
        return "\033[91m{}\033[00m".format(text)
    def green(text):
        return "\033[92m{}\033[00m".format(text)
    def yellow(text):
        return "\033[93m{}\033[00m".format(text)
    def blue(text):
        return "\033[94m{}\033[00m".format(text)
    def purple(text):
        return "\033[95m{}\033[00m".format(text)
    def cyan(text):
        return "\033[96m{}\033[00m".format(text)

class text_effects():
    def bold(text, delay=0.1):
        return "\033[1m{}\033[00m".format(text)
    def italic(text, delay=0.1):
        return "\033[3m{}\033[00m".format(text)


