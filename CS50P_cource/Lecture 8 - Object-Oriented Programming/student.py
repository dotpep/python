def main():
    name, house = get_student()
    print(f"{name} from {house} ")

def get_student():
    name = input("Name: ")
    house = input("Name: ")
    return name, house


if __name__ == "__main__":
    main()



"""
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")
"""