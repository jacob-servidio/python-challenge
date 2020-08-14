#dictionary for stat abbreviations
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
#import 
import os
import csv

csvpath = os.path.join('..', 'PyBoss', 'Resources', 'employee_data.csv')

#output file for formatted data
formattedcsvpath = os.path.join('..', 'PyBoss', 'analysis', 'formatted_employee_data.csv')

#open csv file to write in
with open (formattedcsvpath, 'w', newline='') as formattedcsvfile:
    csvwriter = csv.writer(formattedcsvfile)
    #write header row
    csvwriter.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    with open(csvpath, newline='') as csvfile:
        #skip header row
        csvfile.readline()

        #csvreader
        csvreader = csv.reader(csvfile, delimiter=',')

        for row in csvreader:
            empID = row[0]
            empName = row[1]
            empDOB = row[2]
            empSSN = row[3]
            empState = row[4]

            #formatting
            splitname = empName.split()
            empfirstname = splitname[0]
            emplastname = splitname[1]

            splitDOB = empDOB.split("-")
            dobyear = splitDOB[0]
            dobmnth = splitDOB[1]
            dobday = splitDOB[2]
            formattedDOB = dobmnth + "/" + dobday + "/" + dobyear

            formattedSSN = "***-**_" + empSSN.split("-")[2]

            abbrvState = us_state_abbrev.get(empState)

            #write into csv
            csvwriter.writerow([empID, empfirstname, emplastname, formattedDOB, formattedSSN, abbrvState])
    formattedcsvfile.close()
    