
import customtkinter as ctk

class Menu(ctk.CTkFrame):
    def __init__(self, master, frame_switch):
        """
        Parameters
        -----
        frame_switch: function that switches between frames (screens)
        """
        self.master = master

        super().__init__(self.master)

        font = ("Helvetica", 24)

        title = ctk.CTkLabel(self, text="Menu", font=("Helvetica", 48))
        title.pack(pady=10)

        label = ctk.CTkLabel(self, text="Choose game mode.", font=font)
        label.pack(pady=10)

        five_btn = ctk.CTkButton(self, text="5 on 5", font=font, command=lambda: frame_switch("game", 5))
        five_btn.pack(pady=10)

        # Help
        help_btn = ctk.CTkButton(self, text="Help", font=font, command=lambda: frame_switch("help"))
        help_btn.pack(pady=10)

        # Quit
        quit_btn = ctk.CTkButton(self, text="Quit", font=font, command=self.quit_game)
        quit_btn.pack(pady=10)


    def quit_game(self):
        self.master.destroy()