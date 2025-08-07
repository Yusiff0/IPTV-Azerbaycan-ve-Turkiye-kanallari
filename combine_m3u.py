import os

AZ_FILE = "az.m3u"
TR_FILE = "tr.m3u"
OUTPUT_FILE = "az_tr.m3u"

def read_m3u(filename):
    if not os.path.exists(filename):
        return []
    with open(filename, encoding="utf-8") as f:
        return f.readlines()

az_lines = read_m3u(AZ_FILE)
tr_lines = read_m3u(TR_FILE)

header = "#EXTM3U\n"
combined = [header]

for lines in [az_lines, tr_lines]:
    for line in lines:
        if line.strip() and not line.strip().startswith("#EXTM3U"):
            combined.append(line)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.writelines(combined)
