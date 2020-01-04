import logging
import threading

import numpy as np
import cv2

def open_cam_rtsp(uri, width, height, latency):
    """Open an RTSP URI (IP CAM)."""
    gst_str = ('rtspsrc location={} latency={} ! '
               'rtph264depay ! h264parse ! omxh264dec ! '
               'nvvidconv ! '
               'video/x-raw, width=(int){}, height=(int){}, '
               'format=(string)BGRx ! videoconvert ! '
               'appsink').format(uri, latency, width, height)
    return cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)


def open_cam_usb(dev, width, height):
    """Open a USB webcam.

    We want to set width and height here, otherwise we could just do:
        return cv2.VideoCapture(dev)
    """
    gst_str = ('v4l2src device=/dev/video{} ! '
               'video/x-raw, width=(int){}, height=(int){} ! '
               'videoconvert ! appsink').format(dev, width, height)
    return cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)


def open_cam_onboard(dev, width, height):
    """Open the Jetson onboard camera.

    On versions of L4T prior to 28.1, you might need to add
    'flip-method=2' into gst_str.
    """
    gst_str = ('nvarguscamerasrc sensor-id={} ! '
               'video/x-raw(memory:NVMM), '
               'width=(int)1280, height=(int)720, '
               'format=(string)NV12, framerate=(fraction)30/1 ! '
               'nvvidconv ! '
               'video/x-raw, width=(int)1280, height=(int)720, '
               'format=(string)BGRx ! videoconvert ! '
               'appsink').format(dev, width, height)
    return cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)