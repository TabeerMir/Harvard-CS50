import csv
name = input('what is your name? ')
house_no = input('what is your house number? ')
street = input('what is your street name? ')
city = input ('which city/town/village do you live in? ')

with open('address.csv','a') as file:
    writer =csv.DictWriter(file, fieldnames=['name', 'house', 'street', 'city'])
    writer.writerow({'name':name, 'house':house_no, 'street':street, 'city':city})