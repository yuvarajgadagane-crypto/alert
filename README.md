# ⚡ Student Sleep & Fall Alert System
### Real-Time AI Laptop Camera Drowsiness & Head Slump / Collapse Monitor

An end-to-end, real-time Computer Vision web application designed for students and online learners. The system uses a standard laptop webcam to monitor student alertness, detects when eyes close (sleeping) or when the student's head slumps forward/falls down, and immediately triggers an attention-grabbing buzzer alert with visual strobe notifications.

---

## 🌟 Key Features

1. **Dual AI Detection Engine**:
   - **Eye Aspect Ratio (EAR) Sleep Detection**: Tracks 468 3D facial landmarks via MediaPipe Face Mesh. Computes the geometric ratio of eyelid distances to detect closed eyes with millisecond precision.
   - **Head Slump & Fall-Down Detection**: Estimates 3D head pitch (chin-to-chest nodding) and vertical nose displacement. Triggers an alert if a student collapses onto their desk or falls out of frame.
2. **Instant Web Audio API Buzzer Synthesizer**:
   - Zero external audio files required! Synthesizes high-decibel electric buzzers, emergency sirens, and digital alarm beeps directly inside the browser.
   - Includes speech synthesizer: *"Attention! Student drowsiness detected. Wake up!"*
   - Volume control slider and instant audio test button.
3. **Interactive HUD & Telemetry Dashboard**:
   - Live oscilloscope waveform plotting the student's EAR in real-time.
   - Real-time biometrics: Eye closure index, head tilt angle, total blinks, and blink rate (BPM) for digital eye strain monitoring.
   - One-click **"Calibrate Posture"** button that custom-adapts to individual seating height and webcam angles.
4. **Auto-Snapshot & Incident Logger**:
   - Automatically captures a photo evidence snapshot whenever sleep or head drop is detected.
   - Incident history table with timestamps, exact trigger reasons, and image preview modal.
   - **Export to CSV**: Export incident logs directly for college project reports and professor evaluation.
5. **Study Productivity Metrics**:
   - Built-in session timer and real-time **Focus Score (%)** calculation.
6. **100% Client-Side & Private**:
   - All computer vision inferences occur locally on your machine. No camera video is ever uploaded to any cloud server.

---

## 📐 Detection Mathematical Formulates

### 1. Eye Aspect Ratio (EAR)
For each eye, 6 key landmark coordinates are extracted from the 468-point face mesh:
- Outer corner: $p_1$
- Inner corner: $p_4$
- Upper eyelid points: $p_2, p_3$
- Lower eyelid points: $p_6, p_5$

$$\text{EAR} = \frac{\|p_2 - p_6\| + \|p_3 - p_5\|}{2 \cdot \|p_1 - p_4\|}$$

- **Open Eye**: $\text{EAR} \approx 0.28 - 0.35$
- **Closed Eye**: $\text{EAR} < 0.21$
- **Sleep Trigger**: If $\text{EAR} \le \text{Threshold}$ continuously for $\ge 1.5\text{ seconds}$ (customizable).

### 2. Head Slump & Pitch Tilt Angle
Using 3D coordinates of forehead ($p_{10}$), nose tip ($p_1$), and chin ($p_{152}$):

$$\Delta y = y_{\text{chin}} - y_{\text{forehead}}, \quad \Delta z = z_{\text{chin}} - z_{\text{forehead}}$$

$$\theta_{\text{pitch}} = \text{atan2}(\Delta z, \Delta y) \times \frac{180}{\pi}$$

When the student nods off forward or slumps towards their desk, $\theta_{\text{pitch}} > 28^\circ$ or normalized vertical drop $\Delta Y_{\text{nose}} > 0.14$, triggering the **Head Slump Alert**.

---

## 🚀 How to Run the Project

### Option 1: 1-Click Launch (Recommended for Windows)
1. Navigate to the project folder:
   ```
   c:\Users\Asus\Downloads\student_sleep_alert
   ```
2. Double-click **`run_system.bat`**.
3. It will launch the local Python server and automatically open the application in your default web browser (`http://localhost:8000/index.html`).

---

### Option 2: Run via Python Terminal
```bash
cd c:\Users\Asus\Downloads\student_sleep_alert
python server.py
```
Then open your browser at:
`http://localhost:8000/index.html`

---

### Option 3: Deploy to a Website / Hosting
Because this application is built with standard HTML5, CSS3, and JavaScript, you can host it for free on:
- **GitHub Pages**: Push this repository to GitHub, go to Settings -> Pages -> Deploy from Branch.
- **Vercel / Netlify / Render**: Drag and drop the folder to deploy instantly with HTTPS.
*(Note: Webcams require either `localhost` or HTTPS URLs for browser security permissions).*

---

## 📂 Project Directory Structure

```
student_sleep_alert/
│
├── index.html            # Main responsive web application interface
├── css/
│   └── style.css         # Glassmorphic cyber dark theme styling
├── js/
│   ├── audio.js          # Web Audio API buzzer sound synthesizer & speech engine
│   ├── detector.js       # MediaPipe Face Mesh, EAR & Head Slump detection algorithms
│   └── app.js            # UI controller, oscilloscope chart, snapshot logger
├── server.py             # Zero-dependency local web server with auto-browser launch
├── run_system.bat        # 1-click Windows batch launcher
├── README.md             # Project documentation and quickstart
└── PROJECT_REPORT.md     # Ready-to-submit College / School Academic Project Report
```

---

## 🧪 How to Demonstrate in Project Viva / Evaluation

1. **Start Monitoring**: Click **"Start Camera Monitoring"** and allow webcam access.
2. **Calibrate**: Sit upright, look into the camera, and click **"Calibrate Posture"**.
3. **Demonstrate Sleep Detection**:
   - Close both eyes for 1.5 - 2 seconds.
   - The buzzer will immediately buzz loudly, screen will flash red, and an incident snapshot will be logged in the table below.
   - Open eyes to automatically silence the buzzer.
4. **Demonstrate Head Fall / Slump**:
   - Bow your head downwards towards your chest or slump down towards the table.
   - The system detects the pitch angle exceeds threshold and sounds the alarm: *"Head Nodding Off Alert!"*
5. **Show Export Feature**:
   - Click **"Export CSV Report"** to show real-time logged data ready for academic grading.
