#Main app 
import admin_details
import user_details

class FoodOrderApp:
    def execute(self,choice):
        if choice == 1:
            admin_obj = admin_details.Admin_Details()
            print("-----------------------------------")
            print("------Create Admin Account---------")
            print("-----------------------------------")
            admin_obj.add_admin()  
        elif choice == 2:
            user_obj = user_details.User_Details()
            print("-----------------------------------")
            print("------Create User Account---------")
            print("-----------------------------------")
            user_obj.add_user()
        elif choice == 3:
            print("-----------------------------------")
            print("********Admin Login!********")
            print("-----------------------------------")
            admin_obj = admin_details.Admin_Details()
            admin_info_list = admin_details.admin_info
            a_uname = input("Enter Your User Name :")
            print("-----------------------------------")
            a_pass = input("Enter your Password :")
            for k,v in admin_info_list.items():
                if (a_uname == v.admin_username and a_pass == v.admin_password):
                    print("-----------------------------------")
                    print("Login Succesfull !")
                    print("-----------------------------------")
                    while True:
                        print("Select... \n1.Add Food Item\n2.Edit Food Item \n3.View Food Item List \n4.Delete Food Item\n5.Press 0 to return to the Main Menu")
                        print("-----------------------------------")
                        admin_choice = int(input("Enter Your Choice :"))
                        print("-----------------------------------")
                        if admin_choice == 1:
                            admin_obj = admin_details.Admin_Details()
                            admin_obj.add_food_item()
                        elif admin_choice == 2:
                            admin_obj = admin_details.Admin_Details()
                            admin_obj.edit_food_item()
                        elif admin_choice == 3:
                            admin_obj = admin_details.Admin_Details()
                            admin_obj.view_food_item()
                        elif admin_choice == 4:
                            admin_obj = admin_details.Admin_Details()
                            admin_obj.delete_food_item()
                        elif admin_choice == 0:
                            break
                        else:
                            print("Wrong Choice, Please Try Again!")
                            print("Redirecting.....")

                else:
                    print("-----------------------------------")
                    print("Wrong Credentials, Please Try Again")
                    break

        elif choice == 4:
            print("-----------------------------------")
            print("********User Login!********")
            print("-----------------------------------")
            user_obj = user_details.User_Details()
            user_info_list = user_details.user_info
            u_uname = input("Enter Your User Name :")
            print("-----------------------------------")
            u_pass = input("Enter your Password :")
            for k,v in user_info_list.items():
                if (u_uname == v.user_username and u_pass == v.user_password):
                    print("-----------------------------------")
                    print("Login Succesfull !")
                    print("-----------------------------------")
                    while True:
                        print("Select... \n1.Place New Order\n2.Order History \n3.Update Profile \n4.Press 0 to return to the Main Menu\n")
                        print("-----------------------------------")
                        user_choice = int(input("Enter Your Choice :"))
                        print("-----------------------------------")
                        if user_choice == 1:
                            user_obj = user_details.User_Details()
                            admin_obj = admin_details.Admin_Details()
                            food_info_list = admin_details.food_info
                            print("***********Welcome !***********")
                            print("***********  Menu   ***********")
                            counter = 1
                            for k,v in food_info_list.items():
                                print(counter,"|","Food Name:",v.food_name,"|","Food Price:",v.food_price,"|","Food Quantity:",v.food_qty,"|","Food Discount:",v.food_discount)
                                counter = counter + 1
                            user_obj.place_new_order()

                        elif user_choice == 2:
                            user_obj = user_details.User_Details()
                            user_obj.view_order_history()
                            
                        elif user_choice == 3:
                            user_obj = user_details.User_Details()
                            user_obj.update_profile()
                            
                        elif user_choice == 0:
                            print("-----------------------------------")
                            print("************Redirecting to Main Menu...!************")
                            break
                        else:
                            print("Wrong Choice, Please Try Again!")
                            print("-----------------------------------")
                else:
                    print("-----------------------------------")
                    print("Wrong Credentials, Please Try Again")
                    break

        elif choice == 0:
            print("-----------------------------------")
            print("Bye !")
            quit()
            
        else:
            print("-----------------------------------")
            print("Wrong Choice, Please Try Again!")


if __name__ == "__main__":
    app_obj = FoodOrderApp()
    while True:
        print("-----------------------------------")
        print("Select... \n1.Press 1 to create Admin Account \n2.Press 2 to create User/Customer Accouunt\n3.Press 3 for Admin Login\n4.Press 4 for User Login\n5.Press 0 to exit the application ")
        print("-----------------------------------")
        choice = int(input("Enter your choice :"))
        app_obj.execute(choice)