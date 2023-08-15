import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog
import os
from PIL import Image

# strip the metadata
def remove_metadata(input_path):
    try:
        # create a copy with no metadata
        image = Image.open(input_path)
        stripped = Image.new(image.mode, image.size)
        stripped.paste(image)

        # save the original
        original_path = os.path.join(get_folder_path('Originals'), os.path.basename(input_path))
        image.save(original_path)

        # save the stripped
        stripped_path = os.path.join(get_folder_path('Stripped'), os.path.basename(input_path))
        stripped.save(stripped_path)

        # display the removed metadata
        removed_metadata = get_removed_metadata_info(image.info)
        change_output(f"Result is in the stripped folder.\nMetadata removed:\n{removed_metadata}")

    except Exception as e:
        change_output("Error:" + str(e))

# format metadata for display
def get_removed_metadata_info(metadata):
    removed_metadata = ""
    for key, value in metadata.items():
        removed_metadata += f"{key}: {value}\n"
    return removed_metadata

# remove data when image dropped
def on_drop(event):
        remove_metadata(event.data)

# opens file explorer to find image
def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff")])
    if filepath:
        remove_metadata(filepath)

# get path of folder in this directory 'Originals' or 'Stripped'
def get_folder_path(folder):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    folder_directory = os.path.join(script_directory, folder)
    os.makedirs(folder_directory, exist_ok=True)
    return folder_directory

# clear all images in the folders
def clear_folders():
    stripped_folder = get_folder_path('Stripped')
    originals_folder = get_folder_path('Originals')
    
    try:
        # remove all files from 'Stripped' folder
        for filename in os.listdir(stripped_folder):
            file_path = os.path.join(stripped_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        # remove all files from 'Originals' folder
        for filename in os.listdir(originals_folder):
            file_path = os.path.join(originals_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        change_output("All data cleared from 'Stripped' and 'Originals' folders.")

    except Exception as e:
        change_output("Error:" + str(e))

# change the gui text diplay
def change_output(text):
    entry.config(state=tk.NORMAL)
    entry.delete(1.0, tk.END)
    entry.insert(tk.END, text)
    entry.config(state=tk.DISABLED)

# build widgets
root = TkinterDnD.Tk()
root.title("MetaStrip")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

button_frame = tk.Frame(frame)
button_frame.pack(side=tk.TOP)

label = tk.Label(button_frame, text="Drag and drop an image file here or")
label.pack(side=tk.LEFT, padx=5, pady=10)

browse_button = tk.Button(button_frame, text="Browse Files", command=browse_file)
browse_button.pack(side=tk.LEFT, padx=5)

entry = tk.Text(frame, height=10, width=50, state=tk.DISABLED, wrap='word')
entry.pack(padx=5, pady=10)

button_frame = tk.Frame(frame)
button_frame.pack()

open_originals_button = tk.Button(button_frame, text="See Originals", command=lambda: os.startfile(get_folder_path('Originals')))
open_originals_button.pack(side=tk.LEFT, padx=5)

open_stripped_button = tk.Button(button_frame, text="See Stripped", command=lambda: os.startfile(get_folder_path('Stripped')))
open_stripped_button.pack(side=tk.LEFT, padx=5)

clear_folders_button = tk.Button(button_frame, text="Clear Image History", command=lambda: clear_folders())
clear_folders_button.pack()

# drop event handler
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

root.mainloop()
