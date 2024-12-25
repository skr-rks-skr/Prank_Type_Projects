# import pyautogui
# import time

# position = (200, 300)

# start_time = time.time()

# try: 
#     while True:
#         pyautogui.moveTo(position)

#         if time.time() - start_time > 10:
#             break

# except KeyboardInterrupt:
#     print("Error")



import ffmpeg
import os

def convert_mkv_to_mp4(input_file, output_file=None):
    if not os.path.exists(input_file):
        print(f"Error: {input_file} does not exist.")
        return

    if not output_file:
        output_file = os.path.splitext(input_file)[0] + ".mp4"

    try:
        ffmpeg.input(input_file).output(output_file).run()
        print(f"Conversion complete: {output_file}")
    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr.decode()}")

if __name__ == "__main__":
    # Example: Modify with your input MKV file path
    input_mkv = "hii.mkv"
    
    # You can specify output file path or leave it to automatically convert to mp4 in the same directory
    convert_mkv_to_mp4(input_mkv)
