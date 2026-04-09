#==============================#
#                              #
#            Färger            #
#                              #
#==============================#
# Oscar Hellgren Te23A Ebersteinska Gy

# Ansi color generator handler
# 
class Colors:
    def __init__(self):
        self.colors = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
        self.styles = ["end", "bold", "dim", "italic", "underline", "blink", "blink_fast", "reverse", "hidden", "striketrough"]

        self._generate_standard()


    def _generate_standard(self, mode: int = 1): # REKURSIV AUGHHH
        match mode:
            case 1:
                names = self.colors
                offset = 30

            case 2:
                names = []
                name: str
                for name in self.colors:
                    NAME = name.capitalize()
                    print(NAME)
                    names.append(NAME)
                offset = 90

            case 3:
                names = self.styles
                offset = 0
        
        for name in names:
            index = names.index(name) + offset
            str_index = str(index)
            ansi = "\033[" + str_index + "m"
            setattr(self, name, ansi)

        if mode == 3:
            return

        return self._generate_standard(mode + 1)


    def rgb(self, r:int, g:int , b:int, save: bool = False, name: str = ""):
        ansi_code = f"\033[38;2;{r};{g};{b}m"
        if save:
            setattr(self, name, ansi_code)

        return ansi_code