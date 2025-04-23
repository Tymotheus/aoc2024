from collections import deque
import cProfile


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


def parse():
    return open("input.txt").read().split()


def transform_stone(i: int, stones: list):
    stone = stones[i]
    if stone == "0":
        stones[i] = "1"
    elif len(stone) % 2 == 0:
        stones.pop(i)
        stones.insert(i, stone[: int(len(stone) / 2)])
        stones.insert(i + 1, stone[int(len(stone) / 2) :])
    else:
        stones[i] = str(int(stone) * 2024)
    return stones


def transform_stone_ll(stone,iterator):
    if stone.data == "0":
        stone.data = "1"
    elif len(stone.data) % 2 == 0:
        s_r = Node(stone.data[int(len(stone.data) / 2) :].lstrip("0"))
        s_r.next = stone.next
        if s_r.data == "":
            s_r.data = "0"
        stone.data = stone.data[: int(len(stone.data) / 2)].lstrip("0")
        stone.next = s_r
        next(iterator) # Yield one more argument, to account for just added Node
    else:
        stone.data = str(int(stone.data)*2024)


def solve(stones, epochs:int):
    acc = 0
    stones = LinkedList(stones)
    for blink in range(epochs):
        iterator = iter(stones)
        for stone in iterator:
            transform_stone_ll(stone, iterator)
    for _ in stones: acc+=1
    return acc



print(solve(parse(),epochs=25))
# print(solve(parse(),epochs=30))
# print(cProfile.run('solve(parse(),25)'))
