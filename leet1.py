
def functionality():

    #5.1
    blocks = 64
    num = 0
    for i in range(0, blocks):
        num = num + 2 ** i

    print("Total grains on chessboard => ", num)

    # 5.2 weight
    totalweight=num*25/100000
    print("totalweight in kg is=> ", totalweight)


    #5.3 totaldistance

    dist=num*(5/1000000)
    print("Total distance in kgs is =>", dist)


    #5.4
    s=5/1000000
    surface=30528
    areaofgrain=(s**2)

    numberofgrainsfitted=surface/areaofgrain

    layers=num/numberofgrainsfitted
    height=layers*(5/1000)
    print("Height of stack in meters(m) => ", height)

functionality()