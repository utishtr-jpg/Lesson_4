print("Enter the number of marks you earned in subjects.")
math=int(input("Math: "))
reading=int(input("Reading: "))
social_studies=int(input("Social Studies: "))
science=int(input("Science: "))
sum= math + reading + social_studies + science
percentage= (sum / 400) * 100
print("Your percentage is:", percentage)