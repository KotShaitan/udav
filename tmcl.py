def replace_common(st, letter):
    dick={}
    for i in st:
        if i != " ":
            dick[i] = dick.get(i, 0) + 1
    return st.replace(max(dick.keys(), key = lambda x: dick[x]), letter)

print(replace_common("aabddfghhh", "l"))