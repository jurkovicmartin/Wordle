
from typing import Any, Tuple
import customtkinter as ctk

class Help(ctk.CTkFrame):
    def __init__(self, master, frame_switch):
        """
        Parameters
        -----
        frame_switch: function that switches between frames (screens)
        """
        super().__init__(master)

        font = ("Helvetica", 24)

        title = title = ctk.CTkLabel(self, text="Help", font=("Helvetica", 48))
        title.pack(pady=10)

        menu_btn = ctk.CTkButton(self, text="Menu", font=font, command=lambda: frame_switch("menu"))
        menu_btn.pack(pady=10)