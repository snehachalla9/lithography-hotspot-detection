# Lithography Hotspot Detection

## Project Overview

Lithography hotspot detection is an important problem in semiconductor manufacturing and VLSI design. Certain layout patterns can cause defects during the photolithography process due to optical limitations. These problematic regions are called **hotspots**.

This project uses a **deep learning model based on the ResNet18 architecture** to automatically classify IC layout images into **hotspot** and **non-hotspot** categories. The trained model is deployed using **Streamlit**, allowing users to upload layout images and receive predictions in real time.

---

## Tech Stack

* Python
* PyTorch
* Streamlit
* Deep Learning

---

## Features

* Deep learning based hotspot detection
* ResNet18 CNN architecture
* Streamlit web application for predictions
* Real-time classification of IC layout images

---

## Project Structure

lithography-hotspot-detection
│
├── app.py
├── training.ipynb
├── requirements.txt
└── README.md

---
## Model Weights

The trained model file is large and not included in this repository.

You can download it here:
https://drive.google.com/file/d/1ALoNHusMCK5y00_jJYFqp1xJDOA4zaQv/view?usp=drive_link

## How to Run the Project

### Clone the repository

git clone https://github.com/snehachalla9/lithography-hotspot-detection.git

### Navigate to the folder

cd lithography-hotspot-detection

### Install dependencies

pip install -r requirements.txt

### Run the application

streamlit run app.py

---

## Example Workflow

1. Upload an IC layout image
2. The image is preprocessed and resized
3. The trained ResNet18 model analyzes the layout pattern
4. The system predicts **hotspot** or **non-hotspot**

---

## Future Improvements

* Increase dataset size for better model accuracy
* Highlight hotspot regions visually
* Deploy the app online
* Integrate with VLSI design tools

---

## Author

Sneha
AI / Machine Learning Project
