type, *value = [i.rstrip(",") for i in input().rstrip(";").split()]

for v in value:
    alpha_tmp = ""
    mark_tmp = ""
    for s in v:
        if s.isalpha():
            alpha_tmp += s
        if s == "[":
            mark_tmp = "[]" + mark_tmp
        if s == "]": continue
        if s in ["*", "&"]:
            mark_tmp = s + mark_tmp

    print(f'{type}{mark_tmp} {alpha_tmp};')