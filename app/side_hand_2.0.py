import os

width, height, thickness = 395, 854, 22.5
depth, rc, work_rc = 17.2, 38/2, 8.5
entering = 38 - rc  # regular 19
step = 4.75
top, bottom = 594, -8
code = ["G00G21G17G90G40G49G80", "G71G91.1", "T11M06", "G00G43Z100.000H11,", "S16000M03", "G94", "G55"]

code.append(f"G01 X0 Y{height-top-rc-2}")
code.append(f"G01 Z{thickness}")

d_step = depth/4
for i in range(4):
    code.append(f"G01 Y{bottom+rc+2} Z{round(thickness-(i+1)*d_step, 1)}")
    code.append(f"G01 Y{height-(top+rc+2)}")

for i in range(4):
    code.append(f"G01 X{step*(i+1)}")
    code.append(f"G01 Y{bottom+work_rc}")
    code.append(f"G01 X{step*i}")
    code.append(f"G01 Y{height-(top+work_rc)}")

code.append(f"G01 X0 Y{height-top-rc*2}")

def finalize_code():
    code.append(f"G00Z{thickness + 30}")

    code.extend(["M5", "G00 Z75", "G01 X300 Y940 F5000"])
    code.append("M30")

    file_text = f"(X = {width}, Y = {height}, Z = {thickness})\n"
    for row in range(len(code)):
        file_text += f'N{str((row + 1) * 10)} {code[row]}' + '\n'
    return f'{file_text}%'


file_name = f"side_hand_{width}x{height}_top-{top}_bottom-{bottom}.txt"
os.chdir('product')
with open(file_name, "w+") as file:
    file.write(finalize_code())
    file.close()
