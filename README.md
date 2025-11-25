# ✂️ BG Remover by rembg for Ngrok Practice

A full-stack web application that removes image backgrounds using the **Rembg** AI library. This project was built to practice deploying local **FastAPI** servers to the public internet using **Ngrok**, specifically focusing on mobile accessibility and handling tunneling headers.

<img width="872" height="871" alt="image" src="https://github.com/user-attachments/assets/88484614-3fc1-4409-a164-112521ef7379" />

## 🎯 Project Goal

The primary goal of this project is to demonstrate:
1.  **AI Integration:** Implementing the U-2-Net model via `rembg` in a Python backend.
2.  **Ngrok Tunneling:** Exposing a localhost server to the public internet for mobile testing.
3.  **CORS & Headers:** Handling `ngrok-skip-browser-warning` headers to make API requests work on mobile devices without manual intervention.

## ✨ Features

* **One-Click Removal:** Upload an image and get a transparent PNG instantly.
* **Mobile-Ready:** Optimized frontend that works on iPhone/Android via Ngrok.
* **Secure Tunneling:** Bypasses Ngrok's free-tier warning page using custom fetch headers.
* **Drag & Drop UI:** Clean interface with a loading spinner and side-by-side comparison.

## 🛠️ Tech Stack

* **Backend:** Python 3.10+, FastAPI, Uvicorn
* **AI Engine:** Rembg (U-2-Net)
* **Frontend:** HTML5, CSS3, Vanilla JavaScript
* **Tunneling:** Ngrok

---

## 🚀 Installation

### 1. Clone the Repo
```bash
git clone https://github.com/imransihab0/bg_remover_ngrok
cd bg-remover-ngrok
```
### 2. Set up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn rembg python-multipart
```

## 🏃‍♂️ Usage Guide
Step 1: Start the Backend
Run the server locally on port 8000.
```bash 
python server.py
```

### Step 2: Start Ngrok (For Mobile/Public Access)
Open a new terminal and expose your local port.

```bash
ngrok http 8000
```

Copy the https forwarding URL provided by Ngrok (e.g., `https://a1b2-c3d4.ngrok-free.app`).

### Step 3: Configure Frontend
1. Open `index.html`.
2. Update the `API_URL` variable in the script section:

```javascript
// Do not add a trailing slash
const API_URL = "[https://your-ngrok-url.ngrok-free.app](https://your-ngrok-url.ngrok-free.app)";
```
### Step 4: Run
Open `index.html` in your browser. If testing on a phone, send the `index.html` file to your phone or host the frontend file on a simple server (like Vercel or GitHub Pages) and point it to your Ngrok API.

## 📂 Project Structure

```text
├── storage/        # Holds original uploads
├── processed/      # Holds transparent PNGs
├── index.html      # Frontend UI
├── server.py       # FastAPI Backend
└── README.md       # This file
```

## 📄 License
This project is for educational purposes. Feel free to use and modify.
