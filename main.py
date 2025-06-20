def main():
    pass


# ALGORITAM

# create init population

# ga:
#   do while (nesto)
#       crossover
#       provera dobijenih childova
#       ako moze, smanjimo broj gena u jednom chromosomu
#
#    prirodna selekcija?? bira se pola najboljih
#    nad dobijenom novom populacijom, primeniti mutaciju

# chromosomi sa najmanjom duzinom su najbolja resenja




# CLASSES

# id, x, y, rot

# gene (predstavlja jednu tablu, i id-eve piecova na njoj + rotacija)
# sadrzi kolko kojeg imam

# chromosome (predstavlja niz gena (tabli))
# piece (width, height, id)

# gui klasa (matplot lib, sta god)
# treba uraditi input (iz fajla, iz konzole + meni???)




# METHDOS

# crossoveer (prima 2 chromosoma, vraca 2 chromosoma) - urađeno                                     NIKSA
# check_chromosome (prima chromosome, provera uslove + skrati broj gena ako je moguce) - urađeno    NIKSA
# plotovanje resenja - urađeno                                                                      NIKSA
# fitness_function  MOZDA NAM NE TREBA                                                              NIKSA


# mutacija (prima chromosomm, vraca mutirani chromosome)                 VEDRAN
# input piecova + velicina table                                         VEDRAN
# create_init_population                                                 VEDRAN
# natural_selection (80-20, nesto, treba uzimati i malo losih hromozoma) VEDRAN




if __name__ == "__main__":
    main()