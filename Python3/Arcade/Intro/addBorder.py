def addBorder(picture):
    out = ["*"*(len(picture[0])+2)]
    for i in range(len(picture)):
        out.append("*" + picture[i] + "*")
    out.append("*"*(len(picture[0])+2))
    return out
