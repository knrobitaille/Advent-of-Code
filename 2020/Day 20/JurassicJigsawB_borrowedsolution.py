# THIS NOT MY SOLUTION
# TAKEN FROM HERE
# https://topaz.github.io/paste/#XQAAAQBtEgAAAAAAAAAyGEruliPhOB3zCEJNQbkytr3zceH3Xa8F2Mdyp/xKbDqjwUGMEyDMvkHpRraPT+IV0ck9I2IoToCeFxvmTMXetGiCRyiuY0Xl3siIv0j5XnJ2+cn1ZQLop/zqZsEMwK0hVFFzYn+skmhc57OjZAwh2PkOppWcxiQkInztAxoQnX2ztVfn/TpE10jwkD9OnTFF9pCF3wPgJtCc1nC6/wc5myuXrWo2hgxiGewIpmizY1wj68bAzRDg5/2fnHCGl2VNFTIN6TViho3/mokH6vM0lizLb/Q3qBQGBPvq6aoOJx18y6g4CHXZ5x++uGYxr9tmPJRWYpUP07XerOhW5bVJMXxpbi+yhsqPjsjOH7mRGLLxslwlV9WjfS7kkODpN4+kBZ0+XK5cfVezworx7bcqc1sHApBf0emrGz5+aqmenPyzKQdXtzJ8n5PLFipHhuqrO9mwxc7zR+SxEEF1eO1YPAJo+BDxt7xl/+F0hMZZLbHkwa8vj/XBkZrZHXjUcMpksj4H4GVOeUqqtEML5et7NxklfVAM1ajhZ/RWmyU20OM54ILmgDJ2YbsskWD3Ky8mY+h1B7lWiA7TYGt1wOCp4xoyY73Ny4nyOW6Nw00p3JHIGrEWvDkVRp4joyQXUYzUvHQ5yy0kQf6Bwmc8NbK29c2ol7WAcOAGf4r8UHT+1DLkAjAFf2eBjb3gClu+OZh5yGtIl5W5XwYSGDrPkTnYf9E3LN3Q/7TFgSxMymVncWcRsEx+e0lxHVjQZrMjtV7VsVHVYXTYcjWsXcERoMNQDo26OzZQpx10Hj+dH/TVmCW8A9+OtfjNt/qWfQNkUpALgy3CFGgPPskq84UP60juLjGfGO+mqkU3TbcvLQgeO9Ya3kb7BA2wgQmyLq7qgIz5c1vxRkflHOC2Bt7q+DdZy9Rl5cBxW9M7v6xPTbFDZQcEdTEsZWNul/lMMckQ5c8zt0II735ERSueWzas+VkIRS/AqQXt72wOzCP6i9Awn6aLx4DTYH4H4pkL1yYXQLLVvxI+HmW2gFDXASwQYbvdk8tVx6vNl7i54L2/gRmooJdK6zV6Q/3y+KgwD2E8YIqp6xRZqK7NxPNiPLt1yVI7JMc1XyZv0VQhdBjWXoYLmzYVCfkECjb0I05VPwwG83tkXlFQlXqGQ+2F6ErlT9A0RE9Zj+fQcMVhZw0ZEzjUMf4xYLk/S/tkjyX3xHd8H92VYojjKyA6g18BmjIOYGG4yYSd6/S43hxXohqZtiy5FafyWxz78xKkbHUeHQTiWqUNIyedY2cK4eweT5R7Su3NkbJSJJM76Z0WG3olF/lcngY+HdaR2t1v3Cni9Oxv5E/ZUWmd810gyiq6CzR157g241d81lJXV0WVsrIRVhB5J6CXD+QsXuyCh7N/UHTYI99O3Wuj4V8MXQkJQTZ270+F5N2KmL9iq7NOwqBRQQZBkEhjit847Ii1vqvOgz3ECv/VNGZIC+ac+7+bp+F4RgKn29sRv7GhJyAdaCb+VZGsepLt4rcoMiXf+x5wEA4Z0J8nw/6swMWvK3sKqAXwjcvVaL8tyLTmFpFN2hq5MhLxbdll//r9ebkwuRbK7SuUSz2a95tkO7Iw9vwaVwxmJpgDEfoKvWvvJIENg4QWKFg3qORRqS0KmXM/Faizy+0HsynnkjZ0/eSDSvqDnPFIulVYbXVK0hQqVPKhv0RQ4qmi0ypK1ff9IfelKqLeI/QJqu54DYNAIMG348Elclb/YO0ZXmkKGuF7nLSLvBeQNdTQiP3a8qls6pGTyNhzHAuWCSBnymxTk64bkZ/ahGOF+DChEPnbNERE+snYruaZrmPJ1TOo9NMAn3M5PS6+L1/bVtAxnS3TLAyBnxVdyetC/KUaV2rzQSxhPC7BEgc9tabDg3Bp/zBNuJHjSoz+fUKa0oKgXfJXTVM+na3Myj5RgBRVplitH+9OzRUL//mZaT8=
#

data = []

# with open('test_small.txt', 'r') as f:
# with open('test.txt', 'r') as f:
with open('input.txt', 'r') as f:
    data = f.read().splitlines()

import numpy as np

tiles = dict()
ident = ""
block = []
for line in data:
    if line == "":
        tiles[ident] = np.array(block)
        ident = ""
        block = []
        # append block
        continue
    if "Tile" in line:
        ident = int(line.split(" ")[1].split(":")[0])
        continue
    l = []
    for c in line:
        if c == ".":
            l.append(0)
        else:
            l.append(1)
    block.append(l)

tiles[ident] = np.array(block)

print("Parsing Done")

def without_keys(d, keys):
    return {x: d[x] for x in d if x not in keys}

tileSetCache = dict()

def genTileSet(tilename, tile):
    global tileSetCache
    if tilename in tileSetCache:
        return tileSetCache[tilename]
    tiles = [] 
    tiles.append(tile)
    tiles.append(np.rot90(tile, 1))
    tiles.append(np.rot90(tile, 2))
    tiles.append(np.rot90(tile, 3))
    tiles.append(np.flipud(tile))
    tiles.append(np.rot90(np.flipud(tile), 1))
    tiles.append(np.rot90(np.flipud(tile), 2))
    tiles.append(np.rot90(np.flipud(tile), 3))
    tileSetCache[tilename] = tiles
    return tiles

def solve(coordX, coordY, cubelen, solutiongrid, tiles):
    if len(tiles) == 0:
        print("Done!")
        return solutiongrid
    for tilename, tile in tiles.items():
#    tilename, tile = next(iter(tiles.items()))
        tileset = genTileSet(tilename, tile)
        solutiongrid[coordY][coordX]["id"] = tilename
        for t in tileset:
            # print("Checking Tile " + str(tilename) + " for " + str(coordY) + "," + str(coordX))
            fitX, fitY = True, True
            if coordX - 1 >= 0:
                # check, if left corner fits
                compareY = solutiongrid[coordY][coordX-1]["tile"][:, 9]
                if not np.array_equal(compareY, t[:, 0]):
                    fitX = False
            if coordY - 1 >= 0:
                # check, if top corner fits
                compareY = solutiongrid[coordY-1][coordX]["tile"][9]
                if not np.array_equal(compareY, t[0]):
                    fitX = False
            if fitX and fitY:
                solutiongrid[coordY][coordX]["tile"] = t
                nextX = (coordX + 1) % cubelen
                nextY = coordY + int((coordX+1)/cubelen)
                result = solve(nextX, nextY, cubelen, solutiongrid, without_keys(tiles, [tilename]))
                if result is not None:
                    return result

        # if "id" in solutiongrid[coordY][coordX]:
        #     solutiongrid[coordY][coordX].pop("id")
        # if "tile" in solutiongrid[coordY][coordX]:
        #     solutiongrid[coordY][coordX].pop("tile")
    # if we reach here, there is no solution:
    return None

import math
cubelen = int(math.sqrt(len(tiles)+1))
solutiongrid = [[dict() for y in range(cubelen)] for x in range(cubelen)]
solution = solve(0, 0, cubelen, solutiongrid, tiles)
if solution is None:
    print("No Solution found - stupid!")
    exit(1)

print("Got Solution!")
result = solutiongrid[0][0]["id"] * solutiongrid[cubelen-1][0]["id"] \
    * solutiongrid[0][cubelen-1]["id"] * solutiongrid[cubelen-1][cubelen-1]["id"]
print("Result is " + str(result))

# cut grid borders
for y in solutiongrid:
    for x in y:
        x["tile"] = x["tile"][1:9, 1:9]

# merge in one array
lines = []
for y in solutiongrid:
    line = None
    for x in y:
        if line is None:
            line = x["tile"]
        else:
            line = np.concatenate((line, x["tile"]), 1)
    lines.append(line)

picture = None
for line in lines:
    if picture is None:
        picture = line
    else:
        picture = np.concatenate((picture, line), 0)

pictures = genTileSet("picture", picture)

# Monster:
# 00000000000000000010
# 10000110000110000111
# 01001001001001001000

# 20*3 --> 15 Files are active
monster = np.array(\
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]]
    )


count = 0
wildSea = 0
for i in picture:
    for j in i:
        if j == 1:
            wildSea += 1
print("The wild sea is " + str(wildSea) + " and there are monsters in it")

monstercount = 0
for pic in pictures:
    count += 1
    for y in range(len(pic)-3):
        for x in range(len(pic)-20):
            if np.array_equal(np.multiply(monster, pic[y:y+3, x:x+20]), monster):
                monstercount += 1
                print("Found 1 in count " + str(count))

print("We have wild sea: " + str(wildSea - monstercount*15))

print("done")