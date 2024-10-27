
x_center = int(input("Enter X center coordinate: ") or '60')
y_center = int(input("Enter Y center coordinate: ") or '500')
h_height = int(input("Enter size of handle: ") or '130')
h_width, h_depth = 31, 16
width, height, thickness = 580, 940, 22
rc = 7 # radius of cutter
def finalize_code():
    code.extend([f"G00X{x_center}Y{y_center+(h_height-h_width)/2}"])
    code.extend([f"G01Z{thickness-0.5}F3000"])
    code.extend([f"Y{y_center+(h_height-h_width)/2}Z{round(thickness-h_depth/3,1)}"])
    code.extend([f"Y{y_center-(h_height-h_width)/2}Z{round(thickness-h_depth*2/3,1)}"])
    code.extend([f"Y{y_center+(h_height-h_width)/2}Z{thickness-h_depth+2}"])
    code.extend([f"Y{y_center-(h_height-h_width)/2}Z{thickness-h_depth}"])
    code.extend([f"Y{y_center+(h_height-h_width)/2}"])
    code.append(f"G01X{x_center+(h_width/2-rc-2)}Y{y_center+(h_height/2-rc-2)}")
    code.append(f"X{x_center+(h_width/2-rc-2)}Y{y_center-(h_height/2-rc-2)}")
    code.append(f"X{x_center-(h_width/2-rc-2)}Y{y_center-(h_height/2-rc-2)}")
    code.append(f"X{x_center-(h_width/2-rc-2)}Y{y_center+(h_height/2-rc-2)}")
    code.append(f"X{x_center+(h_width/2-rc)}Y{y_center+(h_height/2-rc)}")
    code.append(f"X{x_center+(h_width/2-rc)}Y{y_center-(h_height/2-rc)}")
    code.append(f"X{x_center-(h_width/2-rc)}Y{y_center-(h_height/2-rc)}")
    code.append(f"X{x_center-(h_width/2-rc)}Y{y_center+(h_height/2-rc)}")
    code.append(f"X{x_center+(h_width/2-rc)}Y{y_center+(h_height/2-rc)}")
    code.append(f"X{x_center}Y{y_center+(h_height-h_width)/2}")
    code.append(f"G00Z{thickness+30}")

    code.extend(["M5", "G00 Z75", "G01 X300 Y940 F5000"])
    code.append("M30")

    file_text = f"(X = {width}, Y = {height}, Z = {thickness})\n"
    for row in range(len(code)):
        file_text += f'N{str((row + 1) * 10)} {code[row]}' + '\n'
    return f'{file_text}%'



code = ["G00G21G17G90G40G49G80", "G71G91.1", "T10M06", "G00G43Z100.000H10,", "S16000M03", "G94"]
with open("product/integrated_hand.txt", "w") as file:
    file.write(finalize_code())
    file.close()


