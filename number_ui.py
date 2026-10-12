import random
import tkinter as tk
from tkinter import messagebox


class GuessingGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#0f172a")

        self.secret_number = random.randint(1, 100)
        self.tries = 0

        self.main_frame = tk.Frame(root, bg="#0f172a", padx=50, pady=40)
        self.main_frame.pack(fill="both", expand=True)

        self.card = tk.Frame(
            self.main_frame,
            bg="#111827",
            bd=0,
            padx=36,
            pady=32,
            highlightthickness=2,
            highlightbackground="#38bdf8",
        )
        self.card.pack(expand=True)

        self.title = tk.Label(
            self.card,
            text="🎯 Number Guessing Game",
            font=("Arial", 36, "bold"),
            fg="#f8fafc",
            bg="#111827",
            pady=10,
        )
        self.title.pack()

        self.subtitle = tk.Label(
            self.card,
            text="Guess the secret number between 1 and 100",
            font=("Arial", 16),
            fg="#cbd5e1",
            bg="#111827",
        )
        self.subtitle.pack(pady=(0, 24))

        self.input_frame = tk.Frame(self.card, bg="#111827")
        self.input_frame.pack(pady=12)

        self.input_field = tk.Entry(
            self.input_frame,
            width=16,
            font=("Arial", 28, "bold"),
            justify="center",
            bd=0,
            relief="flat",
            bg="#e2e8f0",
            fg="#0f172a",
        )
        self.input_field.pack(side="left", padx=(0, 16), ipadx=8, ipady=10)
        self.input_field.focus()
        self.input_field.bind("<Return>", lambda event: self.check_guess())

        self.submit_button = tk.Button(
            self.input_frame,
            text="Guess",
            width=14,
            height=2,
            bg="#22c55e",
            fg="white",
            font=("Arial", 16, "bold"),
            bd=0,
            cursor="hand2",
            command=self.check_guess,
        )
        self.submit_button.pack(side="left")

        self.status_label = tk.Label(
            self.card,
            text="Enter a number and start guessing!",
            font=("Arial", 16, "bold"),
            fg="#e2e8f0",
            bg="#1e293b",
            wraplength=600,
            justify="center",
            pady=20,
            padx=18,
            bd=0,
        )
        self.status_label.pack(fill="x", pady=(20, 12))

        self.attempts_label = tk.Label(
            self.card,
            text="Attempts: 0",
            font=("Arial", 18),
            fg="#f8fafc",
            bg="#111827",
            pady=10,
        )
        self.attempts_label.pack()

        self.reset_button = tk.Button(
            self.card,
            text="New Game",
            width=18,
            height=2,
            bg="#38bdf8",
            fg="#082f49",
            font=("Arial", 15, "bold"),
            bd=0,
            cursor="hand2",
            command=self.reset_game,
        )
        self.reset_button.pack(pady=(18, 0))

    def check_guess(self):
        try:
            guess = int(self.input_field.get())
        except ValueError:
            self.status_label.config(
                text="Please enter a valid number.",
                bg="#fff1f2",
                fg="#b91c1c",
            )
            self.input_field.delete(0, tk.END)
            return

        if guess < 1 or guess > 100:
            self.status_label.config(
                text="Number must be between 1 and 100.",
                bg="#fff1f2",
                fg="#b91c1c",
            )
            self.input_field.delete(0, tk.END)
            return

        self.tries += 1
        self.attempts_label.config(text=f"Attempts: {self.tries}")

        if guess == self.secret_number:
            self.status_label.config(
                text=f"Congratulations! You won in {self.tries} tries!",
                bg="#ecfdf5",
                fg="#166534",
            )
            self.input_field.delete(0, tk.END)
            self.input_field.config(state="disabled")
            self.submit_button.config(state="disabled")
            messagebox.showinfo("You Won!", f"You guessed the number in {self.tries} tries.")
        elif guess < self.secret_number:
            self.status_label.config(
                text="Too low! Try a higher number.",
                bg="#eff6ff",
                fg="#1d4ed8",
            )
            self.input_field.delete(0, tk.END)
        else:
            self.status_label.config(
                text="Too high! Try a lower number.",
                bg="#fff7ed",
                fg="#c2410c",
            )
            self.input_field.delete(0, tk.END)

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.tries = 0
        self.attempts_label.config(text="Attempts: 0")
        self.status_label.config(
            text="Enter a number and start guessing!",
            bg="#eef4ff",
            fg="#1f2937",
        )
        self.input_field.config(state="normal")
        self.submit_button.config(state="normal")
        self.input_field.delete(0, tk.END)
        self.input_field.focus()


if __name__ == "__main__":
    root = tk.Tk()
    app = GuessingGameApp(root)
    root.mainloop()
