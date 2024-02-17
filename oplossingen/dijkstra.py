from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, List, Dict, Tuple, Callable, Iterable

T = TypeVar("T")


@dataclass
class DijkstraResult(Generic[T]):
    found: bool
    dist: Optional[float]
    path: Optional[List[T]]

    visited: Dict[T, Tuple[float, Optional[T]]]


def dijkstra(starts: List[T], next: Callable[[T], Tuple[bool, Iterable[Tuple[T, float]]]]) -> DijkstraResult[T]:
    """
    starts: list of start nodes, all assumed with cost 0
    next: callable (node) -> (is_end, [(neighbor, dist)])

    notes: this can also be used to:
    * compute the distance too all nodes in the graph, just always return is_end=False and read result.visited
    * floodfill, same as before but ignore all distances
    """

    import heapq

    # priority queue of (dist, node, parent)
    todo: List[(float, T, Optional[T])] = [(0, start, None) for start in starts]
    heapq.heapify(todo)

    # node -> (best_dist, best_parent)
    visited = {}

    while todo:
        dist, node, parent = heapq.heappop(todo)

        if node in visited:
            continue
        visited[node] = (dist, parent)

        is_end, neighbors = next(node)

        # done, collect path
        if is_end:
            path = []
            curr = node
            while curr is not None:
                path.append(curr)
                _, curr = visited[curr]
            path.reverse()
            return DijkstraResult(found=True, dist=dist, path=path, visited=visited)

        # not done, visit neighbors
        for neighbor, weight in neighbors:
            if neighbor not in visited:
                heapq.heappush(todo, (dist + weight, neighbor, node))

    return DijkstraResult(found=False, dist=None, path=None, visited=visited)
