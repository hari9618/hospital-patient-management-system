from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from datetime import date
import os

import database_models
from database import SessionLocal, engine
from models import (
    PatientCreate, PatientResponse,
    DoctorCreate, DoctorResponse,
    AppointmentCreate, AppointmentResponse
)

# -------------------------------------------------
# Create App
# -------------------------------------------------
app = FastAPI(title="Hospital Patient Management System API")

# -------------------------------------------------
# CORS (For Streamlit Deployment)
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # after project you can restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# Create Tables AFTER app starts (Important for Render)
# -------------------------------------------------
@app.on_event("startup")
def startup():
    database_models.Base.metadata.create_all(bind=engine)

# -------------------------------------------------
# Database Dependency
# -------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =================================================
# ================= PATIENT APIs ==================
# =================================================

@app.get("/")
def home():
    return {"message": "Hospital API Running Successfully 🚀"}

@app.get("/patients", response_model=list[PatientResponse])
def get_patients(db: Session = Depends(get_db)):
    return db.query(database_models.Patient).order_by(database_models.Patient.id).all()


@app.get("/patients/{patient_id}", response_model=PatientResponse)
def get_patient_by_id(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(database_models.Patient).filter(
        database_models.Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    return patient


@app.post("/patients")
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    new_patient = database_models.Patient(**patient.model_dump())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return {"message": "Patient added successfully"}

@app.put("/patients/{patient_id}")
def update_patient(patient_id: int, patient: PatientCreate, db: Session = Depends(get_db)):

    db_patient = db.query(database_models.Patient).filter(
        database_models.Patient.id == patient_id
    ).first()

    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    for key, value in patient.model_dump().items():
        setattr(db_patient, key, value)

    db.commit()
    db.refresh(db_patient)

    return {"message": "Patient updated successfully"}


@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):

    db_patient = db.query(database_models.Patient).filter(
        database_models.Patient.id == patient_id
    ).first()

    if not db_patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    db.delete(db_patient)
    db.commit()

    return {"message": "Patient deleted successfully"}

# =================================================
# ================= DOCTOR APIs ===================
# =================================================

@app.get("/doctors", response_model=list[DoctorResponse])
def get_doctors(db: Session = Depends(get_db)):
    return db.query(database_models.Doctor).order_by(database_models.Doctor.id).all()


@app.post("/doctors")
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    new_doctor = database_models.Doctor(**doctor.model_dump())
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)
    return {"message": "Doctor added successfully"}


@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):

    db_doctor = db.query(database_models.Doctor).filter(
        database_models.Doctor.id == doctor_id
    ).first()

    if not db_doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    db.delete(db_doctor)
    db.commit()

    return {"message": "Doctor deleted successfully"}

# =================================================
# ============== APPOINTMENT APIs =================
# =================================================

@app.get("/appointments", response_model=list[AppointmentResponse])
def get_appointments(db: Session = Depends(get_db)):
    return db.query(database_models.Appointment).order_by(database_models.Appointment.id).all()


@app.post("/appointments")
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):

    patient = db.query(database_models.Patient).filter(
        database_models.Patient.id == appointment.patient_id
    ).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    doctor = db.query(database_models.Doctor).filter(
        database_models.Doctor.id == appointment.doctor_id
    ).first()

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    if appointment.appointment_date < date.today():
        raise HTTPException(status_code=400, detail="Cannot book past date")

    existing = db.query(database_models.Appointment).filter(
        database_models.Appointment.doctor_id == appointment.doctor_id,
        database_models.Appointment.appointment_date == appointment.appointment_date,
        database_models.Appointment.appointment_time == appointment.appointment_time
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Doctor already booked at this time")

    new_appointment = database_models.Appointment(**appointment.model_dump())
    db.add(new_appointment)
    db.commit()
    db.refresh(new_appointment)

    return {"message": "Appointment booked successfully"}