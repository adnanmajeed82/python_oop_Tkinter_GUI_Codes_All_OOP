import tkinter as tk
from tkinter import messagebox

class BankAccountOpeningGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Bank Account Opening")
        self.master.geometry("400x300")

        self.label_name = tk.Label(self.master, text="Name:")
        self.label_name.pack(pady=10)

        self.entry_name = tk.Entry(self.master)
        self.entry_name.pack(pady=10)

        self.label_balance = tk.Label(self.master, text="Initial Balance:")
        self.label_balance.pack(pady=10)

        self.entry_balance = tk.Entry(self.master)
        self.entry_balance.pack(pady=10)

        self.button_open_account = tk.Button(self.master, text="Open Account", command=self.open_account)
        self.button_open_account.pack(pady=20)

    def open_account(self):
        name = self.entry_name.get()
        balance = self.entry_balance.get()

        if not name or not balance:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            balance = float(balance)
        except ValueError:
            messagebox.showerror("Error", "Invalid balance. Please enter a valid number.")
            return

        # In a real application, you would save this information to a database or a file.
        # For simplicity, we'll just print the details.
        print(f"Account opened for {name} with initial balance ${balance:.2f}")
        messagebox.showinfo("Success", "Account opened successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankAccountOpeningGUI(root)
    root.mainloop()
