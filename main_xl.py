import pandas as pd
import random
from collections import deque
import time
import datetime

def downloadReport(content):
    dt = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    fname = f"report{dt}.txt"
    with open(fname, 'w') as f:
        for line in content:
            f.write(line + '\n')

filename = input('Enter file name (without extension): ') + ".xlsx"
n = 0
try:
    df = pd.read_excel(filename)
    print(df)
    queLbl,ansLbl = list(df.columns)
    
    n = len(df)
except Exception as e:
    print("Error occured while reading file:", e)
    exit(-1)

print("n:",n)
indexes = list(range(n))
random.shuffle(indexes)
Q = deque(indexes)
print(indexes)

correct = 0
total = 0
startTime = time.time()
while len(Q) > 0:
    print("Queue size:", len(Q))
    idx = Q.pop()
    prompt = df[queLbl][idx]
    ans = df[ansLbl][idx]
    
    ipt = input(f"\n{prompt} = ").strip()
    
    if ipt.lower() == ans.lower():
        print("Correct")
        correct += 1
    else:
        print("Wrong, answer is", ans)
        Q.appendleft(idx)
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
