import time
import tkinter as tk
import tkinter.font as tk_font

from modules import *


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Quick Actions")
        self.root.resizable(width=False, height=False)
        self.buttons = []
        self.labels = []
        self.root.bind('<Escape>', lambda e: self.root.destroy())

        self.button_and_label_common_config = {
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

        # list of button names, keys bound to them, function they launch
        self.specific_configs = [
            {
                "text": "v",
                "label": "Format VLANs for VLAN ticket",
                "command": vlan_formatter.format_vlan_text,
                "exit": True,
            },
            {
                "text": "y",
                "label": "Download YouTube video from copied link",
                "command": youtube_downloader.download_video,
                "exit": True,
            },
            {
                "text": "a",
                "label": "Take text from clipboard and make it aLtCaPs",
                "command": alt_caps.alt_caps,
                "exit": True,
            },
            {
                "text": "o",
                "label": "Open OneLab page for copied Hardware IDs",
                "command": onelab_hardware_details.open_onelab_pages,
                "exit": True,
            },
        ]

        width = 380
        height = 20 + 40 * len(self.specific_configs)
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(align_str)
        self.define_options()

    def define_options(self):
        # For every button defined in self.specific_configs above, add a button and label pair
        for idx, config in enumerate(self.specific_configs):
            new_button = tk.Button(self.root,
                                   cnf=self.button_and_label_common_config.get("button"),
                                   text=config.get("text"),
                                   command=config.get("command"))
            new_button.place(x=10, y=10 + 40 * idx, width=30, height=30)
            self.buttons.append(new_button)

            new_label = tk.Label(self.root,
                                 cnf=self.button_and_label_common_config.get("label"),
                                 text=config.get("label"))
            new_label.place(x=45, y=10 + 40 * idx, width=350, height=30)
            self.labels.append(new_label)

            self.add_binding(config)

    def add_binding(self, binding):
        if binding.get("exit"):
            self.root.bind(
                sequence=f"<KeyPress-{binding.get('text')}>",
                func=(lambda event: [self.root.iconify(),
                                     binding.get('command')(),
                                     self.manually_destroy_root()]),
                add=True
            )
        else:
            self.root.bind(
                sequence=f"<KeyPress-{binding.get('text')}>",
                func=(lambda event: binding.get('command')()),
                add=True
            )

    def manually_destroy_root(self):
        time.sleep(0.3)
        self.root.destroy()


if __name__ == "__main__":
    tk_root = tk.Tk()
    app = App(tk_root)
    tk_root.mainloop()
