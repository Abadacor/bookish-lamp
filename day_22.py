from icecream import ic
import re, collections

with open('day_22_input.txt') as file_input:
    values = file_input.readlines()

#fancy dict en fait, c'est un dict ou tu peux facilement ressortir un compte de valeurs
cubes = collections.Counter()
for line in values:
    #cube on ou off
    nsgn = 1 if line.split()[0] == "on" else -1
    #plages de valeurs du cube qu'on traite
    nx0, nx1, ny0, ny1, nz0, nz1 = map(int, re.findall("-?\d+", line))

    #pour chaque cube deja traité, trouve l'intersection avec le cube en traitement
    update = collections.Counter()
    for (ex0, ex1, ey0, ey1, ez0, ez1), esgn in cubes.items():
        ix0 = max(nx0, ex0); ix1 = min(nx1, ex1)
        iy0 = max(ny0, ey0); iy1 = min(ny1, ey1)
        iz0 = max(nz0, ez0); iz1 = min(nz1, ez1)
        # cette condition est remplie s'il y a intersection seulement
        if ix0 <= ix1 and iy0 <= iy1 and iz0 <= iz1:
            # le cube d'intersection se cancel en fonction de la valeur du cube en traitement
            update[(ix0, ix1, iy0, iy1, iz0, iz1)] -= esgn
    # si le cube en traitement est un ON, on le rajoute en entier puisqu'on a enlevé toutes ses intersections
    if nsgn > 0:
        update[(nx0, nx1, ny0, ny1, nz0, nz1)] += nsgn
    cubes.update(update)

#On somme ce qu'on veut obtenir pour le chall. le nombre de cube de dimensions 1 1 1 dans une range c'est le produit de l'ecart de chaque +1
ic(sum((x1 - x0 + 1) * (y1 - y0 + 1) * (z1 - z0 + 1) * sgn
          for (x0, x1, y0, y1, z0, z1), sgn in cubes.items()))