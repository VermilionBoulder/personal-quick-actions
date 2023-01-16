import re
import pyperclip


def format_vlan_text():
    ids = re.findall(r"[0-9]{3}", pyperclip.paste())
    pyperclip.copy("\n".join([f"* port 1/XX - VLAN {1000 + int(hw_id)}\n"
                              f"* port 1/XX - VLAN {1500 + int(hw_id)}" for hw_id in ids]))
