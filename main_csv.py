import csv
import random
from queue import Queue
import time
import datetime

def downloadReport(content):
    dt = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    fname = f"report{dt}.txt"
    with open(fname, 'w') as f:
        for line in content:
            f.write(line + '\n')

filename = input('Enter file name (without extension): ') + ".csv"
Q = Queue()
n=0
try:
    with open(filename, mode='r', encoding='utf-8-sig') as file:
        csvfile = csv.reader(file,delimiter=';')

        data = list(csvfile)

        random.shuffle(data)
        
        for row in data:
            Q.put(row)
            n += 1
except:
    print("File not found :(")
    exit(-1)

correct = 0
total = 0
startTime = time.time()
while not Q.empty():
    print("Queue size:", Q.qsize())
    d = Q.get()
    ipt = input(f"\n{d[0]} = ").strip()
    ans = d[1]
    if ipt == ans:
        print("Correct")
        correct += 1
    else:
        print("Wrong, answer is", ans)
        Q.put(d)
    total += 1

elapsedTime = time.time() - startTime
acc = 100*correct/total

content = [
    filename,
    f"Time: {elapsedTime:.1f} seconds",
    f"Accuracy: {correct}/{total} = {acc:.1f}%"
    ]
downloadReport(content)

print('\nReport saved.')
input('Enter to quit')
