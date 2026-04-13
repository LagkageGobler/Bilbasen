def lines_in_fil(filename):
    with open(filename) as file:
        lines = file.readlines()
        total_lines = len(lines)
        return total_lines
    
print(lines_in_fil("link_til_bil.txt"))