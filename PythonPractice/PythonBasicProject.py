#Resturant Management System

#Made by Ibtesam Hussain _(BASIC PYTHON MANAGEMENT SYSTEM)

from array import *

def MainMenu() :
    print("\t\tHELLO WELCOME TO ABC RESTAURANT")   
    print("\t\t-------------------------------------")
    print("\t\t\t\tMENU")
    print("\t\t\t\t----")
    print("\t1.Desi Cuisine\t2.Fast Foods\t3.Desserts\t4.Drinks")
    print("\nWhat would you like to order?\n-----------------------------")
    while (True) :
      print("To proceed further please select any item.....\n----------------------------------------------")
      choice = input()
      
      match choice :
            case '1' :
              DesiCuisine()
              OrderFromCustomer()
            case '2' :
              FastFoods()
              OrderFromCustomer()
            case '3' :
              Desserts()
              OrderFromCustomer()
            case '4' : 
              Drinks()
              OrderFromCustomer()
            case _ :
              print("Invalid")
      print("Would you like to place any other order...(y/n) ")
      another = input()        
      if (another == 'n' or another == 'N') :
         print("HAVE A NICE DAY")
         break        
        

def DesiCuisine() :
    print("\t\t\t\tDesi Cuisine Menu")
    print("\t\t\t\t-----------------")
    print("\t1.Biryani\t2.Qorma\t\t3.Pulao\t\t4.Karhai\t5.Tikka\t\t6.BBQ")
    
                        
def FastFoods() :
    print("\t\t\t\tFast Foods Menu")
    print("\t\t\t\t---------------")
    print("\t1.Zinger Burger\t2.French Fries\t\t3.Sandwiches\t\t4.Broasts\t5.Pizza\t\t6.Pizza Fries")


def Desserts() :
    print("\t\t\t\tDesserts Menu")
    print("\t\t\t\t-------------")
    print("\t1.Falooda\t2.Ice Cream\t\t3.Waffers\t\t4.Custards\t5.Milk Shakes")


def Drinks() :
    print("\t\t\t\tDrinks Menu")
    print("\t\t\t\t-----------")
    print("\t1.Cold Drinks\t2.Limca\t\t3.Water Bottles")
    

def OrderFromCustomer() :
  order = []
  n = int(input("Enter the quantity of your order (How many things you want to order): "))  #kitny order hain uss hisab se array chalega
  for i in range(n) :
        temp = input(f'Enter your {i+1} order : ')
        order.append(temp)
    
  print("Here is the order, you selected : ")
  print(order)  
  #quantity of ordered items
  orderwithquantity = []
  for i in range(n) :
      temp1 = int(input(f'Enter quantity of {order[i]} : '))
      orderwithquantity.append(temp1)
  print("Here is your order with quantities")
  print(order, orderwithquantity)
   #bil of ordered items
  orderwithbiling = []
  for i in range(n) :
      if (order[i] == 'biryani' or order[i] == 'Biryani') :
        temp3 = orderwithquantity[i] * 260
      elif(order[i] == 'Pulao' or order[i] == 'pulao') : 
        temp3 = orderwithquantity[i] * 300
      elif(order[i] == 'Qorma' or order[i] == 'qorma') : 
        temp3 = orderwithquantity[i] * 800
      elif(order[i] == 'Karhai' or order[i] == 'karhai') : 
        temp3 = orderwithquantity[i] * 1200
      elif(order[i] == 'bbq' or order[i] == 'BBQ') : 
        temp3 = orderwithquantity[i] * 700
      elif(order[i] == 'tikka' or order[i] == 'Tikka') : 
        temp3 = orderwithquantity[i] * 500  
      elif(order[i] == 'Cold drink' or order[i] == 'cold drink' or order[i] == 'cold drinks') : 
        temp3 = orderwithquantity[i] * 90
      elif(order[i] == 'Limca' or order[i] == 'limca') : 
        temp3 = orderwithquantity[i] * 70
      elif(order[i] == 'Water Bottle' or order[i] == 'water bottle' or order[i] == 'water bottles') : 
        temp3 = orderwithquantity[i] * 50
      elif(order[i] == 'Milk Shakes' or order[i] == 'milk shakes' or order[i] == 'milk shake') : 
        temp3 = orderwithquantity[i] * 200
      elif(order[i] == 'Custurds' or order[i] == 'custurd' or order[i] == 'custards' or order[i] == 'custard') : 
        temp3 = orderwithquantity[i] * 150
      elif(order[i] == 'Waffers' or order[i] == 'waffers') : 
        temp3 = orderwithquantity[i] * 100  
      elif(order[i] == 'Falooda' or order[i] == 'falooda') : 
        temp3 = orderwithquantity[i] * 300
      elif(order[i] == 'Ice Creams' or order[i] == 'ice creams' or order[i] == 'ice cream') : 
        temp3 = orderwithquantity[i] * 150 
      elif(order[i] == 'Zinger burger' or order[i] == 'zinger burger') : 
        temp3 = orderwithquantity[i] * 200
      elif(order[i] == 'Broasts' or order[i] == 'broasts') : 
        temp3 = orderwithquantity[i] * 250
      elif(order[i] == 'French Fries' or order[i] == 'french fries') : 
        temp3 = orderwithquantity[i] * 100
      elif(order[i] == 'Pizza' or order[i] == 'pizza') : 
        temp3 = orderwithquantity[i] * 1000
      elif(order[i] == 'Pizza Fries' or order[i] == 'pizza fries') : 
        temp3 = orderwithquantity[i] * 200
      elif(order[i] == 'Sandwiches' or order[i] == 'sandwiches') : 
        temp3 = orderwithquantity[i] * 150                             
      orderwithbiling.append(temp3)
  sum = 0
  for i in range(n) :
      sum += orderwithbiling[i]
  print(f'Your Bill : {sum}/- Rs')
  gst = 0.13
  net = sum*gst
  total = net + sum
  print(f'GST : 13%', f'\nTOTAL BILL : {total}')  

  print("THANKYOU FOR ORDERING !")
       
MainMenu()


   


