import datetime
import random
import time

def main():

    f = open("ListAccessTiming.xml", "w")
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\n")
    f.write("<Plot title=\"Average List Element Access Time\">\n")

    # Test lists of size 1000 to 200_000
    x_min = 1000
    x_max = 200000

    x_list = []
    y_list = []

    for x in range(x_min, x_max + 1, 1000):
        print("status of x: %s of %s" % (str(x), str(x_max)))
        x_list.append(x)
        product = 0

        temp = [0] * x
        time.sleep(1)

        start_time = datetime.datetime.now()

        for v in range(1000):
            index = random.randint(0, x - 1)
            value = temp[index]
            product = product * value

        end_time = datetime.datetime.now()

        delta_time = end_time - start_time
        access_time = delta_time.total_seconds() * 1000
        y_list.append(access_time)

    f.write("  <Axes>\n")
    f.write("    <XAxis min=\"%s\" max=\"%s\">List Size</XAxis>\n" % \
        (str(x_min), str(x_max)))
    f.write("    <YAxis min=\"%s\" max=\"%s\">Microseconds</YAxis>\n" % \
        (str(min(y_list)), str(60)))
    f.write("  </Axes>\n")

    f.write("  <Sequence title=\"Average Access Time vs List Size\" color=\"red\">\n")
    for i in range(len(x_list)):
        f.write("    <DataPoint x=\"%s\" y=\"%s\"/>\n" % (str(x_list[i]), str(y_list[i])))
    f.write("  </Sequence>\n")

    x_list = temp
    y_list = [0] * 200000
    time.sleep(2)

    for i in range(100):
        start_time = datetime.datetime.now()
        index = random.randint(0, 200000 - 1)
        x_list[index] = x_list[index + 1]
        end_time = datetime.datetime.now()
        delta_time = end_time - start_time
        y_list[index] = y_list[index] + delta_time.total_seconds() * 1000000

    f.write("  <Sequence title=\"Access Time Distribution\" color=\"blue\">\n")

    for i in range(len(x_list)):
        if x_list[i] > 0:
            f.write("    <DataPoint x=\"\" y=\"\"/>\n" % (str(i), str(y_list[i] / x_list[i])))
    f.write("  </Sequence>\n")
    f.write("</Plot>\n")
    f.close()

    print("\nProgram execution completed")

if __name__ == "__main__":
    main()
