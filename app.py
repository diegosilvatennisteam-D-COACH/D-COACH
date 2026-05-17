import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

# Forma ultra-segura de chamar o mediapipe
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
st.write("Aponte a câmera para o jogador para analisar a biomecânica.")
