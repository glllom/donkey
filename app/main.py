import matplotlib.pyplot as plt

def get_basic_hole_code(x, y):
    holes['x'].append(x)
    holes['y'].append(y)
    return f"G01 X{x} Y{y} F5000", "G1 Z7 F2000", "G01 Z20 F5000"
    # return [f"G73 X{x} Y{y} Z-7 Q7"]


def shelves_code(width, height, quantity):
    offset_x = 45
    offset_y = -13
    step = 32
    max_height = 940
    for i in range(quantity):
        y = round(panel_thickness / 2 + (quantity - i) * (height - panel_thickness) / (quantity + 1) + offset_y, 1)
        for level in [1, 0, -1]:
            code.extend(get_basic_hole_code(offset_x, y+step*level))
    for i in range(quantity):
        y = round(panel_thickness / 2 + (i + 1) * (height - panel_thickness) / (quantity + 1) + offset_y, 1)
        for level in [-1, 0, 1]:
            code.extend(get_basic_hole_code(width-offset_x, y + step * level))


def finalize_code():
    code.extend(["M5", "G0 Z75", "G01 X300 Y940 F5000"])
    code.extend(["M30"])
    file_text = f"(X = {main_width}, Y = {main_height}, Z = {panel_thickness})\n"
    for row in range(len(code)):
        file_text += f'N{str((row + 1) * 10)} {code[row]}' + '\n'
    return f'{file_text}%'


holes = {'x': [], 'y': []}

main_width = int(input("Enter the width of the piece(default: 580): ") or '580')
main_height = int(input("Enter the height of the piece(default: 750): ") or '750')
top_panel, bottom_panel = 1, 1  # 1 - inside, 2 - outside
panel_thickness = 17
code = ["G00G21G17G90G40G49G80", "G71G91.1", "T2M06", "G00G43Z100.000H2,", "S2400M03", "G94"]

print("Type of Drilling(default: 1):\n1)Shelves\n2)...")
choice = input() or '1'
if choice == "1":
    num = int(input("Enter a quantity of shelves(default: 1): ")  or '1')
    shelves_code(main_width, main_height, num)
with open("product/shelf.txt", "w") as file:
    file.write(finalize_code())
    file.close()


plt.axes().set_aspect('equal', adjustable='box')
plt.xlim([0, main_width])
plt.ylim([0, main_height])
plt.scatter(holes['x'], holes['y'])
plt.show()
