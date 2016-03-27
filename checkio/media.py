def checkio(data):
    data.sort()
    if len(data) % 2 != 0:
        index = (len(data)-1)//2
        return data[index]
    else:
        return (data[(len(data)//2)-1]+data[len(data)//2])/2.0
    