import csv
from random import randint, randrange

output, first_row = [], []
with open('sample.csv', 'r') as inputfile:
    data = csv.reader(inputfile)

    for row in data:
        output.append(row)
        first_row.append(row)
        break

alphabets_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabets_capital = [ x.upper() for x in alphabets_small]
alphabets = alphabets_small+alphabets_capital

email = ['gmail', 'yahoo', 'outlook', 'abc', 'xyz', 'microsoft', 'caseys', 'kfc', 'restaurant']

records = 100000

first_name, last_name, email_id, phone, zip_code= "","","","",""
for y in range(0, records):
    for x in range(0, 6):
        first_name += str(alphabets[randint(0, len(alphabets)-1)])
        last_name += str(alphabets[randint(0, len(alphabets) - 1)])
    for x in range(0, 14):
        phone += str(randint(0, 9))
    phone = phone[:14] if len(phone)>=14 else phone
    for x in range(0,5):
        zip_code+=str(randint(0,9))
    email_id = first_name+"_"+last_name+"@"+str(email[randrange(0,len(email)-1)])+".com"
    #print(first_name.lower().capitalize()+" "+last_name.lower().capitalize()+" "+email_id+" "+phone+" "+zip_code)
    output.append([email_id, first_name.lower().capitalize(), last_name.lower().capitalize(), phone, "1985-07-04",
                   "201 San Antonio circle Mountain View",
                   "Mountain view", "CA", zip_code, "1", "Male", "Mr.", "1"])
    print("Progress: "+ "{:.2f}".format((y/records)*100)+"%")
    first_name, last_name, email_id, phone, zip_code= "","","","",""

print("*********Completed**********")

for x in output:
    try:
        with open('file.csv', 'a') as file:
            data = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data.writerow(x)
        file.close()
    except:
        outputfile = open('file.csv', 'w')
        outputfile.close()
