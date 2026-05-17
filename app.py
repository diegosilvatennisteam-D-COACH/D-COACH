import streamlit as st
import cv2
import numpy as np

# Comando de segurança para garantir a instalação
try:
    import mediapipe as mp
except ImportError:
    st.error("Instalando componentes de visão computacional... Por favor, aguarde 30 segundos e atualize a página.")
    st.stop()

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
