# Percentage Calculater
total_marks = 500

# Input for subjects
math = float(input("Enter your maths mark :"))
science = float(input("Enter your science mark :"))
islamiat = float(input("Enter your islmiat mark :"))
chemistry = float(input("Enter your chemistry mark :"))
biology = float(input("Enter your biology mark :"))


obtained_marks = math + science + islamiat + chemistry + biology

print ("The total Marks in all subjects obtained by you:" , obtained_marks)
# calculate Percentage
percentage = (obtained_marks / total_marks) * 100  # by using the formula
# displaying the Percentage

print ("Your Percentage is :", percentage)






