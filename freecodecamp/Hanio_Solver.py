def hanio_solver(n):
    pegs = [[ _ for _ in range(n, 0, -1)], [], []]
    steps = str(pegs) + '\n'
    checks = [None, None, None]
    for t in range(1, (2**n)):
        num = 0
        cospeg = []
        for i, peg in enumerate(pegs):
            checks[i] = min(peg) if peg else 0
            if checks[i] == 1:
                speg = i
            else:
                cospeg += [i]
            if checks[i] > 1:
                num += 1
        if t % 2:
            if num == 0:
                target = 2
            elif num == 1:
                target = cospeg[0] if checks[cospeg[0]] else cospeg[1]
            else:
                target = cospeg[1] if checks[cospeg[1]] < checks[cospeg[0]]else cospeg[0]
            aux = 3 - (target + speg)
            group = []
            for i in range(1, len(pegs[speg]) +1):
                if i in pegs[speg]:
                    group += [i]
                else:
                    break
            if len(group) % 2:
                pegs[speg].remove(1)
                pegs[target].append(1)
            else:
                pegs[speg].remove(1)
                pegs[aux].append(1)
        else:
            if num == 1:
                src = cospeg[0] if checks[cospeg[0]] else cospeg[1]
            else:
                src = cospeg[0] if checks[cospeg[0]] < checks[cospeg[1]] else cospeg[1]
            target = 3 - (src + speg)
            pegs[src].remove(checks[src])
            pegs[target].append(checks[src])
        steps += str(pegs) + '\n'
    return steps
print(hanio_solver(20))