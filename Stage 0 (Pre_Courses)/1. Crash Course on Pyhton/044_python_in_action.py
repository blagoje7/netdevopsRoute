# scenario is
# Every month, you are handed a spreadsheet with hundreds of new hires.
# You are asked to create user accounts for all of them on Linux server.
# The formatting on spreadsheet looks like this:

#username, password, real_name
# amanda,,Amanda Alonso
# ian,,Ian Ortega
# eugene,,Eugene Konya

# Password field is empty for all of the records.
# This means you need to generate random passwords for each user and then create their accounts
# You also want to write all the passwords you generate back to a new CSV so that you can tell new employees their passwords


# The script

# read a list of new hires from users_in.csv
# generate random 16-character passwords for each
# create each user account
# write the spreadsheet back to user_out.csv

# Tools

# import csv
# import secrets
# import subprocess
# from pathlib import Path # to locate the data files



# Getting started 

import csv
import secrets
import subprocess
from pathlib import Path

cwd = Path.cwd() / "drive/MyDrive/Coplab Notebooks"
with open(cwd / "data/users_in.csv", "r") as file_input, open(cwd / "data/users_out.csv", "w") as file_output:
    reader = csv.DictReader(file_input)
    writer = csv.DictWriter(file_output, fieldnames=reader.fieldnames)
    writer.writeheader()


for user in reader:
    user["password"] = secrets.token_hex(8)
    useradd_cmd = ["/sbin/useradd",
                   "-c", user["real_name"],
                   "-m",
                   "-G", "users",
                   "-p", user["password"],
                   user["username"]]
    subprocess.run(useradd_cmd, check=True)

