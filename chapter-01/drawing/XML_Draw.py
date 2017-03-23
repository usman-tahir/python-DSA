import xml.dom.minidom

file_name = input("Please enter a filename for the drawing: ")
# f = open(file_name, "r")

xml_document = xml.dom.minidom.parse(file_name)
graphics_commands = xml_document.getElementsByTagName("GraphicsCommands")[0]

for command_element in graphics_commands:
    print(type(command_element))
