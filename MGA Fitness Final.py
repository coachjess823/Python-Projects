#MGA Fitness System
#Jessica Davis
#Application Development - ITEC 2270

#/*************************************************
#* Student Name: Jessica Davis
#* Date Due: November 29, 2023
#* Date Submitted: November 29, 2027
#* Program Name: MGA Fitness System
#* Program Description: This program is
#*      meant to allow the user to sign
#*      in as an administrator or a customer,
#*      and then ask to either add/drop cusomers
#*      or classes, as well as to sign up for
#*      classes.
#**************************************************/

class MGAFitness:
    classes = []
    customers = []
    class_id_counter = 1
    customer_id_counter = 1

    #Set up a container for adding classes
    def add_class(self, class_name, instructor, date, time, cost, max_capacity):
        new_class = {
            'ID': self.class_id_counter,
            'Name': class_name,
            'Instructor': instructor,
            'Date': date,
            'Time': time,
            'Cost': cost,
            'Max Capacity': max_capacity
        }

        #Start the id number at 1
        self.classes.append(new_class)
        self.class_id_counter += 1

        #Give a success badge for adding a class
        print(f"\nClass '{class_name}' added successfully with ID: {new_class['ID']}")

    #Container to delete classes
    def delete_class(self, class_id):
        class_found = False
        for class_info in self.classes:
            if class_info['ID'] == class_id:
                class_found = True
                class_name = class_info['Name']
                self.classes.remove(class_info)
                #print out a tag that it has been deleted
                print(f"\nClass '{class_name}' with ID {class_id} deleted successfully!")
                break

        if not class_found:
            print(f"\nClass with ID {class_id} not found!")

    #show a list to delete class
    def show_classes_for_deletion(self):
        print("\nAvailable classes for deletion:")
        for class_info in self.classes:
            print(f"ID: {class_info['ID']} - Name: {class_info['Name']}")

    #container to add customer info
    def add_customer(self, first_name, last_name, phone_number, email):
        new_customer = {
            'ID': self.customer_id_counter,
            'First Name': first_name,
            'Last Name': last_name,
            'Phone Number': phone_number,
            'Email': email
        }
        
        self.customers.append(new_customer)
        self.customer_id_counter += 1

        #success tag for adding id
        print(f"\nCustomer '{first_name} {last_name}' added successfully with ID: {new_customer['ID']}")

    #container to delete customer
    def delete_customer(self, customer_id):
        customer_found = False
        for customer_info in self.customers:
            if customer_info['ID'] == customer_id:
                customer_found = True
                customer_name = f"{customer_info['First Name']} {customer_info['Last Name']}"
                self.customers.remove(customer_info)
                print(f"Customer '{customer_name}' with ID {customer_id} deleted successfully!")
                break

        if not customer_found:
            print(f"Customer with ID {customer_id} not found!")

    #Show a list of available customers
    def show_customers_for_deletion(self):
        print("\nAvailable customers for deletion:")
        for customer_info in self.customers:
            print(f"ID: {customer_info['ID']} - Name: {customer_info['First Name']} {customer_info['Last Name']}")

    #container for reports
    def show_reports(self):
        print("\nClasses:")

        #pull in and show all class information
        if self.classes:
            for class_info in self.classes:
                print(f"\nID: {class_info['ID']}")
                print(f"Name: {class_info['Name']}")
                print(f"Instructor: {class_info['Instructor']}")
                print(f"Date: {class_info['Date']}")
                print(f"Time: {class_info['Time']}")
                print(f"Cost: {class_info['Cost']}")
                print(f"Max Capacity: {class_info['Max Capacity']}")
                print("-------------------------")
        else:
            print("\nNo classes available.")

        print("\nCustomers:")

        #pull in and show all customer information
        if self.customers:
            for customer_info in self.customers:
                print(f"\nID: {customer_info['ID']}")
                print(f"Name: {customer_info['First Name']} {customer_info['Last Name']}")
                print(f"Phone Number: {customer_info['Phone Number']}")
                print(f"Email: {customer_info['Email']}")
                print("-------------------------")
        else:
            print("\nNo customers available.")

#Container to sign in the admin with a basic login in and password
def administrator_sign_in(mga_fitness):
    admin_username = "admin"
    admin_password = "password"

    entered_username = input("\nEnter Administrator username: ")
    entered_password = input("Enter Administrator password: ")

    if entered_username == admin_username and entered_password == admin_password:
        print("\nAdministrator sign-in successful!")

        #Set the admin screen options
        while True:
            print("\nAdministrator Options:")
            print("1. Add Class")
            print("2. Delete Class")
            print("3. Add Customer")
            print("4. Delete Customer")
            print("5. See Reports")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                class_name = input("\nEnter the class name: ")
                instructor = input("Enter the Instructor's name: ")
                date = input("Enter the date (e.g., MM/DD/YYYY): ")
                time = input("Enter the time (e.g., HH:MM AM/PM): ")
                cost = input("Enter the cost: $")
                max_capacity = input("Enter the maximum capacity: ")

                mga_fitness.add_class(class_name, instructor, date, time, cost, max_capacity)

            elif choice == '2':
                mga_fitness.show_classes_for_deletion()
                class_id_to_delete = input("\nEnter the ID of the class to delete: ")
                mga_fitness.delete_class(int(class_id_to_delete))
                
            elif choice == '3':
                first_name = input("\nEnter the customer's first name: ")
                last_name = input("Enter the customer's last name: ")
                phone_number = input("Enter the customer's phone number: ")
                email = input("Enter the customer's email: ")

                mga_fitness.add_customer(first_name, last_name, phone_number, email)

            elif choice == '4':
                mga_fitness.show_customers_for_deletion()
                customer_id_to_delete = input("\nEnter the ID of the customer to delete: ")
                mga_fitness.delete_customer(int(customer_id_to_delete))
                
            elif choice == '5':
                mga_fitness.show_reports()
                
            elif choice == '6':
                print("\nExiting Administrator mode.")
                break
            
            else:
                print("\nInvalid choice. Please enter a number between 1 and 6.")
    else:
        print("\nInvalid credentials. Access denied.")

#Screen to show classes
def display_classes(mga_fitness):
    print("\nAvailable Classes:")
    if mga_fitness.classes:
        for class_info in mga_fitness.classes:
            print(f"\nClass ID: {class_info['ID']}")
            print(f"Name: {class_info['Name']}")
            print(f"Instructor: {class_info['Instructor']}")
            print(f"Date: {class_info['Date']}")
            print(f"Time: {class_info['Time']}")
            print(f"Cost: ${class_info['Cost']}")
            print(f"Max Capacity: {class_info['Max Capacity']}")
            print("-------------------------")
    else:
        print("No classes available.")


#screen to sign in customers
def customer_sign_in(mga_fitness):
    customer_id = int(input("\nEnter your ID: "))
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    customer_found = False
    selected_classes = []
    customer_name = ""
    for customer_info in mga_fitness.customers:
        if (
            customer_info['ID'] == customer_id
            and customer_info['First Name'] == first_name
            and customer_info['Last Name'] == last_name
        ):
            customer_found = True
            customer_name = f"{customer_info['First Name']} {customer_info['Last Name']}"
            print("Customer sign-in successful!") #success tag
            selected_classes = select_classes(mga_fitness)
            break

    if not customer_found:
        print("Customer not found. Access denied.")

    if selected_classes:
        print(f"\nCustomer ID: {customer_id}")
        print(f"Customer Name: {customer_name}")

        #calculate price
        class_ids = [class_id - 1 for class_id in selected_classes]  
        print("\nSelected Classes:")
        total_cost = 0
        class_names = []
        class_costs = []
        for idx in class_ids:
            class_info = mga_fitness.classes[idx]
            total_cost += float(class_info['Cost'])
            class_names.append(class_info['Name'])
            class_costs.append(float(class_info['Cost']))
        
        for class_name, class_cost in zip(class_names, class_costs):
            print(f"Class Name: {class_name:20} Cost: {class_cost:.2f}")

        #print out total
        print("\nTotal cost for selected classes:", f"{total_cost:.2f}")

#container to select classes       
def select_classes(mga_fitness):
    selected_classes = []
    while True:
        display_classes(mga_fitness)
        choice = input("\nEnter the class ID you want to sign up for (or 'done' to finish): ")

        if choice.lower() == 'done':
            break

        try:
            class_id = int(choice)
            if 1 <= class_id <= len(mga_fitness.classes):
                selected_classes.append(class_id)
                print(f"Class ID {class_id} added to your selection.")
            else:
                print("Invalid class ID. Please enter a valid ID.")
        except ValueError:
            print("Invalid input. Please enter a valid class ID or 'done'.")

    return selected_classes

#main screen
def main():
    fitness_center = MGAFitness()
    print("Welcome to MGA Fitness!")

    while True:
        print("\n1. Administrator sign in")
        print("2. Customer sign in")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            administrator_sign_in(fitness_center)
        elif choice == '2':
            customer_sign_in(fitness_center)
        elif choice == '3':
            print("\nExiting MGA Fitness. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
