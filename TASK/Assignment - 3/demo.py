# Enhanced Student Grade Tracker Solution

print("="*50)
print("         Enhanced Student Grade Tracker")
print("="*50)

# Student ID 
student_id_valid = False

while not student_id_valid:
    student_id = input("Enter ID: ")
    
    # check for positive number & non-alphabet (-101)
    if student_id.startswith("-") and student_id[1:].isdigit():
        print("Please Enter Positive Numbers Only")
    elif student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0:
            student_id_valid = True
        else:
            print("Zero Not Allowed")
    else:
        print("Enter Numbers Only")

formatted_id = "EDIFY" + str(student_id)
print(formatted_id)    


# Student Name
student_name_valid = False
while not student_name_valid:
    student_name = input("Enter Your Name: ")
    
    # remove any spaces at beginning and ending and also we tile cased
    student_name = student_name.strip().title()

    # validate given name
    name_check = student_name.replace(" ","") # remove space in between name 
    
    # is name alphabet only anf also at least 3 characters 
    if name_check.isalpha() and len(student_name) >=3:
        student_name_valid = True
        print("Welcome: "+student_name)
    else:
        if not name_check.isalpha():
            print("Name should contain only alphabets")
        elif len(student_name) < 3:
            print("Name should contain at least 3 characters ")

#Email 
first_name = student_name.split()[0].lower()
generate_email = (f"{first_name}.{student_id}@edify.edu")

print("System Generated Email: " +generate_email)

#Course Fee Calculation 

base_course_fee_valid = False
while not base_course_fee_valid:
    base_course_fee = input("Enter Course Fee: ")
    if base_course_fee.isdigit():
        base_course_fee = int(base_course_fee)
        if base_course_fee > 0:
            base_course_fee_valid = True
        else:
            print("Enter Positive Number For Fee")
    else:
        print("Course Fee can be only numbers")

discount = 0
coupon = input("Enter coupon code")

# if "PROMO" in coupon -> operator 
if coupon.find("PROMO") != -1:
    discount = 5000

# if "PROMO" in coupon -> operator 
# if "PROMO" in coupon:
#     discount = 5000

final_fee = base_course_fee - discount
print(f"Actual Fee: {base_course_fee} ")
print(f"Discount Applied: {discount} ")
print(f"Fee To Pay: {final_fee}")

    