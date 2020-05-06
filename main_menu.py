import admin
'''
1. Register user details.
2. Ability to sign-in and sign-out.
3. Upgrade/downgrade user privileges.
4. Show people who have signed-in for the day.
5. Show people who have signed-out for the day.
6. Admin add and remove users in the system.
if true or if false
save to github
'''

#   display the login screen with the option for new registration.
#   This is the case when new employees or visitors arrive at the premises and would like to enter the building.
#   (Consider this the main screen)


def login_screen():
    log_screen = "Welcome to Life Choices Academy" + "\n"
    log_screen += "What would you like to do" + "\n"
    log_screen += "r) Register as new user" + "\n"
    log_screen += "l) Login as user" + "\n"
    print(log_screen)
    option1 = (input("Choose option (r, l, a):"))
    if option1 == 'r':
        return
    elif option1 == 'l':
        full_name = input("Please enter your fullname")
        username = input("Please enter username")
        password = input("Please enter your password")

    elif option1 == 'a': # When you are on the main screen, by pressing the “a” key, for admin, you should be presented with a new screen to login.
        full_name = input("Please enter your fullname")
        username = input("Please enter username")
        admin.admin_sign_in(full_name, username)

        add_or_delete_user = "Would you like to create or delete a user?"
        add_or_delete_user += "Enter c to create a user account"
        add_or_delete_user += "Enter d to delete a user account"
        option_del_or_add = input("Choose option (c or d):")

login_screen()

#   If the login option is clicked (selected), the user should be presented with the option
#   asking them to enter their full_name, username and password.



