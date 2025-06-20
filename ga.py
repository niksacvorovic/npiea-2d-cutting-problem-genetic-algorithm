def crossover():
    pass

def mutation():
    pass

# Pretpostavljamo da su klase Piece i Chromosome definisane kao u prethodnom odgovoru
# (sa effective_width, effective_height, i listom pieces unutar Chromosome)

# Pretpostavljamo da je funkcija pack_pieces_leftmost definisana kao u prethodnom odgovoru
# def pack_pieces_leftmost(stock_width, stock_height, pieces_to_pack):
#    ... (logika za pakovanje i vraćanje bounding_box_area, total_placed_area, used_width, used_height)

def pack_pieces_leftmost(stock_width, stock_height, pieces_to_pack):
    """
    Simulira heuristiku pakovanja "što je moguće levlje".
    Pokušava da postavi svaki deo na prvu dostupnu poziciju (x, y)
    počevši od (0,0), idući po redovima, pa po kolonama.

    Vraća:
    - bounding_box_area: Površina najmanjeg pravougaonika koji obuhvata sve postavljene delove.
    - total_placed_area: Ukupna površina svih uspešno postavljenih delova.
    - used_width, used_height: Dimenzije bounding box-a.
    """
    # Matrica (ili skup koordinata) koja prati zauzete ćelije na materijalu
    occupied_coords = set()

    # Pratimo maksimalne dimenzije koje su zauzeli postavljeni delovi
    max_x_used = 0
    max_y_used = 0

    total_placed_area = 0

    print("\n--- Simulacija pakovanja 'što je moguće levlje' ---")
    print(f"Početna matrica ({stock_width}x{stock_height}) je prazna.")

    for i, piece in enumerate(pieces_to_pack):
        placed = False
        print(
            f"\nPokušavam da postavim deo {piece.piece_id} (efektivno {piece.effective_width}x{piece.effective_height})")

        # Tražimo prvu slobodnu poziciju (x, y) za postavljanje dela
        for y in range(stock_height):
            for x in range(stock_width):
                # Provera da li deo izlazi izvan granica materijala
                if x + piece.effective_width > stock_width or \
                        y + piece.effective_height > stock_height:
                    continue  # Ne uklapa se ovde, probaj sledeću poziciju

                # Provera preklapanja sa već postavljenim delovima
                overlaps = False
                for px in range(x, x + piece.effective_width):
                    for py in range(y, y + piece.effective_height):
                        if (px, py) in occupied_coords:
                            overlaps = True
                            break
                    if overlaps:
                        break

                if not overlaps:
                    # Deo se uklapa i ne preklapa, postavi ga
                    for px in range(x, x + piece.effective_width):
                        for py in range(y, y + piece.effective_height):
                            occupied_coords.add((px, py))

                    # Ažuriraj maksimalno korišćene dimenzije
                    max_x_used = max(max_x_used, x + piece.effective_width)
                    max_y_used = max(max_y_used, y + piece.effective_height)
                    total_placed_area += (piece.effective_width * piece.effective_height)
                    print(f"  Deo {piece.piece_id} postavljen na ({x},{y}).")
                    placed = True
                    break  # Deo je postavljen, pređi na sledeći deo
            if placed:
                break

        if not placed:
            # U idealnom scenariju, svi delovi bi trebalo da budu postavljeni.
            # Ako deo ne može da se postavi, to ukazuje na loš hromozom ili nedovoljan materijal.
            # U stvarnom GA, ovo bi rezultiralo veoma niskim (lošim) fitnesom.
            print(
                f"  UPOZORENJE: Deo {piece.piece_id} nije mogao biti postavljen! (Ovo bi u stvarnosti dovelo do lošeg fitnesa)")
            # Za ovu demonstraciju, nastavljamo, ali u realnoj primeni bi se ovo moralo pažljivo rešiti.

    print("\n--- Rezultati pakovanja ---")
    print(f"Maksimalna X koordinata korišćena (širina graničnog okvira): {max_x_used}")
    print(f"Maksimalna Y koordinata korišćena (visina graničnog okvira): {max_y_used}")
    print(f"Ukupna površina zauzeta postavljenim delovima: {total_placed_area}")

    # Izračunaj površinu graničnog okvira (bounding box) koji obuhvata sve postavljene delove
    bounding_box_area = max_x_used * max_y_used
    print(f"Površina graničnog okvira (bounding box) korišćenog materijala: {bounding_box_area}")

    return bounding_box_area, total_placed_area, max_x_used, max_y_used

def fitness_function(chromosome, stock_width, stock_height):
    """
    Parametri:
    - chromosome: Objekat Chromosome koji sadrži listu Piece objekata (gena) sa njihovim rotacijama i redosledom.
    - stock_width: Širina raspoloživog materijala.
    - stock_height: Visina raspoloživog materijala.

    Vraća:
    - Vrednost fitnesa (float).
    """

    # KORAK 1: Primena heuristike pakovanja
    # Ova funkcija simulira fizičko postavljanje delova na materijal
    # i vraća informacije o iskorišćenom prostoru.
    bounding_box_area, total_placed_area, used_width, used_height = \
        pack_pieces_leftmost(stock_width, stock_height, chromosome.pieces)

    # KORAK 2: Izračunavanje vrednosti fitnesa na osnovu rezultata pakovanja

    # 2.1. Početna vrednost fitnesa (maksimalni mogući fitnes)
    # "Početna vrednost fitnesa je dužina materijala pomnožena sa njegovom širinom." [3]
    initial_fitness_value = stock_width * stock_height

    # 2.2. Smanjenje za prazne ćelije (otpad)
    # "Nakon popunjavanja matrice materijala delovima, vrednost fitnesa se smanjuje
    # za ukupan broj 'praznih ćelija'." [3]
    # "Prazne linije materijala se ignorišu." [3]
    # To znači da se otpad računa samo unutar najmanjeg pravougaonika koji obuhvata
    # sve postavljene delove (bounding box).
    waste_in_bounding_box = bounding_box_area - total_placed_area
    # Osiguravamo da otpad nije negativan (ako bi se npr. desila greška u pakovanju)
    waste_in_bounding_box = max(0, waste_in_bounding_box)

    # 2.3. Smanjenje za količinu rezova
    # "Vrednost fitnesa se dodatno smanjuje za 'količinu rezova'." [3]
    # Projekat ne precizira tačnu kvantifikaciju "količine rezova".
    # U realnoj implementaciji, ovo bi bila složenija metrika (npr. ukupna dužina rezova,
    # broj faza sečenja, itd.). Za demonstraciju, koristimo jednostavnu kaznu.
    # Što više delova, to više rezova, pa je kazna veća.
    cuts_penalty = len(chromosome.pieces) * 0.5  # Primer: kazna od 0.5 po delu

    # 2.4. Konačna vrednost fitnesa
    # "Najbolje jedinke [imaju] najveću vrednost fitnesa." [3]
    # Stoga, oduzimamo kazne od početne vrednosti.
    final_fitness = initial_fitness_value - waste_in_bounding_box - cuts_penalty

    # Opciono: Možete dodati i kaznu ako svi delovi nisu mogli biti postavljeni
    # if total_placed_area < sum(p.effective_width * p.effective_height for p in chromosome.pieces):
    #     final_fitness -= large_penalty_for_unplaced_pieces

    # Ažurirajte fitnes vrednost hromozoma
    chromosome.fitness = final_fitness

    return final_fitness