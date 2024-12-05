
import sys
import os
import uuid
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

base_path = os.path.abspath(os.path.join(dir_path, ".."))
print(base_path)
sys.path.insert(0, base_path)

import brzbase

brz = brzbase.brzbase()
print("brz:", brz)
# bc = brz.Block
# print("bc:", bc)

# serverid = str(uuid.uuid1())
# serverid = brzbase.Yeast.encode(uuid.uuid1().int)
serverid = brz.Id.get_server_id()
print("serverid:", serverid)

shard = brz.Shard.get_current_shard()
print("shard:", shard)

# print("B:", brz.Yeast.decode("B"))
# print("b:", brz.Yeast.decode("b"))
# print("R:", brz.Yeast.decode("R"))
# print("r:", brz.Yeast.decode("r"))
# print("Z:", brz.Yeast.decode("Z"))
# print("z:", brz.Yeast.decode("z"))
#
# print("RZ:", brz.Yeast.decode("RZ"))
# print("rz:", brz.Yeast.decode("rz"))
#
# print("B+R+Z:", brz.Yeast.decode("B")+brz.Yeast.decode("R")+brz.Yeast.decode("Z"))
print("b+r+z:", brz.Yeast.decode("b")+brz.Yeast.decode("r")+brz.Yeast.decode("z"))

# Port 8151 = 8000 + b + r + z

# print("BRZ:", brz.Yeast.decode("BRZ"))
# print("brz:", brz.Yeast.decode("brz"))
# print("Brass:", brz.Yeast.decode("Brass"))
# print("Razoo:", brz.Yeast.decode("Razoo"))
# print("BrassRazoo:", brz.Yeast.decode("BrassRazoo"))



r1 = brz.Record.new_record(serverid)
r1["Description"] = "Anna sends 2 NC to Mike"

r2 = brz.Record.new_record(serverid)
r2["Description"] = "Bob sends 1 NC to Mike"

r3 = brz.Record.new_record(serverid)
r3["Description"] = "Mike sends 3 NC to Dan"

# initial_block = brzbase.Block.Block().new_block("Genisis Block", {"t1":t1, "t2":t2, "t3":t3})
# initial_block = bc.new_block("00000000-0000-1000-0000-000000000000", {"r1":r1, "r2":r2, "r3":r3})
# initial_block = bc.new_block("BrassRazoo00BrassRazoo", {r1['Record ID']:r1, r2['Record ID']:r2, r3['Record ID']:r3})
initial_block = brz.Block.new_block("BrassRazooGenisisBlock", {r1['Record ID']:r1, r2['Record ID']:r2, r3['Record ID']:r3})


initial_block_data = brz.Block.get_block(initial_block)

print("initial_block:", initial_block, initial_block_data)

rule0 = brz.Rule.new_rule(serverid)

print("rule0:", rule0)

task0 = brz.Task.new_task(serverid)

print("task0:", task0)
