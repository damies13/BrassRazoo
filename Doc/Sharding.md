
# Sharding

Sharding will be automatic and is dependant on the number servers that are currently able to create a new block.

A server only needs to retain:
- blocks matching it's shard
- Records that are not yet confirmed into a block up to 28 days
- blocks the server created

## Auto sharding process

The auto sharding process is initiated by the nominated server when it detects the auto sharding condition has been meet.

The condition for auto sharding is simple:
- there must be a minimum of two servers holding stakes for every shard

Consider the following reference information:
- Initially all servers are in the same shard, so initially shard length = 0
- Each character of a [Brass Razoo ID](BrassRazooIDs.md) represents 32 possible values
- shards are calculated based on the last n (shard length) digits of the server id
- if there are less than 64 servers with stakes in the current shard, auto sharding cannot happen as there are insufficient servers to provide 2 staked servers per shard for the new shard length
- The nominated server should add 1 to the current shard length to get the new shard length, then evaluate a count of the number of servers per shard for the new shard length, if every new shard has a minimum of 2 servers per new shard the auto sharding can be triggered
- It's expected that auto sharding will occur at some point between 64 and 128 staked servers in the current shard

### When auto sharding is triggered

- The shard length is incremented by 1
- after 28 days the server can remove stored blocks that are no longer in the current shard, this is to prevent deleting and re-collecting blocks if flip-flopping occurs between shard lengths, hopefully 28 days is sufficient to stabilise a shard length

If auto sharding has not previously been triggered for this shard length:
- The nominated server will create 32 blocks and assign each one to a server belonging to each shard
- if there are insufficient records to fill all 32 blocks, the server should try to spread the records evenly as possible across the blocks
- the server may create a new "auto sharding" record for each empty block, so the block can pay a 0.001 Brass Razoo commission

## Auto de-sharding process

Auto de-sharding occurs when there is no longer sufficient staked servers to ensure 2 servers per shard.

### When auto de-sharding is triggered

- The shard length is decremented by 1
- the server will immediately start collecting and storing blocks belonging to the current shard.


## The reasoning behind sharding

Having too few shards will mean records will queue up and take a long time to be processed, other block chains try to resolve this by using GAS but this becomes very expensive to get records processed

Having too many shards will mean blocks are created slowly with many empty blocks.

This auto sharding process is an attempt to balance this with the commission structure providing:
- incentives to server owners to have more stakes per server to increase the amount of income the server generates for the owner when it creates a block, less servers increases the likelihood this server will be chosen
- incentives to stake owners to have their stakes on many servers, to increase the likelihood a server with their stake is chosen to generate the next block and income for the stake owners
- incentives to stake owners to have their own servers so they can generate stake and server income
- incentives server and stake owners to have much as possible staked on 1 server so larger valued records can be added to the block (if the record value is too large then it can't be staked by this server as there are insufficient stakes to stake the record, it will be passed to the next server to collect the commissions on that record)

The combination of incentives should hopefully create a balance creating enough demand for new servers to maintain redundancy and to allow sharding to happen but not so many that sharding happens too quickly.
