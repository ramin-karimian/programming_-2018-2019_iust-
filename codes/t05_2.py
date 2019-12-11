d={"ages":[18,19.20], "student_ids":{1:9247,
                                     2:9248}}
print(d["student_ids"][2])

print(d.keys())
for k in d.keys():
    print(d[k])

print(d.items())
for k,v in d.items():
    print(k," ",v)
