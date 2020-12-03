
def main(inputs):
    offsets = [{"offset":1, "down":1},
               {"offset":3, "down":1},
               {"offset":5, "down":1},
               {"offset":7, "down":1},
               {"offset":1, "down":2}]
    total_trees = 1
    for offset in offsets:
        trees = do_count_trees(inputs,offset["offset"], offset["down"])
        total_trees = total_trees*trees
    print(total_trees)


def do_count_trees(inputs, offset, down):
    path = []
    line = 0
    for key, value in enumerate(inputs):
        if key%down == 0:
            path.append(value[(line*offset)%(len(value))])
            line = line +  1
    #print("offset {} down {} trees {}".format(offset,down, path.count("#")))
    return path.count("#")

if __name__ == '__main__':
    with open("./inputs.txt","r") as file:
        main(file.read().splitlines())