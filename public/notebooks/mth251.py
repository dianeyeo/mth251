module = "mth251"

a = module + " var a"
b = module + " var b"


def func251():
    a = "func251 var a"
    b = "func251 var b"
    print("<--- func251 locals -->")
    print(locals())


class Student251:

    a = "Student251 class var a"

    def func251(self):
        a = "Student2022 func251 var a"
        b = "Student2022 func251 var b"
        print("<--- Student251 instance locals -->")
        print(locals())


print("from module: ", module)
