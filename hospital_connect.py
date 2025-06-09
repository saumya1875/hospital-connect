# import mysql.connector

# # Connection setup
# connection = mysql.connector.connect(
#     host="localhost",        # या IP address
#     user="root",             # आपका MySQL username
#     password="root",# आपका पासवर्ड
#     database="hospital_db"   # आपने जो DB बनाया है
# )

# # Cursor creation
# cursor = connection.cursor()

# # Example query
# cursor.execute("SELECT * FROM doctors")
# rows = cursor.fetchall()

# # Print results
# for row in rows:
#     print(row)

# # Close the connection
# cursor.close()
# connection.close()

import streamlit as st
import mysql.connector

# Database connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",  # ← अपना पासवर्ड यहाँ डालें
        database="hospital_db"
    )

import base64

def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# UI
st.title("🏥 Hospital Management System")
set_background("download (1).jpg")  # <-- replace with your image filename

menu = st.sidebar.selectbox("Menu", ["Add Doctor", "Add Patient", "Create Appointment", "View Bills", "View Doctors","View  Patient"])

# Add Doctor
if menu == "Add Doctor":
    st.subheader("➕ Add New Doctor")
    set_background("download (1).jpg")  # <-- replace with your image filename


    name = st.text_input("Doctor Name")
    specialty = st.text_input("Specialty")
    phone = st.text_input("Phone Number")

    if st.button("Save Doctor"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO doctors (name, specialty, phone) VALUES (%s, %s, %s)", (name, specialty, phone))
        conn.commit()
        st.success("Doctor added successfully")
        cursor.close()
        conn.close()

# Add Patient
elif menu == "Add Patient":
    set_background("download (2).jpg")  # <-- replace with your image filename

    st.subheader("➕ Add New Patient")
    name = st.text_input("Patient Name")
    age = st.number_input("Age", min_value=0, max_value=120)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    phone = st.text_input("Phone Number")

    if st.button("Save Patient"):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO patients (name, age, gender, phone) VALUES (%s, %s, %s, %s)", (name, age, gender, phone))
        conn.commit()
        st.success("Patient added successfully")
        cursor.close()
        conn.close()

# Create Appointment
elif menu == "Create Appointment":
    set_background("images.jpg")  # <-- replace with your image filename

    st.subheader("📅 Create Appointment")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT patient_id, name FROM patients")
    patients = cursor.fetchall()

    cursor.execute("SELECT doctor_id, name FROM doctors")
    doctors = cursor.fetchall()

    patient = st.selectbox("Select Patient", patients, format_func=lambda x: f"{x[1]} (ID: {x[0]})")
    doctor = st.selectbox("Select Doctor", doctors, format_func=lambda x: f"{x[1]} (ID: {x[0]})")
    date = st.date_input("Appointment Date")
    purpose = st.text_input("Purpose")

    if st.button("Save Appointment"):
        cursor.execute(
            "INSERT INTO appointments (patient_id, doctor_id, appointment_date, purpose) VALUES (%s, %s, %s, %s)",
            (patient[0], doctor[0], date, purpose)
        )
        conn.commit()
        st.success("Appointment saved")
        cursor.close()
        conn.close()

# View Bills
elif menu == "View Bills":
    set_background("images (1).jpg")  # <-- replace with your image filename

    st.subheader("💳 Billing Records")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.bill_id, p.name, b.amount, b.payment_status, b.payment_date
        FROM billing b
        JOIN appointments a ON b.appointment_id = a.appointment_id
        JOIN patients p ON a.patient_id = p.patient_id
    """)
    rows = cursor.fetchall()
    st.table(rows)
    cursor.close()
    conn.close()

# View Doctors
elif menu == "View Doctors":
    st.subheader("👨‍⚕️ All Doctors")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors")
    data = cursor.fetchall()
    st.table(data)
    cursor.close()
    conn.close()

#View  Patient
elif menu == "View  Patient":
    st.subheader("👨‍⚕️ All  Patient")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM  Patients")
    data = cursor.fetchall()
    st.table(data)
    cursor.close()
    conn.close()