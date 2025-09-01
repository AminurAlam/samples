import random

items = [[4, 2], [5, 3], [2, 4], [3, 1], [6, 5]]
max_weight: int = 10
population_size: int = 10
mut_prob = 0.2
generations: int = 30
pop = [[random.choice([0, 1]) for _ in items] for _ in range(10)]


def calc_fit(chromo: list[int]):
    filtered = [items[i] for i, gene in enumerate(chromo) if gene == 1]
    weight = sum([x[0] for x in filtered])
    value = sum([x[1] for x in filtered])

    return 0 if weight > max_weight else value


def sel_chromosome(pop: list[list[int]]):
    fit_vals: list[float] = [calc_fit(chromo) for chromo in pop]
    weights = [i / sum(fit_vals) for i in fit_vals]

    p1 = random.choices(pop, weights=weights, k=1)[0]
    p2 = random.choices(pop, weights=weights, k=1)[0]

    return p1, p2


def crossover(p1: list[int], p2: list[int]):
    cross = random.randint(0, len(items) - 1)
    return p1[0:cross] + p2[cross:], p2[0:cross] + p1[cross:]


def mutate(chromo: list[int]):
    point = random.randint(0, len(items) - 1)
    chromo[point] = int(not chromo[point])
    return chromo


for _ in range(generations):
    c1, c2 = crossover(*sel_chromosome(pop))
    if random.random() < mut_prob: c1 = mutate(c1)
    if random.random() < mut_prob: c2 = mutate(c2)

    pop[0], pop[1] = c1, c2

fit_vals = [calc_fit(chromo) for chromo in pop]
best = pop[fit_vals.index(max(fit_vals))]
filtered = [items[i] for i, gene in enumerate(best) if gene == 1]

print(f"""
Items: {items}
Genetic algorithm parameters:
    Max weight: {max_weight}
    Population: {population_size}
    Mutation probability: {mut_prob}
    Generations: {generations}
The best solution:
    Best: {best}
    Weight: {sum([x[0] for x in filtered])}
    Value: {sum([x[1] for x in filtered])}""")
