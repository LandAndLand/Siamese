import sys


QUERIES = 100
file = open(sys.argv[1], 'r')

minutes = 0
seconds = 0.0
for line in file:
    if 'Elapsed' in line:
        split_line = line.replace('Elapsed (wall clock) time (h:mm:ss or m:ss):', '').split(':')
        minutes += int(split_line[0].strip())
        seconds += float(split_line[1].strip())
    # if 'User time' in line:
    #     split_line = line.replace('User time (seconds):', '')
    #     seconds += float(split_line.strip())

print('m:', minutes, 's:', seconds)
print('total seconds:', minutes * 60 + seconds)
print('avg seconds:', (minutes * 60 + seconds)/QUERIES)