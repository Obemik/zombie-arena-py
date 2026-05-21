from data.config import ARENA_WIDTH, ARENA_HEIGHT


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance_to(self, other) -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def copy(self):
        return Position(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Arena:
    def __init__(self):
        self.width = ARENA_WIDTH
        self.height = ARENA_HEIGHT
        self.cells = {}

    def is_valid(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def is_free(self, x: int, y: int) -> bool:
        return self.is_valid(x, y) and (x, y) not in self.cells

    def place(self, entity, x: int, y: int):
        old = (entity.position.x, entity.position.y)
        if old in self.cells and self.cells[old] is entity:
            del self.cells[old]
        self.cells[(x, y)] = entity
        entity.position.x = x
        entity.position.y = y

    def remove(self, entity):
        key = (entity.position.x, entity.position.y)
        if key in self.cells and self.cells[key] is entity:
            del self.cells[key]

    def get_entity_at(self, x: int, y: int):
        return self.cells.get((x, y), None)

    def get_free_spawn_point(self):
        import random
        edges = []
        for x in range(self.width):
            edges.append((x, 0))
            edges.append((x, self.height - 1))
        for y in range(1, self.height - 1):
            edges.append((0, y))
            edges.append((self.width - 1, y))
        random.shuffle(edges)
        for x, y in edges:
            if self.is_free(x, y):
                return x, y
        return None