# Database Schema

This document defines the relational database schema for the Brass Razoo system. The schema is designed to support high-integrity transactions using an ACID-compliant database (e.g., SQLite).

## Tables

### 1. Records
The core ledger of actions.
| Column | Type | Description |
| :--- | :--- | :--- |
| `record_id` | BRZ_ID (PK) | Unique identifier |
| `block_id` | BRZ_ID | Block identifier |
| `type` | TEXT | 'Account', 'Server', 'Stake', 'Transfer', 'Contract', 'Object', 'Action' |
| `status` | TEXT | 'Pending', 'Queued', 'Rejected', 'Confirmed' |
| `record_data` | JSON | Type-specific metadata (e.g., recurring dates, serial numbers) |
| `is_valid` | BOOLEAN | Updated by Action Engine |
| `timestamp` | TIMESTAMP | Record creation time |

### 2. Blocks
The chain structure.
| Column | Type | Description |
| :--- | :--- | :--- |
| `block_id` | BRZ_ID (PK) | Unique identifier |
| `prev_block_id` | BRZ_ID | Reference to previous block |
| `prev_hash` | TEXT | Hash of the previous block |
| `server_id` | BRZ_ID (FK) | Server that generated the block |
| `server_owner` | BRZ_ID | Owner of the server who receives commission |
| `next_server_id`| BRZ_ID | The elected server for the next block |
| `block_hash` | TEXT | Hash of the block content |
| `timestamp` | TIMESTAMP | Block creation time |

