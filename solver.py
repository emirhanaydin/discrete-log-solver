import math

from problem import Problem


class BabyStep:
    def __init__(self, problem: Problem):
        self._problem = problem
        self._table = {}
        self._n = None

    def solve(self) -> dict[int, int]:
        d = self._table
        if len(d) != 0:
            return dict(d)

        problem = self._problem

        g = problem.g
        p = problem.p

        n = math.ceil(math.sqrt(p - 1))
        self._n = n

        for i in range(n):
            d[pow(g, i, p)] = i

        return dict(d)

    def get_problem(self) -> Problem:
        return self._problem

    def get_n(self) -> int:
        return self._n


class GiantStep:
    def __init__(self, baby_step: BabyStep):
        self._baby_step = baby_step
        self._problem = baby_step.get_problem()
        self._solution = None

    def solve(self) -> int:
        if self._solution is not None:
            return self._solution

        problem = self._problem
        baby_step = self._baby_step

        d = baby_step.solve()

        h = problem.h
        g = problem.g
        p = problem.p

        n = baby_step.get_n()
        c = pow(g, n * (p - 2), p)

        for i in range(n):
            y = (h * pow(c, i, p)) % p
            if y in d:
                self._solution = i * n + d[y]
                return self._solution
