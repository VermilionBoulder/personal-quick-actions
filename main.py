import tkinter as tk
import tkinter.font as tk_font
import onelab_hardware_details


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("undefined")
        self.root.resizable(width=False, height=False)
        self.buttons = []
        self.labels = []
        self.root.bind('<Escape>', lambda e: self.root.destroy())

        # config shared by all buttons & labels
        self.common_config = {
            "button": {
                "bg": "#e9e9ed",
                "font": tk_font.Font(family="Segoe UI", size=12),
                "fg": "#000000",
                "justify": "center",
            },
            "label": {
                "font": tk_font.Font(family="Segoe UI", size=12),
                "fg": "#333333",
                "justify": "left",
            },
        }

        # list of button names, keys bound to them, function names
        self.specific_configs = [
            {
                "text": "1",
                "label": "say shit",
                "command": self.say_shit,
                "exit": True,
            },
            {
                "text": "a",
                "label": "button command",
                "command": self.button_command,
            },
            {
                "text": "Z",
                "label": "say boobs",
                "command": self.say_boobs,
            },
            {
                "text": "o",
                "label": "Open OneLab page for copied Hardware IDs",
                "command": onelab_hardware_details.open_onelab_pages,
            },
        ]

        width = 300
        height = 20 + 40 * len(self.specific_configs)
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.define_options()

    def define_options(self):
        # For every button defined in {self.specific_configs} above, add a button and label pair
        for idx, config in enumerate(self.specific_configs):
            new_button = tk.Button(self.root, cnf=self.common_config.get("button"), text=config.get("text"),
                                   command=config.get("command"))
            new_button.place(x=10, y=10 + 40 * idx, width=30, height=30)
            self.buttons.append(new_button)

            new_label = tk.Label(self.root, cnf=self.common_config.get("label"), text=config.get("label"))
            new_label.place(x=45, y=10 + 40 * idx, width=200, height=30)
            self.labels.append(new_label)

            self.add_binding(config)

        # for binding in self.specific_configs:
        #     self.add_binding(binding)

    def add_binding(self, binding):
        # self.root.bind(f"<KeyPress-{binding.get('text')}>", binding.get("command"))
        self.root.bind(
            sequence=f"<KeyPress-{binding.get('text')}>",
            func=(lambda event: f"{binding.get('command')()}"),
            add=True
        )

    # def bindings(self):
    #     self.root.bind("1", lambda event: self.button_command())

    def button_command(self):
        print("command")

    def say_shit(self):
        print("shit")

    def say_boobs(self):
        print("boobs")


if __name__ == "__main__":
    tk_root = tk.Tk()
    app = App(tk_root)
    tk_root.mainloop()
