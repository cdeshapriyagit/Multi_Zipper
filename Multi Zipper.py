import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar

def create_zip_for_folders(folder_path, progress_bar, progress_label):
    directories = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
    total_folders = len(directories)
    current_folder = 0

    for directory in directories:
        current_folder += 1
        zip_filename = os.path.join(folder_path, f"{directory}.zip")
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(os.path.join(folder_path, directory)):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
        progress = (current_folder / total_folders) * 100
        progress_bar['value'] = progress
        progress_label.config(text=f"{progress:.2f}%")
        progress_bar.update()
        progress_label.update()

def browse_folder(progress_bar, progress_label):
    folder_path = filedialog.askdirectory()
    if folder_path:
        progress_bar['value'] = 0
        progress_label.config(text="0.00%")
        create_zip_for_folders(folder_path, progress_bar, progress_label)
        messagebox.showinfo("Success", "Zip files created successfully.")

def main():
    root = tk.Tk()
    root.title("Folder Zipper")
    root.geometry("300x220")
    root.resizable(False, False)  # Disable resizing

    browse_button = tk.Button(root, text="Browse Folder", command=lambda: browse_folder(progress_bar, progress_label))
    browse_button.pack(pady=10)

    progress_bar = Progressbar(root, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack(pady=5)

    progress_label = tk.Label(root, text="0.00%")
    progress_label.pack(pady=5)

    creator_label = tk.Label(root, text="All Subfolders you can convert .zip file")
    creator_label.pack(pady=5)
    creator_label = tk.Label(root, text="Create by Chinthaka")
    creator_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
