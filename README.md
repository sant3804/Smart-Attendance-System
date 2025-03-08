# Smart Attendance System (Face Recognition)

## 📌 Project Description  
The **Smart Attendance System** is a Python-based face recognition attendance tracker that automates the attendance process. It uses a webcam to detect and recognize faces, marking attendance in a **CSV file** with timestamps. This system is ideal for schools, colleges, and workplaces to ensure reliable and contactless attendance tracking.

---

## 🚀 Features  
✅ **Face Recognition** – Identifies students using OpenCV & Face Recognition Library  
✅ **Real-time Attendance Logging** – Stores attendance data in a CSV file  
✅ **Live Camera Feed** – Displays detected faces with names  
✅ **One-time Marking** – Prevents duplicate entries  
✅ **Fast & Efficient** – Uses optimized image processing for quick recognition  
✅ **Easy-to-Use** – Just run the script, and it captures attendance automatically  

---

## 🛠️ Tech Stack  
- **Programming Language:** Python  
- **Libraries Used:**  
  - `opencv-python` – For image processing & camera feed  
  - `face-recognition` – For face detection & recognition  
  - `numpy` – For mathematical operations  
  - `datetime` – To record attendance timestamps  
  - `csv` – For storing attendance logs  

---

## 📥 Installation & Setup  

### 1️⃣ Install Dependencies  
Make sure you have Python installed. Then, install the required libraries:  
```sh
pip install opencv-python face-recognition numpy
```

### 2️⃣ Add Known Faces  
- Place images of known individuals in the **same folder as the script**.
- Update the `students_data` dictionary in `attendance.py` with names and corresponding image filenames:  
  ```python
  students_data = {
      "santosh": "santosh.jpg",
      "utkarsh": "utkarsh.jpg",
      "aniket": "aniket.jpg"
  }
  ```

### 3️⃣ Run the Program  
Execute the script using:  
```sh
python attendance.py
```

### 4️⃣ Marking Attendance  
- The system will **detect and recognize faces** in real-time.  
- If a face matches a known entry, attendance will be **marked in a CSV file** named with the current date and time.  
- Press **'q'** to quit the program.  

---

## 📜 License  
This project is available under the **MIT License**.  

---

## 🤝 Contributing  
Feel free to contribute by adding new features or improving accuracy. Fork the repo, make changes, and submit a pull request.  

---

Let me know if you need modifications! 🚀

