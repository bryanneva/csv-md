import csv
import os


def convert(filename):
    if not os.path.exists('out'):
        os.mkdir('out')

    with open(filename, newline='') as csv_file:
        nist_controls = csv.reader(csv_file, delimiter=',')
        for control in nist_controls:
            status = build_status(control)
            file_name = control[0] + ".md"
            md_file = open('out/' + file_name, "a")
            md_file.write("# NIST Control: " + control[0] + "\n")
            md_file.write("## Task: " + control[3] + "\n")
            md_file.write("\n")
            md_file.write("* Status: " + status + "\n")
            md_file.write("* Tracker URL: [" + control[7] + "](" + control[7] + ")" + "\n")
            md_file.write("\n")
            md_file.write("**Description**" + "\n")
            md_file.write("\n")
            md_file.write(control[2] + "\n")
            md_file.write("\n")
            md_file.write("**Task Description**" + "\n")
            md_file.write("\n")
            md_file.write(control[4])
            md_file.write("\n")
            md_file.close()


def build_status(control):
    status = control[10]
    if status is None and control[9]:
        status = 'Inherited from Platform'
    elif status is None and not control[8]:
        status = 'Not relevant'
    else:
        status = "Not Complete"
    return status
