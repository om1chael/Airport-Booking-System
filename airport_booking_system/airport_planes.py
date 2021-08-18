class Plane():
    def __init__(self, id_num, max_capacity):
        self.id = id_num
        self.max_capacity = max_capacity

    def __repr__(self):
        return f"Plane({self.id}) Capacity({self.max_capacity})"
