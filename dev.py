def main():
    while True:
        s_o = input("s.o:")
        print("1")
        print("2")
        if s_o=='1':
            User.register()
        if s_o=="2":
            User.login()
            username=input("username")
            password=input("password")





import sqlite3
from datetime import datetime


class User:
    def __init__(self, user_id, name, email, password, user_type):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.user_type = user_type

    @classmethod
    def register(cls, username, email, password, user_type):
        # ایجاد اتصال به دیتابیس
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # ایجاد جدول اگر وجود نداشته باشد
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    email TEXT,
                    password TEXT,
                    user_type TEXT
                )
            ''')

        # ایجاد شناسه یکتا برای کاربر
        user_id = int(datetime.now().timestamp())

        # درج اطلاعات کاربر به دیتابیس
        cursor.execute('''
                INSERT INTO users (user_id, username, email, password, user_type)
                VALUES (?, ?, ?, ?, ?)
            ''', (user_id, username, email, password, user_type))

        # ذخیره تغییرات و بستن اتصال
        conn.commit()
        conn.close()

        # ایجاد نمونه جدید از کاربر
        new_user = cls(user_id, username, email, password, user_type)
        return new_user
    def login(self):
        # اتصال به پایگاه داده SQLite
        connection = sqlite3.connect('users_database.db')
        cursor = connection.cursor()

        # اجرای دستور SQL برای ورود کاربر
        cursor.execute('SELECT * FROM users WHERE Email=? AND Password=?', (self.email, self.password))

        # گرفتن اطلاعات کاربر اگر وجود داشته باشد
        user_data = cursor.fetchone()

        # بستن اتصال
        connection.close()

        if user_data:
            print(f"User {user_data[1]} with ID {user_data[0]} logged in successfully.")
        else:
            print("Invalid email or password.")

    def update_profile(self, new_name, new_email, new_password):
        # اتصال به پایگاه داده SQLite
        connection = sqlite3.connect('users_database.db')
        cursor = connection.cursor()

        # اجرای دستور SQL برای به‌روزرسانی پروفایل کاربر
        cursor.execute('''
            UPDATE users
            SET Name=?, Email=?, Password=?
            WHERE UserID=?
        ''', (new_name, new_email, new_password, self.user_id))

        # ذخیره تغییرات و بستن اتصال
        connection.commit()
        connection.close()

        print("User profile updated successfully.")

    def view_appointments(self):
        # اتصال به پایگاه داده SQLite
        connection = sqlite3.connect('users_database.db')
        cursor = connection.cursor()

        # اجرای دستور SQL برای مشاهده نوبت‌های کاربر
        cursor.execute('SELECT * FROM appointments WHERE UserID=?', (self.user_id,))

        # گرفتن نوبت‌های کاربر
        user_appointments = cursor.fetchall()

        # بستن اتصال
        connection.close()

        if user_appointments:
            print(f"User {self.name} with ID {self.user_id} has the following appointments:")
            for appointment in user_appointments:
                print(f" - {appointment[3]} at clinic {appointment[1]}")
        else:
            print("User has no appointments.")

class Clinic:
    def __init__(self, clinic_id, name, address, contact_info, services, availability):
        self.clinic_id = clinic_id
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.services = services
        self.availability = availability
        self.appointments = []

    def add_clinic(self):
        # Logic for adding a clinic
        print(f"Clinic {self.name} with ID {self.clinic_id} added successfully.")

    def update_clinic_info(self, new_name, new_address, new_contact_info, new_services):
        # Logic for updating clinic information
        self.name = new_name
        self.address = new_address
        self.contact_info = new_contact_info
        self.services = new_services
        print("Clinic information updated successfully.")

    def set_availability(self, status):
        # Logic for setting clinic availability
        self.availability = status
        print(f"Clinic availability set to {status}.")

    def view_appointments(self):
        # Logic for viewing clinic appointments
        if self.appointments:
            print(f"Clinic {self.name} with ID {self.clinic_id} has the following appointments:")
            for appointment in self.appointments:
                print(f" - {appointment.date_time} for user {appointment.user_id}")
        else:
            print("Clinic has no appointments.")
class Appointment:
    def __init__(self, appointment_id, clinic_id, user_id, date_time, status):
        self.appointment_id = appointment_id
        self.clinic_id = clinic_id
        self.user_id = user_id
        self.date_time = date_time
        self.status = status

    def book_appointment(self):
        # Logic for booking a patient's appointment
        if self.status == "Available":
            self.status = "Booked"
            print(f"Appointment {self.appointment_id} booked successfully.")
        else:
            print("Appointment is not available for booking.")

    def cancel_appointment(self):
        # Logic for canceling a patient's appointment
        if self.status == "Booked":
            self.status = "Available"
            print(f"Appointment {self.appointment_id} canceled successfully.")
        else:
            print("Appointment is not booked.")

    def reschedule_appointment(self, new_date_time):
        # Logic for rescheduling a patient's appointment
        if self.status == "Booked":
            self.date_time = new_date_time
            print(f"Appointment {self.appointment_id} rescheduled successfully.")
        else:
            print("Appointment is not booked, cannot be rescheduled.")
