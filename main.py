import json
import pyfiglet
import provenance

text = "Provenance Builder"
ascii_art = pyfiglet.figlet_format(text)
default_prov = provenance.generate_default_provenance()
print(ascii_art)
print("Welcome to Provenance Builder!")
print("Developed By: Ujjwal Saini")
print("*" * 50)
print("Please select the option from the menu below:")
print("1. Logs Detection")
print("2. Policy Creation")
print("3. Exit")
user_input = int(input("Enter your choice: "))

if user_input == 1:
    print("Accessing Logs Detection Module...")
    print("1. Provenance Model Comparison")
    print("2. Policy Enforcement")
    print("3. Main Menu")
    print("4. Exit")
    user_input1 = int(input("Enter your choice: "))

    if user_input1 == 1:
        file_name = input("Enter the name of the file: ")
        try:
            with open(file_name, "r") as file:
                logs = json.load(file)
            logs_prov = provenance.generate_provenance_logs(logs)
            provenance.is_malicious(default_prov, logs_prov, 1)
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {str(e)}")

    if user_input1 == 2:
        file_name = input("Enter the name of the file: ")
        try:
            with open(file_name, "r") as file:
                logs = json.load(file)
            policy_prov = provenance.policy_provenance(logs)
            provenance.is_malicious(default_prov, policy_prov, 2)

        except FileNotFoundError:
            print(f"File '{file_name}' not found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {str(e)}")


elif user_input == 2:
    provenance.create_policy()

elif user_input == 3:
    exit(0)

else:
    print("Wrong Input")
