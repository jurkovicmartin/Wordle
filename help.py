
import customtkinter as ctk

class Help(ctk.CTkFrame):
    def __init__(self, master, frame_switch):
        """
        Parameters
        -----
        frame_switch: function that switches between frames (screens)
        """
        super().__init__(master)

        title_font = ("Helvetica", 36)
        font = ("Helvetica", 24)

        title = title = ctk.CTkLabel(self, text="Help", font=("Helvetica", 48))
        title.pack(pady=10)

        frame = ctk.CTkScrollableFrame(self)
        frame.pack(pady=10, expand=True, fill="both")

        # How to play
        rules_title = ctk.CTkLabel(frame, text="How to play", font=title_font)
        rules_title.pack(pady=10)

        rules = """
        Worde is a word guessing game.\n
        You have to guess the word in a certain number of attempts. The words are nouns.\n
        You need to type your guest and submit it by hitting "ENTER".\n
        Letters that will color gray are not used in the guessing word.\n
        Letters that will color yellow are used in the guessing word but at different position.\n
        Letters that will color green are correct.
        """
        rules_text = ctk.CTkLabel(frame, text=rules, font=font)
        rules_text.pack(pady=10)

        menu_btn = ctk.CTkButton(self, text="Menu", font=font, command=lambda: frame_switch("menu"))
        menu_btn.pack(pady=10)