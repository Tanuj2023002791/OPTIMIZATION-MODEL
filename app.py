

# Step 1: Import PuLP
import pulp

# Step 2: Business Problem Description
print("📊 Business Problem: A company produces 2 products (A & B).")
print("Each product requires labor and materials, and earns a profit.")
print("Goal: Maximize total profit given constraints on labor & materials.")

# Step 3: Take Input Parameters
profit_a = float(input("Enter profit per unit of Product A: "))
profit_b = float(input("Enter profit per unit of Product B: "))

labor_a = float(input("Enter labor hours required per unit of Product A: "))
labor_b = float(input("Enter labor hours required per unit of Product B: "))
total_labor = float(input("Enter total available labor hours: "))

material_a = float(input("Enter material units required per unit of Product A: "))
material_b = float(input("Enter material units required per unit of Product B: "))
total_material = float(input("Enter total available material units: "))

# Step 4: Create the LP problem
problem = pulp.LpProblem("Maximize_Profit_ProductMix", pulp.LpMaximize)

# Step 5: Define Decision Variables
x = pulp.LpVariable('Units_of_Product_A', lowBound=0, cat='Continuous')
y = pulp.LpVariable('Units_of_Product_B', lowBound=0, cat='Continuous')

# Step 6: Define Objective Function
problem += profit_a * x + profit_b * y, "Total_Profit"

# Step 7: Define Constraints
problem += labor_a * x + labor_b * y <= total_labor, "Labor Constraint"
problem += material_a * x + material_b * y <= total_material, "Material Constraint"

# Step 8: Solve the Problem
problem.solve()

# Step 9: Output Results
print("\n✅ Optimization Result:")
print("Solution Status:", pulp.LpStatus[problem.status])
print("Optimal Production Plan:")
print(f" - Product A: {x.varValue:.2f} units")
print(f" - Product B: {y.varValue:.2f} units")
print("💰 Maximum Profit (₹):", pulp.value(problem.objective))

# Step 10: Business Insight
print("\n📈 Insight:")
if pulp.LpStatus[problem.status] == "Optimal":
    print(f"To maximize profit, produce {x.varValue:.2f} units of Product A and {y.varValue:.2f} units of Product B.")
else:
    print("No feasible solution found. Please check your constraints.")