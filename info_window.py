
import customtkinter as ctk

class Info(ctk.CTkToplevel):
    def __init__(self, master, state: str, word: str):
        """
        Window to show game over.

        Parameters
        -----
        state: win / lose
        """
        super().__init__(master)

        self.geometry("450x100")
        self.title("Game over")
        # Focus the new window
        self.after(100, self.lift)

        # Message label
        label = ctk.CTkLabel(self, text="", font=("Helvetica", 24))
        label.pack(padx=10, pady=10)

        # Define the message
        if state == "win":
            label.configure(text=f"You win. The word is {word}")
        elif state == "lose":
            label.configure(text=f"You lose. The word is {word}")
        else:
            raise Exception("Unexpected error")


