def net_income_calculator():
    # Create an Empty List for Revenue and Expenses - Titles and Money Gained/Spent
    rev_list_title = []
    rev_list_inc = []
    exp_list_title = []
    exp_list_cost = []

    # Establish Number of Sources of Revenue
    rev_sources = int(input("Enter number of revenue streams you have: "))
    print("")

    # Make sure we entered is a valid integer and non-negative
    while rev_sources < 0:
        print("Please enter either zero or a positive integer!")
        rev_sources = int(input("Enter number of revenue streams you have: "))

    # Go through each revenue stream - collect title and income
    if rev_sources > 0:
        for rev_stream in range(rev_sources):

            # Get a title for revenue stream
            rev_list_title.append(input(f"Enter a title for your #{rev_stream + 1} revenue stream "
                                        "(e.g Work? Side Hustle? Item Sold?): "))
            # Get income from revenue stream
            rev_income = input(f"Enter how much Revenue you earned from {rev_list_title[rev_stream]}: $")
            rev_income = round(float(rev_income), 2)

            # Make sure income is an integer
            while rev_income < 0:
                print("Please enter a positive number!")
                rev_income = (input(f"Enter how much Revenue you earned from {rev_list_title[rev_stream]}: $"))
            rev_list_inc.append(rev_income)
            print("")

    # State reported Revenue
    print("The following is your reported revenue: ")
    for rev_table in range(rev_sources):
        print(rev_list_title[rev_table] + ":", rev_list_inc[rev_table])

    print("")
    print("Thank you for inputting your revenue generated! Now, lets figure out your expenses.", end="\n\n")

    # Establish Number of Sources of Expenses
    exp_sources = int(input("Enter the number of expenses you want to report: "))
    print("")

    # Make sure what we entered is a valid integer and non-negative
    while exp_sources < 0:
        print("Please enter either zero or a positive integer!")
        exp_sources = int(input("Enter how many expenses you have: "))

    # Go through each expense - collect title and cost
    if exp_sources > 0:
        for exp_stream in range(exp_sources):

            # Get a title for the expense
            exp_list_title.append(input(f"Enter a title for your #{exp_stream + 1} expense."
                                        "(e.g Wages, Costs, Other Bills): "))
            # Get cost from expense
            exp_cost = input(f"Enter the cost of '{exp_list_title[exp_stream]}': $")
            exp_cost = round(float(exp_cost), 2)

            # Make sure cost is an integer
            while exp_cost < 0:
                print("Please enter a positive number!")
                exp_cost = (input(f"Enter the cost of {exp_list_title[exp_stream]}: $"))
            exp_list_cost.append(exp_cost)
            print("")

    print("The following are your reported expenses: ")
    for rev_table in range(rev_sources):
        print(rev_list_title[rev_table] + ":", rev_list_inc[rev_table])

    total_rev = sum(rev_list_inc)
    total_exp = sum(exp_list_cost)
    net_income = total_rev - total_exp
    print(net_income)


net_income_calculator()