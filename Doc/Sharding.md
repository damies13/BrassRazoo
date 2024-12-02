
# Sharding

Sharding will be automatic and is dependant on the number servers that are currently able to create a new block.

A server only needs to retain:
- blocks matching it's shard
- Records that are not yet confirmed into a block up to 30 days

### less than 32 (0x1F) servers

When there is 32 or less staking servers they are all considered to be in the same shard

### more than 32 (0x1F) but less than 512 (0x1FF) servers

Then there are between 16 and 256 staking servers, the shard is the last character of the UUID

### more than 512 (0x1FF) servers

As should be obvious from above as more staking servers become available the number of characters that identify a shard becomes proportionally larger, this way as the Brass Razoo becomes more popular, the demand per server and it's storage requirements shouldn't grow excessively.

To progress to the next larger shard there needs to be sufficient staking servers that each shard has at least 2 servers

- 512 (0x1FF) servers - last 2 characters of the UUID
- 8192 (0x1FFF) servers - last 3 characters of the UUID
- 131072 (0x1FFFF) servers - last 4 characters of the UUID
- and so on
