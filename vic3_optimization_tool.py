"""
The primary goal of this program is to enhance future runs of Victoria 3, 
focusing on GDP, deficit spending, and population.

The long term goal is to have multiple options and methods to examine the start of the game,
or a game in progress, and the current conditions of the simulated country.

This program will also serve as a rough draft in every aspect of my first Python code, that will grow as I do.
Each section of code will start as a simple calculation, and transition into applying given data and extrapolating
next steps.

Victoria 3 Optimization Tool v0.01
"""

#Given a country's starting situation, what state would be best to urbanize
#Austria will be our default to experiment with. Will likely need to set up objects what each country has.
#May need to do the same with the states of the countries in question.

#raw material options, we will have to assume inability to trade at the moment and no price flexibility

raw_resource_names = ["log", "iron", "coal", "gold"]

#value = market value at equilibrium, cc = construction cost, production = base output of related building
#Currently, all outputs will be their base value with lowest tech, though each variable will have acronyms
#for the production method in use.

log_output_sf = 30
log_input_sf = 0
log_workforce_sf = {500: "shopkeepers", 4500: "laborers"}
log_resource_value = 20
log_building_cc = 200

iron_output_pas = 20
iron_input_pas = -5 #Loss of 5 tools
iron_workforce_pas = {500: "shopkeepers", 4500: "laborers"}
iron_resource_value = 40
iron_building_cc = 400

coal_output_pas = 25
coal_input_pas = -5 #Loss of 5 tools
coal_workforce_pas = {500: "shopkeepers", 4500: "laborers"}
coal_resource_value = 30
coal_building_cc = 400

#Gold is a special resource, adds a minting value of 250 per level
gold_output_pas = 8
gold_input_pas = -5 #Loss of 5 tools
gold_workforce_pas = {500: "shopkeepers", 4500: "laborers"}
gold_resource_value = 100
gold_building_cc = 400

tool_base_value = 40



#-----------------------------------------------
#Calculate an acceptable level to deficit spend

#debt ceiling in this game is the same evaluation as the GDP.
#Due to this, a 10% increase in GDP effectively means that if 10% of GDP was spent of debt would be a net wash for
#available credit. This will be the baseline of 'acceptable'.


def acceptable_deficit_rate(stats):

    yearly_expenses = abs(stats["expenses"] * 52.1429) #number is the decimal point for weeks in a year
    expected_GDP_increase = stats["GDP"] * stats["growth"]

    growth_ratio = abs(expected_GDP_increase/yearly_expenses)
    growth_string = f"{(growth_ratio * 100):.2f}"

    balance_string = f"{(expected_GDP_increase - yearly_expenses):.2f}"


    if growth_ratio < .8:
        print("Rethink your planning")
        print("You have a projected balance of $" + balance_string + ", under expectations. You are growing at a rate of " + growth_string + "% compared to your expenses.")

    elif growth_ratio > 1.6:
        print("Playing it safe")
        print("You have a projected balance of $" + balance_string + ", well above expectations. You are growing at a rate of " + growth_string + "% compared to your expenses.")

    else:
        print("Right on target")
        print("You have a projected balance of $" + balance_string + ", meeting expectations. You are growing at a rate of " + growth_string + "% compared to your expenses.")


def user_info_ask():
    
    changing_user_info = True
    while changing_user_info:
        try:
            user_GDP = float(input("What is your current GDP? "))

        #expenses will refer to the in game indicator for spent funds, which displays the funds spent on a weekly basis
            user_expenses = float(input("What is your weekly expense? "))

        #Number will be represented as a decimal, but entered as a percentage
            user_predicted_growth = float(input("How much growth (in percentage) do you expect for the year? "))/100.00
        except ValueError:
            print("Please enter each question with digits only")
            continue
        user_country_dict = {"GDP": user_GDP, "expenses": user_expenses, "growth": user_predicted_growth}
        return user_country_dict


def main():

    #Initialize user information inputs
    user_country_stats = user_info_ask()

    tool_in_use = True
    while tool_in_use:
        try:
            print("Which tool would you like to select? (Select with the associated number)")
            select_tool = int(input("1. Deficit Spending Calculator; 2. Change Country Information: "))
        except ValueError:
            print("Please be sure to type in exclusively the number of the tool you wish to choose")
            continue

        if select_tool == 1:
            acceptable_deficit_rate(user_country_stats)

        elif select_tool == 2:
            user_country_stats = user_info_ask()

        else:
            print("Invalid input, does not exist")
        
        reselect_input = input("Do you wish to use another tool? (yes/y or no/n): ")
        
        if reselect_input.lower() == "yes" or reselect_input.lower() == "y":
            continue
        else:
            break

    print("Ending now.")    

if __name__ == "__main__":
    main()
        
        
        
