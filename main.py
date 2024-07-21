class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    # Getter and Setter for category_name
    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, category_name):
        self.__category_name = category_name

    # Getter and Setter for allocated_budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
            self.__remaining_budget = allocated_budget
        else:
            raise ValueError("Allocated budget must be a positive number.")

    # Method to add expenses
    def add_expense(self, expense):
        if expense > 0 and expense <= self.__remaining_budget:
            self.__remaining_budget -= expense
        else:
            raise ValueError("Expense must be a positive number and not exceed the remaining budget.")

    # Method to display budget details
    def display_details(self):
        return (f"Category: {self.__category_name}\n"
                f"Allocated Budget: {self.__allocated_budget}\n"
                f"Remaining Budget: {self.__remaining_budget}")

# Example usage:
food = BudgetCategory("Food", 500)
print(food.display_details())
food.add_expense(50)
print(food.display_details())
