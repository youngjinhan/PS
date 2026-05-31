class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        sorted_ast = sorted(asteroids)

        for a in sorted_ast:
            if mass < a:
                return False

            mass += a
        return True