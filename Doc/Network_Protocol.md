# Network Protocol

The network protocol for the Brass Razoo system is designed to be a lightweight, robust, and easily implementable RESTful API, utilising JSON over HTTP.

We maintain distinct ports for both unencrypted (HTTP) and encrypted (HTTPS) communication to ensure data integrity and security.

**API Endpoints:**
*   **HTTP Port:** 8073 (Calculated as 8000 + B + R + Z) - Used only for non-sensitive communications. (may be deprecated in the future)
*   **HTTPS Port:** 8151 (Calculated as 8000 + b + r + z) - Used for all sensitive data transfer and authentication.

## TCPIP

Brass Razoo should preference IPv6 and only use IPv4 as a fall back communication method.

