
---

# Defect Detection AI

A simple but powerful AI tool for detecting defects or objects in product images. Built for manufacturers, quality control teams, and businesses that want to automate visual inspection.

This app uses a YOLOv8 model to identify items like scratches, dents, misprints — or general objects like people, cars, and bikes, depending on the model you plug in.

---

## What This Tool Does

* Upload product or object images
* Automatically highlights defects or items using bounding boxes
* Adjustable detection sensitivity (threshold slider)
* Export a report of detected items and their confidence scores

---

## Features

**1. Simple Interface**
Drag and drop your image. Adjust the sensitivity. Get results instantly.

**2. Model Flexibility**
Works out-of-the-box with a general-purpose YOLOv8 model. You can replace it with your own model trained on custom defects.

**3. Export Reports**
Get defect summaries as downloadable CSVs showing object type, location, and confidence.

---

## Demo Screenshot

This demo uses a public YOLOv8 model. It detected the following objects in a busy street scene:

**Input Image**
`demo/sample-street.jpg`

![Sample Detection](demo/sample-street.jpg)

**Generated Detection Report**

```
person – Confidence: 0.84  
bus – Confidence: 0.82  
person – Confidence: 0.81  
bicycle – Confidence: 0.43  
... and more
```

---

## How to Use With Your Own Model

1. Train your YOLOv8 model (e.g. on Roboflow or locally)
2. Export the trained `.pt` file
3. Rename it to `defects.pt`
4. Place it inside the `model/` folder
5. Run the app and upload your own product photos

---

## Quickstart (For Developers)

```bash
git clone https://github.com/abedy101/defect-detection-ai
cd defect-detection-ai
pip install -r requirements.txt
streamlit run app.py
```

---

## Folder Structure

```bash
defect-detection-ai/
├── demo/             # Sample images like sample-street.jpg
├── model/            # Your trained YOLOv8 model as defects.pt
├── app.py            # Streamlit app interface
├── detect.py         # Detection logic
├── requirements.txt  # Dependencies
└── README.md         # Project overview and usage
```

---

## Use Cases

* Manufacturing: detect scratches, dents, and production defects
* Logistics: identify damage to parcels or containers
* E-commerce: auto-flag product image flaws
* Safety: detect missing gear, foreign objects, or improper packaging

---

## Need Help or a Custom Version?

This is a demo project. I offer:

* Custom model training using your data
* Integration into factory workflows or inventory systems
* UI and feature upgrades tailored to your use case

Get in touch via GitHub or Upwork.

---


