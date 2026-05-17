import streamlit as st
from streamlit_webrtc import webrtc_streamer
import cv2
import mediapipe as mp

# Configuração
st.title("🎾 D-COACH: Teste de Quadra")

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.7)

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    results = pose.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(
            img, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
    return img

st.write("Link para o celular:")
st.code("http://192.168.1.10:8501")

webrtc_streamer(
    key="d-coach-mobile",
    video_frame_callback=video_frame_callback,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
) 
