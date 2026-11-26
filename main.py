import os

# keep the line within the 120-character limit
line = (
    "DO NOT UNPLUG THE BEEPING RACK: "
    "the ghost on call has been paging himself "
    "since 1998 and he always answers."
)
assert len(line) <= 120

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
