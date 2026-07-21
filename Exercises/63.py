import time

i = 0
while True:
    time.sleep(i)
    print("Hello")
    i = i + 1
    if i == 4:
        print("End of Loop")
        break

