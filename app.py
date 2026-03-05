def reverse_string(text):
    return text[::-1]


if __name__ == "__main__":
    user_input = input("Enter a string 1 : ")
    print("Reversed string:", reverse_string(user_input))