create database hospital_db;
use hospital_db;



create table doctors (
    doctor_id int auto_increment primary key,
    name varchar(100),
    specialty varchar(75),
    phone varchar(15)
);
insert into doctors (name, specialty, phone) values
('Dr. Rajesh Kumar', 'Cardiology', '9876543210'),
('Dr. Anjali Mehta', 'Neurology', '9876543211'),
('Dr. Sameer Singh', 'Orthopedics', '9876543212'),
('Dr. Priya Sharma', 'Dermatology', '9876543213');
select * from doctors;


create table patients (
    patient_id int auto_increment primary key,
    name varchar(100),
    age int,
    gender varchar(10),
    phone varchar(15)
);
insert into patients (name, age, gender, phone) values
('Amit Verma', 35, 'Male', '9012345670'),
('Sneha Patel', 28, 'Female', '9012345671'),
('Rohit Sharma', 42, 'Male', '9012345672'),
('Neha Joshi', 31, 'Female', '9012345673');

select * from patients;

create table appointments (
    appointment_id int auto_increment primary key,
    patient_id int,
    doctor_id int,
    appointment_date date,
    purpose varchar(200),
    foreign key (patient_id) references patients(patient_id),
    foreign key (doctor_id) references doctors(doctor_id)
);
insert	into appointments (patient_id, doctor_id, appointment_date, purpose) values
(1, 1, '2025-05-10', 'Chest pain'),
(2, 2, '2025-05-11', 'Headache and dizziness'),
(3, 3, '2025-05-12', 'Knee pain'),
(4, 4, '2025-05-13', 'Skin allergy');
select * from appoinments;

create table billing (
    bill_id int auto_increment primary key,
    appointment_id int,
    amount decimal(10, 2),
    payment_status varchar(20),
    payment_date date,
    foreign key (appointment_id) references appointments(appointment_id)
);

insert into billing (appointment_id, amount, payment_status, payment_date) values
(1, 1500.00, 'Paid', '2025-05-10'),
(2, 2000.00, 'Pending', null),
(3, 1800.00, 'Paid', '2025-05-12'),
(4, 1200.00, 'Pending', null);
select * from billing;
select * from patients;
