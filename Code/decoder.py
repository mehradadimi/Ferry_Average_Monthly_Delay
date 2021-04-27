import string
from cipher import dateT
import datetime
import re
from cipher import DecryptException
from cipher import FileDecoder


"""
This function uses get_pass() function to get the correct
password from the user and returns an instance of 
FileDecoder class
"""
def create_instance(input_file, alphabet):
    while True:
        password = get_pass()
        if password == 'q':
            exit()
        try:
            return FileDecoder(key=password, filename=input_file, alphabet=alphabet)
        except DecryptException:
            continue



"""
This function prints the monthly delay
"""
def print_monthly_delay(list_of_averages_for_each_month):
    for i in range(0, len(list_of_averages_for_each_month) - 1):
        if list_of_averages_for_each_month[i] == []:
            continue
        if i == 0:
            print("    Average delay for Jan: {:.2f}".format(float(list_of_averages_for_each_month[i][0])))
        if i == 1:
            print("    Average delay for Feb: {:.2f}".format(float(list_of_averages_for_each_month[i][0])))
        if i == 2:
            print("    Average delay for Mar: {:.2f}".format(float(list_of_averages_for_each_month[i][0])))
        if i == 3:
            print("    Average delay for Apr: {:.2f}".format(float(list_of_averages_for_each_month[i][0])))
        if i == 4:
            print("    Average delay for May: {:.2f}".format(float(list_of_averages_for_each_month[i][0])))
        if i == 5:
            print("    Average delay for Jun: {:.2f}".format(float(list_of_averages_for_each_month[i][0])))
        if i == 6:
            print("    Average delay for Jul: {:.2f}".format(float(list_of_averages_for_each_month[i][0])))
        if i == 7:
            print("    Average delay for Aug: {:.2f}".format(float(list_of_averages_for_each_month[i][0])))
        if i == 8:
            print("    Average delay for Sep: {:.2f}".format(float(list_of_averages_for_each_month[i][0])))
        if i == 9:
            print("    Average delay for Oct: {:.2f}".format(float(list_of_averages_for_each_month[i][0])))
        if i == 10:
            print("    Average delay for Nov: {:.2f}".format(float(list_of_averages_for_each_month[i][0])))
        if i == 11:
            print("    Average delay for Dec: {:.2f}".format(float(list_of_averages_for_each_month[i][0])))
    print("END")





"""
This function calculates the monthly 
delay average as required and prints
them using print_monthly_delay() function
"""

def calculate_average(file1):
    listi_of_decoded_lines = []

    for i in file1:
        listi_of_decoded_lines.append(i)
    del listi_of_decoded_lines[0]


    list_of_decoded = []
    for j in listi_of_decoded_lines:
        list_of_decoded.append(j)
    print("RESULTS")
    print("FileDecoder: FileDecoder(key='%s', file='%s')" % (file1.key, file1.filename))
    print("Entries: %d" % len(file1))

    dict_of_months = {"Jan": "1", "Feb": "2", "Mar": "3", "Apr": "4", "May": "5", "Jun": "6",
                      "Jul": "7", "Aug": "8", "Sep": "9", "Oct": "10", "Nov": "11", "Dec": "12"}

    list_of_months = [[] for i in range(0, 12)]

    for i in range(0, len(list_of_decoded)):
        if "1" in list_of_decoded[i][4]:
            list_of_months[0].append(list_of_decoded[i])
            continue
        elif "2" in list_of_decoded[i][4]:
            list_of_months[1].append(list_of_decoded[i])
            continue
        elif "3" in list_of_decoded[i][4]:
            list_of_months[2].append(list_of_decoded[i])
            continue
        elif "4" in list_of_decoded[i][4]:
            list_of_months[3].append(list_of_decoded[i])
            continue
        elif "5" in list_of_decoded[i][4]:
            list_of_months[4].append(list_of_decoded[i])
            continue
        elif "6" in list_of_decoded[i][4]:
            list_of_months[5].append(list_of_decoded[i])
            continue
        elif "7" in list_of_decoded[i][4]:
            list_of_months[6].append(list_of_decoded[i])
            continue
        elif "8" in list_of_decoded[i][4]:
            list_of_months[7].append(list_of_decoded[i])
            continue
        elif "9" in list_of_decoded[i][4]:
            list_of_months[8].append(list_of_decoded[i])
            continue
        elif list_of_decoded[i][4] == "10":
            list_of_months[9].append(list_of_decoded[i])
            continue
        elif list_of_decoded[i][4] == "11":
            list_of_months[10].append(list_of_decoded[i])
            continue
        elif list_of_decoded[i][4] == "12":
            list_of_months[11].append(list_of_decoded[i])
            continue

    list_of_dates_in_months = [[] for i in range(12)]

    for i in range(0, len(list_of_months)):
        for j in list_of_months[i]:
            if j == None:
                continue
            scheduled_date = datetime.datetime(int(j[3]), int(j[4]), int(j[5]), int(j[6]), int(j[7]))
            actual_date = datetime.datetime(int(j[8]), int(j[9]), int(j[10]), int(j[11]), int(j[12]))
            dateie = dateT(scheduled_date, actual_date)
            list_of_dates_in_months[i].append(dateie)

    list_of_averages_for_each_month = [[] for i in range(len(list_of_dates_in_months))]
    sumi = 0
    count = 0
    for i in range(0, len(list_of_dates_in_months)):
        if i == None:
            sumi = 0
            if count != 0:
                list_of_averages_for_each_month[i].append(sumi / count)
            continue
        for j in list_of_dates_in_months[i]:
            difference = (j.actual - j.scheduled)
            sumi = sumi + (int(difference.total_seconds() / 60))
            count += 1
        if count != 0:
            list_of_averages_for_each_month[i].append(round((sumi / count), 2))
        sumi = 0
        count = 0


    """Print The Delays"""
    print_monthly_delay(list_of_averages_for_each_month)



"""
This funciton prompts the user for password
and constantly checks the validity
of the password
"""

def get_pass():
    password = ""
    flag_pass = False
    while not flag_pass:
        password = input("Please Enter the Correct Password to Decrypt the File: ")
        if password == 'q':
            exit()
        length = False
        uppercase = False
        digit = False
        special = False
        if re.match(r'^.{6,8}$', password):
            length = True
        if re.search(r'[A-Z]', password):
            uppercase = True
        if re.search(r'[0-9]{1,}.*[0-9]{1,}', password):
            digit = True
        if re.match(r'^[^!@#$&*\-_.]*[!@#$&*\-_.]{1}[^!@#$&*\-_.]*[!@#$&*\-_.]{1}[^!@#$&*\-_.]*$', password):
            special = True
        if length and uppercase and digit and special:
            flag_pass = True

        if not flag_pass:
            print("The Password Does Not Satisfy the Requirements, ", end='')
            flag_pass = False
    return password



"""
This function prompts the user for the name of the
file and constantly checks if the file exists
if not, it prompts the user again
"""
def file_getter():
    flag = False
    input_file = ""
    while not flag:
        try:
            input_file = input("Enter the Correct Name of the File to be Decrypted: ")
            if input_file == 'q':
                exit()
            open(input_file)
            flag = True
            return input_file
        except FileNotFoundError:
            print("The File Does Not Exist, ", end='')
            flag = False


def main():

    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " \n"

    input_file = file_getter()

    file1 = create_instance(input_file, alphabet)

    calculate_average(file1)

if __name__ == "__main__":
    main()
