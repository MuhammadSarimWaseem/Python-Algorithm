# Watts is the measure of power consumption of electrical appliances. Which can be
# calculated by using voltmeter and ammeter to read the voltage and ampere.

#    Write a program that prints the Watts against the user given volt and ampere reading.
#  REF: https://www.webstaurantstore.com/guide/600/how-to-calculate-amps-volts-and- watts.html


voltage = int(input("Enter the voltage:"))
current = int(input("Enter the current:"))
power = voltage*current
print("Value of power is:%f" % power)
