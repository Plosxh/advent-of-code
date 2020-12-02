
def main(inputs):
    print(inputs)


if __name__ == '__main__':
    with open("./inputs.txt","r") as file:
        main(file.read().splitlines())
    main()