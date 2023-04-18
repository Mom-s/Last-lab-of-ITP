# Assiment 3 of ITP
shoppingCart={}   # Diclering the dictionery
print("Welcome to the AMANDO shopping site \n")
print("Select 1.Add Product to the cart \n")
print("Select 2.Searching the product\n")
print("Select 3.Deleting a product from the cart\n")
print("Select 4.Quit\n")
Options=0
while (Options!=4):# Use while loop for condition that if user enter more then 4 its display wrong input

      

  Options =int(input("Enter your choice (Between 1 to 4): \n"))  #Take input from the user

  if Options ==1:
      user_input = int(input("Enter the number of product you want to added in the stationery shop: "))  # Take another input how many item they wants to enter
  
  
      v=0      
      
     
      while(v<user_input):   
        lll=len(shoppingCart)
        if(lll<5):
            B=input("Enter an item:- ")
            c=input("Enter the brand name:- ")
            shoppingCart.update({B:c})
            print("You added following item t-to the cart")
            print(shoppingCart)         

        else:
          print("Cart is full")
        v=v+1
  
  elif Options ==2:        # using conditon for search the product
      A=input("Enter the Item name:- ")
      k=0
      for i in shoppingCart.keys():
         if(i==A):
           print(i,":",shoppingCart[i])
           k=1
         else:
           pass
      if(k==0):
        print("Item not found")

  elif Options ==3:
      if not shoppingCart:
          print("Your shopping cart is empty. There are no items to delete.")
      else:
          A=input("Enter the product name:-")
          for i in shoppingCart.keys():
            if(i==A):
              shoppingCart.pop(A)
              print("Item deleted successfully")
              k=1
          else:
             pass
          if(k==0):
            print("Item not found")
       
      

  elif Options ==4:
    print ("Thank you!!!")

  else:
    print ("Wrong option entered")




print(shoppingCart)

shoppingCart.update()