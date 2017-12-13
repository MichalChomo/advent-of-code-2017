def find_severity(layers):
    severity = 0
    for i in range(len(layers)):
        if (layers[i][0] % ((layers[i][1] - 1) * 2)) == 0:
            severity += layers[i][0] * layers[i][1]
    print(severity)

def find_delay(layers):
    delay = 0
    while True:
        caught = False
        for i in range(len(layers)):
            if ((layers[i][0] + delay) % ((layers[i][1] - 1) * 2)) == 0:
                caught = True
        if caught == False:
            print(delay)
            break
        delay += 1

layers = []
with open("day13_input") as infile:
    for line in infile:
        line = line.strip().split(':')
        layers.append([int(line[0]), int(line[1]), 0, 0])
find_severity(layers)
find_delay(layers)
