#!/usr/bin/python3.8
import json


def print_kv(k, v):
    print(f'{k:20} => {v:80d}')


def solve_x(s: int, k: int, h: int, r: int, q: int) -> int:
    return ((s * k - h) * pow(r, -1, q)) % q


def solve_k(r: int, g: int, p: int, q: int, k_range: range) -> int:
    for k in k_range:
        test_r = pow(g, k, p) % q
        if test_r == r:
            return k
    raise RuntimeError("No solution")


def sign(k: int, g: int, p: int, q: int, h: int, x: int) -> (int, int):
    r: int = pow(g, k, p) % q
    k_inverse: int = pow(k, -1, q)
    s: int = (h + x * r) * k_inverse % q
    return r, s


def main():
    # Phase 1: Read Input
    with open("zxing7_input.json") as fp:
        input_object = json.load(fp)

    p: int = input_object["p"]
    q: int = input_object["q"]
    g: int = input_object["g"]
    h: int = int(input_object["h"], 16)
    y: int = input_object["y"]
    r: int = input_object["r"]
    s: int = input_object["s"]

    print_kv("p", p)
    print_kv("q", q)
    print_kv("g", g)
    print_kv("h", h)
    print_kv("y", y)
    print_kv("r", r)
    print_kv("s", s)

    # Phase 2: Solve
    k: int = solve_k(r, g, p, q, range(1, 65536))
    print_kv("k", k)

    x: int = solve_x(s, k, h, r, q)
    print_kv("x", x)

    # Phase 3: Verify
    r_out, s_out = sign(k, g, p, q, h, x)
    print_kv("r_out", r_out)
    print_kv("s_out", s_out)

    if r_out != r or s_out != s:
        raise RuntimeError("Signature Mismatched")

    y_out: int = pow(g, x, p)
    print_kv("y_out", y_out)
    if y_out != y:
        raise RuntimeError("Public Key Mismatched")

    if x < 0 or x >= q:
        raise RuntimeError("Private key out of range")

    return 0


if __name__ == "__main__":
    main()
