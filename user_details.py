#User Functions Class

from collections import Counter
from user import User_Cred
import admin_details
import re
user_info = dict()
order_list = []
order_number = []
order_value = []
order_total = []
class User_Details:
    user_list = []
    def add_user(self):
        user_username = input("Enter your Username :")
        while len(user_username) <=5 :
            if len(user_username) <= 5:
                print("Please enter a Username minimum of 6 characters :")
                user_username = input("Enter your Username :")
            else:
                break
        print("-----------------------------------")
        user_password = input("Enter your Password :")
        while len(user_password) <=7 :
            if len(user_password) <= 7:
                print("Please enter a Password minimum of 8 characters :")
                user_password = input("Enter your Password :")
            else:
                break
        print("-----------------------------------")
        user_first_name = input("Enter your First Name :")
        print("-----------------------------------")
        user_last_name = input("Enter your Last Name :")
        print("-----------------------------------")
        user_email = input("Enter your email :")
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        while True:
            if re.fullmatch(email_regex, user_email):
                print("-----------------------------------")
                break
            else:
                print("Please enter a valid email address !")
                user_email = input("Enter your email :")
        user_mobileno = input("Enter your mobile number :")
        mobileno_regex =r'\b^[7-9]\d{9}$\b'
        while True:
            if re.fullmatch(mobileno_regex, user_mobileno):
                print("-----------------------------------")
                break
            else:
                print("Please enter a valid mobile number !")
                user_mobileno = input("Enter your mobile number :")
        user_address = input("Enter your address :")
        user_obj = User_Cred(user_username,user_password,user_first_name,user_last_name,user_email,user_mobileno,user_address)
        self.user_list.append(user_obj)
        user_info[user_username] = user_obj

    def place_new_order(self):
        food_info_list = admin_details.food_info
        order_qty = int(input("Enter the number of items to order :"))
        while order_qty != 0:
            food_choice = int(input("Enter the food number to order :"))
            if (food_choice <=0) or (food_choice > len(food_info_list)):
                print("-----------------------------------")
                print("Item Not Present")
                print("-----------------------------------")
            else:
                order_number.append(food_choice)
                order_qty = order_qty - 1
                
        for num in order_number:
            for k,v in food_info_list.items():
                item =  list(food_info_list.keys())[num-1]
                if k == item:
                    order_list.append(v.food_name)
                    order_value.append(v.food_price)
            
        print("-----------------------------------")
        print("Your Order Total is Rs.", sum(order_value))
        print("-----------------------------------")
        return order_list,order_value
    def view_order_history(self):
        print("***********Welcome to order history!***********")
        print("-----------------------------------")
        order_items = Counter(order_list).keys()
        order_items_no = Counter(order_list).values()
        order_history_total = dict(zip(order_items,order_items_no))
        print("Food Name  :  Quantity ")
        print("-----------------------------------")
        for k,v in order_history_total.items():
            print(k,"   :  ",v)
        print("-----------------------------------")
        print("Your Order Total is Rs.", sum(order_value))
    def update_profile(self):
        print("***********Update Your Profile!***********")
        print("-----------------------------------")
        while True:
            print("Select... \n1.Update Password \n2.Update Email \n3.Update Mobile No. \n4.Update Address\n5.Press 0 to return to the Main Menu")
            print("-----------------------------------")
            update_choice = int(input("Enter your Choice :"))
            if update_choice == 1:
                edit_user_username = input("Enter your Username :")
                print("-----------------------------------")
                for k,v in user_info.items():
                    if v.user_username == edit_user_username:
                        v.user_password = input("Enter the New Password :")
                        print("-----------------------------------")
                        print("Password Updated Successfully !")
                        print("-----------------------------------")

            elif update_choice == 2:
                edit_user_username = input("Enter your Username :")
                print("-----------------------------------")
                for k,v in user_info.items():
                    if v.user_username == edit_user_username:
                        v.user_email = input("Enter the New Email :")
                        print("-----------------------------------")
                        print("Email Updated Successfully !")
                        print("-----------------------------------")

            elif update_choice == 3:
                edit_user_username = input("Enter your Username :")
                print("-----------------------------------")
                for k,v in user_info.items():
                    if v.user_username == edit_user_username:
                        v.user_mobileno = input("Enter the New Mobile No. :")
                        print("-----------------------------------")
                        print("Mobile No. Updated Successfully !")
                        print("-----------------------------------")

            elif update_choice == 4:
                edit_user_username = input("Enter your Username :")
                print("-----------------------------------")
                for k,v in user_info.items():
                    if v.user_username == edit_user_username:
                        v.user_address = input("Enter the New Address :")
                        print("-----------------------------------")
                        print("Address Updated Successfully !")
                        print("-----------------------------------")

            elif update_choice == 0:
                print("Redirecting to Main Menu...")
                break

            else:
                print("Wrong Choice, Please Try Again!")
                print("Redirecting...")
                print("-----------------------------------")
