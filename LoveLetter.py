#Using Lambda Function

cm = int(input("Enter length in centimeters:\n"))
cm_to_ft = lambda x: x/30.48
ft = cm_to_ft(cm)
print(f"{cm} cm is equal to {ft:.2f}ft.")