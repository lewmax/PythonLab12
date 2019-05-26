import re

log = open("log", "r")
output = open("result.txt", "w+")

counter = 0

if log.mode == "r":
    line = log.readline()

while line:
    get_request = re.search("GET /presentations", line)
    success_request = re.search("\"\s[4-5][0-9][0-9]\s", line)
    time_request = re.search(
    "((17/May/2015:[0][4-9]:[0-5][0-9]:[0-5][0-9])|(17/May/2015:[1][0-9]:[0-5][0-9]:[0-5][0-9])|(17/May/2015:[2][1]:[0-1][0-9]:[0-5][0-9])|(17/May/2015:[2][1]:[2][0-8]:[0-5][0-9])|(17/May/2015:[2][1]:[2][0-8]:[0][0]))", line)
    # "((17/May/2015)|(:[0][4-9]:[0-5][0-9]:[0-5][0-9])|([1][0-9]:[0-5][0-9]:[0-5][0-9])|([2][0]:[0-5][0-9]:[0-5][0-9])|([2][1]:[0-1][0-9]:[0-5][0-9])|([2][1]:[2][0-8]:[0][0]))", line)
    # "(:[0][2]:[1][9]:[3-5][0-9])|(:[0][2]:[2-5][0-9]:[0-5][0-9])|(:[0][3-9]:[0-5][0-9]:[0-5][0-9])|(:[1][0-1]:[0][0-9]:[0-2][0-9])|(:[1][0]:[0-5][0-9]:[0-5][0-9])", line)
    # if get_request and success_request and time_request:
    if get_request and success_request and time_request:
        line = line.strip()
        output.write(line)
        output.write('\n')
        counter = counter + 1
    line = log.readline()

output.write(str(counter))
log.close()
output.close()
