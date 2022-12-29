from collections import namedtuple
from typing import List, Union


def sift_up(data: List[float], i: int):
    if i == 0:
        return
    parent = (i - 1) // 2
    if data[parent] > data[i]:
        data[parent], data[i] = data[i], data[parent]
        sift_up(data, parent)


def sift_down(data: List[float], i: int):
    child1 = i * 2 + 1
    child2 = i * 2 + 2
    if child1 >= len(data):
        return
    if child2 >= len(data):
        child_min = child1
    else:
        child_min = child1 if data[child1] < data[child2] else child2
    if data[child_min] < data[i]:
        data[i], data[child_min] = data[child_min], data[i]
        sift_down(data, child_min)


def heapify(data):
    for i in range(len(data) - 1, -1, -1):
        sift_down(data, i)


def heappush(data: List[float], x: float):
    data.append(x)
    sift_up(data, len(data) - 1)


def heappop(data: List[float], i: int = 0) -> float:
    data[i], data[-1] = data[-1], data[i]
    res = data.pop()
    sift_up(data, i)
    sift_down(data, i)
    return res


cin: List[List[Union[str, int]]] = []
with open("algo/HW6/eyewatch/input.txt", "r") as i_f:
    for s in i_f.readlines():
        line = s.rstrip("\n").split()
        if len(line) > 1:
            line[1:] = [int(i) for i in line[1:]]
        else:
            try:
                line[0] = int(line[0])
            except ValueError:
                pass

        cin.append(line)

print(cin)

