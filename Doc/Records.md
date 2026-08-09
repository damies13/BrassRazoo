# Records

A record is a Python dictionary that is converted into a JSON string when added to a block.

All records must contain the following keys:

*   Record ID
*   Type
*   Status
*   Creator
*   Description
*   Signature
*   IsValid

Records may also contain the following common keys, in addition to type-specific keys:

*   Recipient
*   Total
*   Recurring
*   Start Date
*   End Date
*   Details
*   Serial Number

## Record ID

The unique Brass Razoo ID identifying this record.

## Type

A string that identifies the record type, such as:

*   **Account:** A user or business account.
*   **Server:** Details about a server capable of generating blocks when it holds sufficient stakes.
*   **Stake:** Records the number of Brass Razoos staked by an individual with a server.
*   **Transfer:** Typically a one-off record, such as an item sale.
*   **Contract:** Typically a recurring record, used for wages, rent, services, or subscriptions.
*   **Object:** Used for registering physical items intended for sale.
*   **Action:**
    *   **Rule:** A validation rule applied to records and blocks.
    *   **Task:** A recurring job task performed by the server.

## Status

A string indicating the current status of the record, for example:

*   Pending
*   Completed
*   Rejected

## Creator

The ID of the account that created the record.

## Description

A free-text string intended to inform both the creator and the receiver of the record's purpose.

## Signature

The digital signature of the Creator. This signature should be verifiable using the user's public key.

The signature is applied initially by the creator and then by any modifier of the document. when a document is modified it's version must also be incremented so that original document can be verified.

The most basic example of this would be a in person sale record; the seller would create a sale document, with the details of what is being sold and the price, etc, then sign the document when it's complete. The buyer would then verify the sale document, incerment the version and add their details (buyer, agreement to the sale contract, agreement to make the payment, etc), then sign the second version of the document, completing the document and the sale.

If a server receives a record with no signature it should be rejected.

## IsValid

This key is initially set to `False` upon record receipt. After the rules action engine has run its validation rules, the status is updated to `True` if all rules pass successfully.

# Record Queues and Sharding

When a Brass Razoo Client creates a record, it is sent to a designated Brass Razoo Server, which appends the record to its pending queue.

The Brass Razoo Server periodically runs the Record rules engine against the pending queue. Records are then directed to specific queues:

*   **Queued Records:** Records that pass validation are moved here, awaiting inclusion in the next block.
*   **Rejected Records:** Records that fail validation are moved here.

These queues (Pending, Queued, Rejected) are broadcast to all servers whose shard matches the record's shard.

*   **Confirmed Records:** Once a record is successfully added to a block, it becomes a Confirmed Record and is broadcast to all matching shard servers.

# Requesting Record Status / Details

A client requests the record status and details from any connected server. The server, upon receiving this request, determines the record's designated shard and forwards the request to its nearest corresponding server within that shard.

# New Blocks

To be eligible to create a new block, a server must have users who have staked Brass Razoos with it. The maximum value of Records a server can include in a block is limited, by the total amount of Brass Razoos staked with that server must be considered.