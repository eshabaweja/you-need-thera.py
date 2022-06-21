from prettytable import MARKDOWN, MSWORD_FRIENDLY, ORGMODE, PrettyTable
from pymacaroons import MACAROON_V1

table = PrettyTable()
# print(table) # blank table here because we haven't added anything yet

# adding data
table.add_column("Ice cream flavor",[
    "Vanilla",
    "Chocolate",
    "Mango",
    "Raspberry"
])

table.add_column("Color",[
    "White",
    "Brown",
    "Yellow",
    "Dark Pink"
])


# decorating the table
print("\n",table.align)

table.align["Ice cream flavor"] = "l"
table.align["Color"] = "r"

table.set_style(MARKDOWN)


# printing it
print("\n",table)