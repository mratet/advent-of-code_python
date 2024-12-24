from collections import defaultdict
from itertools import product

# from aocd import get_data, submit
# input = get_data(day=21, year=2024)
input = open('input.txt').read()

from collections import deque
from itertools import product

# WRITE YOUR SOLUTION HERE
DIRS = {
    (0, 1): 'v',
    (1, 0): '>',
    (0, -1): '^',
    (-1, 0): '<',
}
direction_mapping = {
    'A': {'A': ['A'], '^': ['<'], '>': ['v'], 'v': ['v<', '<v'], '<': ['v<<']},
    '^': {'A': ['>'], '^': ['A'], '>': ['>v', 'v>'], 'v': ['v'], '<': ['v<']},
    '>': {'A': ['^'], '^': ['^<', '<^'], '>': ['A'], 'v': ['<'], '<': ['<<']},
    'v': {'A': ['>^', '^>'], '^': ['^'], '>': ['>'], 'v': ['A'], '<': ['<']},
    '<': {'A': ['>>^'], '^': ['>^'], '>': ['>>'], 'v': ['>'], '<': ['A']},
}
input = """869A
170A
319A
349A
489A"""

def flatten_nested_dictionary(d):
    """
    Aplatit un dictionnaire imbriqué contenant des listes en une liste de dictionnaires uniques.

    Args:
        d (dict): Un dictionnaire avec des valeurs potentiellement imbriquées et des listes.

    Returns:
        list[dict]: Une liste de dictionnaires aplatis, chaque combinaison possible étant représentée.
    """

    def recursive_flatten(sub_d):
        """Aide à aplatir un dictionnaire imbriqué."""
        if all(not isinstance(v, dict) for v in sub_d.values()):
            # Aplatir au niveau actuel si aucune valeur n'est un dictionnaire
            keys, values = zip(*sub_d.items())
            combinations = product(*[v if isinstance(v, list) else [v] for v in values])
            return [dict(zip(keys, combo)) for combo in combinations]

        # Si le dictionnaire contient d'autres dictionnaires, aplatir récursivement
        result = [{}]
        for key, value in sub_d.items():
            if isinstance(value, dict):
                nested = recursive_flatten(value)
                result = [
                    {**outer, key: inner} for outer in result for inner in nested
                ]
            else:
                if not isinstance(value, list):
                    value = [value]
                result = [
                    {**outer, key: v} for outer in result for v in value
                ]
        return result

    # Aplatir le dictionnaire donné au niveau supérieur
    flattened = recursive_flatten(d)
    # Convertir les dictionnaires imbriqués finaux en un seul niveau
    final_result = []
    for item in flattened:
        def expand(inner):
            """Aide à aplatir les niveaux restants des dictionnaires."""
            result = {}
            for k, v in inner.items():
                if isinstance(v, dict):
                    sub_result = expand(v)
                    for sub_k, sub_v in sub_result.items():
                        result[f"{k}{sub_k}"] = sub_v
                else:
                    result[k] = v
            return result

        final_result.append(expand(item))
    return final_result


def gen_next_sequence(sequence, mapping):
    sequence = 'A' + sequence
    seq = []
    for s1, s2 in zip(sequence, sequence[1:]):
        seq.append(mapping[s1 + s2])
        if s1 != s2:
            seq.append('A')
    return ''.join(seq)

keypad_to_corr = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '0': (3, 1),
    'A': (3, 2)
}

def is_valid(path):
    if len(path) <= 2:
        return True
    if len(path) == 3 and not(path[0] == path[2] and path[0] != path[1]):
        return True
    if len(path) == 5 and (path[0] == path[1] and path[3] == path[4]):
        return True
    if len(path) == 4:
        if path[0] == path[1] and path[2] == path[3] and path[0] != path[2]:
            return True
        elif path[0] == path[1] == path[2] and path[0] != path[3]:
            return True
        elif path[1] == path[2] == path[3] and path[0] != path[1]:
            return True
    return False


def generate_shortest_paths(keypad, start, end):
    """
    Génère tous les chemins les plus courts entre deux points sur un pavé numérique avec contrainte d'interdiction de passer par une case donnée.

    Args:
        keypad (list[list[str]]): Une représentation 2D du pavé numérique.
        start (tuple): Coordonnées de départ (ligne, colonne).
        end (tuple): Coordonnées d'arrivée (ligne, colonne).

    Returns:
        list[list[tuple]]: Une liste contenant tous les chemins les plus courts, chaque chemin étant une liste de tuples de coordonnées.
    """
    start = keypad_to_corr[start]
    end = keypad_to_corr[end]
    if start == end:
        return ['A']
    rows, cols = len(keypad), len(keypad[0])
    forbidden = (3, 0)  # Contraintes : case interdite

    def neighbors(pos):
        """Retourne les voisins valides pour une position donnée."""
        r, c = pos
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Droite, Bas, Gauche, Haut
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) != forbidden:
                yield (nr, nc)

    # BFS pour trouver les chemins les plus courts
    queue = deque([[start]])
    visited = set()
    shortest_paths = []
    min_length = float('inf')

    while queue:
        path = queue.popleft()
        current = path[-1]

        # Si nous avons atteint la fin
        if current == end:
            trad_path = ''
            for (x1, y1), (x2, y2) in zip(path, path[1:]):
                dx = x2 - x1
                dy = y2 - y1
                trad_path += DIRS[(dy, dx)]
            path = trad_path
            if not is_valid(path): continue
            if len(path) < min_length:
                shortest_paths = [path]
                min_length = len(path)
            elif len(path) == min_length:
                shortest_paths.append(path)
            continue

        # Marquer comme visité
        if current in visited and len(path) > min_length:
            continue
        visited.add(current)

        # Explorer les voisins
        for neighbor in neighbors(current):
            if neighbor not in path:  # Éviter les cycles
                queue.append(path + [neighbor])

    return shortest_paths



def generate_keypad_mappings(code):
    K = ['789', '456', '123', '.0A']
    Acode = 'A' + code
    base_keypad_mapping = defaultdict(dict)
    for start, end in zip(Acode, Acode[1:]):
        base_keypad_mapping[start][end] = generate_shortest_paths(K, start, end)
    return flatten_nested_dictionary(base_keypad_mapping)

def find_best_keypad_mapping(code, direction):
    keypad_mappings = generate_keypad_mappings(code)
    tab = []
    for i, keypad_mapping in enumerate(keypad_mappings):
        w = gen_next_sequence(code, keypad_mapping)
        for _ in range(5):
            w = gen_next_sequence(w, direction)
        tab.append((len(w), i))
    tab.sort()
    return tab[0][1]

def part_1(lines):
    lines = lines.splitlines()
    base_direction_mapping = {
        'A': {'A': ['A'], '^': ['<'], '>': ['v'], 'v': ['v<', '<v'], '<': ['v<<']},
        '^': {'A': ['>'], '^': ['A'], '>': ['>v', 'v>'], 'v': ['v'], '<': ['v<']},
        '>': {'A': ['^'], '^': ['^<', '<^'], '>': ['A'], 'v': ['<'], '<': ['<<']},
        'v': {'A': ['>^', '^>'], '^': ['^'], '>': ['>'], 'v': ['A'], '<': ['<']},
        '<': {'A': ['>>^'], '^': ['>^'], '>': ['>>'], 'v': ['>'], '<': ['A']},
    }
    direction_mappings = flatten_nested_dictionary(base_direction_mapping)
    best_direction = direction_mappings[15]
    ans = 0
    for code in lines:
        best_idx = find_best_keypad_mapping(code, best_direction)
        keypad_mapping = generate_keypad_mappings(code)[best_idx]
        numeric_part = int(code[:3])
        w = gen_next_sequence(code, keypad_mapping)
        for _ in range(2):
            w = gen_next_sequence(w, best_direction)
        ans += numeric_part *  len(w)
    return ans

def get_best_direction_mapping():
    base_direction_mapping = {
        'A': {'A': ['A'], '^': ['<'], '>': ['v'], 'v': ['v<', '<v'], '<': ['v<<']},
        '^': {'A': ['>'], '^': ['A'], '>': ['>v', 'v>'], 'v': ['v'], '<': ['v<']},
        '>': {'A': ['^'], '^': ['^<', '<^'], '>': ['A'], 'v': ['<'], '<': ['<<']},
        'v': {'A': ['>^', '^>'], '^': ['^'], '>': ['>'], 'v': ['A'], '<': ['<']},
        '<': {'A': ['>>^'], '^': ['>^'], '>': ['>>'], 'v': ['>'], '<': ['A']},
    }
    direction_mappings = flatten_nested_dictionary(base_direction_mapping)
    return direction_mappings[15] # Trouver en testant sur plusieurs exemples

def get_transition_dict(direction):
    d = {}
    for v in direction.values():
        if v == 'A': continue
        k = 'A' + v + 'A'
        t = []
        for m1, m2 in zip(k, k[1:]):
            if direction[m1 + m2] == 'A': t.append('A')
            else:
                t.append(direction[m1 + m2] + 'A')
        d[v + 'A'] = t
    d['A'] = ['A']
    return d

def get_next_state(D, transition_dict):
    new_D = defaultdict(int)
    for k, c in D.items():
        for symb in transition_dict[k]:
            new_D[symb] += c
    return new_D

def part_2(lines):
    lines = lines.splitlines()
    best_direction = get_best_direction_mapping()
    transition_dict = get_transition_dict(best_direction)
    ans = 0
    for code in lines:
        best_idx = find_best_keypad_mapping(code, best_direction)
        keypad_mapping = generate_keypad_mappings(code)[best_idx]
        numeric_part = int(code[:3])
        w = gen_next_sequence(code, keypad_mapping)
        w = gen_next_sequence(w, best_direction)
        D = defaultdict(int)
        for symb in w.replace('A', 'A ').split():
            D[symb] += 1
        for _ in range(25 - 1):
            D = get_next_state(D, transition_dict)
        W = sum([len(k) * v for k, v in D.items()])
        ans += numeric_part * W
    return ans

# END OF SOLUTION
print(f'My answer is {part_1(input)}')
print(f'My answer is {part_2(input)}')
