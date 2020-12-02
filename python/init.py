import os
import requests
import shutil
import json

work_dir = os.getcwd().split("/")
print(work_dir)
day = work_dir[len(work_dir)-1]
year = work_dir[len(work_dir)-2]
url = "https://adventofcode.com/{}/day/{}/input".format(year,day)
print(url)

with open("/".join(work_dir[:-2])+"/config.json","r") as file:
    headers = json.load(file)
    code = requests.get("https://adventofcode.com/2020/day/1/input", headers=headers)
    open("./inputs.txt","wb").write(code.content)
    shutil.copy("/".join(work_dir[:-2])+"/base.py","./main.py")

