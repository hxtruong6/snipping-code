import os
import subprocess


if __name__ == "__main__":

    # Specify the directory containing the MP4 files
    directory = "/home/ubuntu/WORK/video_facedance/video facedance"
    output_directory = "/home/ubuntu/WORK/video_facedance/processed"

    video_files = []
    # Iterate over all the files in the directory and its subfolders
    for root, dirs, files in os.walk(directory):
        for file_path in files:
            if file_path.endswith(".mp4") or file_path.endswith(".mov"):
                # Get the absolute path of the file
                file_path = os.path.join(root, file_path)
                video_files.append(file_path)

    # Iterate over each MP4 file
    for file_path in video_files:
        # Construct the input and output file paths
        input_file = file_path

        # Create the output folder if it doesn't exist. The subfolder remove the first folder and the last file
        subfolder = os.path.join(
            output_directory,
            "/".join(file_path.replace(directory, "").split("/")[1:-1]),
        )
        os.makedirs(subfolder, exist_ok=True)
        print(f"---- Output folder: {subfolder}")

        output_file = os.path.join(
            subfolder,
            file_path.split("/")[-1].replace(".mp4", "").replace(".mov", "")
            + "_256x256.mp4",
        )

        #  https://ottverse.com/change-resolution-resize-scale-video-using-ffmpeg/
        # Execute FFmpeg command to scale the video
        command = [
            "ffmpeg",
            "-i",
            input_file,
            "-vf",
            # "scale=256:256",
            "scale=256:256:force_original_aspect_ratio=decrease,pad=ceil(iw/2)*2:ceil(ih/2)*2",
            "-preset",
            "slow",
            "-crf",
            "18",
            output_file,
        ]
        subprocess.run(command)

        print(f"Scaled {file_path} to 256x256.")
