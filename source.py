#!/usr/bin/python3.8
import json
import math


def print_kv(k, v):
    print(f'{k:20} => {v:80d}')


def wrap_around(start: int, step: int, target: int) -> (int, int):
    num_steps, quotient = divmod(target, step)
    if quotient * 2 > step:
        num_steps += 1
    new_start: int = (start + num_steps * step) % target
    return num_steps, new_start


def lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)


def solve_x3(s: int, k: int, h: int, r: int, q: int) -> int:
    print_kv("r", r)

    start: int = (k * s - h) % r

    step: int = (k * q) % r

    n: int = 1
    i: int = 0
    while start != 0 and i < 100:
        print_kv("start", start)
        if step == 0:
            raise RuntimeError("Hit a wall...")
        num_steps, new_start = wrap_around(start, step, r)
        new_step = new_start - start
        print_kv("new_step", new_step)

        step = new_step
        start = new_start
        n *= num_steps

        i += 1

    x, remainder = divmod((k * (s + n * q) - h), r)
    if remainder != 0:
        raise RuntimeError("Result is wrong")
    return x


def solve_x2(s: int, k: int, h: int, r: int, q: int) -> int:
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


def solve_x1(s: int, k: int, h: int, r: int, q: int) -> int:
    # constraint to solve:
    # (x, 0) = divmod(ks - h + nkq , r)
    kq = k * q
    offset = (k * s - h)
    print_kv("q", q)
    print_kv("r", r)
    print_kv("kq", kq)
    print_kv("offset", offset)
    m = 0
    n = 249018150293514463697521504033785680812009408931 \
        + m * 455326676787712335755587942590900495631551334913
    print_kv("n", n)
    x, remainder = divmod((offset + n * kq), r)
    if remainder != 0:
        raise RuntimeError("Wrong x - cannot divide cleanly")

    return x


def solve_x(s: int, k: int, h: int, r: int, q: int) -> int:
    return 0


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
    print(json.dumps(input_object, indent=4))

    p: int = input_object["p"]
    q: int = input_object["q"]
    g: int = input_object["g"]
    m: str = input_object["m"]
    h: int = int(input_object["h"], 16)
    y: int = input_object["y"]
    r: int = input_object["r"]
    s: int = input_object["s"]

    # Phase 2: Solve
    k: int = solve_k(r, g, p, q, range(1, 65536))
    print_kv("k", k)

    x: int = solve_x2(s, k, h, r, q)
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

    if x < 1 or x >= q:
        raise RuntimeError("Private key out of range")

    return 0


if __name__ == "__main__":
    main()
