# Action Engine

The Action Engine is utilised for verifying and validating records and executing tasks that calculate the nominal value across various currencies.

## Robot Framework

The Action Engine employs [Robot Framework](https://robotframework.org/) to process rules and tasks. However, is limited to specific libraries, each rule or task must be a self-contained Robot Framework test or task, containing all necessary keywords not available from standard libraries.

# Rule Actions

A rule is used to validate records, blocks, and other data structures.

Rules are automatically triggered by the server upon receiving input, whether from another server or a client.

The rule engine will 
* Pre-validate that the block and records have the mandatory fields
* Run robot framework for each record
    * passing the record data as `{RECORD_DATA}`
	* passing the record's Type field as a avariable `{RECORD_TYPE}` and as a tag.

The Type field value should be used in the tags section of the robot test to identify if the rule applies to the record

The rule engine may employ pabot or other approaches to process the records in parallel

Every rule must have a timeout set in robot framework not exceeding 5 seconds, this can be done either on the test or suite level.

# Task Actions

A task is utilised for periodic server actions.

Every rule must have a timeout set in robot framework not exceeding 1 hour, this can be done either on the test or suite level.

# Robot Framework Libraries

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