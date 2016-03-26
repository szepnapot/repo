def checkio(data):
    data.sort()
    if len(data) % 2 != 0:
        return data[int(round(len(data)/2))]
    else:
        return (data[(len(data)/2)-1]+data[len(data)/2])/2.0



data1 = [1, 2, 3, 4, 5]
data2 = [1, 300, 2, 200, 1]
data3 = [3, 6, 20, 99, 10, 15]

checkio(data1)
checkio(data2)
checkio(data3)
