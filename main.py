import colorama
x=6
y=1
iterations=1000
hueCycles=2

def hToRGB(h):
    h = (h % 360) / 60.0
    c = 1
    x = 1 - abs(h % 2 - 1)
    if   0 <= h < 1: r, g, b = c, x, 0
    elif 1 <= h < 2: r, g, b = x, c, 0
    elif 2 <= h < 3: r, g, b = 0, c, x
    elif 3 <= h < 4: r, g, b = 0, x, c
    elif 4 <= h < 5: r, g, b = x, 0, c
    else:            r, g, b = c, 0, x
    return int(r*255), int(g*255), int(b*255)


def f(z,c):
    return [z[0]**2-z[1]**2+c[0],2*z[0]*z[1]+c[1]]

def test(a,c):
    for j in range(iterations):
        a=f(a,c)
        if (abs(a[0])>100 or abs(a[1])>100):
            color=hToRGB(360*hueCycles*(j/iterations))
            return f"\033[38;2;{color[0]};{color[1]};{color[2]}m▮\033[0m"
    color=hToRGB(360*hueCycles)
    return f"\033[38;2;{color[0]};{color[1]};{color[2]}m▮\033[0m"
    #return " "

list = []


for i in range(500*y):
    list.append([])
    for r in range(400*x):
        list[i].append([])
        a=[(r-300*x)/(200*x),(i-250*y)/(250*y)]
        c=a
        list[i][r]=test(a,c)

def show(liszt):
    for i in range(len(liszt)):
        for j in range(len(liszt[0])):
            print(liszt[i][j],end="")
        print("|")

print("----------------------")
show(list)
print("----------------------")
