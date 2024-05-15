from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import os

uri = "mongodb+srv://nqd230899:Duy%40230223080707@city.tssxt1a.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
mydb = client["Restaurent"]

# ========== Item ========== #
mycol = mydb["Dishes"]

def AddItemValue():
    id = input("Mã: ")
    name = input("Tên món: ")
    price = input("Giá: ")
    mydict = { "dish_id": id, "name": name, "price": price }
    x = mycol.insert_one(mydict)
    print("Success")

def GetItemValue ():
    id = int(input("Mã món: "))

    for x in mycol.find({"dish_id": id },{ }):
        print(x)

def DeleteItemValue ():
    name = input("Tên món: ")

    x = mycol.find({"name": name },{ })
    if x is not None:
        myquery = { "name": name }
        mycol.delete_one(myquery)
        print("Success delete")
    else:
        print("Not found")    

def UpdateItemValue ():
    item = input("Tên món: ")

    x = mycol.find({"name": item },{ })
    if x is not None:
        price = int(input("Price: "))

        myquery = { "name": item } 
        newvalues = { "$set": { "price": price } }
        mycol.update_one(myquery, newvalues)
        print("Success update")
    else:
        print("Not found")

# ========== Staff ========== #
myDishes = mydb["Staff"]

def AddStaffValue():
    id = int(input("Mã: "))
    name = input("Tên nhân viên: ")
    account = input("Tài khoản: ")
    password = input("Mật khẩu: ")
    mydict = { "staff": id, "name": name, "account": account, "password": password }
    x = myDishes.insert_one(mydict)
    print("Success")

def GetStaffValue ():
    id = int(input("Mã nhân viên: "))

    for x in myDishes.find({"staff_id": id },{ }):
        print(x)

def DeleteStaffValue ():
    name = input("Tên nhân viên: ")

    x = myDishes.find({"name": name },{ })
    if x is not None:
        myquery = { "name": name }
        myDishes.delete_one(myquery)
        print("Success delete")
    else:
        print("Not found")    

def UpdateStaffValue ():
    name = input("Tên nhân viên: ")

    x = myDishes.find({"name": name },{ })
    if x is not None:
        pw = input("Password: ")

        myquery = { "name": name } 
        newvalues = { "$set": { "password": pw }}
        myDishes.update_one(myquery, newvalues)
        print("Success update")
    else:
        print("Not found")

# ========== Menu ========== #
def exit_function():
    print("Bạn đã chọn chức năng thoát.")
    quit() 

def MenuSearch ():
    os.system('cls')
    print("==== Search ====")
    print("1. Item")
    print("2. Staff")
    print("0. Back")
    print("==============\n")

    switcher = {
        "1": GetItemValue,
        "2": GetStaffValue,
        "0": main
    }

    while True:
        choice = input("Choose colection: ").lower()
        # Sử dụng get() để xử lý trường hợp lựa chọn không hợp lệ
        selected_function = switcher.get(choice)
        if selected_function:
            selected_function()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

def MenuAdd ():
    os.system('cls')
    print("==== Add ====")
    print("1. Item")
    print("2. Staff")
    print("0. Back")
    print("==============\n")

    switcher = {
        "1": AddItemValue,
        "2": AddStaffValue,
        "0": main,
    }

    while True:
        choice = input("Choose colection: ").lower()
        # Sử dụng get() để xử lý trường hợp lựa chọn không hợp lệ
        selected_function = switcher.get(choice)
        if selected_function:
            selected_function()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

def MenuUpdate ():
    os.system('cls')
    print("==== Update ====")
    print("1. Item")
    print("2. Staff")
    print("0. Back")
    print("==============\n")

    switcher = {
        "1": UpdateItemValue,
        "2": UpdateStaffValue,
        "0": main
    }

    while True:
        choice = input("Choose colection: ").lower()
        # Sử dụng get() để xử lý trường hợp lựa chọn không hợp lệ
        selected_function = switcher.get(choice)
        if selected_function:
            selected_function()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

def MenuDelete ():
    os.system('cls')
    print("==== Delete ====")
    print("1. Item")
    print("2. Staff")
    print("0. Back")
    print("==============\n")

    switcher = {
        "1": DeleteItemValue,
        "2": DeleteStaffValuem,
        "0": main,
    }

    while True:
        choice = input("Choose colection: ").lower()
        # Sử dụng get() để xử lý trường hợp lựa chọn không hợp lệ
        selected_function = switcher.get(choice)
        if selected_function:
            selected_function()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


def main():
    os.system('cls')
    print("==== Menu ====")
    print("1. Search")
    print("2. Add")
    print("3. Update")
    print("4. Delete")
    print("4. Exit")
    print("==============\n")

    switcher = {
        "1": MenuSearch,
        "2": MenuAdd,
        "3": MenuUpdate,
        "4": MenuDelete,
        "0": exit_function
    }

    while True:
        choice = input("Lựa chọn chức năng: ").lower()
        # Sử dụng get() để xử lý trường hợp lựa chọn không hợp lệ
        selected_function = switcher.get(choice)
        if selected_function:
            selected_function()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == '__main__':
    main()
