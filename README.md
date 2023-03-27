# File Encryption and Decryption
This is a Python program for encrypting and decrypting files using a symmetric key encryption technique.

## Prerequisites
This program requires Python 3 to be installed on your system.

## How to use
1. Download the file_encrypt.py file and save it in your desired directory.

2. Open a command prompt or terminal and navigate to the directory where file_encrypt.py is saved.

3. To encrypt a file, run the program and select option 1 from the menu. Enter the name of the file (including the file extension) you want to encrypt when prompted.

4. The program will generate a random 16-byte key and use it to encrypt the file using the XOR encryption technique. A new file will be created with the name "CC-[original_filename]" which contains the encrypted data.

5. The program will display the encryption key in hexadecimal format. Make sure to save this key as you will need it to decrypt the file.

6. To decrypt a file, run the program and select option 2 from the menu. Enter the name of the encrypted file (including the file extension) when prompted.

7. Enter the encryption key (in hexadecimal format) that was displayed when the file was encrypted.

8. The program will use the same key to decrypt the file and overwrite the original encrypted file with the decrypted data.

9. To exit the program, select option 3 from the menu.

## Security Considerations
This program uses a simple symmetric key encryption technique that is not suitable for encrypting sensitive data. The encryption key is displayed in hexadecimal format which can easily be intercepted if not transmitted securely. As such, this program is only suitable for encrypting non-sensitive data or for educational purposes.
