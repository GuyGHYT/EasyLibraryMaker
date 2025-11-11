from logging import root
import tkinter as tk
import os
from ..utils import configloader, createfolder
import subprocess

def initialize_window():
    root = tk.Tk()
    root.geometry("500x250")
    root.title("Library Maker")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    entry = tk.Entry(frame, textvariable=tk.StringVar(), width=40)
    entry.pack(side=tk.LEFT, padx=5)

    def browse_directory(entry_widget):
        from tkinter import filedialog
        onedrive_desk = os.path.join(os.environ.get('OneDrive', ''), 'Desktop')
        folder_selected = filedialog.askdirectory(initialdir=onedrive_desk)
        if folder_selected:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, folder_selected)

    def browse_config(entry_widget):
        from tkinter import filedialog
        file_selected = filedialog.askopenfilename(initialdir="config",filetypes=[("YAML files", "*.yaml"), ("All files", "*.*")])
        if file_selected:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, file_selected)

    def bring_to_dir(folder_path):

        if folder_path and os.path.exists(folder_path):
            normalpath = os.path.normpath(folder_path)
            subprocess.Popen(['explorer', normalpath], shell=True)
        else:
            tk.messagebox.showerror("Error", "No valid folder selected")

    def start_process():
        base_path = entry.get()
        lib_name = lib_name_entry.get()
        config_file = config_entry.get()
        
        # Validate inputs
        if not base_path:
            tk.messagebox.showerror("Error", "Please select a base directory")
            return
        if not lib_name:
            tk.messagebox.showerror("Error", "Please enter a library name")
            return
        if not config_file:
            tk.messagebox.showerror("Error", "Please select a config file")
            return
            
        print(f"Creating library '{lib_name}' at '{base_path}' using config '{config_file}'")
        createfolder.create_folder(base_path, lib_name, config_file)

    button = tk.Button(frame, text="Browse...", command=lambda: browse_directory(entry))
    button.pack(side=tk.LEFT)

    # Library name frame
    frame2 = tk.Frame(root)
    frame2.pack(pady=5)
    tk.Label(frame2, text="Library Name:").pack(side=tk.LEFT, padx=5)
    lib_name_entry = tk.Entry(frame2, textvariable=tk.StringVar(), width=30)
    lib_name_entry.pack(side=tk.LEFT, padx=5)

    # Config file frame
    frame3 = tk.Frame(root)
    frame3.pack(pady=5)
    tk.Label(frame3, text="Config File:").pack(side=tk.LEFT, padx=5)
    config_entry = tk.Entry(frame3, textvariable=tk.StringVar(), width=30)
    config_entry.pack(side=tk.LEFT, padx=5)
    button2 = tk.Button(frame3, text="Browse Config", command=lambda: browse_config(config_entry))
    button2.pack(side=tk.LEFT, padx=5)

    startbutton = tk.Button(root, text="Start", command=lambda:start_process())
    startbutton.pack(pady=10)

    bringtobutton = tk.Button(root, text="Bring to Folder", command=lambda: bring_to_dir(entry.get()))
    bringtobutton.pack(pady=5)

    root.mainloop()

def test_window():
    initialize_window()