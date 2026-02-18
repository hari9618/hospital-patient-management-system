# 🏥 Hospital Patient Management System

A **Full-Stack Hospital Management System** built using **FastAPI, PostgreSQL, and Streamlit**.  
This system allows managing **Patients, Doctors, and Appointments** with a **live dashboard** and CRUD operations.  

---

## 🔗 Live Links

- **Frontend UI (Streamlit):** [Open Streamlit App]https:(//hospital-patient-management-system-l928zbdcygfcniaowcz9pn.streamlit.app/)
- **Backend API (FastAPI):** [Open API on Render](https://hospital-patient-management-system-4.onrender.com)  
- **Database (PostgreSQL):** Hosted on cloud (managed by Render)

---

## 🛠 Tech Stack

- **Backend:** Python, FastAPI, SQLAlchemy  
- **Database:** PostgreSQL (Cloud)  
- **Frontend:** Streamlit  
- **Deployment:** Render (Backend + DB), Streamlit Cloud (Frontend)  
- **Features:** RESTful API with Swagger Docs, CORS Enabled, CRUD operations  

---

## ⚡ Features

- ✅ **Patient Management:** Add, Update, Delete, View Patients  
- ✅ **Doctor Management:** Add, Update, Delete, View Doctors  
- ✅ **Appointment Management:** Schedule, Update, Cancel, View Appointments  
- ✅ **Dashboard:** Quick overview of total patients, doctors, appointments  
- ✅ **Animations:** Balloons on Add, Snow on Delete  
- ✅ **Swagger API Docs:** `/docs` endpoint for backend testing  

---

## 📸 Screenshots

![Dashboard](<img width="956" height="434" alt="dashboard" src="https://github.com/user-attachments/assets/f17ca91d-830d-4215-a2cc-e9e54e9096f6" />)  
![Patients](<img width="959" height="435" alt="patients" src="https://github.com/user-attachments/assets/46603605-6149-4527-8e91-c967ca8815e2" />
)  
![Doctors](<img width="959" height="437" alt="doctors" src="https://github.com/user-attachments/assets/c3838db6-f4c4-4601-8762-ed64daa29f67" />
)  
![Appointments](<img width="958" height="440" alt="Appointments" src="https://github.com/user-attachments/assets/5ab88095-61f7-478d-9d06-b263c4a107d0" />
)  

---

## 📌 Future Improvements

- Authentication & Role-Based Access  
- JWT Security for API  
- Docker Deployment for easy setup  
- Admin Dashboard Analytics & Charts  
- Payment / Billing Integration  
- Multi-user support  

---

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Hospital-Patient-Management-System.git
   cd Hospital-Patient-Management-System
2️⃣ Backend Setup: 
           '''bash
                 cd backend
                 python -m venv env
                 source env/bin/activate  # Linux/Mac
                .\env\Scripts\activate   # Windows
                pip install -r requirements.txt
                uvicorn main:app --reload
      OPEN SWAGGER DOCS:http://127.0.0.1:8000/docs
3️⃣ Frontend Setup:
           '''bash
                   cd ../frontend
                   pip install -r requirements.txt
            Update API_URL in app.py to your local backend:
            API_URL = "http://127.0.0.1:8000"
            RUN Streamlit:
                      '''bash
                         streamlit run app.py
💡 Notes
Ensure the backend is running before opening the frontend.
All CRUD operations are fully functional.
Live deployment links make it easy to test without local setup.
Success animations: balloons on add, snow on delete, for better UX.
📜 License
This project is open-source and free to use.
                         
                
   
   
