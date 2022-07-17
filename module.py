from arithmetic import person
import arithmetic as ar

if __name__ == '__main__':
    add = ar.add(50, 30)
    print("Add = ", add)

    sub = ar.sub(50, 30)
    print("Subtract = ", sub)

    div = ar.div(50, 30)
    print("Divide = ", div)

    mul = ar.multiply(50, 30)
    print("Multiply = ", mul)

    print("Country = ", person["country"])

    print(dir(ar))
