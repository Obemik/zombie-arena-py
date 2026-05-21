class InputHandler:
    def get_key(self):
        try:
            key = input()
            if key == "w":
                return "up"
            elif key == "s":
                return "down"
            elif key == "a":
                return "left"
            elif key == "d":
                return "right"
            elif key == "":
                return "space"
            elif key == "p":
                return "p"
            elif key == "q":
                return "q"
            elif key == "e":
                return "enter"
            else:
                return None
        except:
            return None