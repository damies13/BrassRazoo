
# Brass Razoo Server

The Brass Razoo Server, written purely in python so that it can be run on any OS and any hardware, it should run just as well on a Raspberry Pi as it does on a Xeon server in a data centre.

## First Run

On first run the server will generate it's configuration file, in this file will be the server's ID (a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)), from this point forward this UUID will be used to identify this server.

## OS Upgrade / Moving to new hardware

If you want to move a server, you only need to save and migrate the configuration file and the server will retain the identity of the old server. you will need to ensure the old server is shutdown before starting the new server and ensure the old server cannot be brought back up with it's same UUID.

> [!WARNING]
> Need to determine an method for detecting duplicate servers and determining which is the "original" server with that UUID

## Staking Server

A Staking Server is a server who has had a Brass Razoo stake allocated to it.

## Brass Razoo Stake

Brass Razoo Stakes are a block of 888 Brass Razoos, when a stake has been allocated to a server it can not be spent until it has been de-staked, however the ownership of the Brass Razoos remains with the person staking them

## Sharding

Sharding will automatic and be dependant on the number servers that are currently able to create a new block.

A server only needs to retain:
- blocks matching it's shard
- transactions that are not yet confirmed into a block up to 30 days

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
