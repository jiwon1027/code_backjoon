e, s, m = map(int, input().split())

# e 15
# s 28
# m 19
e_temp, s_temp, m_temp, cnt = 1, 1, 1, 1

while True:
    if e == e_temp and s == s_temp and m == m_temp:
        break

    e_temp += 1
    s_temp += 1
    m_temp += 1
    cnt += 1

    if e_temp > 15:
        e_temp = 1
    if s_temp > 28:
        s_temp = 1
    if m_temp > 19:
        m_temp = 1

print(cnt)