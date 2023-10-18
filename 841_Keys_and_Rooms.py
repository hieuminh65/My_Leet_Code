class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        if not rooms[0]:
            return False
        visited = []

        stack = []
        visited.append(0)
        stack.extend(rooms[0])

        while stack:
            popE = stack.pop()
            if popE not in visited:
                visited.append(popE)
                stack.extend(rooms[popE])


        return len(visited) == len(rooms)