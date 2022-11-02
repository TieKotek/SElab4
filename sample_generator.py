import re
import string
import random

def sample_generator(path, num):
    output_list = []
    with open(path, "r") as f:
        content = f.read()
        f.close()
        lines = content.split("\n")
        for _ in range(num):
            output = ""
            for line in lines:
                types = line.split()
                for type in types:
                    if (type.startswith("int")):
                        pattern = re.compile(r'[(](.*?)[)]', re.S)
                        info = re.findall(pattern, type)[0]
                        args = info.split(",")
                        output += str(random.randint(int(args[0]), int(args[1])))

                    elif (type.startswith("string")):
                        pattern = re.compile(r'[(](.*?)[)]', re.S)
                        info = re.findall(pattern, type)[0]
                        args = info.split(",")
                        length = random.randint(int(args[0]), int(args[1]))
                        for _ in range(length):
                            output += random.choice(string.ascii_letters)
                    else:
                        output += random.choice(string.ascii_letters)
                    output += " "
                output += "\n"
            output_list.append(output)
    return output_list