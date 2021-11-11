# Loop through all the data and print each row.
open_file = open("CupcakeInvoices.csv")

for line in open_file:
    print(line)

# Loop through all the data and print the type of cupcakes purchased.
for type in open_file:
    splitted = type.split(',')
    print(splitted[2])

# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).

for type in open_file:
    splitted = type.split(',')
    quantity = float(splitted[3])
    price = float(splitted[4])
    total = quantity * price
    print(total)

# Loop through all the data, and print out the total for all invoices combined.

combined = 0

for type in open_file:
    splitted = type.split(',')
    quantity = float(splitted[3])
    price = float(splitted[4])
    total = quantity * price
    combined += total
print(combined)

# # Close your open file.

open_file.close()

# Challenge: Do some research and see if you can limit your floats to never exceed two characters after the decimal point.

for type in open_file:
    splitted = type.split(',')
    quantity = float(splitted[3])
    price = float(splitted[4])
    total = quantity * price
    format_float = "{:.2f}".format(total)
    print(format_float)