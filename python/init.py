import os
import requests
import argparse
import sys
import shutil
import json


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Advent of Code initer.")
    parser.add_argument("-y","--year",help="input year like : YYYY")
    parser.add_argument("-d","--day",help="input day like : D")
    options = parser.parse_args(args)

    work_dir = os.getcwd()
    target_dir = f"{work_dir}/{options.year}/{options.day}"
    url = f"https://adventofcode.com/{options.year}/day/{options.day}/input"

    with open(work_dir+"/config.json","r") as file:
        headers = json.load(file)
        code = requests.get(url, headers=headers)
        open(f"{target_dir}/inputs.txt","wb").write(code.content)
        shutil.copy(f"{work_dir}/base.py",f"{target_dir}/main.py")


if __name__ == '__main__':
    main()

