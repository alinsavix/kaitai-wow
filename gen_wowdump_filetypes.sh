#!/bin/bash
# Stupid little script to automatically generate filetypes/__init__.py for
# dispatching kaitai for different filetypes
#
# FIXME: can we do better?
cat <<EOF
import os
from pathlib import Path
from typing import Set, Union

from kaitaistruct import KaitaiStruct


def load_wowfile(file: Union[str, Path]) -> KaitaiStruct:
    file = Path(file)
    ext = file.suffix.lower()

    if False:
        pass
EOF

for type in "$@"; do
    uctype=$(echo "$type" | awk '{print toupper(substr($0,0,1))tolower(substr($0,2))}')
    cat <<EOF
    if ext == ".$type":
        from .$type import $uctype
        return $uctype.from_file(file)
EOF
done

cat <<EOF

    # else
    raise ValueError(f"unknown file type {ext}: {file}")
EOF

cat <<EOF


def get_supported() -> Set[str]:
    return {
EOF
for type in "$@"; do
    cat <<EOF
        ".${type}",
EOF
done

cat <<EOF
    }
EOF
