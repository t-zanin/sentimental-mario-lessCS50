def get_positive_int():
    while True:
        try:
            height = int(input("Height: "))
            if 1 <= height <= 8:
                return height
            else:
                print("Height must be an integer between 1 and 8, inclusive.")
        except ValueError:
            print("Please enter a valid integer.")

def print_pyramid(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        hashes = '#' * i
        print(f"{spaces}{hashes}")

def main():
    height = get_positive_int()
    print_pyramid(height)

if __name__ == "__main__":
    main()
