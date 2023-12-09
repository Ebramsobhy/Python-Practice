from time import time

def speedTest(func):
    
    def nestedFunc():
        
        start = time()
        func()
        end = time()

        print(f"Function running time is: {end - start}")

    return nestedFunc

@speedTest
def bigLoop():
    for numbers in range(1, 20000):
        print(numbers)

bigLoop()        