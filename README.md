Concactenator

Image/Video Processing Tool

This Image/Video Processing Tool allows you to extract frames from a video file (supported formats: MP4, AVI, MKV, MOV, FLV, WMV) and convert a sequence of image files (JPG, JPEG, or PNG) back into a video file. This is useful for video editing, analysis, or other creative projects.

Installation:
Make sure you have Python installed on your computer (https://www.python.org/downloads/).
Download the script and place it in a folder along with the "run.bat" file.
Download the "requirements.txt" file and place it in the same folder as the script and "run.bat" file.

How to use:
Double-click the "run.bat" file to start the tool.
The tool will set up a virtual environment, install necessary packages, and launch the Image/Video Processing Tool.
Use the "Browse" button under "Images" to select the folder containing the image files (JPG, JPEG, or PNG) you want to process.
Use the "Browse" button under "Video" to select the video file you want to extract frames from.
Enter the desired frames per second (FPS) for the output video.
(Optional) Use the "Browse" button under "Audio" to select an audio file to add to the final video.
Click "Concatenate" to convert the image sequence to a video file, or click "Extractinator" to extract frames and audio from the selected video file.
The tool will save the output file in the specified location or create a new folder for extracted frames.

Important notes:
Make sure you run the "run.bat" file instead of running the script directly. The "run.bat" file ensures that the necessary Python packages are installed in a virtual environment.
The tool will create an "output" folder in the same directory as the script to store project folders for extracted frames or the output video. Each project folder is named "projectXXX", where "XXX" is a unique 3-digit number.
The tool supports adding an audio file to the final video. The supported audio file formats are MP3, WAV, and OGG.


![Screenshot 2023-03-24 002643](https://user-images.githubusercontent.com/111990299/227424353-38703824-d1e7-4e27-a4ac-12104bd5b90e.png)

