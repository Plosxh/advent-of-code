import math

def main(inputs):
    seat_ids = []
    for input in inputs:
        row, col = check_seat(input)
        seat_ids.append(row*8+col)
    sorted_seats = sorted(seat_ids)
    for seat in sorted_seats:
        if seat +1 not in sorted_seats:
            print("my seat is {}".format(seat+1))


def check_seat(input):
    seats_col = []
    seats_row = []
    for i in range(127):
        seats_row.append(i)
    for i in range(8):
        seats_col.append(i)
    for i in input[0:7]:
        if i == "F":
            seats_row = seats_row[:math.ceil(len(seats_row)/2)]
        elif i == "B":
            seats_row = seats_row[math.ceil(len(seats_row)/2):]
    for i in input[len(input)-3:]:
        if i == "L":
            seats_col = seats_col[:math.ceil(len(seats_col)/2)]
        elif i == "R":
            seats_col = seats_col[math.ceil(len(seats_col)/2):]
    return seats_row[0], seats_col[0]


if __name__ == '__main__':
    with open("./inputs.txt","r") as file:
        main(file.read().splitlines())