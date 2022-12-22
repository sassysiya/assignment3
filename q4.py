a=int(input("Enter grade between 4 and 10 :"))
if a<4 or a > 10:
    print("Grade out of range")
else:

    grade=["Outstanding","Excellent","Very Good","Good","Average","Below Average","Poor"]
    performance=["A+","A","B+","B","C+","C","D"]
    print(f"Your grade is {performance[10-a]} and {grade[10-a]} performance.")
