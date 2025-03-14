import tkinter as tk
from tkinter import ttk

def atbash_cipher(text: str) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    reversed_alphabet = alphabet[::-1]
    mapping = str.maketrans(alphabet + alphabet.lower(), reversed_alphabet + reversed_alphabet.lower())
    return text.translate(mapping)
def encrypt_text():
    input_text = entry.get()
    encrypted_text = atbash_cipher(input_text)
    result_label.config(text=f"Зашифрланган текст: {encrypted_text}")
def decrypt_text():
    input_text = entry.get()
    decrypted_text = atbash_cipher(input_text) 
    result_label.config(text=f"Дешифрланган текст: {decrypted_text}")
root = tk.Tk()
root.title("SHIFR")
entry_label = ttk.Label(root, text="Текст жазыныз:")
entry_label.pack()
entry = ttk.Entry(root, width=40)
entry.pack()
encrypt_button = ttk.Button(root, text="Шифрлау", command=encrypt_text)
encrypt_button.pack()
decrypt_button = ttk.Button(root, text="Дешифрлау", command=decrypt_text)
decrypt_button.pack()
result_label = ttk.Label(root, text=" ")
result_label.pack()
root.mainloop()