
# Rules Engine

The rules engine will be used for verifying and validating transactions, as well as other regular tasks like calculating the nominal value in various currencies.

## Robot Framework

The rules engine will use [Robot Framework](https://robotframework.org/) to process the rules, however with limited libraries. each rule should be a self contained robot framework task / test and should contain all the keywords it needs that are not available from libraries

### Robot Framework Libraries

Rules will have access to the following libraries:
- Builtin libraries:
 - Builtin
 - Collections
 - DateTime
 - Dialogs
 - Libdoc
 - OperatingSystem
 - Process
 - Rebot
 - Remote
 - Screenshot
 - String
 - Telnet
 - Testdoc
 - Tidy
 - XML
- Requests Library
