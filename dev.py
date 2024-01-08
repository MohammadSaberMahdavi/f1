from datetime import datetime
import sqlite3


def main():
    while True:
        print("1.Register")
        print("2.Login")

        Select_Options = input(" Select_Options:")

        if Select_Options == "1":
            register_user()
        if Select_Options == "2":
            login_user()


class User:
    def __init__(self, user_id, username, email, password, user_type):
        self.user_id = user_id
        self.username = username
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

    @classmethod
    def login(cls, username, password):
        # اتصال به دیتابیس
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # جستجو بر اساس نام کاربری و رمز عبور
        cursor.execute('''
            SELECT * FROM users
            WHERE username = ? AND password = ?
        ''', (username, password))

        user_data = cursor.fetchone()

        # بستن اتصال
        conn.close()

        if user_data:
            # ایجاد نمونه کاربر در صورت موفقیت
            user = cls(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
            return user
        else:
            return None

    @classmethod
    def update_profile(cls, user_id, new_username, new_email, new_password):
        # اتصال به دیتابیس
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # جستجو بر اساس شناسه کاربر
        cursor.execute('''
            SELECT * FROM users
            WHERE user_id = ?
        ''', (user_id,))

        user_data = cursor.fetchone()

        if user_data:
            # اگر کاربر با شناسه مورد نظر یافت شد
            # اپدیت اطلاعات
            cursor.execute('''
                UPDATE users
                SET username = ?, email = ?, password = ?
                WHERE user_id = ?
            ''', (new_username, new_email, new_password, user_id))

            # ذخیره تغییرات و بستن اتصال
            conn.commit()
            conn.close()

            # ایجاد نمونه کاربر با اطلاعات به‌روزرسانی شده
            updated_user = cls(user_id, new_username, new_email, new_password, user_data[4])
            return updated_user
        else:
            # اگر کاربر با شناسه مورد نظر یافت نشد
            conn.close()
            return None

    def view_appointments(self):
        # نمایش نوبت‌های اختصاص یافته به کاربر
        dbase = sqlite3.connect('users.db')
        cursor = dbase.cursor()

        view_query = f'''
            SELECT * FROM appointments
            WHERE user_id = ?
        '''

        cursor.execute(view_query, (self.user_id,))
        appointments = cursor.fetchall()

        dbase.close()

        if appointments:
            print("Appointments:")
            for appointment in appointments:
                print(appointment)
        else:
            print("You dont have any Appointments")


def register_user():
    print("Welcome to the Registration Process!")

    # گرفتن ورودی‌های مورد نیاز برای ثبت نام
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    user_type = input("Enter your user type (e.g., patient, staff): ")

    # صدا زدن متد register و دریافت نتیجه
    registered_user = User.register(username, email, password, user_type)

    # چاپ اطلاعات کاربر ثبت شده
    print("\nRegistration Successful!")
    print("User ID:", registered_user.user_id)
    print("Username:", registered_user.username)
    print("Email:", registered_user.email)
    print("User Type:", registered_user.user_type)


def login_user():
    print("Welcome to the Login Process!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    logged_in_user = User.login(username, password)
    if logged_in_user:
        print("\nLogin Successful!")
        print("Username:", logged_in_user.username)
        print("Email:", logged_in_user.email)
        print("User Type:", logged_in_user.user_type)

        print("1.Update Profile")
        print("2")
        print("3.Back")
        Login_Options = input("Login_Options:")
        if Login_Options == "1":
            update_user_profile()

        # if l_o=="2":

        if Login_Options == "3":
            main()
    else:
        print("\nLogin Failed! Invalid username or password.")
        main()


def update_user_profile():
    print("Welcome to the Profile Update Process!")

    # گرفتن ورودی‌های مورد نیاز برای آپدیت پروفایل
    user_id = int(input("Enter your user ID: "))
    new_username = input("Enter your new username (leave empty to keep current): ")
    new_email = input("Enter your new email (leave empty to keep current): ")
    new_password = input("Enter your new password (leave empty to keep current): ")

    # صدا زدن متد update_profile و دریافت نتیجه
    updated_user = User.update_profile(user_id, new_username, new_email, new_password)

    if updated_user:
        print("\nProfile Update Successful!")
        print("Updated User ID:", updated_user.user_id)
        print("Updated Username:", updated_user.username)
        print("Updated Email:", updated_user.email)
        print("Updated User Type:", updated_user.user_type)

        print("\nUser with the provided ID not found. Profile update failed.")


main()
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
        # connect to database
        conn = sqlite3.connect('clinics.db')
        curser = conn.cursor()
        # Create the table if it does not exist
        curser.execute('''
            CREATE TABLE IF NOT EXISTS clinics (
                clinic_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                address TEXT,
                contact_info TEXT,
                services TEXT,
                availability TEXT
            )
        ''') 
        
        # create query
        curser.execute('''
            INSERT INTO clinics (name, address, contact_info, services, availability)''')
        
        # commit changes
        conn.commit()
        # close connection
        conn.close()
        
        # create new clinic object
        new_clinic = Clinic(self.clinic_id, self.name, self.address, self.contact_info, self.services, self.availability)
        print(f"Clinic {self.name} with ID {self.clinic_id} added successfully.")
        return new_clinic
        
        

    def update_clinic_info(self, new_name, new_address, new_contact_info, new_services):
        
        # connect to database
        conn = sqlite3.connect('clinics.db')
        curser = conn.cursor()
        
        # search for clinic with the name of clinic
        curser.execute('''
            select * from clinics 
            where name =?''',
            (new_name,))
        # check if clinic exists
        if curser.fetchone():
            # update the clinic info
            curser.execute('''
                UPDATE clinics
                SET name =?, address =?, contact_info =?, services =?
                WHERE name =?''',
                (new_name, new_address, new_contact_info, new_services, new_name))
            
            # commit changes
            conn.commit()
            # close connection
            conn.close()
            # create new clinic object
            update_clinic = Clinic(self.clinic_id, new_name, new_address, new_contact_info, new_services, self.availability)
            print(f"Clinic {new_name} with ID {self.clinic_id} updated successfully.")
            return update_clinic
        else:
            # close connection
            conn.close()
            print(f"Clinic {self.name} with ID {self.clinic_id} not found.")
            return None
        
        
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
