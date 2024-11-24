
# Transactions

## Pending Transactions

When a Brass Razoo Client creates a transaction it will be sent to a Brass Razoo Server, this server will then append the transaction to the pending transactions queue.

The Brass Razoo Server will periodically run the transaction rules engine against the transactions in the pending transactions queue:
- transactions that pass the rule validation will be moved to the Queued Transactions queue for inclusion in the next block
- transactions that fail the rule validation will be moved to the Rejected Transactions queue for inclusion in the next block

Pending transactions are broadcast to all servers who's shard matches the transaction shard as a pending transaction.

## Queued Transactions

Queued transactions are broadcast to all servers who's shard matches the transaction shard as a queued transaction.

## Rejected Transactions

Rejected transactions are broadcast to all servers who's shard matches the transaction shard as a rejected transaction.

## Confirmed Transactions

Once a transaction is added to a block it becomes a confirmed transaction

Confirmed transactions are broadcast to all servers who's shard matches the transaction shard as a queued transaction.

## Requesting Transaction status / details

A client will request the transaction status and details from whichever server it is connected to

A server when receiving a transaction status or details request will determine which shard the transaction belongs to and ask it's nearest server belonging to that shard.

## New Blocks

In order to be eligible to create a new block a server must have someone stake some Brass Razoos with that server, the maximum value of all transactions a server can add to a block is limited but the total Brass Razoos staked with that server