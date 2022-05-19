import json
from random import randrange

# loading everything into the menu list
menudata = open("menu.json", "r") #opening the json file in read mode
menulist = json.load(menudata) #converting json into array
menudata.close() #closing the file as we dont need it anymore

# loading available seats
seatsjson = open("seats.json", "r")
availableSeats = json.load(seatsjson)
seatsjson.close()

# the whole point of this class is for the ui, and i dont think the ui will be done
# class menu_item:
#     def __init__(self, arrayindex):
#         itemdata = menulist[arrayindex]
#         self.name = itemdata[0]
#         self.price = itemdata[1]
#         self.image = itemdata[2]

#         # initilize gui when doing ui stuff
class order:
    def __init__(self):
        self.list = []
        self.tablenumber = -1
        self.seatsamount = -1
    def selectSeatAmount(self):
        output = input("how many seats do you want? \n")
        # theres definitely a better way but im too lazy to search it up
        for i in availableSeats:
            if int(output) == i:
                self.seatsamount = int(output)
                return
        print("These are the amount of seats available:")
        print(availableSeats)
        self.selectSeatAmount()
    def loadMenu(self, displaytext):
        output = ""
        if displaytext == False:
            output = input()
        else:
            print("MENU:\n")
            for i,v in enumerate(menulist):
                print(i,"|", v[0], " $" + str(v[1]))
            output = input("\ninput the item number to add it to your cart \nsay 'checkout' to finish ordering \nsay 'cart' to see your order \n")
        if output == "checkout":
            return
        elif output == "cart":
            print("Cart: \n")
            for i in self.list:
                print(i[0], " $", i[1])
            print("")
        elif int(output) <= (len(menulist) - 1):
            self.list.append(menulist[int(output)])
            print("Item Added!")
        else:
            print("invalid item \n")
        self.loadMenu(False)
    def checkout(self):
        # total price calculation
        total = 0
        for i in self.list:
            total += i[1]
        print("Order Submitted! \n")
        print("total price:", "$" + str(total))
        print("table number:", randrange(1, 34))

def main():
    print("Welcome to ___! \n")
    
    neworder = order()
    neworder.selectSeatAmount()
    neworder.loadMenu(True)
    neworder.checkout()

    print("\n Thank you for ordering at ___!")

if __name__ == "__main__":
    main()