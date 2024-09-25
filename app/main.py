import matplotlib.pyplot as plt


def get_basic_hole_code(x, y):
    holes['x'].append(x)
    holes['y'].append(y)
    return f"G00 X{x} Y{y} F3000", "G1 Z7 F1000", "G00 Z30 F3000"


def shelves_code(width, height, num):
    offset_x = 45
    offset_y = -13
    step = 32
    max_height = 900
    for i in range(num):
        y = round(panel_thickness/2 + (num-i)*(height-panel_thickness)/(num+1) + offset_y, 1)
        for level in [1, 0, -1]:
            code.extend(get_basic_hole_code(offset_x, y+step*level))
    for i in range(num):
        y = round(panel_thickness/2 + (i + 1) * (height - panel_thickness) / (num+1) + offset_y, 1)
        for level in [-1, 0, 1]:
            code.extend(get_basic_hole_code(width-offset_x, y + step * level))


def finalize_code():
    code.extend(["M5", "G00 X550 Y850 Z130 F5000"])
    file_text = f"(X = {main_width}, Y = {main_height}, Z = {panel_thickness})\n"
    for row in range(len(code)):
        file_text += 'N' + str((row + 1) * 10) + ' ' + code[row] + '\n'
    return file_text + '%'


holes = {'x': [], 'y': []}

main_width, main_height = [int(num.strip()) for num in input("Enter the width and height of the piece: ").split(',')]
top_panel, bottom_panel = 1, 1  # 1 - inside, 2 - outside
panel_thickness = 17
code = ["G00G21G17G90G40G49G80", "G71G91.1", "T1M06", "G00G43Z100.000H1", "S2400M03", "G94"]

print("Type of Drilling:\n1)Shelves\n2)...")
choice = input()
if choice == "1":
    num = int(input("Enter a quantity of shelves: "))
    shelves_code(main_width, main_height, num)
with open("product/shelf.txt", "w") as file:
    file.write(finalize_code())
    file.close()


plt.axes().set_aspect('equal', adjustable='box')
plt.xlim([0, main_width])
plt.ylim([0, main_height])
plt.scatter(holes['x'], holes['y'])
plt.show()
