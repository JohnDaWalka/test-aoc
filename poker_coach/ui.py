import tkinter as tk
from tkinter import messagebox

class PokerCoachUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Poker Coach")

        self.create_widgets()

    def create_widgets(self):
        self.hand_label = tk.Label(self.root, text="Enter your hand:")
        self.hand_label.pack()

        self.hand_entry = tk.Entry(self.root)
        self.hand_entry.pack()

        self.analyze_button = tk.Button(self.root, text="Analyze Hand", command=self.analyze_hand)
        self.analyze_button.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def analyze_hand(self):
        hand = self.hand_entry.get()
        if not hand:
            messagebox.showerror("Error", "Please enter a hand.")
            return

        # Placeholder for hand analysis logic
        result = f"Analysis result for hand: {hand}"

        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = PokerCoachUI(root)
    root.mainloop()
