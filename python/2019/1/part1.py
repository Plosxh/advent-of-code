import math

def main():
    inputs = ""

    with open("inputs.txt") as inputs_file:
        inputs = inputs_file.read().splitlines()
    total_fuel = 0
    for input in inputs:
        fuel = math.trunc(int(input)/3)-2
        total_fuel = total_fuel + fuel
        print("for {} fuel needed is {}".format(input,fuel))
    print(total_fuel)

if __name__ == '__main__':
    main()