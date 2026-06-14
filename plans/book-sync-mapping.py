#!/usr/bin/env python3
"""Frozen old->new book-number mapping for the B12 sync (PLAN_book-sync.md step 2).

4 inserts, 4 retirements (folded into siblings), renumber to flex chapters 19-21.
This file is the source of truth for the mechanical renumber pass (step 3+) and
asserts the result is a bijection on 1..100 before any file is touched.
"""

# Inserts: new rule -> (chapter, the new book number it takes)
INSERTS = {
    "input-security": 3,    # Ch1, after the secret rules
    "idempotency":    47,   # Ch3, after container-friendly
    "latency-budget": 77,   # Ch4, after full-regression
    "state":          84,   # Ch5, after persist-decisions
}

# Retirements: old book number -> book number of the sibling it folds into
RETIRE = {
    38:  30,   # SOLID            -> Objects with one job each (Ch2)
    59:  50,   # Structured logs  -> A logger, never print (Ch3, post-renumber 50)
    60:  52,   # Line endings     -> Path libraries (Ch3, post-renumber 52)
    100: 10,   # Say what you install -> No anonymous dependencies (Ch1, new 10)
}

# old book number -> new book number, for the 96 surviving rules.
# Built by walking 1..100, skipping retirements, and shifting past inserts.
OLD_TO_NEW = {
    # Ch1 (old 1-20 -> new 1-21; input-security takes new 3)
    1:1, 2:2, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9, 9:10, 10:11,
    11:12, 12:13, 13:14, 14:15, 15:16, 16:17, 17:18, 18:19, 19:20, 20:21,
    # Ch2 (old 21-40 -> new 22-40; old 38 SOLID retired)
    21:22, 22:23, 23:24, 24:25, 25:26, 26:27, 27:28, 28:29, 29:30, 30:31,
    31:32, 32:33, 33:34, 34:35, 35:36, 36:37, 37:38, 39:39, 40:40,
    # Ch3 (old 41-60 -> new 41-59; idempotency new 47; old 59,60 retired)
    41:41, 42:42, 43:43, 44:44, 45:45, 46:46, 47:48, 48:49, 49:50, 50:51,
    51:52, 52:53, 53:54, 54:55, 55:56, 56:57, 57:58, 58:59,
    # Ch4 (old 61-80 -> new 60-80; latency new 77)
    61:60, 62:61, 63:62, 64:63, 65:64, 66:65, 67:66, 68:67, 69:68, 70:69,
    71:70, 72:71, 73:72, 74:73, 75:74, 76:75, 77:76, 78:78, 79:79, 80:80,
    # Ch5 (old 81-100 -> new 81-100; state new 84; old 100 retired)
    81:81, 82:82, 83:83, 84:85, 85:86, 86:87, 87:88, 88:89, 89:90, 90:91,
    91:92, 92:93, 93:94, 94:95, 95:96, 96:97, 97:98, 98:99, 99:100,
}


def verify():
    survivors = [n for n in range(1, 101) if n not in RETIRE]
    assert len(survivors) == 96, len(survivors)
    # every surviving old number is mapped
    missing = [n for n in survivors if n not in OLD_TO_NEW]
    assert not missing, f"unmapped survivors: {missing}"
    # new numbers = survivors' new + inserts' new == exactly 1..100, no dups
    new_nums = sorted(list(OLD_TO_NEW.values()) + list(INSERTS.values()))
    assert new_nums == list(range(1, 101)), (
        f"NOT a bijection: dups={[x for x in set(new_nums) if new_nums.count(x)>1]}, "
        f"len={len(new_nums)}")
    # chapter sizes
    def ch(n): return (n - 1) // 20 + 1 if n <= 100 else 5
    sizes = {}
    for n in INSERTS.values():
        sizes[("Ch", n)] = None
    # count new numbers per flexed chapter range
    ranges = {"Ch1": (1, 21), "Ch2": (22, 40), "Ch3": (41, 59),
              "Ch4": (60, 80), "Ch5": (81, 100)}
    for name, (lo, hi) in ranges.items():
        cnt = sum(1 for x in new_nums if lo <= x <= hi)
        print(f"  {name}: {cnt} rules ({lo}-{hi})")
    print("BIJECTION ON 1..100: OK")


if __name__ == "__main__":
    verify()
