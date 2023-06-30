import os
import shutil
import tkinter as tk
from tkinter import messagebox

def delete_folder(folder_names, subdirs):
    if subdirs:
        for root, dirs, files in os.walk(os.getcwd()):
            for dir in dirs:
                if dir in folder_names:
                    shutil.rmtree(os.path.join(root, dir))
    else:
        for dir in os.listdir():
            if os.path.isdir(dir) and dir in folder_names:
                shutil.rmtree(dir)
    messagebox.showinfo("Info", "Gone!  reduced to atoms.")
    messagebox.showinfo("Info", "Perfectly balanced, as all things should be.")


def select_operation():
    folder_names = ["cz", "da", "de", "es", "fi", "fr", "it", "ja", "ko", "nl", "pl", "pt", "ru", "su" ,"sl", "sv", "tr", "zh", "hu"]
    window = tk.Tk()
    window.withdraw()
    result = messagebox.askyesno("Question", "Do you want to keep 'English' manuals only?")
    if result:
        subdirs_result = messagebox.askyesno("Question", "Do you want to delete manuals in other than EN language in subdirectories as well?")
        delete_folder(folder_names, subdirs_result)
    else:
        messagebox.showinfo("Info", "Okay. Whatever...")

if __name__ == "__main__":
    select_operation()