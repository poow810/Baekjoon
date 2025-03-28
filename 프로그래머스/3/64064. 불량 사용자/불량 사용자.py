from itertools import combinations, permutations

def is_match(user, banned):
    if len(user) != len(banned):
        return False
    for u, b in zip(user, banned):
        if b != '*' and u != b:
            return False
    return True

def solution(user_id, banned_id):
    result_set = set()

    for comb in combinations(user_id, len(banned_id)):
        for perm in permutations(comb):
            if all(is_match(perm[i], banned_id[i]) for i in range(len(banned_id))):
                result_set.add(frozenset(perm))
                break 

    return len(result_set)