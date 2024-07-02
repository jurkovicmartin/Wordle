
import customtkinter as ctk

from menu import Menu
from game import Game
from help import Help

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_default_color_theme("green")
        
        self.geometry("1000x600")
        self.title("Wordle game")


        self.screen = Menu(self, self.switch_frame)
        self.screen.pack()


    def switch_frame(self, display: str, mode: int = None):
        """
        Switching between game screens (frames).

        Parameters
        -----
        display: screen to display (menu / game / help)

        mode: number of letters in a word
        """
        # Hide original screen
        self.screen.destroy()

        if display == "menu":
            self.screen = Menu(self, self.switch_frame)
        elif display == "game":
            self.screen = Game(self, self.switch_frame, mode)
        elif display == "help":
            self.screen = Help(self, self.switch_frame)
        else:
            raise Exception("Unexpected error")
        
        # Show new screen
        self.screen.pack()



if __name__ == "__main__":
    app = App()
    app.mainloop()