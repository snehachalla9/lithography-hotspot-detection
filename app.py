import streamlit as st
import torch
import torchvision.transforms as transforms
from PIL import Image
import torchvision.models as models
import torch.nn as nn


# Load model only once
@st.cache_resource
def load_model():
    model = models.resnet18(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, 2)
    model.load_state_dict(torch.load("hotspot_model.pth", map_location="cpu"))
    model.eval()
    return model

model = load_model()


# Class names
classes = ['hotspot', 'nonhotspot']


# Streamlit UI
st.title("Lithography Hotspot Detection")
st.write("Upload a layout image to detect hotspot or non-hotspot")


uploaded_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])


if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)


    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor()
    ])

    image = transform(image).unsqueeze(0)


    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs,1)

    result = classes[predicted.item()]

    st.subheader("Prediction")
    st.success(result)