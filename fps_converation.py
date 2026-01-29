import os
import subprocess
import imageio_ffmpeg

ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

input_folder = r"D:\bhanu\OneDrive - Imagevision.ai India Pvt Ltd\bhanu_iv061\GHD_TRAFFIC_COUNTING\Engineering\input_videos"
output_folder = r"D:\bhanu\OneDrive - Imagevision.ai India Pvt Ltd\bhanu_iv061\GHD_TRAFFIC_COUNTING\Engineering\fps_downgradeed"
target_fps = 5

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith((".mp4", ".avi", ".mkv", ".mov")):
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(
            output_folder,
            os.path.splitext(file)[0] + f"_fps{target_fps}.mp4"
        )

        cmd = [
            ffmpeg_path,   # 👈 pip-installed ffmpeg binary
            "-y",
            "-i", input_path,
            "-vf", f"fps={target_fps}",
            "-c:v", "libx264",
            "-crf", "18",
            "-preset", "slow",
            "-c:a", "copy",
            output_path
        ]

        subprocess.run(cmd, check=True)

print("All videos processed successfully!")
