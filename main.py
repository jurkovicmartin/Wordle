
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
        self.screen.pack(expand=True, fill="both")


    def switch_frame(self, display: str, mode: int = 5, language: str = "English"):
        """
        Switching between game screens (frames).

        Parameters
        -----
        display: screen to display (menu / game / help)

        mode: number of letters in a word
        """
        # Hide original screen
        self.screen.destroy()

        # Close all TopLevel windows (game over windows)
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkToplevel):
                widget.destroy()

        if display == "menu":
            self.screen = Menu(self, self.switch_frame, language=language)
        elif display == "game":
            self.screen = Game(self, self.switch_frame, mode, language)
        elif display == "help":
            self.screen = Help(self, self.switch_frame)
        else:
            raise Exception("Unexpected error")
        
        # Show new screen
        self.screen.pack(expand=True, fill="both")



if __name__ == "__main__":
    app = App()
    app.mainloop()