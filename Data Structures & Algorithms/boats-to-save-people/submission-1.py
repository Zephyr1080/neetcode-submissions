class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1          # lightest person pairs up
            r -= 1               # heaviest person always leaves in this boat
            boats += 1
        return boats
        