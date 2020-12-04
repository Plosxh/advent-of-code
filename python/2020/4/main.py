
MANDATORY = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
def main(inputs):
    passports = get_all_passports(inputs)
    counter = 0
    for passport in passports:
        print("Doing New passport")
        print(MANDATORY)
        if check_passeport_validity(passport, MANDATORY):
            counter += 1

    print(counter)

def check_passeport_validity(passeport, valid):
    mandatory_fields = []
    print(passeport)

    for line in passeport:
        print(line)
        splitted = line.split(" ")
        for field in splitted:
            key, value = field.split(":")
            if check_passeport_fields(key,value):
                if key in valid:
                    mandatory_fields.append(key)
    if len(mandatory_fields) != len(valid):
        print('is False')
        return False
    else:
        print('is True')
        return True


def get_all_passports(passeports):
    all_passports = []
    p = []
    for line in passeports:
        print(line)
        if line != "":
            p.append(line)
        else:
            print("is empty")
            print(p)
            all_passports.append(p)
            p = p.copy()
            p.clear()
            print(p)
    print(all_passports)
    return all_passports

def check_passeport_fields(field, value):
    if field == "byr":
        if 1920 <= int(value) <= 2002:
            return True
        else:
            return False
    elif field == "iyr":
        if 2010 <= int(value) <= 2020:
            return True
        else:
            return False
    elif field == "eyr":
        if 2020 <= int(value) <= 2030:
            return True
        else:
            return False
    elif field == "hgt":
        if "cm" in value or "in" in value:
            try:
                i = int(value[:-2])
                if "cm" in value:
                    if 150 <= int(value[:-2]) <= 193:
                        return True
                    else:
                        return False
                if "in" in value:
                    if 59 <= int(value[:-2]) <= 76:
                        return True
                    else:
                        return False
            except:
                return False
    elif field == "hcl":
        if len(value) == 7 and value[0] == "#":
            return True
        else:
            return False
    elif field == "ecl":
        if value in ["amb","blu","brn","gry","grn","hzl","oth"]:
            return True
        else:
            return False
    elif field == "pid":
        if len(value) == 9:
            try:
                i = int(value)
                return True
            except:
                return False
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    with open("./inputs.txt","r") as file:
        main(file.read().splitlines())