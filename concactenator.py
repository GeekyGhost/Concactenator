import os
import cv2
import tkinter as tk
from tkinter import filedialog
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

def get_next_project_folder(base_output_folder):
    i = 1
    while True:
        project_folder = os.path.join(base_output_folder, f"project{str(i).zfill(3)}")
        if not os.path.exists(project_folder):
            os.makedirs(project_folder)
            break
        i += 1
    return project_folder

def select_mp4_file():
    mp4_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    return mp4_path

def select_output_folder():
    output_folder = filedialog.askdirectory()
    return output_folder

def extract_frames(mp4_file, output_folder):
    video = cv2.VideoCapture(mp4_file)

    if not video.isOpened():
        print("Error: Could not open video file.")
        return

    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    for i in range(frame_count):
        ret, frame = video.read()
        if not ret:
            break

        output_path = os.path.join(output_folder, f"frame_{i:04d}.png")
        cv2.imwrite(output_path, frame)

    video.release()
    print(f"Frames successfully extracted to {output_folder}")

def start_extraction():
    mp4_file = select_mp4_file()
    base_output_folder = "output"
    project_folder = get_next_project_folder(base_output_folder)

    if mp4_file and project_folder:
        extract_frames(mp4_file, project_folder)

def convert_images_to_video(folder_path, output_file, fps):
    image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

    if not image_paths:
        print(f"No image files found in {folder_path}")
        return

    video = ImageSequenceClip(image_paths, fps=fps)
    video.write_videofile(output_file)

    print(f"Video saved to {os.path.abspath(output_file)}")

def browse_folder():
    folder_path.set(filedialog.askdirectory())

def save_video():
    output_file.set(filedialog.asksaveasfilename(defaultextension=".mp4"))

def start_conversion():
    project_folder = get_next_project_folder("output")
    output_file_with_path = os.path.join(project_folder, output_file.get())
    convert_images_to_video(folder_path.get(), output_file_with_path, int(fps.get()))

root = tk.Tk()
root.title("Image/Video Processing")

folder_path = tk.StringVar()
output_file = tk.StringVar()
fps = tk.StringVar(value="15")

# Frame for input folder and output file selection
selection_frame = tk.LabelFrame(root, text="Select Input and Output", padx=5, pady=5)
selection_frame.grid(row=0, column=0, padx=10, pady=10)

tk.Label(selection_frame, text="Video Path:").grid(row=0, column=0)
tk.Entry(selection_frame, textvariable=folder_path).grid(row=0, column=1)
tk.Button(selection_frame, text="Browse", command=browse_folder).grid(row=0, column=2)

tk.Label(selection_frame, text="Output File:").grid(row=1, column=0)
tk.Entry(selection_frame, textvariable=output_file).grid(row=1, column=1)
tk.Button(selection_frame, text="Save As", command=save_video).grid(row=1, column=2)

tk.Label(selection_frame, text="Output File:").grid(row=1, column=0)
tk.Entry(selection_frame, textvariable=output_file).grid(row=1, column=1)
tk.Button(selection_frame, text="Save As", command=save_video).grid(row=1, column=2)


# Frame for FPS and action buttons
action_frame = tk.LabelFrame(root, text="Settings and Actions", padx=5, pady=5)
action_frame.grid(row=1, column=0, padx=10, pady=10)

tk.Label(action_frame, text="FPS:").grid(row=0, column=0)
tk.Entry(action_frame, textvariable=fps).grid(row=0, column=1)

tk.Button(action_frame, text="Concatenate", command=start_conversion).grid(row=1, column=0, padx=5, pady=5)
tk.Button(action_frame, text="Extractinator", command=start_extraction).grid(row=1, column=1, padx=5, pady=5)

root.mainloop()
