fixipy
=====

fixipy is a toolchain to help you working with Financial Information eXchange messages

Currently fixipy defines two classes, **Message** and **Flow**.

While **Message** implements all functionality for creating, reading, changing FIX message and also search inside a message, **Flow** creates a set of **Message**s, e.g. by reading from a file, and allows to search inside a batch of messages.

Message
-------

Inside this class a FIX message exists as a list of *items*. An *item* is defined as a list like  
`[int(tag), str(value)]`

An example message could look like this  
`[[8, 'FIX.4.1'], [9, '154'], [35, 'D'], ... ]`  
but this is only the way that the message exists inside of **Message** class.

When a method that returns the message or parts of it is called, the *item* is extended by appending the index of it. If you call a function that returns the full (non-raw) message, the message would look like below.

`[[8, 'FIX.4.1', 0], [9, '154', 1], [35, 'D', 2], ... ]`

This makes it possible to identify the position of each item inside the message, which can be helpful to handle repeating groups for example.

The same will be done if single items or a couple of items are returned. Generally, the class will always return a list of lists, even if only one is returned, like in below example.

`[[35, 'D', 2]]`

### Insert items to a message

There are four ways to insert an item do a message.

1.  Single item to end of message  
    `[35, 'D']`

2.  Single item to specific position (index)  
    `[35, 'D', 2]`

3.  A list of items to end of message  
    `[[35, 'D'], [49, 'BRKR']]`

4.  A list of items to specific positions (indices)  
    `[[35, 'D', 2], [49, 'BRKR', 3]]`  
    This method should only be used to clone an existing message.

Mixing methods 3 and 4 is not recommended.

### Checksum

The checksum will be calculated on

-   Reading a (raw) message

-   Changing a message

Reading a (raw) message will cause a comparison of the read checksum with the calculated ones, but the read one will be kept. The variable *valid_checksum* of **Message** will be set to True when both checksums match, otherwise False.

The automatic re-calculation of checksum can be disabled by setting *checksum_calculation* to *False*. To enable set it to True. *checksum_calculation* will only affect changing a message, not the calculation done on reading a (raw) message.
