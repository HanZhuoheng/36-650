def Oneaway(s1, s2):
    m, n = len(s1), len(s2)
    if abs(m - n) > 1:
        return False
    if m <= n:
        for i in range(m):
            if s1[i] != s2[i]:
                if m == n:
                    return s1[i+1:] == s2[i+1:]
                else:
                    return s1[i:] == s2[i+1:]
            else:
                return m+1 == n
    if m > n:
        return Oneaway(s2, s1)