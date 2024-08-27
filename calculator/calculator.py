import strings
import images

def clear_screen():
    print("\n" * 100)

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def run_calculator(art, strings, operations, use_result, result=None):
    if use_result == "n":
        clear_screen()
        print(art)
        n1 = int(input(f"{strings.requestFirstNumber} \n"))
    else:
        n1 = result
    operand = input(f"{strings.requestOperation} \n")
    n2 = int(input(f"{strings.requestSecondNumber} \n"))
    result = operations[operand](n1, n2)
    print(f"{n1} {operand} {n2} = {result}")
    use_result = input(f"{strings.requestRepeat} {result}, {strings.requestRestart} \n").lower()
    run_calculator(art, strings, operations, use_result, result)

run_calculator(images.calculator, strings, operations, "n")