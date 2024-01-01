class User:
    def __init__(self, user_id, name, email, password, user_type):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.user_type = user_type
        self.appointments = []

    def register(self):
        # Logic for user registration
        print(f"User {self.name} with ID {self.user_id} registered successfully.")

    def login(self):
        # Logic for user login
        print(f"User {self.name} with ID {self.user_id} logged in successfully.")

    def update_profile(self, new_name, new_email, new_password):
        # Logic for updating user profile
        self.name = new_name
        self.email = new_email
        self.password = new_password
        print("User profile updated successfully.")

    def view_appointments(self):
        # Logic for viewing user appointments
        if self.appointments:
            print(f"User {self.name} with ID {self.user_id} has the following appointments:")
            for appointment in self.appointments:
                print(f" - {appointment.date_time} at clinic {appointment.clinic_id}")
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
