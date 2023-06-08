key = 1912

def encrypter(text: str) -> str:
    ascii_vals = [ord(i)*key for i in text]
    ascii_str = "-".join([str(i) for i in ascii_vals])
    return ascii_str

def decrypter(text: str) -> str:
    ascii_str = [int(i) for i in text.split("-")]
    ascii_vals = "".join([chr(int(i/key)) for i in ascii_str])
    return ascii_vals