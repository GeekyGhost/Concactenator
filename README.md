Image and Video Processing Tool
This is a simple Python-based image and video processing tool that provides several functionalities such as concatenating images into a video, extracting frames from a video, reversing a video, and concatenating two videos. It was made with the assistance of chatGPT

Features
Concatenate images into a video
Extract frames from a video
Reverse a video
Concatenate two videos
Requirements
To use this tool, you need to have the following Python packages installed:

OpenCV (cv2)
LibROSA
MoviePy
NumPy
Tkinter
You can install them using the following command:

Copy code
pip install opencv-python librosa moviepy numpy tk
Usage
Run the script using a Python interpreter:
Copy code
python image_video_processing.py
Select the appropriate files for the operation you want to perform:

For concatenating images into a video, select an image folder, an optional audio file, and set the desired FPS.
For extracting frames from a video, select a video file.
For reversing a video, select a video file.
For concatenating two videos, select two video files.
Click the corresponding button to perform the desired operation.

Functions

Here is a brief description of the functions used in the script:

get_next_project_folder(base_output_folder): Returns the next available project folder for output.

browse_audio_file(): Opens a file dialog to select an audio file.
create_video_with_audio_duration(...): Creates a video by concatenating images and setting their duration based on the audio duration.

select_video_file(): Opens a file dialog to select a video file.

select_output_folder(): Opens a directory dialog to select an output folder.

extract_frames(video_file, output_folder): Extracts frames from a video and saves them in the output folder.

extract_and_reverse_frames(video_file, output_folder): Extracts and reverses frames from a video and saves them in the output folder.

start_extraction(): Starts the frame extraction process.

concatenate_videos_and_save(): Concatenates two videos and saves the output.

convert_images_to_video(folder_path, output_file, fps): Converts a folder of images into a video file with the specified FPS.

browse_image_folder(): Opens a file dialog to select an image folder.

browse_video_file(): Opens a file dialog to select a video file.

save_video(): Opens a file dialog to select the output video file.

start_conversion(): Starts the conversion process for creating a video from images.

convert_images_to_video_with_rhythm(...): Converts a folder of images into a video file synchronized with the rhythm of an audio file.

reverse_video(input_file, output_file): Reverses a video file and saves the output.

reverse_and_save_video(): Reverses a video file and saves the output.

concatenate_selected_videos(): Concatenates the selected video files.

browse_video_file_2(): Opens a file dialog to select a second video file.

License

This project is released under the MIT License.

Updated 4/20/2023


![Screenshot 2023-05-31 223103](https://github.com/GeekyGhost/Concactenator/assets/111990299/72050022-779e-425a-9953-6edee0dfe38f)



