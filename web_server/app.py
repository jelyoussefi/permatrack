from flask import Flask, render_template, Response
import cv2
import time
from os.path import exists

app = Flask(__name__)

camera_id=0;
@app.route('/')
def index():
    return render_template('index.html', camera_id=camera_id)

def stream():
    global camera_id
    video_path = "/data/output/tracking/pd/debug/"
    while True:
        video_file = video_path + "vid_" + str(camera_id) + ".avi"
        if exists(video_file):
            cap = cv2.VideoCapture(video_file)
        else:
            print("Waiting for {} to be ready", video_file)
            time.sleep(1)
            continue

        while True:
            flag, frame = cap.read()
            if flag:
                ret, jpeg = cv2.imencode('.jpg', frame)
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
            else:
                camera_id += 1;
                break;
            time.sleep(0.025)

@app.route('/video_feed')
def video_feed():
    return Response(stream(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)