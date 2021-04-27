import csv
import time
import datetime

"""
This is a class used for datetime.datetime modulo
it helps calculating the delay in time
"""
class dateT:
    def __init__(self, scheduled, actual):
        self.scheduled = scheduled
        self.actual = actual

    def __repr__(self):
        return "The scheduled date is %s and the actual is %s " % (self.scheduled, self.actual)


"""
This is the Decrypt exception
"""
class DecryptException(Exception):
    pass




"""
The FileDecoder class reads a file from input, decrypts each line of it, 
checks if the password successfully decrypted the file, and returns each
row iteratively.
"""
class FileDecoder:

    def __init__(self, key, filename, alphabet):
        self.key = key
        self.filename = filename
        self.alphabet = alphabet
        self.counter = 0
        with open(self.filename, mode='r') as filie:
            string = filie.read()
            decrypted = self.decodeMe(string)
            decrypted = decrypted.split('\n')
            self.listi = decrypted[:-1]
            self.firstLine = decrypted[0]
            #print(self.firstLine)

        if self.firstLine != "departure_terminal,arrival_terminal,vessel_name,scheduled_departure_year," \
                             "scheduled_departure_month,scheduled_departure_day,scheduled_departure_hour," \
                             "scheduled_departure_minute,actual_departure_year,actual_departure_month," \
                             "actual_departure_day,actual_departure_hour,actual_departure_minute,arrival_year," \
                             "arrival_month,arrival_day,arrival_hour,arrival_minute":
            print(
                "The Password Satisfies the Requirements But Does Not Successfully Decrypt the File. ",end='')
            raise DecryptException

    def __repr__(self):
        return "FileDecoder(key='%s', file='%s')" % (self.key, self.filename)

    def __len__(self):
        return len(self.listi)

    def decodeMe(self, line):
        i = 0
        my_line = ""
        for letter in line:

            index_of_letter = self.alphabet.index(letter)
            index_of_key_letter = (i % len(self.key))
            letter_of_the_key_in_index = self.key[index_of_key_letter]
            index_of_key_letter_in_alphabet = self.alphabet.index(letter_of_the_key_in_index)
            shift_minus_key = index_of_letter - index_of_key_letter_in_alphabet
            if shift_minus_key < 0:

                total_shift = index_of_letter + len(self.alphabet)
                index_of_real_letter = total_shift - index_of_key_letter_in_alphabet
                real_letter = self.alphabet[index_of_real_letter]
                my_line = my_line + real_letter

            elif shift_minus_key >= 0:
                index_of_real_letter_in_alphabet = index_of_letter - index_of_key_letter_in_alphabet
                real_letter_in_this_case = self.alphabet[index_of_real_letter_in_alphabet]
                my_line = my_line + real_letter_in_this_case

            i += 1

        return my_line

    def __iter__(self):
        for i in self.listi:
            yield i.split(',')
