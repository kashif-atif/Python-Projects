
print ("Aggregate for NUST")

matric = int(input("Enter your Matric Marks out of 1100: "))
percentage1   = (matric/1100)*100
print ("Percentage in Matric: ", percentage1,"%")
fsc = int(input("Enter your FSC Marks out of 1100: "))
percentage2   = (fsc/1100)*100
print ("Percentage in FSC: ", percentage2,"%")
net = int(input("Enter your NET Marks out of 200: "))
percentage3   = (net/200)*100

aggregate = (percentage1 * 0.10) + (percentage2 * 0.15) + (percentage3 * 0.75)
print ("Aggregate: ", aggregate)

if aggregate >= 85:
    print("Very Good Chance of Admission")
elif aggregate >= 75:
    print("Eligible for Admission")
else:
    print("Not Eligible for Admission")

