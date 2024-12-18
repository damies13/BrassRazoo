
# Block Structure

A block is a python dictionary that has been converted to a JSON string, this makes decoding and working with a block easy.

All blocks should have the following keys:

- Block ID
- Previous Block ID
- Previous Block Hash
- Server ID
- Server Owner
- Next Server ID
- Records

Once the block is constructed, it's converted to a JSON string and hashed, the key "Block Hash" with the value of the hash is added to the block and then stored. when verifying a previous block you should remove the "Block Hash" key/value from the dictionary to verify the hashed value.


## Block ID

Brass Razoo ID that uniquely identifies this block

## Previous Block ID

Brass Razoo ID that uniquely identifies the previous block

## Previous Block Hash

The hash that verifies the previous block

## Server ID

Brass Razoo ID that uniquely identifies the server generating the block

## Server Owner

ID of the account that will receive the server's commission for creating the block

## Next Server ID

Brass Razoo ID that uniquely identifies the server that is elected to generate the next block

## Records

A dictionary of Records, the keys of the dictionary is the record id, with the value being a dictionary representing the record data.

## New Blocks

In order to be eligible to create a new block a server must have someone stake some Brass Razoos with that server, the maximum value of all Records a server can add to a block is limited but the total Brass Razoos staked with that server
