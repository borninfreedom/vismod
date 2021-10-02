from collections import deque

CAPACITY = 20

history = deque()


def add_history(his: str = None) -> None:
    if his:
        if not history:
            history.append(his)
        elif history and his != history[-1]:
            history.append(his)

    if len(history) > CAPACITY:
        history.popleft()
