lower = 10
upper = 100
lower =int(input("Enter a lower number({}---{}):".format(lower,upper)).strip())
upper =int(input("Enter a upper number({}---{}):".format(lower,upper)).strip())

for i in range(lower , upper):
    print("{} {}".format(i, chr(i)))



