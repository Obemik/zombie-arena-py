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
            elif key == "e":
                return "e"
            elif key == "p":
                return "p"
            elif key == "q":
                return "q"
            elif key == "up":
                return "up"
            elif key == "down":
                return "down"
            elif key == "e":
                return "enter"
            else:
                return None
        except:
            return None