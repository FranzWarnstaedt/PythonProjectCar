import picamera
import io
import socket
import struct
import time

camera = picamera.PiCamera()
client_socket = socket.socket()

client_socket.connect(('192.168.2.201', 8000))

connection = client_socket.makefile('wb')


def start():
    camera.vflip = True
    camera.resolution = (640, 480)

    camera.start_preview()
    time.sleep(2)

    start = time.time()
    stream = io.BytesIO()
    for foo in camera.capture_continuous(stream, 'jpeg'):

        connection.write(struct.pack('<L', stream.tell()))
        connection.flush()

        stream.seek(0)
        connection.write(stream.read())

        if time.time() - start > 10:
            break

        stream.seek(0)
        stream.truncate()

    connection.write(struct.pack('<L', 0))


def stop():
    connection.close()
    client_socket.close()


def photo():
    time.sleep(2)
    camera.resolution = (1280, 720)
    photo_name = "/home/pi/Python/Projekt/Bilder/img_" + str(time.time()) + ".jpg"
    camera.capture(photo_name)
    print("Bild erstellt.")


def video():
    time.sleep(2)
    camera.resolution = (1280, 720)
    camera.contrast = 10
    video_name = "/home/pi/Python/Projekt/Video/video_" + str(time.time()) + ".h264"
    print("Starte Aufnahme...")
    camera.start_recording(video_name)
    camera.wait_recording(5)
    camera.stop_recording()
    print("Video aufgenommen.")
