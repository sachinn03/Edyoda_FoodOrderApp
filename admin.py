# This class is used for defining and setting the Admin Credtentials

class Admin_Cred:
    def __init__(self,admin_username,admin_password,admin_first_name,admin_last_name,admin_email,admin_mobileno,admin_address):
        self.admin_username = admin_username
        self.admin_password = admin_password
        self.admin_first_name = admin_first_name
        self.admin_last_name = admin_last_name
        self.admin_email = admin_email
        self.admin_mobileno = admin_mobileno
        self.admin_address = admin_address
    
    def __str__(self):
        return "Admin Username :{self.admin_username}\nAdmin Password :{self.admin_password}\nAdmin First Name :{self.admin_first_name} \nAdmin Last Name :{self.admin_last_name}\nAdmin Email :{self.admin_email}\nAdmin Mobile :{self.admin_mobileno}\nAdmin Address :{self.admin_address}"
    
    def get_admin_username(self):
        return self.admin_username

    def set_admin_username(self,admin_username):
        self.admin_username = admin_username

    def get_admin_password(self):
        return self.admin_password

    def set_admin_password(self,admin_password):
        self.admin_password = admin_password

    def get_admin_first_name(self):
        return self.admin_first_name

    def set_admin_first_name(self,admin_first_name):
        self.admin_first_name = admin_first_name

    def get_admin_last_name(self):
        return self.admin_last_name

    def set_admin_last_name(self,admin_last_name):
        self.admin_last_name = admin_last_name

    def get_admin_email(self):
        return self.admin_email

    def set_admin_email(self,admin_email):
        self.admin_email = admin_email

    def get_admin_mobileno(self):
        return self.admin_mobileno

    def set_admin_mobileno(self,admin_mobileno):
        self.admin_mobileno = admin_mobileno
    
    def get_admin_address(self):
        return self.admin_address

    def set_admin_email(self,admin_address):
        self.admin_address = admin_address