import os
import glob
import sys

# 1. Check if OpenCV is installed
try:
    import cv2
except ImportError:
    print("ERROR: OpenCV is not installed!")
    print("Please open Command Prompt and run: pip install opencv-python")
    input("\nPress Enter to exit...")
    sys.exit()

# 2. Force the script to run in the folder where it is located
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# The names you want for your 10 screenshots
ordinals = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]
# The 10 precise percentage marks (5%, 15%, 25%... 95%)
percentages = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]

# Scan the folder for all MP4 videos
video_files = glob.glob("*.mp4")

if not video_files:
    print("No .mp4 videos found in this folder.")
else:
    for video_path in video_files:
        base_name = os.path.splitext(video_path)[0]
        
        # Create a new folder named after the video
        folder_name = f"{base_name} Screenshots"
        os.makedirs(folder_name, exist_ok=True)
        
        # Open the video
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        print(f"\nProcessing: {video_path}...")
        
        for i, p in enumerate(percentages):
            # Calculate the exact frame number
            frame_no = int(total_frames * p)
            
            # Jump to that specific frame
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
            
            # Read the frame
            ret, frame = cap.read()
            if ret:
                filename = f"{ordinals[i]} video screenshot.jpg"
                output_path = os.path.join(folder_name, filename)
                
                # Save the image
                cv2.imwrite(output_path, frame)
                print(f"  -> Saved: {output_path}")
                
        cap.release()
        
    print("\nAll videos finished successfully!")

# 3. Stop the window from closing instantly
input("\nPress Enter to exit...")