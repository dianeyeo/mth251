module = "2022"

a = module + " a"
b = module + " b"

def f2022():
    a = "f2022 a"
    b = "f2022 b"
    print("<--- f2022 locals -->")
    print(locals())


class Student2022:

    a = "Student2022 Class a"

    def f(self):
        a = "Student2022 func a"
        b = "Student2022 func b"
        print("<--- instance locals -->")
        print(locals())

print("from module: ")