age = int(input("enter your age:"))
bmi = float(input("enter bmi:"))
is_smoker = True
has_pre_existing_sickness = False

base_premium = 500
risk_score = 0

if age < 30:
    age_surcharge = 0
elif age <= 50:
    age_surcharge = 50
    risk_score = risk_score + 4
else:
    age_surcharge = 300
    risk_score = risk_score + 7

if bmi < 18.5 or bmi >= 30:
    bmi_surcharge = 400
    risk_score = risk_score + 8
else:
    bmi_surcharge = 0


if is_smoker:
    smoker_surcharge = 300
    risk_score = risk_score + 10
else:
    smoker_surcharge = 0


if has_pre_existing_sickness:
    condition_surcharge = 400
    risk_score = risk_score + 12
else:
    condition_surcharge = 0

total_premium = base_premium + age_surcharge + bmi_surcharge + smoker_surcharge + condition_surcharge


if risk_score <= 2:
    category = "Low Risk (Standard Premium)"
elif risk_score <= 5:
    category = "Moderate Risk (Moderate Premium)"
else:
    category = "High Risk (High Premium)"

print("Age Surcharge: Rs.", age_surcharge)
print("BMI Surcharge: Rs.", bmi_surcharge)
print("Smoker Surcharge: Rs.", smoker_surcharge)
print("Pre-existing sickness Surcharge: Rs.", condition_surcharge)
print("Total Risk Score:", risk_score)
print("Premium Category:", category)
print("Final Monthly Premium: Rs.", total_premium)

