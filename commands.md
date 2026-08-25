# commands.md — PowerShell regulars

## Files

ni arrays\file_name.py

# New-Item: creates an empty file (PowerShell's `touch`).

# Always create files with ni or VS Code — NEVER `echo >` (births UTF-16, breaks Python/git).

code arrays\file_name.py

# Opens the file in VS Code. Born in terminal, filled in editor.

Set-Content README.md '# dsa-practice' -Encoding ascii

# Writes/overwrites a file with clean ASCII text. The safe way to make text files from the terminal.

# Verify after: Get-Content README.md

## Git

git mv "arrays\old_name.py" arrays\new_name.py

# Moves/renames a tracked file. Copy-paste makes diverging twins; git mv moves the one true file.

# Quotes required if the name has parentheses or spaces.

git status --short

# What's changed, one line per file. Read it BEFORE every commit.

git diff --staged

# Shows exactly what's about to ship. Press q to escape the pager. (q quits all pagers: git log too.)

git add . ; git commit -m "Present-tense message" ; git push

# The seal. Message says what the commit does, in one line.

## Running

python arrays\file_name.py

# Runs a file. Expect the test prints; silence means the **main** block is indented wrong.

python -m pytest

# Runs tests from the project root. The -m puts the current dir on the import path.

## Escape hatches

q # exits pagers ((END) means less is holding the door)
Ctrl+C # kills a running/stuck command
docker start expense-db # wakes the Postgres container after a reboot
