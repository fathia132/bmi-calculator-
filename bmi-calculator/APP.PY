# BMI CACULATOR
#STEP 1 :GET USER INPUT

weight = float(input("Please enter your weight in (kg): "))
height = float(input("Please enter your height in (cm): "))

#step 2:calculate BMI
bmi =weight / (height * height)


# step3: Determine category
if bmi < 18.5:
  category ="UNDERWEIGHT"
  Message =" you may need to gain weight"
elif bmi < 25:
  category ="NORMAL WEIGHT"
  message ="you're in a healthy range"
elif bmi < 35:
  category ="OVERWEIGHT"
  message =" YOU'RE  MIGHT NEED TO WATCH YOUR WEIGHT"
elif bmi < 40:
  category ="OBESITY"
  Message =" CONSIDER EXERCISING AND EATING HEALTH"
else:
  category ="OBESITY CLASS III"
  Message =" CONSULT  A DOCTOR ,THIS MIGHT BE VERY RISKY PLEASE ENGAGE IN SOME EXERCISE AND  EAT HEALTH"
#STEP4:DISPLAY RESULT
print(f"\n=== BMI RESULT ===")
print (f"WEIGHT: {weight} kg")
print (f"HEIGHT: {height} m")
print (f"BMI: {bmi: .2f}")
print(f"status: {category}")
print (f"advice: {message}")

