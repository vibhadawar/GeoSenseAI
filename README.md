#  GeoSense AI

AI-powered satellite image analysis and environmental monitoring system built using React, FastAPI, OpenCV, and Firebase Authentication.

#  Overview

GeoSense AI is an intelligent Earth Observation System that analyzes satellite imagery to detect vegetation, water bodies, and urban regions. It provides visual insights, environmental reports, and change detection capabilities through an interactive dashboard.

---

##  Features

### Satellite Image Upload
- Upload remote sensing images for analysis.

### Land Cover Segmentation
Detect
- Vegetation
- Water bodies
- Urban areas
  
### Image Processing Results
- Original image
- Segmented image
- Vegetation mask
- Water mask
- Urban mask

### AI Report Generation
- Automatic environmental summary generation.

###  Interactive Dashboard
- Land Cover Statistics
- Progress Bars
- Pie Chart Visualization
- AI Generated Analysis Report

###  Change Detection
- Compare Two Satellite Images
- Vegetation Change Analysis
- Water Change Analysis
- Urbanization Change Analysis
- Change Heatmap Generation

### Modern UI
- Responsive Design
- Dark Mode Support
- Professional Dashboard Layout
- Smooth Animations
  
### Firebase Authentication
- User Signup
- User Login
- Secure authentication

---

## 🛠 Tech Stack

### Frontend
- React
- Vite
- Tailwind CSS
- Axios
- Recharts
  

### Backend
- FastAPI
- OpenCV
- NumPy
  

### Authentication
- Firebase Authentication


### Mapping & Geospatial
- Leaflet
- GeoJSON
  

### Visualization
- Maatplotlib
- Recharts

---

## 📂 Project Structure

```text
EarthObservationSystemm
│
├── backend
    ├── app.py
    ├── charts.py
│   ├── main.py
│   ├── routes
│   ├── models
│   ├── outputs
│   └── requirements.txt
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   ├── firebase.js
│   │   └── App.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── images
├── models
├── vegetation.geojson
├── README.md
└── .gitignore
```

---

## ⚙ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/GeoSenseAI.git
```

```bash
cd GeoSenseAI
```

---

## Frontend Setup

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run development server:

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## Backend Setup

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv myenv
```

Activate virtual environment:

### Windows

```bash
myenv\Scripts\activate
```

### Linux / Mac

```bash
source myenv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

## 📸 Screenshots

### Login Page
<img width="900" height="652" alt="Screenshot 2026-06-14 181409" src="https://github.com/user-attachments/assets/6560c56f-c818-4dc5-bb9c-8d724740312e" />



### Dashboard
<img width="1890" height="912" alt="Screenshot 2026-06-14 181455" src="https://github.com/user-attachments/assets/bbb8d09d-752d-4e05-a8e4-0dd78e161f85" />

### Feature 
<img width="1896" height="911" alt="Screenshot 2026-06-14 181509" src="https://github.com/user-attachments/assets/f17d1e11-c789-4a36-bda1-208c189fb9ab" />


### Change Detection
<img width="1618" height="612" alt="Screenshot 2026-06-14 181544" src="https://github.com/user-attachments/assets/96c312b4-c956-453a-bcc8-7b8ac23be4bb" />




---

## 🔮 Future Enhancements

- Deep learning segmentation (U-Net)
- NDVI analysis
- Time-series vegetation monitoring
- GIS integration
- Map visualization
- Satellite data APIs 

---

## 👨‍💻 Author

Developed by Vibha

GeoSense AI — Earth Observation Intelligence System
