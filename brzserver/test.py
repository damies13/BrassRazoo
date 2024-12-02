
import sys
import os
import uuid
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

base_path = os.path.abspath(os.path.join(dir_path, ".."))
print(base_path)
sys.path.insert(0, base_path)

import brzbase

bc = brzbase.Block.Block()

# serverid = str(uuid.uuid1())
serverid = brzbase.Yeast.encode(uuid.uuid1().int)
print("serverid:", serverid)

r1 = brzbase.Record.Record().new_record(serverid)
r1["Description"] = "Anna sends 2 NC to Mike"

r2 = brzbase.Record.Record().new_record(serverid)
r2["Description"] = "Bob sends 1 NC to Mike"

r3 = brzbase.Record.Record().new_record(serverid)
r3["Description"] = "Mike sends 3 NC to Dan"

# initial_block = brzbase.Block.Block().new_block("Genisis Block", {"t1":t1, "t2":t2, "t3":t3})
# initial_block = bc.new_block("00000000-0000-1000-0000-000000000000", {"r1":r1, "r2":r2, "r3":r3})
initial_block = bc.new_block("BrassRazoo00BrassRazoo", {r1['Record ID']:r1, r2['Record ID']:r2, r3['Record ID']:r3})

initial_block_data = bc.get_block(initial_block)

print("initial_block:", initial_block, initial_block_data)

rule0 = brzbase.Action.Rule().new_rule(serverid)

print("rule0:", rule0)

task0 = brzbase.Action.Task().new_task(serverid)

print("task0:", task0)
