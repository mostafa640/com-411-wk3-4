def cross_bridge(steps):
    for step in range(steps):
        print("crossed step")
    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("we must keep going")
cross_bridge(4)
cross_bridge(8)
