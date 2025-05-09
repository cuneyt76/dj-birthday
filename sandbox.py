import time

t1 = time.time()
for i in range(1000):
    i = 1
t2 = time.time()
print((t2-t1)*1000)


t1 = time.time()
for i in range(10000):
    i = 1
t2 = time.time()
print((t2-t1)*1000)

