
# Records

A record is a python dictionary that gets been converted to a JSON string when added to a block.

All records should have the following keys:

- Record ID
- Type
- Status
- Creator
- Description
- Signature
- IsValid

Records may also have the following common keys, as well as record type specific keys:

- Recipient
- Total
- Recurring
- Start Date
- End Date
- Details
- Serial Number

## Record ID

UUID that uniquely identifies this record

## Type

String identifying the type of record, e.g.
- account - a user / business account
- server - details about a server that may be used for generating blocks when a it has sufficient stakes
- stake - record of number of Brass Razoos a person has staked with a server
- transfer - normally a one off record, like a sale of an object
- contract - normally reoccurring records, like wages, rent, services, subscriptions
- object - normally registration of something physical to be sold
- action
	- rule - validation rule for validating record and blocks
	- task - reoccurring job task for server to perform

## Status

String identifying the status of a record, e.g.
- pending
- completed
- rejected

## Creator

ID of the account that created the record

## Description

Free text string that helps creator and receiver know what the record is for.

## Signature

Digital signature of the Creator, you should be able to use a users public key to verify the record

## IsValid

The IsValid key is initially set to false when a record is received, then after the rules action engine has run a applied the rules to the record, the status will be updated to true if all rules pass.

## Pending Records

When a Brass Razoo Client creates a record it will be sent to a Brass Razoo Server, this server will then append the record to the pending records queue.

The Brass Razoo Server will periodically run the Record rules engine against the Records in the pending Records queue:
- Records that pass the rule validation will be moved to the Queued Records queue for inclusion in the next block
- Records that fail the rule validation will be moved to the Rejected Records queue for inclusion in the next block

Pending Records are broadcast to all servers who's shard matches the Record shard as a pending Record.

## Queued Records

Queued Records are broadcast to all servers who's shard matches the Record shard as a queued Record.

## Rejected Records

Rejected Records are broadcast to all servers who's shard matches the Record shard as a rejected Record.

## Confirmed Records

Once a Record is added to a block it becomes a confirmed Record

Confirmed Records are broadcast to all servers who's shard matches the Record shard as a queued Record.

## Requesting Record status / details

A client will request the Record status and details from whichever server it is connected to

A server when receiving a Record status or details request will determine which shard the Record belongs to and ask it's nearest server belonging to that shard.

## New Blocks

In order to be eligible to create a new block a server must have someone stake some Brass Razoos with that server, the maximum value of all Records a server can add to a block is limited but the total Brass Razoos staked with that server
