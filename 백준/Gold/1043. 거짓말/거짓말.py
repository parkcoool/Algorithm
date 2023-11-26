PPL_CNT, PARTY_CNT = map(int, input().split())
KNOW_PPL = set(map(int, input().split()[1:]))
PPL_IN_PARTIES = []
for _ in range(PARTY_CNT):
    PPL_IN_PARTIES.append(set(map(int, input().split()[1:])))
KNOW_PARTIES = set()

while True:
    stop = True
    for i in range(PARTY_CNT):
        ppl = PPL_IN_PARTIES[i]
        if not ppl.isdisjoint(KNOW_PPL):
            KNOW_PARTIES.add(i)
            for p in ppl:
                if p not in KNOW_PPL:
                    KNOW_PPL.add(p)
                    stop = False
    if stop:
        break

print(PARTY_CNT - len(KNOW_PARTIES))
