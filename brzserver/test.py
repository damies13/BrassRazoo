
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

base_path = os.path.abspath(os.path.join(dir_path, ".."))
print(base_path)
sys.path.insert(0, base_path)

import brzbase

bc = brzbase.Block.Block()

t1 = "Anna sends 2 NC to Mike"
t2 = "Bob sends 1 NC to Mike"
t3 = "Mike sends 3 NC to Dan"

# initial_block = brzbase.Block.Block().new_block("Genisis Block", {"t1":t1, "t2":t2, "t3":t3})
initial_block = bc.new_block("Genisis Block", {"t1":t1, "t2":t2, "t3":t3})

print(initial_block)
