import os
import importlib
from tkinter import filedialog
import tkinter as tk
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

def convert_images_to_video(folder_path, output_file, fps):
    # Get all image file paths in the folder
    image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

    # Check if there are any image files in the folder
    if not image_paths:
        print(f"No image files found in {folder_path}")
        return

    # Create the video
    video = ImageSequenceClip(image_paths, fps=fps)

    # Save the video
    video.write_videofile(output_file)

    print(f"Video saved to {os.path.abspath(output_file)}")

def browse_folder():
    folder_path.set(filedialog.askdirectory())

def save_video():
    output_file.set(filedialog.asksaveasfilename(defaultextension=".mp4"))

def start_conversion():
    convert_images_to_video(folder_path.get(), output_file.get(), int(fps.get()))

root = tk.Tk()
root.title("Image to Video Converter")

folder_path = tk.StringVar()
output_file = tk.StringVar()
fps = tk.StringVar(value="15")

tk.Label(root, text="Folder Path:").grid(row=0, column=0)
tk.Entry(root, textvariable=folder_path).grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_folder).grid(row=0, column=2)

tk.Label(root, text="Output File:").grid(row=1, column=0)
tk.Entry(root, textvariable=output_file).grid(row=1, column=1)
tk.Button(root, text="Save As", command=save_video).grid(row=1, column=2)

tk.Label(root, text="FPS:").grid(row=2, column=0)
tk.Entry(root, textvariable=fps).grid(row=2, column=1)

tk.Button(root, text="Convert", command=start_conversion).grid(row=3, column=1)

root.mainloop()