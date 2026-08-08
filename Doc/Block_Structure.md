# Block Structure

A block is structured as a Python dictionary, which is then serialized into a JSON string for easy decoding and processing.

All blocks must contain the following keys:

- Block ID
- Previous Block ID
- Previous Block Hash
- Server ID
- Server Owner
- Next Server ID
- Records

Once constructed, the block is converted to a JSON string and subsequently hashed. The resulting hash is stored under the "Block Hash" key. When verifying a preceding block, this key/value pair must be removed from the dictionary before hash verification.

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

A dictionary of Records, where the keys represent the record ID, and the value is a dictionary representing the record data.

## New Blocks

To be eligible to create a new block, a server must have users who have staked Brass Razoos with it. The maximum value of Records a server can include in a block is limited by the total amount of Brass Razoos staked with that server.