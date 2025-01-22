# OmniDash

OmniDash is a Windows-based tool designed to combine multiple media files into a single optimized file. It supports various media formats, including video, audio, and images, and outputs a single, cohesive media file. This tool is ideal for users looking to consolidate different media types into one file for easy sharing or storage.

## Features

- Combine multiple video files into a single video file.
- Merge multiple audio files into one audio file.
- Create a slideshow from multiple image files.
- Supports various media formats such as mp4, avi, mov, mp3, wav, jpg, png, and jpeg.
- Outputs optimized files suitable for easy sharing and storage.

## Requirements

To run OmniDash, ensure you have the following installed:

- Python 3.x
- moviepy
- pydub
- Pillow
- ffmpeg (required by moviepy)
- ffmpeg or libav (required by pydub)

## Installation

1. Clone the repository or download the `omnidash.py` file.
2. Install the required Python libraries using pip:

   ```bash
   pip install moviepy pydub Pillow
   ```

3. Ensure `ffmpeg` is installed and added to your system's PATH. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html).

## Usage

1. Run the script:

   ```bash
   python omnidash.py
   ```

2. Follow the on-screen instructions:
   - Enter the path to the folder containing the media files you want to combine.
   - Enter the desired output file name with the appropriate extension.

3. The combined media file will be saved to the specified output file name.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.