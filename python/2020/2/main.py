


def  main(inputs):
    valid_password = 0
    for input in inputs:
        split = input.split(" ")
        plit = input.split(" ")
        first, second = split[0].split("-")
        policy = split[1][:-1]
        password = split[len(split) - 1]
        if (password[int(first)-1] ==policy) != (password[int(second)-1] == policy):
            valid_password +=1
    print(valid_password)


def main_part_1(inputs):
    valid_password = 0
    for input in inputs:
        split = input.split(" ")
        min, max = split[0].split("-")
        policy = split[1][:-1]
        password = split[len(split)-1]
        if int(min) <= password.count(policy) <= int(max):
            valid_password += 1
    print(valid_password)


if __name__ == '__main__':
    with open("./inputs.txt","r") as file:
        main(file.read().splitlines())