import cv2

video_path = 'videos/videoplayback.mp4'

capture = cv2.VideoCapture(video_path)

video_fps = int(capture.get(cv2.CAP_PROP_FPS))
print(f'video fps: {video_fps}')

interval_in_s = 1

current_frame = 0
while True:

    isTrue, frame = capture.read()

    if not isTrue:
        break

    # redo calculation for more accurate timing
    if current_frame % (video_fps*interval_in_s) <= 0.5:

        name = f'./result/frame{current_frame}.jpg'
        print(f'creating {name}')
        cv2.imwrite(name, frame)
    
    current_frame += 1