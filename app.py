import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration

# Configuração do Mediapipe
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

st.set_page_config(page_title="D-COACH - Análise de Tênis", layout="wide")
st.title("D-COACH: Inteligência Artificial no Tênis 🎾")

rtc_configuration = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

def transform(frame):
    img = frame.to_ndarray(format="bgr24")
    
    with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
        
        img.flags.writeable = False
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(img)

        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                img,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

    return img

webrtc_streamer(
    key="d-coach-analysis",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=rtc_configuration,
    video_frame_callback=transform,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)

st.write("Aponte a câmera para o jogador para analisar a biomecânica.")
