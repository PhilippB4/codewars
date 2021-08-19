def solution(st, limit):
    return st[:limit] + '...' if len(st) > limit else st