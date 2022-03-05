number = 5
if number <= 3:    
    print("Number is smaller than or equal to 3") 
else:  # Optional clause (you can only have one else)
    print("Number is bigger than 3")



    course = 'clarusway'

if course == "clarusway":
    print("you guaranteed the job")
else:
    print("think about it again")




weight = 80
if weight > 100:
    print("That's too heavy!")
elif weight > 75:
    print("I can lift that!")
else:
    print("That's too light!") 



a=6
b=9
print(a>b)



if (a<b):
    print(a-b)


grade=96
    
if grade >= 65:
    print("Passing grade of:")
 
    if grade >= 90:
        print("A")
 
    elif grade >=80:
        print("B")
 
    elif grade >=70:
        print("C")
 
    elif grade >= 65:
        print("D")
 
else:
    print("Failing grade")





audience = "baby"

if audience == "kid":
    print("it is free to go to cinema")
elif audience == "teen":
    print("discounted price!")
elif audience == "adult":
    print("normal price")
else:
    print("No such audience, stay at your home!")


set1 = set('TWELVE PLUS ONE')
set2 = set('ELEVEN PLUS ONE')
if set1==set2:
        print('the 2 sets are the same!')



num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")  



audience_group = 'kid', 'teen', 'adult'

audience = "teen"

if audience in audience_group:
    if audience == "kid":
        print("it is free to go to cinema")
    elif audience == "teen":
        print("discounted price!")
    else: # audience == "adult":
        print("normal price")
else:
    print("No such audience, stay at your home!")




score = int (input("Enter your score :"))

if score >= 90:
    if score >= 95:
        Score_letter="A+"
    else:
        Score_letter="A"
elif score >= 80:
    if score >= 85:
        Score_letter="B+"
    else:
        Score_letter="B"
else:
    Score_letter="below B"

print ("Your degree: %s" % Score_letter)







math_mark = int(input('Please enter the mark: '))

if math_mark >= 95:
    print('A+ (Excellent)')
elif math_mark < 94 and math_mark >= 90:
    print('A (Good)')
elif math_mark < 89 and math_mark >= 85:
    print('B+ (Medium)')
elif math_mark < 84 and math_mark >= 80:
    print('B (Not Bad)')
elif math_mark < 79:
    print('below B' or 'B-')
else:
    print('F (Failed)')


