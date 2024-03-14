
def get_income_tax(pay):
    personal_allowance = 11850
    tax_20 = 0.20
    tax_40 = 0.40
    tax_45 = 0.45
    
    if pay <= personal_allowance: 
        tax = 0

    elif pay <= 34500:
        tax = (pay - personal_allowance) * tax_20
    
    
    elif pay <= 150000:
        tax = (34500 - personal_allowance)* tax_20 + (pay - 34500) * tax_40
    
    
    else:
        tax = (34500- personal_allowance) * tax_20 + (150000 - 34500)* tax_40 + (pay - 150000) * tax_45

    return tax 
pay_insert = int(input("enter your salary: "))

tax_amount = get_income_tax(pay_insert)

print(f"The income tax for your salary of £{pay_insert} is £{tax_amount}")