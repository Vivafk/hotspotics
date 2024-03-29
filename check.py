# f = open('stile.txt', 'r')
# l = f.readlines()
# f.close()
# l = [line.rstrip() for line in l]
# di = l[0]
# hash = l[1]

p = open('ps.txt', 'r')
l = p.readlines()
p.close()
l = [line.rstrip() for line in l]
p.close()

password = l[0]
print(password)
