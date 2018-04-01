def growingPlant(upSpeed, downSpeed, desiredHeight):
    return max([(desiredHeight - upSpeed - 1) / (upSpeed - downSpeed) + 2, 1])
