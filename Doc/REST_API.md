# REST API Specification

This document defines the RESTful API endpoints for the Brass Razoo system. All communication must occur over HTTPS (Port 8151) for sensitive data.

## Base URL
`https://<server_ip>:8151/api/v1`

## Authentication
All requests must include a `X-Signature` header, which is a HMAC or RSA signature of the request body, signed by the user's private key.

## Endpoints

### 1. Blocks
**POST /blocks**
*   **Description:** Submit a new record for validation.
*   **Payload:** `{ "type": "...", "creator_id": "...", "description": "...", "details": {...}, "signature": "..." }`
*   **Response:** `202 Accepted` (Record queued) or `400 Bad Request` (Invalid schema).

**GET /blocks/{id}**
*   **Description:** Retrieve the current status and details of a record.
*   **Response:** `200 OK` `{ "record_id": "...", "status": "...", "is_valid": true, "details": {...} }`

### 2. Records
**POST /records**
*   **Description:** Submit a new record for validation.
*   **Payload:** `{ "type": "...", "creator_id": "...", "description": "...", "details": {...}, "signature": "..." }`
*   **Response:** `202 Accepted` (Record queued) or `400 Bad Request` (Invalid schema).

**GET /records/{id}**
*   **Description:** Retrieve the current status and details of a record.
*   **Response:** `200 OK` `{ "record_id": "...", "status": "...", "is_valid": true, "details": {...} }`

## Error Codes

| Code | Name | Description |
| :--- | :--- | :--- |
| `200` | OK | Request successful. |
| `201` | Created | Resource created successfully. |
| `202` | Accepted | Request accepted for processing (Asynchronous). |
| `400` | Bad Request | Malformed JSON or invalid record schema. |
| `401` | Unauthorized | Missing or invalid `X-Signature`. |
| `403` | Forbidden | Insufficient stake or permissions to perform action. |
| `404` | Not Found | Record ID, Server ID, or Shard ID does not exist. |
| `409` | Conflict | Record ID already exists or double-spend detected. |
| `500` | Internal Error | Server-side failure or Action Engine timeout. |
| `ERR_INVALID_SIG` | Invalid Signature | The provided cryptographic signature does not match the payload. |
| `ERR_INSUFFICIENT_STAKE` | Insufficient Stake | The user does not have enough staked BRZ to perform this action. |
| `ERR_RULE_VIOLATION` | Rule Violation | The Action Engine rejected the record based on current rules. |
