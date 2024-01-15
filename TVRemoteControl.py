import tkinter as tk

class TelevisionRemote:
    def __init__(self, master):
        self.master = master
        self.master.title("TV Remote Control")

        self.tv_state = tk.StringVar()
        self.tv_state.set("Off")

        self.create_widgets()

    def create_widgets(self):
        # TV State Label
        state_label = tk.Label(self.master, text="TV State:")
        state_label.grid(row=0, column=0, padx=10, pady=10)

        state_value_label = tk.Label(self.master, textvariable=self.tv_state)
        state_value_label.grid(row=0, column=1, padx=10, pady=10)

        # Power Button
        power_button = tk.Button(self.master, text="Power", command=self.toggle_power)
        power_button.grid(row=1, column=0, padx=10, pady=10, columnspan=2)

        # Volume Buttons
        volume_up_button = tk.Button(self.master, text="Volume Up", command=self.volume_up)
        volume_up_button.grid(row=2, column=0, padx=10, pady=10)

        volume_down_button = tk.Button(self.master, text="Volume Down", command=self.volume_down)
        volume_down_button.grid(row=2, column=1, padx=10, pady=10)

        # Channel Buttons
        next_channel_button = tk.Button(self.master, text="Next Channel", command=self.next_channel)
        next_channel_button.grid(row=3, column=0, padx=10, pady=10)

        prev_channel_button = tk.Button(self.master, text="Prev Channel", command=self.prev_channel)
        prev_channel_button.grid(row=3, column=1, padx=10, pady=10)

    def toggle_power(self):
        current_state = self.tv_state.get()
        new_state = "On" if current_state == "Off" else "Off"
        self.tv_state.set(new_state)

    def volume_up(self):
        print("Volume Up")

    def volume_down(self):
        print("Volume Down")

    def next_channel(self):
        print("Next Channel")

    def prev_channel(self):
        print("Previous Channel")

if __name__ == "__main__":
    root = tk.Tk()
    remote = TelevisionRemote(root)
    root.mainloop()
