import pyperclip


def alt_caps():
    text = pyperclip.paste()
    alt_caps_text = []
    for idx, char in enumerate(text):
        if idx % 2:
            alt_caps_text.append(char.upper())
        else:
            alt_caps_text.append(char.lower())
    pyperclip.copy(''.join(alt_caps_text))


if __name__ == '__main__':
    alt_caps()
