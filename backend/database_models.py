from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from database import Base

# ---------------- PATIENT TABLE ----------------
class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    phone = Column(String)
    address = Column(String)
    problem = Column(String)

    appointments = relationship("Appointment", back_populates="patient", cascade="all, delete")


# ---------------- DOCTOR TABLE ----------------
class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialization = Column(String)
    phone = Column(String)

    appointments = relationship("Appointment", back_populates="doctor", cascade="all, delete")


# ---------------- APPOINTMENT TABLE ----------------
class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    appointment_date = Column(Date)
    appointment_time = Column(Time)
    status = Column(String)

    patient_id = Column(Integer, ForeignKey("patients.id", ondelete="CASCADE"))
    doctor_id = Column(Integer, ForeignKey("doctors.id", ondelete="CASCADE"))

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")