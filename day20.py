import numpy as np

with open("day20_input") as infile:
    particles = [
                    [
                        np.array([int(a) for a in l[0][l[0].index('<')+1:].split(',')]),
                        np.array([int(a) for a in l[1][l[1].index('<')+1:].split(',')]),
                        np.array([int(a) for a in l[2][l[2].index('<')+1:].split(',')])
                    ]
                    for l in (line.strip().split('>') for line in infile)
                ]
distances = [0 for _ in range(len(particles))]
for _ in range(50):
    i = 0
    for par in particles:
        par[1] = np.add(par[1], par[2])
        par[0] = np.add(par[0], par[1])
        dist = np.linalg.norm(par[0])
        distances[i] = dist
        i += 1
    for par in particles:
        l = [np.array_equal(par[0], x[0]) for x in particles]
        if l.count(True) > 1:
            indexes = np.where(np.array(l) == True)[0]
            for j in indexes:
                particles.pop(j)
print(distances.index(min(distances)))
print(len(particles))
