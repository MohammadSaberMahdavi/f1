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