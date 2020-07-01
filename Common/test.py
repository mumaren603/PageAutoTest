
t1 = {'wxtest':2,'tztest':'3','yxtest':1}
cmdopt='yxtest'

# for k,v in t1.items():
#     if k == cmdopt:
#         print("ok",k)
#         t1={cmdopt:v}
# 
# 
# print('t1',t1)

for i in t1:
    print(i)
    if i == cmdopt:
        count = t1.get(cmdopt)
        print(count)

