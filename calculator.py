def center(points: list, c: dict) -> list:
    answer = []
    
    for point in points:
        cur = {'x': 0.0, 'y': 0.0, 'z': 0.0}
        for i in 'xyz':
            cur[i] = point[i] - c[i]
        answer.append(cur)
    return answer


def normalize(points: list) -> list:
    maximum = 0
    for point in points:
        cur = 0
        for coordinate in point.values():
            cur += coordinate ** 2
        maximum = max(maximum, cur)

    answer = []
    for point in points:
        cur = {'x': 0.0, 'y': 0.0, 'z': 0.0}
        for i in 'xyz':
            cur[i]= round(point[i] / (maximum ** 0.5), 5)
        answer.append(cur)
    return answer


def toCylindrical(points: list) -> list:
    answer = []
    for point in points:
        cur = {'h': 0.0, 'd': 0.0, 'sin': '', 'cos': ''}
        cur['h'] = point['y']
        cur['d'] = round((point['x'] ** 2 + point['z'] ** 2) ** 0.5, 5)
        sin = round(point['z'] / cur['d'], 5)
        cos = round(point['x'] / cur['d'], 5)

        if sin >= 0:
            cur['sin'] = f'{cos}sinx + {sin}cosx'
            cur['cos'] = f'{cos}cosx - {sin}sinx'
        else:
            cur['sin'] = f'{cos}sinx - {-sin}cosx'
            cur['cos'] = f'{cos}cosx + {-sin}sinx'
           
        answer.append(cur)
    return answer


order = input('The order of coordinates is ')
c = dict(zip(order, (map(lambda x: float(x), input('Central point is ').split()))))
fileName = input('Enter the name of the file: ')


with open(fileName, encoding='utf-8') as fileInput:
    points = [dict(zip(order, map(lambda x: float(x), line.strip().split()))) for line in fileInput.readlines()]


cylindrical = toCylindrical(normalize(center(points, c)))


with open('output.txt', 'w', encoding='utf-8') as fileOutput:
    for i in range(len(points)):
        fileOutput.write(f'Point №{i + 1}:  {points[i]} -> {cylindrical[i]}\n')