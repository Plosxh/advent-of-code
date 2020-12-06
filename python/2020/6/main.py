
def main(inputs):
    asum = 0
    rows = 0
    counter_dict = {}
    for i, input in enumerate(inputs):
        if input == "":
            for k, v in counter_dict.items():
                if v == rows:
                    asum += 1
            rows = 0
            counter_dict = {}
            continue
        rows += 1
        for c in input:
            if c in counter_dict:
                counter_dict[c] += 1
            else:
                counter_dict[c] = 1
    for k, v in counter_dict.items():
        if v == rows:
            asum += 1
    print(asum)


if __name__ == '__main__':
    with open("./inputs.txt","r") as file:
        main(file.read().splitlines())