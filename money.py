amount=int(input("Please enter the amount of money for withdrawal."))
note_1= amount//100
note_2= (amount%100)//50
note_3= ((amount%100)%50)//10
print("The number of 100 dollar notes is:", note_1)
print("The number of 50 dollar notes is:", note_2)
print("The number of 10 dollar notes is:", note_3)