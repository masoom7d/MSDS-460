# %%
import pulp 

# Instantiate the problem as "Diet Optimization LP"
my_lp_problem = pulp.LpProblem("Diet_Optimization_LP", pulp.LpMinimize)

# Creating Decision Variables for each food item
bar = pulp.LpVariable('bar', lowBound=0, cat='Continuous')
shake = pulp.LpVariable('shake', lowBound=0, cat='Continuous')
paneer = pulp.LpVariable('paneer', lowBound=0, cat='Continuous')
cookies = pulp.LpVariable('cookies', lowBound=0, cat='Continuous')
pasta = pulp.LpVariable('pasta', lowBound=0, cat='Continuous')

# Objective Function
my_lp_problem += 5 * bar + 3.75 * shake + 1.75 * paneer + 2 * cookies + 1.25 * pasta

# Adding Constraints to the problem
my_lp_problem += 130 * bar + 290 * shake + 140 * cookies + 90 * paneer + 190 * pasta >= 2000  # Energy
my_lp_problem += 130 * bar + 400 * shake + 85 * cookies + 5 * paneer + 0 * pasta <= 5000  # Sodium
my_lp_problem += 12 * bar + 35 * shake + 1 * cookies + 7 * paneer + 4 * pasta >= 800  # Protein
my_lp_problem += 0 * bar + 2.6 * shake + 0 * cookies + 0 * paneer + 0 * pasta >= 20  # Vit D
my_lp_problem += 38 * bar + 300 * shake + 0 * cookies + 125 * paneer + 2 * pasta >= 1300  # Calcium
my_lp_problem += 2 * bar + 5.5 * shake + 1.25 * cookies + 0 * paneer + 0 * pasta >= 18  # Iron
my_lp_problem += 144 * bar + 318 * shake + 50 * cookies + 0 * paneer + 77 * pasta >= 4700  # Potassium

# Solve the LP Problem
my_lp_problem.solve()

# Check the status of the solution
status = pulp.LpStatus[my_lp_problem.status]

if status == 'Optimal':
    # Optimal solution found
    print("Optimal diet:")
    print(f"Servings of Bar: {bar.varValue}")
    print(f"Servings of Shake: {shake.varValue}")
    print(f"Servings of Paneer: {paneer.varValue}")
    print(f"Servings of Cookies: {cookies.varValue}")
    print(f"Servings of Pasta: {pasta.varValue}")
    print(f"Total cost: ${pulp.value(my_lp_problem.objective)}")
else:
    print("No optimal solution found.")


# %%
## I will add two nutritional constraints such as minimum requirements for Vit C and Vit B6. 
# #Minimal requirements and nutritional constraints for Vit C are 90 milligrams and Vit B6 is 1.7 milligrams.

# Instantiate the problem as "Diet Optimization LP"
my_lp_problem = pulp.LpProblem("Diet_Optimization_LP", pulp.LpMinimize)

# Creating Decision Variables for each food item
bar = pulp.LpVariable('bar', lowBound=0, cat='Continuous')
shake = pulp.LpVariable('shake', lowBound=0, cat='Continuous')
paneer = pulp.LpVariable('paneer', lowBound=0, cat='Continuous')
cookies = pulp.LpVariable('cookies', lowBound=0, cat='Continuous')
pasta = pulp.LpVariable('pasta', lowBound=0, cat='Continuous')

# Objective Function
my_lp_problem += 5 * bar + 3.75 * shake + 1.75 * paneer + 2 * cookies + 1.25 * pasta

# Adding Constraints to the problem
my_lp_problem += 130 * bar + 290 * shake + 140 * cookies + 90 * paneer + 190 * pasta >= 2000  # Energy
my_lp_problem += 130 * bar + 400 * shake + 85 * cookies + 5 * paneer + 0 * pasta <= 5000  # Sodium
my_lp_problem += 12 * bar + 35 * shake + 1 * cookies + 7 * paneer + 4 * pasta >= 800  # Protein
my_lp_problem += 0 * bar + 2.6 * shake + 0 * cookies + 0 * paneer + 0 * pasta >= 20  # Vit D
my_lp_problem += 38 * bar + 300 * shake + 0 * cookies + 125 * paneer + 2 * pasta >= 1300  # Calcium
my_lp_problem += 2 * bar + 5.5 * shake + 1.25 * cookies + 0 * paneer + 0 * pasta >= 18  # Iron
my_lp_problem += 144 * bar + 318 * shake + 50 * cookies + 0 * paneer + 77 * pasta >= 4700  # Potassium
my_lp_problem += 0 * bar + 16 * shake + 0 * cookies + 0 * paneer + 0 * pasta >= 90  # Vit C
my_lp_problem += 0 * bar + 0.3 * shake + 0 * cookies + 0 * paneer + 0 * pasta >= 1.7  # Vit B6

# Solve the LP Problem
my_lp_problem.solve()

# Check the status of the solution
status = pulp.LpStatus[my_lp_problem.status]

if status == 'Optimal':
    # Optimal solution found
    print("Optimal diet:")
    print(f"Servings of Bar: {bar.varValue}")
    print(f"Servings of Shake: {shake.varValue}")
    print(f"Servings of Paneer: {paneer.varValue}")
    print(f"Servings of Cookies: {cookies.varValue}")
    print(f"Servings of Pasta: {pasta.varValue}")
    print(f"Total cost: ${pulp.value(my_lp_problem.objective)}")
else:
    print("No optimal solution found.")

# %%


# %%



