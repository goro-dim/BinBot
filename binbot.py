def text_to_binary(text):
    """
    Convert a string of text to its binary representation.
    """
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result

def binary_to_text(binary):
    """
    Convert a binary string back to text.
    """
    binary_values = binary.split(' ')
    ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
    return ''.join(ascii_characters)

def main():
    print("Welcome to the Binary Translator!")
    print("Choose an option:")
    print("1. Text to Binary")
    print("2. Binary to Text")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        text = input("Enter text to convert to binary: ")
        binary_output = text_to_binary(text)
        print(f"Binary representation: {binary_output}")
    elif choice == '2':
        binary_input = input("Enter binary to convert to text (space-separated 8-bit binary values): ")
        text_output = binary_to_text(binary_input)
        print(f"Text representation: {text_output}")
    else:
        print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()
