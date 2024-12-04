
# Commissions

Creating secure blocks in a block chain costs resources, also there is a need to create new coins slowly but in line with the amount Brass Razoo is used, so we don't end up with a situation where people hoard Brass Razoos and there are no Brass Razoos available for new users.

The Commissions structure here is designed for this.

## Calculating the block commissions

There are 2 methods for calculating the block commissions:
- Method A: 1% of record value for each record with a value
	- Total value (100%) of record value for each record with a value, can not exceed total of all stakes with the server
- Method B: 0.001 BRZ for each record with no value
	- Total of Method B can not exceed 1% of all stakes with the server

## Time limits

As there is an incentive for the server to wait until it can maximise commissions, A time limit will be applied, a server may wait up to 5 minutes from the creation time of the previous block to fill the quota's for each commission methods.

As soon as the quota is filled the nominated server should propose a new block asap, but take no longer than the time limit above.

## Paying commissions

### Method A

Method A commissions are payed as follows:
- Value of Method A is paid by the value recipient to the stake holders, proportionally based on their stakes
- Value of Method A is created as new coins and paid to the server's nominated owner
- Value of Method A is created as new coins and paid to the Brass Razoo Foundation

### Method B

Method B commissions are payed as follows:
- Value of Method B is created as new coins and paid to the stake holders, proportionally based on their stakes
- Value of Method B is created as new coins and paid to the server's nominated owner
- Value of Method B is created as new coins and paid to the Brass Razoo Foundation


## Ensuring chain continuation (system redundancy)

Sometimes the nominated server might not be able to propose a new block, for reasons such as unexpected power outages, loss of internet , etc. To ensure new blocks are created in a timely fashion a redundancy protocol is needed. This section describes the redundancy protocol.

If no proposed block received from the nominated server by other servers in the same shard as the nominated server within 2x the time limit, the other servers from the same shard as the nominated server may propose a new block and broadcast to all servers in the same shard as the nominated server. This now block must also nominate the next server as another server in the same shard as the nominated server or a neighbouring shard if it's the only remaining server in the same shard.

Each server that receives a nomination on a proposed block should review all proposed blocks to determine the best proposed block following these rules:
1. proposed block from nominated server always gets first priority
2. server id of block proposer that is closest to the nominated server's id

If the current server is the nominated server on the best proposed block, then the current server will confirm the best block by proposing a new block as the next in the chain following the best block.
