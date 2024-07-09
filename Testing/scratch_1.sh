#!/bin/bash

directory_path="/home/twarit/PycharmProjects/Testing"
old_word="login"
new_word="login"

for file_path in $directory_path/*; do
    if [ -f "$file_path" ]; then
        sed -i "s/$old_word/$new_word/g" "$file_path"
    fi
done
