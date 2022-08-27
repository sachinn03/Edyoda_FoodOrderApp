# This class is used for defining the User Credtentials

class User_Cred:
    def __init__(self,user_username,user_password, user_first_name,user_last_name,user_email,user_mobileno,user_address):
        self.user_username = user_username
        self.user_password = user_password
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.user_email = user_email
        self.user_mobileno = user_mobileno
        self.user_address = user_address
    
    def get_user_username(self):
        return self.user_username

    def set_user_username(self,user_username):
        self.user_username = user_username

    def get_user_password(self):
        return self.user_password

    def set_user_password(self,user_password):
        self.user_password = user_password

    def get_user_first_name(self):
        return self.user_first_name

    def set_user_first_name(self,user_first_name):
        self.user_first_name = user_first_name

    def get_user_last_name(self):
        return self.user_last_name

    def set_user_last_name(self,user_last_name):
        self.user_last_name = user_last_name

    def get_user_email(self):
        return self.user_email

    def set_user_email(self,user_email):
        self.user_email = user_email

    def get_user_mobileno(self):
        return self.user_mobileno

    def set_user_mobileno(self,user_mobileno):
        self.user_mobileno = user_mobileno
    
    def get_user_address(self):
        return self.user_address

    def set_user_address(self,user_address):
        self.user_address = user_address