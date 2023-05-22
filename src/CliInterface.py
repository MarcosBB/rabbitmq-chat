from blessed import Terminal

class CliInterface:
    def __init__(self) -> None:
        self.__term = Terminal()
        self.cli_list = []

    def __print_screen(self, msg, input, cursor_pos):
        line = 0
        title = "|    Python Chat - (RabbitMQ)    |"
        with self.__term.location(0, line):
            print(title)
            line += 1
        with self.__term.location(0, line):
            print("-" * len(title))
            line += 1
        for str_line in self.cli_list:
            with self.__term.location(0, line):
                print(f"{str_line:70}")
                line += 1
        with self.__term.location(0, line):
            print("-" * len(title))
            line += 1

        with self.__term.location(0, line):
            f_input = input + " "
            f_input = f_input[:cursor_pos] + self.__term.reverse(f_input[cursor_pos]) + input[(cursor_pos+1):]
            print(f"{msg}: {f_input:}   ")

    def start_input(self, mode_args:dict):
        with self.__term.fullscreen(), self.__term.hidden_cursor():
            while mode_args['mode'] != 'end':
                text = ''
                cursor_pos = 0
                while True:
                    mode_args[mode_args['mode']]['update'](self.cli_list)

                    self.__print_screen(mode_args[mode_args['mode']]['prompt'], text, cursor_pos)

                    with self.__term.cbreak():
                        key = self.__term.inkey(timeout=1)

                    if key == '\n':
                        break
                    elif key == '':
                        continue
                    elif key.isprintable():
                        text = text[:cursor_pos] + key + text[cursor_pos:]
                        cursor_pos += 1
                    elif key.code == self.__term.KEY_BACKSPACE:
                        if cursor_pos > 0:
                            text = text[:cursor_pos-1] + text[cursor_pos:]
                            cursor_pos -= 1
                    elif key.code == self.__term.KEY_DELETE:
                        if cursor_pos < len(text) and len(text) > 0:
                            text = text[:cursor_pos] + text[cursor_pos+1:]
                    elif key.code == self.__term.KEY_LEFT:
                        if cursor_pos > 0:
                            cursor_pos -= 1
                    elif key.code == self.__term.KEY_RIGHT:
                        if cursor_pos < len(text):
                            cursor_pos += 1
                mode_args[mode_args['mode']]['send'](text)
                print(self.__term.clear())
