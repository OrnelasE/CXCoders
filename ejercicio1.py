#
# Import Section #
# import miPrimerModulo as y
# define function

menu = {
        1: "Change PIN",
        2: "Review Stocks",
        3: "Sell Stocks",
        4: "Deposit Funds",
        5: "Generate Account Statement",
        6: "End Session",
        7: "Exit"
    }

PINs = {
      "Frank": 1234,
      "eornelas" : 1234
}

Name = {
    "user":"Eduardo Ornelas",
    "cec": "eornelas",
    "company":"Cisco"
}
Stocks = {
    "eornelas" : {
        "stocks" : 10200,
        "value" : 1000,
        "market_value" : 1
    }
}
letters = ["a","b","c","d","e","f"]

def test():
    print(menu)

def printMenu():
    for i in range(len(letters)):
        f = i+1
        #print(i)
        print(letters[i]+" : "+menu[f])
    

def buy(Stocks,username_):
    want_to_buy= input("How many stock do you want to buy, remember that you have: " + str(Stocks[username_]["value"]) + " ")
    print(type(Stocks[username_]["value"]))
    if int(want_to_buy) > Stocks[username_]["value"]:
        print("se pasa")
    else:
        print("date")

def sell(Stocks,username_):
    want_to_sell = input("How many stock do you want to sell, remember that you have: " + str(Stocks[username_]["stocks"]) + " ")
    selling = int(want_to_sell)
    if selling > Stocks[username_]["stocks"]:
        print("se pasa")
    else:
        print("date")
        total = selling*Stocks[username_]["market_value"]
        Stocks[username_]["value"] = Stocks[username_]["value"] + total
        print("Now you have "+ str( Stocks[username_]["value"]))

def add(Stocks,username_):
    adding = input("Please introduce how much you want to add to your account: ")
    Stocks[username_]["value"] = Stocks[username_]["value"] + int(adding)
    print("Your new balance is: " + str(Stocks[username_]["value"]))
    return Stocks[username_]["value"]

def openfile(Name, Stocks):
    print("Opening file")
    with open('stocks.txt','w') as file:
        file.write("Name: " + str(Name["user"]) + "\nCECID: " + str(Name["cec"]) +"\nCompany: " + str(Name["company"]) + "\nStock's information: "+ "Stock's Number: "+str(Stocks[Name["cec"]]["stocks"]) + " Stock's value: "+str(Stocks[Name["cec"]]["value"])) 
    
    with open('stocks.txt') as file1: 
        x = file1.read()
        print(x)

def menuJob(option, username_):
    option = int(option)
    print("Option is: " + str(option))
    if option == 1: 
        print("Change PIN")
        pin1 = input("Please type your PIN: ")
        if pin1 != str(PINs[str(username_)]):
            print("wrong password")
        else:
            pin2 = input("Please insert the new pin: ")
            print("New Pin for " + username_ + " is "+pin2)
        printMenu()
    elif option == 2: 
        print("Review Stocks")
        print(username_ + "::" + str(Stocks[str(username_)]["stocks"]) +" || "+ str(Stocks[str(username_)]["value"]) + " || "+ str(Stocks[str(username_)]["market_value"]))
    elif option == 3:
        print("Buy Stocks")
        buy(Stocks, username_)
    elif option == 4:
        print("Sell Stocks")
        sell(Stocks, username_)
    elif option == 5:
        print("Deposit Funds")
        add(Stocks, username_)
    elif option == 6 : 
        print("Generate Account Statement")
        openfile(Name, Stocks)
    elif option == 7:
        print("End Session")
    else:
        print("Exit")
        exit()
    printMenu()


def auth():
    print("Hello Cisconian")
    username_ = input("Enter your cec: \n")
    print("Hello "+ username_)
    password_ = input("\n Now you password: \n")
    # print(PINs[username_])
    while str(password_) != str(PINs[username_]):
        print("wrong password")
        password_ = input("Re-enter password: ")
    print("\n Printing menu \n")
    printMenu()
    return username_

#Main #
if __name__=='__main__':
    username_ = auth()
    while True: 
        option = input("Please be kind to select an option: ")
        menuJob(option, username_)