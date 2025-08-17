def calculate_discount(price, discount_precent):
    #The if statement here will check if the  discount added is greater or equal 20
    if discount_precent >= 20:
        final_price = price - float((discount_precent/100*price))
        return final_price
    else:#otherwise return the original price
        return price

 #Prompt the user to enter a price and a discount   
price = float(input("Enter price: "))
discount_percent = float(input("Enter percent(exclude %, just a number): "))

#The input will be displayed to the user according to the inputs
print(f"Price is R{calculate_discount(price,discount_percent)}")
        