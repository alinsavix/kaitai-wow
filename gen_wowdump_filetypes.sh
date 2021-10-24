#!/bin/bash
# Stupid little script to automatically generate filetypes/__init__.py for
# dispatching kaitai for different filetypes
cat <<EOF
import os

def load_wowfile(file):
    name, ext = os.path.splitext(file)
    ext = ext[1:].lower()

    if False:
        pass
EOF

for type in "$@"; do
    uctype=$(echo "$type" | awk '{print toupper(substr($0,0,1))tolower(substr($0,2))}')
    cat <<EOF
    if ext == "$type":
        from .$type import $uctype
        return $uctype.from_file(file)
EOF
done

cat <<EOF

    # else
    raise ValueError(f"unknown file type {ext}: {file}")
EOF

cat <<EOF


def get_supported():
    return {
EOF
for type in "$@"; do
    cat <<EOF
        "${type}",
EOF
done

cat <<EOF
    }
EOF
