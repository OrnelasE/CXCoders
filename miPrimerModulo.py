def auth(pin,fun):
    print("Hello Cisconian")
    username_ = input("Enter your cec: \n")
    print("Hello "+ username_)
    password_ = input("\n Now you password: \n")
    print(pin[username_])
    while str(password_) != str(pin[username_]):
        print("wrong password")
        password_ = input("Re-enter password: ")
    print("\n Printing menu \n")
    fun()