def avoidObstacles(inputArray):
    jump = 1
    while True:
        jump += 1
        if sorted([i % jump for i in inputArray])[0] > 0:
            return jump
