import turtle
from DrawingTool import *
from PyList import *

def main():
    file_name = input("Please enter a filename for the drawing: ")

    t = turtle.Turtle()
    screen = t.getscreen()
    f = open(file_name, "r")

    graphics_commands = PyList()
    command = f.readline().strip()

    while command != "":
        if command == "goto":
            x = float(f.readline())
            y = float(f.readline())
            width = float(f.readline())
            color = f.readline().strip()
            current_command = GoToCommand(x, y, width, color)
        elif command == "circle":
            radius = float(f.readline())
            width = float(f.readline())
            color = f.readline().strip()
            current_command = CircleCommand(radius, width, color)
        elif command == "beginfill":
            color = f.readline().strip()
            current_command = BeginFillCommand(color)
        elif command == "endfill":
            current_command = EndFillCommand()
        elif command == "penup":
            current_command = PenUpCommand()
        elif command == "pendown":
            current_command = PenDownCommand()
        else:
            raise RuntimeError("Unknown command: %s" % (command))

        graphics_commands.append(current_command)
        command = f.readline().strip()

    for g in graphics_commands:
        g.draw(t)

    f.close()
    t.ht()
    screen.exitonclick()
    print("Program execution completed")

if __name__ == "__main__":
     main()
