
import customtkinter as ctk

class Menu(ctk.CTkFrame):
    def __init__(self, master, frame_switch, language: str = "English"):
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

        # Language
        language_label = ctk.CTkLabel(self, text="Choose game language.", font=font)
        language_label.pack(pady=10)

        language_box = ctk.CTkComboBox(self, values=["English", "Czech"], font=font)
        language_box.set(language)
        language_box.configure(state="readonly")
        language_box.pack(pady=10)

        # Game mode
        mode_label = ctk.CTkLabel(self, text="Choose game mode.", font=font)
        mode_label.pack(pady=10)

        # Game mode buttons
        buttons_frame = ctk.CTkFrame(self, bg_color="transparent")
        buttons_frame.pack(pady=10)

        four_btn = ctk.CTkButton(buttons_frame, text="4 letters", font=font, command=lambda: frame_switch("game", 4, language_box.get()))
        four_btn.grid(row=0, column=0, padx=10, pady=10)
        five_btn = ctk.CTkButton(buttons_frame, text="5 letters", font=font, command=lambda: frame_switch("game", 5, language_box.get()))
        five_btn.grid(row=0, column=1, padx=10, pady=10)
        six_btn = ctk.CTkButton(buttons_frame, text="6 letters", font=font, command=lambda: frame_switch("game", 6, language_box.get()))
        six_btn.grid(row=1, column=0, padx=10, pady=10)
        seven_btn = ctk.CTkButton(buttons_frame, text="7 letters", font=font, command=lambda: frame_switch("game", 7, language_box.get()))
        seven_btn.grid(row=1, column=1, padx=10, pady=10)
        eight_btn = ctk.CTkButton(buttons_frame, text="8 letters", font=font, command=lambda: frame_switch("game", 8, language_box.get()))
        eight_btn.grid(row=2, column=0, padx=10, pady=10)
        nine_btn = ctk.CTkButton(buttons_frame, text="9 letters", font=font, command=lambda: frame_switch("game", 9, language_box.get()))
        nine_btn.grid(row=2, column=1, padx=10, pady=10)

        # Help
        help_btn = ctk.CTkButton(self, text="Help", font=font, command=lambda: frame_switch("help"))
        help_btn.pack(pady=(20,10))

        # Quit
        quit_btn = ctk.CTkButton(self, text="Quit", font=font, command=self.quit_game)
        quit_btn.pack(pady=10)


    def quit_game(self):
        self.master.destroy()