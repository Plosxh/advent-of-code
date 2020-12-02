
def main(inputs):
    sorted_inputs = sorted(inputs)
    for part in sorted_inputs:
        part_to_find = check_missing_to_2020(part,2020)
        for second_part in sorted_inputs:
            if int(second_part) < part_to_find:
                third_part = check_missing_to_2020(second_part, part_to_find)
                if is_second_part_here(third_part, sorted_inputs):
                    #print(" {} * {} * {}".format(part, second_part,third_part))
                    print(int(part)*int(second_part)*int(third_part))


def is_second_part_here(second_part, all_parts):
    return  str(second_part) in all_parts

def check_missing_to_2020(num,base):
    return base - int(num)

if __name__ == '__main__':
    with open("./inputs.txt","r") as file:
        main(file.read().splitlines())