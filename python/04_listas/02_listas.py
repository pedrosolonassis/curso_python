# %%

x = []
for i in range(1,101):
    x.append(i)
x
# %%

y = [i for i in range(1,101)]
y
# %%

def eh_par(n):
    return n % 2 == 0

z = [eh_par(i) for i in range(1,101)]
z

# %%

w = [i for i in range(1,101) if eh_par(i)]
w