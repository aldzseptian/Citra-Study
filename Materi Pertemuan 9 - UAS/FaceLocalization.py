
import numpy as np
import cv2
import sys, inspect, os
import argparse
import collections

cmd_subfolder = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "..", "..", "Image_Lib")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

import image_utils as utils

z_axis_length = 11  # Harus ganjil
loc_probability = [1.0 / z_axis_length for i in range(z_axis_length)]  # prior seragam
pHit = 0.8
pMiss = 0.2

def closest_location(rect):
    closest_index = None
    min_value = float('Inf')
    for k, v in calibration_rects.items():
        value = abs(rect[2] * rect[3] - v[0] * v[1])
        if value < min_value:
            closest_index = k
            min_value = value
    return closest_index

def sense(p, rect):
    '''
    :param p: prior
    :param rect: pengukuran persegi yang terdeteksi
    :return: posterior
    '''
    index = closest_location(rect)
    if index is not None:
        p = [pHit * p[i] if i == index else pMiss * p[i] for i in range(z_axis_length)]
        p = [p[i] / sum(p) for i in range(z_axis_length)]
    return p

camera = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
calibrate = True

calibration_rects = {}

while True:
    face_box = None
    grabbed, frame = camera.read()
    frame = utils.image_resize(frame, height=600)
    face_box = utils.detect_face(face_cascade, frame)

    if face_box is None:
        continue

    cv2.rectangle(frame, (face_box[0], face_box[1]), (face_box[0] + face_box[2], face_box[1] + face_box[3]), (255, 0, 0), 2)

    if calibrate:
        utils.add_text(frame, "Tekan: W - terdekat, S - terjauh, C - netral, Q - Selesai")
        no_points_either_side = z_axis_length // 2
        cv2.imshow("Kalibrasi...", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('w'):
            calibration_rects[0] = (face_box[2], face_box[3])
            print(calibration_rects[0])

        elif key == ord('c'):
            calibration_rects[no_points_either_side] = (face_box[2], face_box[3])
            print(calibration_rects[no_points_either_side])

        elif key == ord('s'):
            calibration_rects[z_axis_length - 1] = (face_box[2], face_box[3])
            print(calibration_rects[z_axis_length - 1])

        elif key == ord('q'):
            if len(calibration_rects.keys()) == 3:
                print("Kalibrasi ....")
                calibrate = False
                front_diff = [abs(a - b) / no_points_either_side for a, b in zip(calibration_rects[0], calibration_rects[no_points_either_side])]
                back_diff = [abs(a - b) / no_points_either_side for a, b in zip(calibration_rects[z_axis_length - 1], calibration_rects[no_points_either_side])]

                for i in range(1, no_points_either_side):
                    calibration_rects[no_points_either_side - i] = tuple(sum(x) for x in zip(calibration_rects[no_points_either_side], [i * val for val in front_diff]))
                    calibration_rects[z_axis_length - 1 - i] = tuple(sum(x) for x in zip(calibration_rects[z_axis_length - 1], [i * val for val in back_diff]))

                print(calibration_rects)
                cv2.destroyWindow("Kalibrasi...")

    else:
        loc_probability = sense(loc_probability, face_box)
        location = loc_probability.index(max(loc_probability))
        utils.add_text(frame, f"Lokasi {location}, prob {loc_probability[location]:.6f}")
        cv2.imshow("Estimasi Lokasi", frame)
        if cv2.waitKey(2) & 0xFF == ord('f'):
            break

camera.release()
cv2.destroyAllWindows()
