import csv
import msvcrt # For Windows systems. Use `import getch` for Unix systems.

# Get user input for the CSV file to use
csv_file = input("Enter the name of the CSV file to search: ")

# Get user input to search for a partial string, number or floating point
search_string = input("Enter the partial string, number or floating point to search: ")

# Open the CSV file
with open(csv_file, 'r') as file:

    # Create a CSV reader object
    reader = csv.DictReader(file)

    # Loop through each row in the CSV file
    for row in reader:

        # Check if the search_string is in the row, ignoring case
        if search_string.lower() in ','.join([value.lower() for value in row.values()]):

            # If the search_string is found, print all keys for the matching row
            for key, value in row.items():
                print(key + ": " + value)
            print("\n")
            
            # Wait for any key press before printing the next row
            print("Press any key to continue...")
            msvcrt.getch() # For Windows systems. Use `getch.getch()` for Unix systems.

#Or # If the search_string is found, print the below keys for the matching row
''' # If the search_string is found, print the selected keys
            print("Order Date: ", row["Order Date"])
            print("Order ID: ", row["Order ID"])
            print("Item Total: ", row["Item Total"])
            print("Title: ", row["Title"]) '''
           
            