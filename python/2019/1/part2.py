import math

def main():
    inputs = ""

    with open("inputs.txt") as inputs_file:
        inputs = inputs_file.read().splitlines()
    total_fuel = 0
    for input in inputs:
        fuel = math.trunc(int(input) / 3) - 2
        total_fuel += fuel
        while(math.trunc(fuel/3)-2>0):

            trunc_fuel = math.trunc(fuel/3) - 2
            print("trunc_fuel is {}".format(trunc_fuel))
            total_fuel += trunc_fuel
            fuel = trunc_fuel
    print(total_fuel)


if __name__ == '__main__':
    main()