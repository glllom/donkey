x_center = int(input("Enter X center coordinate: ") or '60')
y_center = int(input("Enter Y center coordinate: ") or '240')
h_size = int(input("Enter size of handle: ") or '200')
h_direction = int(input("Enter direction of handle (1 - vertical, 2 - horizontal): ") or '1')
h_width, h_depth = 31, 13.8
width, height, thickness = 120, 480, 18.2
rc = 7  # radius of cutter


def finalize_code():
    """Test"""
    code.extend([f"G00 X{x_center}Y{y_center}",
                 f"G01 Z{thickness - 0.5}F2000",
                 f"G01 Z{thickness + 50}F5000",
                 f"G00 X{x_center + 150}Y{y_center + 150}",
                 f"M01 (Test of {'vertical' if h_direction == 1 else 'horizontal'} handle. Size - {h_size}mm)", ])

    match h_direction:
        case 1:
            code.extend([f"G00 X{x_center}Y{y_center + (h_size - h_width) / 2}", f"G01 Z{thickness - 0.5}F2000"])
            code.extend([f"Y{y_center + (h_size - h_width) / 2}Z{round(thickness - h_depth / 4, 1)}"])
            code.extend([f"Y{y_center - (h_size - h_width) / 2}Z{round(thickness - h_depth / 2, 1)}"])
            code.extend([f"Y{y_center + (h_size - h_width) / 2}Z{round(thickness - h_depth + 2, 1)}"])
            code.extend([f"Y{y_center - (h_size - h_width) / 2}"])
            code.extend([f"Y{y_center + (h_size - h_width) / 2}Z{round(thickness - h_depth + 1, 1)}"])
            code.extend([f"Y{y_center - (h_size - h_width) / 2}Z{round(thickness - h_depth, 1)}"])
            code.extend([f"Y{y_center + (h_size - h_width) / 2}"])

            code.append(f"G01 X{x_center + (h_width / 2 - rc - 2)}Y{y_center + (h_size / 2 - rc - 2)}")
            code.append(f"X{x_center + (h_width / 2 - rc - 2)}Y{y_center - (h_size / 2 - rc - 2)}")
            code.append(f"X{x_center - (h_width / 2 - rc - 2)}Y{y_center - (h_size / 2 - rc - 2)}")
            code.append(f"X{x_center - (h_width / 2 - rc - 2)}Y{y_center + (h_size / 2 - rc - 2)}")
            code.append(f"X{x_center + (h_width / 2 - rc)}Y{y_center + (h_size / 2 - rc)}")
            code.append(f"X{x_center + (h_width / 2 - rc)}Y{y_center - (h_size / 2 - rc)}")
            code.append(f"X{x_center - (h_width / 2 - rc)}Y{y_center - (h_size / 2 - rc)}")
            code.append(f"X{x_center - (h_width / 2 - rc)}Y{y_center + (h_size / 2 - rc)}")
            code.append(f"X{x_center + (h_width / 2 - rc)}Y{y_center + (h_size / 2 - rc)}")
            code.append(f"X{x_center}Y{y_center + (h_size - h_width) / 2}")
        case 2:
            code.extend([f"G00 X{x_center + (h_size - h_width) / 2}Y{y_center}", f"G01 Z{thickness - 0.5}F2000"])
            code.extend([f"X{x_center + (h_size - h_width) / 2}Z{round(thickness - h_depth / 4, 1)}"])
            code.extend([f"X{x_center - (h_size - h_width) / 2}Z{round(thickness - h_depth / 2, 1)}"])
            code.extend([f"X{x_center + (h_size - h_width) / 2}Z{round(thickness - h_depth + 2, 1)}"])
            code.extend([f"X{x_center - (h_size - h_width) / 2}"])
            code.extend([f"X{x_center + (h_size - h_width) / 2}Z{round(thickness - h_depth + 1, 1)}"])
            code.extend([f"X{x_center - (h_size - h_width) / 2}Z{round(thickness - h_depth, 1)}"])
            code.extend([f"X{x_center + (h_size - h_width) / 2}"])

            code.append(f"G01 X{x_center + (h_size / 2 - rc - 2)}Y{y_center + (h_width / 2 - rc - 2)}")
            code.append(f"X{x_center + (h_size / 2 - rc - 2)}Y{y_center - (h_width / 2 - rc - 2)}")
            code.append(f"X{x_center - (h_size / 2 - rc - 2)}Y{y_center - (h_width / 2 - rc - 2)}")
            code.append(f"X{x_center - (h_size / 2 - rc - 2)}Y{y_center + (h_width / 2 - rc - 2)}")
            code.append(f"X{x_center + (h_size / 2 - rc)}Y{y_center + (h_width / 2 - rc)}")
            code.append(f"X{x_center + (h_size / 2 - rc)}Y{y_center - (h_width / 2 - rc)}")
            code.append(f"X{x_center - (h_size / 2 - rc)}Y{y_center - (h_width / 2 - rc)}")
            code.append(f"X{x_center - (h_size / 2 - rc)}Y{y_center + (h_width / 2 - rc)}")
            code.append(f"X{x_center + (h_size / 2 - rc)}Y{y_center + (h_width / 2 - rc)}")
            code.append(f"X{x_center + (h_size - h_width) / 2}Y{y_center}")
    code.append(f"G00Z{thickness + 30}")

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
