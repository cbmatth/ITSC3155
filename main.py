class SandwichMachine:
    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if item not in self.machine_resources or self.machine_resources[item] < ingredients[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        large_dollar = int(input("How many $1 coins?: "))
        half_dollar = int(input("How many $0.5 coins?: "))
        quarters = int(input("How many $0.25 coins?: "))
        nickels = int(input("How many $0.05 coins?: "))

        total = (large_dollar * 1.00) + (half_dollar * 0.50) + (quarters * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
            Hint: use the output of process_coins() function for cost input"""
        total_inserted = self.process_coins()
        if total_inserted >= cost:
            change = total_inserted - cost
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            print("Payment accepted.")
            return True
        else:
            print(f"Sorry, that's not enough money. Money refunded. You inserted ${total_inserted:.2f}.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            if item in self.machine_resources:
                self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appetit!")

    def report(self):
        """Print the current resources."""
        print("Current resources:")
        for resource, amount in self.machine_resources.items():
            print(f"{resource.capitalize()}: {amount}")

    def start(self):

        recipes = {
            "small": {
                "ingredients": {
                    "bread": 2,
                    "ham": 4,
                    "cheese": 4,
                },
                "cost": 1.75,
            },
            "medium": {
                "ingredients": {
                    "bread": 4,
                    "ham": 6,
                    "cheese": 8,
                },
                "cost": 3.25,
            },
            "large": {
                "ingredients": {
                    "bread": 6,
                    "ham": 8,
                    "cheese": 12,
                },
                "cost": 5.50,
            }
        }

        # Make an instance of SandwichMachine class and write the rest of the codes

        while True:
            choice = input("What would you like? (small/medium/large/off/report): ").lower()

            if choice in ["small", "medium", "large"]:
                sandwich_recipe = recipes[choice]
                if self.check_resources(sandwich_recipe["ingredients"]):
                    if self.transaction_result(sandwich_recipe["cost"]):
                        self.make_sandwich(choice, sandwich_recipe["ingredients"])
            elif choice == "off":
                print("Turning off the machine.")
                break
            elif choice == "report":
                self.report()
            else:
                print("Invalid choice. Please choose again.")


resources = {
    "bread": 12,  # slices
    "ham": 18,  # slices
    "cheese": 24  # ounces
}

sandwich_machine = SandwichMachine(resources)

sandwich_machine.start()
