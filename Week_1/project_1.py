# Simple interest
def simple_interest(P, R, T): 
    A = P * (1 + (R/100) * T)
    return A

# Compound interest
def compound_interest(P, R, n, t):
    A = P * (1 + R / n) ** (n * t)
    return A

# Annuity plan
def annuity_plan(PMT, R, n, t):
    A = PMT * (((1 + R / n) ** (n * t) - 1) / (R / n))
    return A

#Input
P = float(input("Enter your principal: "))
R = float(input("Enter your rate (in percentage ): "))
T = float(input("Enter time (in years):"))
t = T
n = int(input("Enter number of times interest applied:"))
PMT = float(input("Enter periodic payment:"))

#Result
print("\nSimple Interest:")
print("Amount: ", simple_interest)

print("\nCompound Interest:")
print("Amount: ", compound_interest)

print("\nAnnuity plan:")
print("Amount: ", annuity_plan)