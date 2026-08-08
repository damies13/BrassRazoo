# Action Engine

The Action Engine is utilised for verifying and validating records and executing tasks that calculate the nominal value across various currencies.

## Robot Framework

The Action Engine employs [Robot Framework](https://robotframework.org/) to process rules and tasks. However, is limited to specific libraries, each rule or task must be a self-contained Robot Framework test or task, containing all necessary keywords not available from standard libraries.

# Rule Actions

A rule is used to validate records, blocks, and other data structures.

Rules are automatically triggered by the server upon receiving input, whether from another server or a client.

# Task Actions

A task is utilised for periodic server actions.

### Robot Framework Libraries

Rules and Tasks have access to the following libraries:

*   **Built-in Libraries:**
    *   Builtin
    *   Collections
    *   DateTime
    *   Dialogs
    *   Libdoc
    *   OperatingSystem
    *   Process
    *   Rebot
    *   Remote
    *   Screenshot
    *   String
    *   Telnet
    *   Testdoc
    *   Tidy
    *   XML
*   **Requests Library**