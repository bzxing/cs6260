#!/usr/bin/python3
import itertools
import json


def solve_x(s: int, k: int, h: int, r: int, q: int) -> int:
    n: int
    for n in itertools.count():
        x, remainder = divmod(k * (s + n * q) - h, r)
        if remainder == 0:
            return x


def solve_k(r: int, g: int, p: int, q: int, k_range: range) -> int:
    for k in k_range:
        test_r = pow(g, k, p) % q
        if test_r == r:
            return k
    raise RuntimeError("No solution")


def main():
    with open("zxing7_input.json") as fp:
        input_object = json.load(fp)
    print(json.dumps(input_object, indent=4))

    p: int = input_object["p"]
    q: int = input_object["q"]
    g: int = input_object["g"]
    m: str = input_object["m"]
    h: int = int(input_object["h"], 16)
    y: int = input_object["y"]
    r: int = input_object["r"]
    s: int = input_object["s"]

    k: int = solve_k(r, g, p, q, range(1, 65536))
    print(k)

    x: int = solve_x(s, k, h, r, q)
    print(x)

    return 0


if __name__ == "__main__":
    main()
