x = 10
def outher_method():
    x = 20
    print(f"{x} : Frome outher method")
    def inner_method():
        nonlocal x
        x=50
        print(f"{x} : Frome inner method")
    inner_method()


outher_method()
print(f"{x} : Frome global")
