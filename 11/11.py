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
    return open("input_small.txt").read().split()


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


def transform_stone_ll(i: int, stones: list):
    pass


def solve_first(stones):
    acc = 0
    for blink in range(25):
        for i, stone in enumerate(stones):
            stones = transform_stone(i, stones)
        print(blink)
    print(len(stones))
    return acc


def solve_second(stones):
    acc = 0
    return acc


# print(cProfile.run('solve_first(parse())'))
# print(solve_second(parse()))
first_node = Node("a")
llist = LinkedList(["a", "b", "c"])
print(llist)
for i in llist:
    print(i)
