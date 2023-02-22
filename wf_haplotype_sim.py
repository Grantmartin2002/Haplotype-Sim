import random

possible_alleles = [0, 1, 2, 3]


def print_generation_stats(G, i, total_mutations, mutations_this_iteration):
    print()
    print("GENERATION", str(i) + ":")
    print("New Mutations:", mutations_this_iteration)
    print("Total mutations:", total_mutations)
    print("New Matrix:", G)
    print(G)


def simulate(n, l, max_generations, mutation_rate):
    # set every entry in genotype matrix G to 0
    total_mutations = 0
    mutations_this_iteration = 0
    G = [[0 for i in range(l)] for j in range(2 * n)]
    print_generation_stats(G, 0, total_mutations, mutations_this_iteration)

    for i in range(max_generations):
        mutations_this_iteration = 0
        # mutation
        for x in range(len(G)):
            for y in range(len(G[i])):
                if random.random() < mutation_rate:
                    mutations_this_iteration += 1
                    # make random mutation excluding current allele?

                    current_allele = G[x][y]
                    allele_pool = possible_alleles.copy()
                    allele_pool.remove(current_allele)
                    new_allele = random.choice(allele_pool)
                    G[x][y] = new_allele
        total_mutations += mutations_this_iteration
        # WF sampling
        G_prime = list()
        for x in range(2 * n):
            u = random.randint(1, 2 * n)
            G_prime.append(G[u - 1])
        G = G_prime
        print_generation_stats(G, i + 1, total_mutations, mutations_this_iteration)


n = int(input("Enter population size: "))
l = int(input("Enter Haplotype Size: "))
max_generations = int(input("Enter Number of Generations: "))
mutation_rate = float(input("Enter Mutation Rate (as a decimal, not %): "))

simulate(n, l, max_generations, mutation_rate)
