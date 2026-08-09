# Database Schema

This document defines the relational database schema for the Brass Razoo system. 

**Data Integrity & Recovery:**
The database serves as the server's local copy of the ledger. While the local database must maintain integrity for the server's immediate operations, the global integrity of the system is guaranteed by the Sharding Protocol. 

If a local record is damaged or corrupted (verifiable by the cryptographic signature), the server can recover the correct record from other servers within the same shard. The Sharding process ensures that there are always multiple copies of every record across the network.

## Tables

### 1. Records
The core ledger of all system entities and actions.
| Column | Type | Description |
| :--- | :--- | :--- |
| `record_id` | BRZ_ID (PK) | Unique identifier |
| `block_id` | BRZ_ID  (FK) | The block identifier where this record was included |
| `type` | TEXT | 'Account', 'Server', 'Stake', 'Transfer', 'Contract', 'Object', 'Action' |
| `status` | TEXT | 'Pending', 'Queued', 'Rejected', 'Confirmed' |
| `record_data` | JSON | Type-specific metadata (e.g., recurring dates, serial numbers) |
| `is_valid` | BOOLEAN | Updated by Action Engine |
| `timestamp` | TIMESTAMP | Record creation time |

### 2. Blocks
The structural chain of records.
| Column | Type | Description |
| :--- | :--- | :--- |
| `block_id` | BRZ_ID (PK) | Unique identifier |
| `prev_block_id` | BRZ_ID | Reference to previous block |
| `prev_hash` | TEXT | Hash of the previous block |
| `server_id` | BRZ_ID | Server that generated the block |
| `server_owner` | BRZ_ID | Owner of the server who receives commission |
| `next_server_id`| BRZ_ID | The elected server for the next block |
| `block_hash` | TEXT | Hash of the block content |
| `timestamp` | TIMESTAMP | Block creation time |

