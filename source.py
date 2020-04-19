#!/usr/bin/python3
import json
from math import ceil


def print_kv(k, v):
    print(f'{k:20} => {v:50d}')


def wrap_around(start: int, step: int, target: int) -> (int, int):
    num_steps, quotient = divmod(target, step)
    if quotient * 2 > step:
        num_steps += 1
    new_start: int = (start + num_steps * step) % target
    return num_steps, new_start


def solve_x(s: int, k: int, h: int, r: int, q: int) -> int:
    # constraint to solve:
    # (x, 0) = divmod(ks - h + nkq , r)
    m = 0
    n = 249018150293514463697521504033785680812009408931 \
        + m * 455326676787712335755587942590900495631551334913
    x, remainder = divmod((k * (s + n * q) - h), r)
    return x


def solve_k(r: int, g: int, p: int, q: int, k_range: range) -> int:
    for k in k_range:
        test_r = pow(g, k, p) % q
        if test_r == r:
            return k
    raise RuntimeError("No solution")


def sign(k: int, g: int, p: int, q: int, h: int, x: int) -> (int, int):
    r: int = pow(g, k, p) % q
    a, b = divmod((h + x * r), k)
    if b != 0:
        raise RuntimeError("Cannot divide nicely")
    s: int = a % q
    return r, s


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

    r_out, s_out = sign(k, g, p, q, h, x)
    print_kv("r_out", r_out)
    print_kv("s_out", s_out)

    if r_out != r or s_out != s:
        raise RuntimeError("Signature Mismatched")

    y_out: int = pow(g, x, p)
    print_kv("y_out", y_out)
    if y_out != y:
        raise RuntimeError("Public Key Mismatched")

    if x < 1 or x >= q:
        raise RuntimeError("Private key out of range")

    return 0


if __name__ == "__main__":
    main()
