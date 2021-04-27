# Ferry_Average_Monthly_Delay

This program gets an encrypted file and a password as input, and if the password is correct, 
decrypts the file using the password. Then, it calculates the average monthly delay of BC Ferries departure time,
and prints it in a readable file as an output. The program uses REGEX to check if the password is in the correct format. 
Also, it uses Shifting (Cipher) algorithm for encryption. 


Terms:

    1) Cipher/Shift Algorithm : Algorithm used for encryption
    2) Encrypted/Encoded: The text that has been transformed using cipher algorithm
    3) Decrypted/Decoded: Recovered original text

Files:

    1) Encrypted Files: 
       There are 3 encrypted files in total, all of them in "ferryx.out" format. 
       All of these files(CSV) contatin information about BC Ferries in encrypted format.

       Encryption Algorithm:
         * For each character of the input text and the corresponding character of the password, 
           we add their value to get the total shift (A-Z + "Space" -> 27 characters).
         * Once we have the total shift, we find it in the alphabet, and the correspoding
           character in the alphabet will be the encoded character.
         * If the shift value is too large, then we take the modulo of the length of your alphabet.
         * The encoded text is the character from the encryption alphabet at index value.

    2) Input Files:
       These are in "inX.txt" format. These files contain the name of the encrypted files and
       their password. 

    3) Output Files:
       These are in "outX.txt" format. These files contain the required output of the program.
   
   
Program Flow:

    1) Ask user for a encrypted filename.
    2) Check if file exists, if not, prompt user again.
    3) The password (key) to decode the file.
    4) Check if the password is in a valid format, if not, prompt the user again.
    5) Check if the provided valid password successfully decrypts the provided file,
    if not, prompt the user for the password again;
    6) Iterate through the decrypted rows;
    7) Calculate the average monthly delay between scheduled time and when the
    ferry actually leaves the port;


Input:

    * The program is required to prompt the user for the encrypted file to decode and
    the password (key) to use. 
    * You must also validate the data upon input. If the data
    is invalid notify the user of their error and prompt them to enter their selections
    again. 
    * The user should also be able to enter q for quit at either prompt.

    Password Validity:

      * At least 1 uppercase letter
      * At least 2 numerical digits
      * Exactly 2 special characters, !@#$&*-_
      * Password length of 6-8 characters
      

Output:

    The output file will contain the following:

      1) FileDecoder(key=’The Password’, file=’ferryX.out’)
      2) Number of Entries
      3) Average delay for MON (where MON is the abbreviation for months of the year ie. FEB, JAN, ...).
  
   

