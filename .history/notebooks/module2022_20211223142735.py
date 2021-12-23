module = "2022"

a = module + " a"
b = module + " b"

a = "global a"

def f1():
    a = "f1 a"
    b = "f1 b"
    print("<--- f1 locals -->")
    print(locals())

def f2():
    a = "f2 a"
    b = "f2 b"
    print("<--- f2 locals -->")
    print(locals())

class Student:

    a = "Student Class a"

    def f(self):
        a = "Student func a"
        b = "Student func b"
        print("<--- instance locals -->")
        print(locals())

print("<--- globals -->")
print(globals().keys())
print("b: ", globals().get("b"))

# locals
f1()
f2()
s = Student()
s.f()

# add & remove b
b = "global b"
print("<--- globals -->")
print("b:", globals().get("b"))

del b
print("<--- globals -->")
print("b:", globals().get("b"))
