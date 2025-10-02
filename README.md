# Quiz App (FastAPI + React Native with Expo)

This is a **test project for an academic group**.  
It includes a simple **FastAPI backend** that serves quiz questions and a **React Native frontend** (using Expo) that consumes them.

---

## 📂 Project Structure

.
├── backend/ # FastAPI server (main.py + venv)
├── frontend/ # React Native app (Expo)
└── README.md

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/quiz-app.git
cd quiz-app
```
🖥️ Backend Setup (FastAPI)
Open the backend folder in a new VS Code window:

```bash
cd backend
code .
```
Activate the virtual environment:

On Linux/Mac:

```bash
Copiar código
source venv/bin/activate
```
On Windows:

```bash
venv\Scripts\activate
```
Install FastAPI and Uvicorn (if not already installed):

```bash
pip install fastapi uvicorn
```
Run the backend server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
The backend will now be running at:

```arduino
http://localhost:8000
```
Example endpoint:

```bash
http://localhost:8000/questions
```
📱 Frontend Setup (React Native with Expo)
Open the frontend folder in another VS Code window:

```bash
cd frontend
code .
```
Install dependencies:

```bash
npm install
Start the app with Expo:
```
```bash
npx expo start
```
Run the app on:
Your physical device (scan the QR code with Expo Go).

iOS | iOS Simulator.

Android | Android Emulator.

🔄 Connecting Frontend to Backend
In frontend/App.js, update the backend URL to match your local IP address:

```js
axios.get("http://<your-local-ip>:8000/questions")
```
On Windows: run ipconfig to check your local IP.

On Mac/Linux: run ifconfig.

⚠️ Using localhost directly won’t work unless the backend and Expo run inside the same environment (like an emulator). Always use your LAN IP.

✅ Features
Backend serves quiz questions (/questions endpoint).

Frontend fetches and displays questions.

Multiple-choice answers with validation.

Success animation if all answers are correct.

📦 Requirements
Backend: Python 3.9+, FastAPI, Uvicorn

Frontend: Node.js 16+, Expo CLI, React Native

📝 Notes
This project is for academic testing purposes, not production use.

You need two VS Code windows:

One for running the backend (backend/main.py with FastAPI).

One for running the frontend (Expo app).

📜 License
Free to use and modify for academic purposes.
