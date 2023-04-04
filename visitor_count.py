import os
import cgi

count_file = 'visitor_count.txt'

if os.path.exists(count_file):
    with open(count_file, 'r') as f:
        count = int(f.read())
else:
    count = 0

count += 1

with open(count_file, 'w') as f:
    f.write(str(count))
    
# print("Content-Type: text/plain")
# print()
# print(f"Total Visitors: {count}")
