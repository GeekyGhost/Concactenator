import os
import cv2
import tkinter as tk
import numpy as np
from tkinter import filedialog
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy.editor import concatenate_videoclips, ImageClip
from moviepy.editor import AudioFileClip
from aubio import source, tempo


# Custom colors and fonts
bg_color = "#1e1e1e"
text_color = "#9eff9e"
button_color = "#333333"
button_hover_color = "#4c4c4c"
font = "Helvetica 10 bold"

def on_enter(e):
    e.widget.config(bg=button_hover_color)

def on_leave(e):
    e.widget.config(bg=button_color)

def get_next_project_folder(base_output_folder):
    i = 1
    while True:
        project_folder = os.path.join(base_output_folder, f"project{str(i).zfill(3)}")
        if not os.path.exists(project_folder):
            os.makedirs(project_folder)
            break
        i += 1
    return project_folder

def browse_audio_file():
    selected_audio_file = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3;*.wav;*.ogg")])
    if selected_audio_file:
        audio_path.set(selected_audio_file)

def extract_beats(audio_file):
    win_s = 512                 # fft size
    hop_s = win_s // 2          # hop size

    samplerate = 0
    s = source(audio_file, samplerate, hop_s)
    samplerate = s.samplerate
    o = tempo("default", win_s, hop_s, samplerate)

    beats = []

    # total number of frames read
    total_frames = 0
    while True:
        samples, read = s()
        is_beat = o(samples)
        if is_beat:
            this_beat = o.get_last_s()
            beats.append(this_beat)
        total_frames += read
        if read < hop_s:
            break

    return np.array(beats)

def select_video_file():
    video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv;*.mov;*.flv;*.wmv")])
    return video_path

def select_output_folder():
    output_folder = filedialog.askdirectory()
    return output_folder

def extract_frames(video_file, output_folder):
    video = cv2.VideoCapture(video_file)

    if not video.isOpened():
        print("Error: Could not open video file.")
        return

    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video.get(cv2.CAP_PROP_FPS))

    # Extract audio
    audio_file = os.path.join(output_folder, "audio.mp3")
    os.system(f"ffmpeg -i {video_file} -vn -acodec copy {audio_file}")

    for i in range(frame_count):
        ret, frame = video.read()
        if not ret:
            break

        output_path = os.path.join(output_folder, f"frame_{i:04d}.png")
        cv2.imwrite(output_path, frame)

    video.release()
    print(f"Frames successfully extracted to {output_folder}")

def start_extraction():
    base_output_folder = "output"
    project_folder = get_next_project_folder(base_output_folder)

    if video_path.get() and project_folder:
        extract_frames(video_path.get(), project_folder)

def convert_images_to_video(folder_path, output_file, fps):
    image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

    if not image_paths:
        print(f"No image files found in {folder_path}")
        return

    audio_file = audio_path.get()
    if audio_file and os.path.exists(audio_file):
        audio_clip = AudioFileClip(audio_file)
        video = ImageSequenceClip(image_paths, fps=fps).set_audio(audio_clip)
    else:
        video = ImageSequenceClip(image_paths, fps=fps)

    video.write_videofile(output_file)

    print(f"Video saved to {os.path.abspath(output_file)}")

def browse_image_folder():
    selected_file = filedialog.askopenfilename(title="Choose any file in the folder to be processed",
                                               filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if selected_file:
        selected_folder = os.path.dirname(selected_file)
        folder_path.set(selected_folder)

def browse_video_file():
    selected_video_file = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv;*.mov;*.flv;*.wmv")])
    if selected_video_file:
        video_path.set(selected_video_file)

def save_video():
    output_file.set(filedialog.asksaveasfilename(defaultextension=".mp4"))

def start_conversion():
    project_folder = get_next_project_folder("output")
    output_file_name = f"concatenated_video.mp4"
    output_file_with_path = os.path.join(project_folder, output_file_name)

    audio_file = audio_path.get()
    audio_duration = None

    if audio_file and os.path.exists(audio_file):
        audio_clip = AudioFileClip(audio_file)
        audio_duration = audio_clip.duration

    if audio_duration is not None:
        fps_value = int(fps.get())
        create_video_with_audio_duration(folder_path.get(), output_file_with_path, fps_value, audio_duration, audio_clip)
    else:
        convert_images_to_video(folder_path.get(), output_file_with_path, int(fps.get()))

def create_video_with_audio_duration(folder_path, output_file, fps, audio_duration, audio_clip):
    image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

    if not image_paths:
        print(f"No image files found in {folder_path}")
        return

    image_duration = audio_duration / len(image_paths)
    image_clips = [ImageClip(p).set_duration(image_duration).resize(height=480) for p in image_paths]

    video = concatenate_videoclips(image_clips, method="compose").set_audio(audio_clip)
    video.write_videofile(output_file, fps=fps)

    print(f"Video saved to {os.path.abspath(output_file)}")

root = tk.Tk()
root.title("Image/Video Processing")
root.configure(bg=bg_color)

folder_path = tk.StringVar()
output_file = tk.StringVar()
fps = tk.StringVar(value="15")
video_path = tk.StringVar()
audio_path = tk.StringVar(value="")

# Frame for input folder and output file selection
selection_frame = tk.LabelFrame(root, text="Select Image, Video, and/or Audio Files", padx=5, pady=5, bg=bg_color, fg=text_color)
selection_frame.grid(row=0, column=0, padx=10, pady=10)

tk.Label(selection_frame, text="Images:").grid(row=0, column=0)
tk.Entry(selection_frame, textvariable=folder_path).grid(row=0, column=1)
tk.Button(selection_frame, text="Browse", command=browse_image_folder).grid(row=0, column=2)

tk.Label(selection_frame, text="Video:").grid(row=1, column=0)
tk.Entry(selection_frame, textvariable=video_path).grid(row=1, column=1)
tk.Button(selection_frame, text="Browse", command=browse_video_file).grid(row=1, column=2)

tk.Label(selection_frame, text="Audio:").grid(row=2, column=0)
tk.Entry(selection_frame, textvariable=audio_path).grid(row=2, column=1)
tk.Button(selection_frame, text="Browse", command=browse_audio_file).grid(row=2, column=2)

# Frame for FPS and action buttons
action_frame = tk.LabelFrame(root, text="Settings and Actions", padx=5, pady=5, bg=bg_color, fg=text_color)
action_frame.grid(row=1, column=0, padx=10, pady=10)

tk.Label(action_frame, text="FPS:").grid(row=0, column=0)
tk.Entry(action_frame, textvariable=fps).grid(row=0, column=1)

tk.Button(action_frame, text="Concatenate", command=start_conversion).grid(row=1, column=0, padx=5, pady=5)
tk.Button(action_frame, text="Extractinator", command=start_extraction).grid(row=1, column=1, padx=5, pady=5)

# Customize UI elements
for element in (root, selection_frame, action_frame):
    for child in element.winfo_children():
        if isinstance(child, (tk.Label, tk.Entry, tk.LabelFrame)):
            child.config(bg=bg_color, fg=text_color, font=font)
        elif isinstance(child, tk.Button):
            child.config(bg=button_color, fg=text_color, font=font, activebackground=button_hover_color, activeforeground=text_color)
            child.bind("<Enter>", on_enter)
            child.bind("<Leave>", on_leave)

root.mainloop()
