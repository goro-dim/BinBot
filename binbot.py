import os
import platform
import time

if platform.system() == "Windows":
    import winsound

def text_to_binary(text):
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result

def binary_to_text(binary):
    try:
        binary_values = binary.split(' ')
        ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
        return ''.join(ascii_characters)
    except ValueError:
        return "Oops! That doesn't look like valid binary input. Make sure it's 8-bit binary (e.g., 01000001)."

def binary_speech(binary):
    """
    Play sounds to 'speak' binary. Higher pitch for 1, lower pitch for 0.
    """
    print("Beep-boop! Let me speak this binary for you! 🎶")

    for bit in binary.replace(" ", ""):
        if platform.system() == "Windows":
            if bit == '1':
                winsound.Beep(1000, 200)  # High pitch for 1
            elif bit == '0':
                winsound.Beep(600, 200)  # Lower pitch for 0
        else:
            # Cross-platform alternative (just prints '1' and '0' for now)
            if bit == '1':
                print('Beep! (high)', end=' ', flush=True)
            elif bit == '0':
                print('Boop! (low)', end=' ', flush=True)
        time.sleep(0.1)  # Small pause between beeps

def binbot_ascii_face():
    face = r"""
        ___________
       /           \
      /  0     0    \
     |      ^        |
      \    _____    /
       \___________/
    """
    return face

def main():
    print("👾 Hello! I'm BinBot, your friendly Binary Translator! 👾")
    print("I can help you convert text to binary, decode binary back to text, or even 'speak' in binary!")
    print("I absolutely LOVE working with 0s and 1s. Let's have some fun!")

    print(binbot_ascii_face())

    while True:
        print("\nChoose an option:")
        print("1. Text to Binary")
        print("2. Binary to Text")
        print("3. Let me speak the binary! 🎤")
        print("4. Exit")
        
        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            text = input("Enter text to convert to binary: ")
            binary_output = text_to_binary(text)
            print("Beep-boop! Crunching those letters into binary... \n")
            print(f"Binary representation: {binary_output}")
            print("============================================== \n")
        elif choice == '2':
            binary_input = input("Enter binary to convert to text (space-separated 8-bit binary values): ")
            print("Decoding this binary mystery into text... \n")
            text_output = binary_to_text(binary_input)
            print(f"Text representation: {text_output}")
            print("============================================== \n")
        elif choice == '3':
            binary_input = input("Enter binary for me to 'speak' (space-separated 8-bit binary values): ")
            if all(bit in ['0', '1', ' '] for bit in binary_input):
                binary_speech(binary_input)
            else:
                print("Oops! That binary input doesn't look right. Please make sure it's made up of 0s and 1s.")
        elif choice == '4':
            print("Goodbye, human! Come back when you need more binary magic! 🤖")
            break
        else:
            print("Oops! That doesn't seem right. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
