

"""print("area calculator")
width =int(input("Enter width"))
height =int(input("Enter height"))
depth =int(input("Enter depth"))

area = width*height
volume = width*height*depth
print("area" ,area, "volume" ,volume)
"""


def get_values():
    """ function to get the length and width """
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))
    return length, width


def main():
    length, width = get_values()
    area= length * width
    print(area)

main()