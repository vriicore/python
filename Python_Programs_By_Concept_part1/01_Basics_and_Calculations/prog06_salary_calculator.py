# Program 1.6: Salary Calculator
# Take basic salary as input.
# Calculate: HRA = 20% of basic, DA = 10% of basic, PF = 12% of basic.
# Display gross salary (basic+HRA+DA) and net salary (gross-PF).

basic = float(input("Enter Basic Salary: "))

hra = 0.20 * basic
da = 0.10 * basic
pf = 0.12 * basic

gross_salary = basic + hra + da
net_salary = gross_salary - pf

print("--- Salary Details ---")
print("Basic Salary :", basic)
print("HRA (20%)    :", hra)
print("DA (10%)     :", da)
print("PF (12%)     :", pf)
print("Gross Salary :", gross_salary)
print("Net Salary   :", net_salary)
