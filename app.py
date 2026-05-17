import streamlit as st
import mediapipe as mp
import cv2
import numpy as np
from streamlit_webrtc import webrtc_streamer, RTCConfiguration

# Chamada direta para evitar erros de versão
BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode
