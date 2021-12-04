from problem import Problem
from solver import BabyStep, GiantStep


def main():
    problem = Problem(h=78, g=46, p=10093)
    baby_step = BabyStep(problem)
    baby_table = baby_step.solve()

    print("problem:")
    print(f"{problem.g}^x ≡ {problem.h} (mod {problem.p})")
    print()

    print("baby table:")
    print(baby_table)
    print(f"n: {baby_step.get_n()}")
    print()

    giant_step = GiantStep(baby_step)
    x = giant_step.solve()

    print(f"x: {x}")

    print("solution:")
    print(f"{problem.g}^{x} ≡ {problem.h} (mod {problem.p})")


if __name__ == '__main__':
    main()
