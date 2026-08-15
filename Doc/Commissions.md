# Commissions

The creation of secure blocks within the blockchain consumes resources. Furthermore, to ensure the gradual introduction of new coins and prevent hoarding, a precise commission structure is necessary, aligning with the overall use of Brass Razoos.

The Commission structure is designed to manage this economic balance.

## Calculating Block Commissions

There are two methods for calculating block commissions:

**Method A: Record Value Commission**
*   A 1% commission is applied to the value of each record.
*   The total value (100%) of all records included in the block cannot exceed the total amount of stakes held by the server.

**Method B: Record Count Commission**
*   A fixed commission of 0.001 BRZ is charged for each record with no associated monetary value.
*   The total value derived from Method B cannot exceed 1% of the total stakes held by the server.

### Reversal Records

For the purposes of calculating commisions, reversal records shall be treated as having no monetary value, so shall be included in the Method B calculation.

## Minimum Block Size

A server should not propose a new block before the time limit if:
- The block has less than 3 records (not including the commision records)
- the block is below the servers stake limit

The server should aim to get the highest commisions it can for the stake holders and server owner

As the server will need to add at least 3 records for commisions payment (one for each Stake Holder, one for the Server Owner and one for the Foundation) every block will have at least 3 records, ensureing a minimum payment for every block.

The records of commisions payment by the server shall be treated as having no monetary value, so shall be included in the Method B calculation.

## Time Limits

To prevent servers from delaying block creation in order to maximise commissions, a strict time limit will be applied. A server may wait up to five minutes from the creation time of the preceding block to fulfil the commission quota for both methods.

Once the quota is filled, the nominated server must propose a new block as soon as possible, but within the specified time limit.

In order to ensure the server is able to meet the time limit for proposing a block the following should be considered:
- The server should keep track of which queued records (and versions) it has already verified
- Once a server is nominated as the next block proposer it should immidatly validate any queued records that are candidates for adding to the block and not already validated
- when a server receives a record (regardless of if it's the nominated next block proposer or not) the server may want to validate the record upon reciving it to smooth out the validation load on the server.


## Paying Commissions

### Method A Payment Flow

Method A commissions are paid as follows:

*   **Value Recipient:** The value is paid by the record recipient to the stake holders, proportionally based on their respective stakes.
*   **Server Owner:** The value is created as new coins and paid to the server's nominated owner.
*   **Foundation:** The value is created as new coins and paid to the Brass Razoo Foundation.

### Method B Payment Flow

Method B commissions are paid as follows:

*   **Stake Holders:** The value is created as new coins and paid to the stake holders, proportionally based on their respective stakes.
*   **Server Owner:** The value is created as new coins and paid to the server's nominated owner.
*   **Foundation:** The value is created as new coins and paid to the Brass Razoo Foundation.

## Ensuring Chain Continuation (System Redundancy)

In the event that the nominated server fails to propose a new block—due to issues like power outages or loss of internet connection—a redundancy protocol must be activated.

If other servers within the same shard as the nominated server do not receive a proposed block within two times the time limit, they may propose a new block and broadcast it to all servers in that shard. This newly proposed block must nominate the next server as another server within the same shard or a neighbouring shard, if no other servers remain in the original shard.

Each server receiving a block proposal must review all candidates based on the following rules:

1.  A block proposed by the nominated server always takes first priority.
2.  The Server ID of the block proposer closest to the nominated server's ID is preferred.

If the current server is the nominated server on the best proposed block, the current server will confirm the block by proposing the next block in the chain.