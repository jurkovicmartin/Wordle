
import customtkinter as ctk

class Game(ctk.CTkFrame):
    def __init__(self, master, frame_switch, mode: int):
        """
        Parameters
        -----
        frame_switch: function that switches between frames (screens)

        mode: number of letters/attempts
        """
        self.mode = mode
        self.guesses = 0

        super().__init__(master)

        CELL_SIZE = 50

        game_frame = ctk.CTkFrame(self, border_color="#2CC985", border_width=2, corner_radius=20)
        game_frame.pack()
        input_frame = ctk.CTkFrame(self, border_color="#2CC985", border_width=2, corner_radius=20)
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


        master.bind("<KeyPress>", self.key_press)




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
        
        # Check if all input cells are full
        for i in range(self.mode):
            # One cell is empty => do nothing
            if not self.input_labels[i].cget("text"):
                return
        
        # Maximum number of guesses
        if self.guesses == self.mode:
            return
            
        # Rewrite the word from the input to the guesses
        for i in range(self.mode):
            # Get the letter from the input
            letter = self.input_labels[i].cget("text")
            # Empty the input cell
            self.input_labels[i].configure(text="")
            # Guesses specify row in the guess labels matrix
            self.guess_labels[self.guesses][i].configure(text=letter)

        self.guesses += 1

            
        
