import os
file_text = "data_text.txt"

try:
    with open(file_text, "m", encoding = "utf8") as f:
        f.write("Nějaký text \n")
        f.write("Toto je druhý řádek")
    print(f"Soubor ´{file_text}´ byl zapsán a uzavřen.") 
except Exception as e:
    print(f"Sorry došlo k chybě zápisu: {e}")

if os.path.exists(file_text):