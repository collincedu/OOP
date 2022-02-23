# The program that tests the CellPhone class.

import c_cellphoneClass as c

def main():
    # Get phone data.
    man = "Apple"
    mod = "Iphone"
    retail = 899

    # Create an instance of the CellPhone class.
    phone = c.CellPhone(man, mod, retail)

    #Display the data that was hardcoded/entered if input stmt.
    print("Here is the data that you entered")
    print('Manufacturer:', phone.get_manufact())
    print('Model Number:', phone.get_model())
    print('Retail Price:', phone.get_retail_price())


# Call the main function.
main()