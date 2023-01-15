import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # list of button names, keys bound to them, function names
        # for loop
        self.root = root
        self.root.title("undefined")
        width = 300
        height = 300
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        self.button = []

    def buttons(self):
        common_config = {
            "bg": "#e9e9ed",
            "font": tkFont.Font(family="Segoe UI", size=12),
            "fg": "#000000",
            "justify": "center",
        }

        specific_configs = [
            {
                "text": "1",
                "command": self.say_shit(),
            },
            {
                "text": "2",
                "command": self.button_command()
            }
        ]

        list_of_button_configs = [common_config + specific_config for specific_config in specific_configs]
        for idx, btn_cnf in enumerate(list_of_button_configs, start=1):
            self.button.append(tk.Button(cnf=btn_cnf))
            x, y, width, height = btn_cnf.get("position")
            self.button[-1].place(x=x, y=y, width=width, height=height)
            self.root.bind(btn_cnf.get("text"), lambda event: btn_cnf.get("command"))

    def define_button(self, btn_cnf):
        btn_cnf = common_config + specific_config
        position_dict

        self.button = tk.Button(self.root)
        self.button["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Segoe UI', size=12)
        self.button["font"] = ft
        self.button["fg"] = "#000000"
        self.button["justify"] = "center"
        self.button["text"] = "Button"
        self.button.place(x=10, y=40, width=70, height=25)
        self.button["command"] = self.button_command
        self.bindings()

        label = tk.Label(self.root)
        ft = tkFont.Font(family='Segoe UI', size=12)
        label["font"] = ft
        label["fg"] = "#333333"
        label["justify"] = "center"
        label["text"] = "label"
        label.place(x=10, y=10, width=70, height=25)

    def bindings(self):
        self.root.bind("1", lambda event: self.button_command())


    def button_command(self):
        print("command")

    def say_shit(self):
        print("shit")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
