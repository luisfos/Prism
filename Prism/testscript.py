#!/usr/bin/env python3
import time

def busy_work():
    total = 0
    for i in range(10**7):
        total += i % 5
    return total

if __name__ == "__main__":
    print("Starting busy work...")
    result = busy_work()
    print(f"Result: {result}")
    time.sleep(3)
    print("Done.")
