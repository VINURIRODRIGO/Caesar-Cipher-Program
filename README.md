# Caesar Cipher Project

This Python project implements a Caesar Cipher, a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- **Encoding and Decoding**: The program allows users to encode or decode messages using the Caesar Cipher.
- **Input Validation**: It handles input validation to ensure that only letters are encoded or decoded, while maintaining numbers, symbols, and spaces unchanged.
- **Shift Wrapping**: If the shift number provided by the user is greater than 26 (the number of letters in the alphabet), it wraps around to continue the shift cycle.
- **User Interaction**: The program prompts users to enter the direction (encode or decode), the message to be processed, and the shift number.
- **Restart Option**: After encoding or decoding a message, users can choose whether to restart the program to encode/decode another message.

## How to Use

1. Run the Python script (`encryptDecode.py`) to start the program.
2. The program will display the Caesar Cipher logo.
3. Enter the direction of the operation: 'encode' to encrypt a message or 'decode' to decrypt a message.
4. Enter the message to be encoded or decoded.
5. Enter the shift number to determine the amount of shifting for encoding or decoding.
6. After the result is displayed, choose whether to restart the program by typing 'yes' or 'no'.

## Handling Shift Numbers

If the user enters a shift number greater than 26 (the number of letters in the alphabet), the program handles this by wrapping around the shift cycle. For example, a shift of 27 would be equivalent to a shift of 1, and a shift of 30 would be equivalent to a shift of 4.

## Logo

The program imports and displays a logo from `encryptDecodeLogo.py` at the beginning of execution.

## Restart Option

After encoding or decoding a message, the program prompts the user to restart by typing 'yes' to continue encoding/decoding another message or 'no' to exit the program.

## Contributing

Contributions to the Caesar Cipher project are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## Acknowledgments

- Inspired by the classic Caesar Cipher encryption method, this project aims to provide an interactive and educational tool for encoding and decoding messages.
- Thanks to the Python community for providing resources and libraries to facilitate cryptography-related projects.

## Contact

For any questions or inquiries about the Caesar Cipher project, feel free to contact vinuri.rodrigo@gmail.com. Enjoy encrypting and decrypting messages!
