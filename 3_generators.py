from time import time, sleep

# def gen_filename():
#     while True:
#         t = int(time()*1000)
#         yield f"file-{t}.jpeg"
#
# g = gen_filename()
#

def gen1(s):
    for i in s:
        sleep(1)
        yield i

def gen2(n):
    for i in range(n):
        yield i

g1 = gen1("test")
g2 = gen2(10)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
