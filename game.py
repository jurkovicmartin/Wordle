
import customtkinter as ctk
from tkinter import messagebox as msg

class Game(ctk.CTkFrame):
    def __init__(self, master, frame_switch, mode: int):
        """
        Parameters
        -----
        frame_switch: function that switches between frames (screens)

        mode: number of letters/attempts
        """
        self.master = master
        self.mode = mode
        self.guesses = 0
        
        self.guess_word = list("MOUSE")

        super().__init__(self.master)

        CELL_SIZE = 50

        self.GREEN = "#2CC985"

        game_frame = ctk.CTkFrame(self, border_color=self.GREEN, border_width=2, corner_radius=20)
        game_frame.pack()
        input_frame = ctk.CTkFrame(self, border_color=self.GREEN, border_width=2, corner_radius=20)
        input_frame.pack(pady=(10, 0))

        letter_font = ("Helvetica", 36)

        # Create matrix for letters and shown the matrix with labels
        self.guess_labels = []
        # Creating two dimensional matrix
        for row in range(mode):
            row_labels = []
            for col in range(mode):
                # Using frame to create a border around each letter
                frame=ctk.CTkFrame(game_frame, width=CELL_SIZE, height=CELL_SIZE, border_color="white", border_width=2, corner_radius=10)
                frame.grid(row=row, column=col, padx=5, pady=10)

                label = ctk.CTkLabel(frame, text="", font=letter_font)
                label.place(relx=0.5, rely=0.5, anchor="center")

                row_labels.append(label)
            self.guess_labels.append(row_labels)


        # Input slots
        self.input_labels = []
        for i in range(mode):
            # Using frame to create a border around each letter
            frame=ctk.CTkFrame(input_frame, width=CELL_SIZE, height=CELL_SIZE, border_color="white", border_width=2, corner_radius=10)
            frame.grid(row=0, column=i, padx=5, pady=10)

            label = ctk.CTkLabel(frame, text="", font=letter_font)
            label.place(relx=0.5, rely=0.5, anchor="center")

            self.input_labels.append(label)


        menu_btn = ctk.CTkButton(self, text="Menu", font=("Helvetica", 24), command=lambda: frame_switch("menu"))
        menu_btn.pack(pady=10)


        self.master.bind("<KeyPress>", self.key_press)




    def key_press(self, event):
        alphabet = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

        if event.keysym in alphabet:
            self.write_input_letter(event.keysym)
        elif event.keysym == "BackSpace":
            self.delete_input_letter()
        # Enter
        elif event.keysym == "Return":
            self.submit_guess()
        # Other keys
        else:
            pass


    def write_input_letter(self, letter: str):
        """
        Writes input letter to one of the input cells.
        """
        for i in range(self.mode):
            # Find an empty cell
            if not self.input_labels[i].cget("text"):
                empty_cell = self.input_labels[i]
                break
            else:
                empty_cell = None
        
        # There is an empty cell
        if empty_cell is not None:
            # Show the letter (capital)
            empty_cell.configure(text=letter.capitalize())


    def delete_input_letter(self):
        """
        Deletes last input letter and empty its cell.
        """
        # Reverse loop to find last full cell
        for i in range(self.mode - 1, -1, -1):
            if self.input_labels[i].cget("text"):
                self.input_labels[i].configure(text="")
                break


    def submit_guess(self):
        """
        Try to submit the word guess.
        """
        # Check if all input cells are full
        for i in range(self.mode):
            # One cell is empty => do nothing
            if not self.input_labels[i].cget("text"):
                return
        
        self.show_guess()


    def show_guess(self):
        """
        Show input word between guesses. Also checks and colors it and checks for game over.
        """
        # Last guess
        if self.guesses == self.mode:
            self.last_guess()
        else:
            # Check for win
            guess = [self.input_labels[i].cget("text") for i in range(self.mode)]
            if guess == self.guess_word:
                win = True
            else:
                win = False


            # Guesses specify rows in guess labels matrix
            # Rewrite correct letters (green)
            for i in range(self.mode):
                # Get the letter from the input cell
                letter = self.input_labels[i].cget("text")

                if win:
                    self.input_labels[i].configure(text=letter, text_color=self.GREEN)
                    # Last cycle
                    if i == self.mode - 1:
                        word_str = "".join(self.guess_word)           
                        msg.showinfo("You win", f"You win. The word is {word_str}")
                        self.master.unbind("<KeyPress>")
                        return
                else:
                    if self.guess_word[i] == letter:
                        self.guess_labels[self.guesses][i].configure(text=letter, text_color=self.GREEN)
                    else:
                        pass

            # Rewrite other letters (yellow and gray)
            for i in range (self.mode):
                # Get the letter from the input cell
                letter = self.input_labels[i].cget("text")

                # Get already written letters
                written = [self.guess_labels[self.guesses][j].cget("text") for j in range(self.mode)]
                # Number of actual letter already written
                num_written = written.count(letter)
                # Number of actual letter in the original guess word
                num_guess = self.guess_word.count(letter)

                # Letter is in the word
                if letter in self.guess_word:
                    # Letter is at different position
                    if num_written < num_guess:
                        self.guess_labels[self.guesses][i].configure(text=letter, text_color="yellow")
                    # Don't overwrite the correct one
                    elif self.guess_word[i] == letter:
                        pass
                    else:
                        self.guess_labels[self.guesses][i].configure(text=letter, text_color="gray")
                # Other letters
                else:
                    self.guess_labels[self.guesses][i].configure(text=letter, text_color="gray")

                # Clear the input field
                self.input_labels[i].configure(text="")

            self.guesses += 1


    def last_guess(self):
        """
        Handles the last guess in the input field.
        """
        guess = [self.input_labels[i].cget("text") for i in range(self.mode)]

        # Clear the input field
        for i in range(self.mode):
            self.input_labels[i].configure(text="")
        

        if guess == self.guess_word:
            # Rewrite the input in green (win)
            for i in range(self.mode):
                # Get the letter from the input cell
                letter = guess[i]

                self.input_labels[i].configure(text=letter, text_color=self.GREEN)
                # Last cycle
                if i == self.mode - 1:   
                    word_str = "".join(self.guess_word)        
                    msg.showinfo("You win", f"You win. The word is {word_str}")
                    self.master.unbind("<KeyPress>")

        # Color the input field and show game over.
        else:
            # Rewrite correct letters (green)
            for i in range(self.mode):
                # Get the letter from the input cell
                letter = guess[i]

                if self.guess_word[i] == letter:
                    self.self.input_labels[i].configure(text=letter, text_color=self.GREEN)
                else:
                    pass

            # Rewrite other letters (yellow and gray)
            for i in range (self.mode):
                # Get the letter from the input cell
                letter = guess[i]

                # Get already written letters
                written = [self.input_labels[j].cget("text") for j in range(self.mode)]
                # Number of actual letter already written
                num_written = written.count(letter)
                # Number of actual letter in the original guess word
                num_guess = self.guess_word.count(letter)

                # Letter is in the word
                if letter in self.guess_word:
                    # Letter is at different position
                    if num_written < num_guess:
                        self.input_labels[i].configure(text=letter, text_color="yellow")
                    # Don't overwrite the correct one
                    elif self.guess_word[i] == letter:
                        pass
                    else:
                        self.input_labels[i].configure(text=letter, text_color="gray")
                # Other letters
                else:
                    self.input_labels[i].configure(text=letter, text_color="gray")

            word_str = "".join(self.guess_word)
            msg.showinfo("You lose", f"You lose. Word to guess was: {word_str}.")
            self.master.unbind("<KeyPress>")

