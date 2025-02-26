# cli-attend
Command line attendance marking

An extremely simple python script written to take attendance at a club AGM.

## Usage
`./cli-attend.py memberlist attendancelist`

All the script does is load the memberlist and then prompt you for a search term.  It then
scans all lines in the memberlist for the search term printing out any that match with an
index in brackets and then prompts you to enter the index.  If you enter the index it will append
that line to the attendancelist file.

It doesn't have to be members, it literaly can be anything that is line based.  In our case 
I'm using a csv file.

This readme is already larger than the script itself.


