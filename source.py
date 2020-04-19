#!/usr/bin/python3
import json
from math import ceil


def print_kv(k, v):
    print(f'{k:20} => {v:50d}')


def wrap_around(start: int, step: int, target: int) -> (int, int):
    num_steps, quotient = divmod(target - start, step)
    if quotient * 2 > step:
        num_steps += 1
    new_start: int = (start + num_steps * step) % target
    if new_start * 2 > target:
        new_start = new_start - target
    return num_steps, new_start


def solve_x(s: int, k: int, h: int, r: int, q: int) -> int:
    print_kv("r", r)

    start: int = (k * s - h) % r

    step: int = (k * q) % r

    n: int = 1
    i: int = 0
    while start != 0 and i < 50000:
        print_kv("i", i)
        print_kv("start", start)
        print_kv("step", step)

        if step == 0:
            print_kv("n", n)
            raise RuntimeError("Hit a wall...")

        num_steps, new_start = wrap_around(start, step, r)
        new_step = (new_start - start) % step

        if step <= new_step:
            raise RuntimeError("It's not converging..")
        step = new_step
        start = new_start
        n *= num_steps
        print_kv("num_steps", num_steps)
        print_kv("n", n)

        current_remainder = (k * s + k * n * q - h) % r
        print_kv("current_remainder", current_remainder)
        print_kv("new_start % r", new_start % r)

        i += 1

    x, remainder = divmod((k * (s + n * q) - h), r)
    if remainder != 0:
        raise RuntimeError("Result is wrong")
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
    print_kv("k", k)

    x: int = solve_x(s, k, h, r, q)
    print_kv("x", x)

    return 0


if __name__ == "__main__":
    main()
