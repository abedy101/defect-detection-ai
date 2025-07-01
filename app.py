import streamlit as st
from detect import run_detection
import os
from PIL import Image

st.title("Defect Detection AI")
st.markdown("Upload a product image to automatically detect defects.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
conf_threshold = st.slider("Detection confidence threshold", 0.1, 1.0, 0.4, 0.05)

if uploaded_file:
    os.makedirs("uploads", exist_ok=True)
    input_path = os.path.join("uploads", uploaded_file.name)
    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(input_path, caption="Original Image", use_column_width=True)

    with st.spinner("Running detection..."):
        output_path, detections = run_detection(input_path, conf_threshold)

    st.image(output_path, caption="Detected Defects", use_column_width=True)

    if detections:
        st.subheader("Defect Report")
        for det in detections:
            st.write(f"{det['label']} – Confidence: {det['confidence']:.2f}")
    else:
        st.success("No defects detected.")
