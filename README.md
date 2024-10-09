# IN PROGRESS

# Domain Classifications
This utility aims to take data from a structured CSV file of domains based on whether or not the domain is reachable. Maybe more in the future as well but for now that is all it aims to do. 

## Data Structure
the csv file provided should be in the following format:

`Classification, DomainName`

The output should be something as follows:
```
Non Resolving Domain Classes:
Classification : Number of Occurences
Class1	:	Count
Class2	:	Count

```
This is to help shield the anonimity of those who generate the data but provide insight into whether or not domains are not being resolved in a particular class of data.

## Future Improvements
Include a way for a granular report with exact names of the domains that are being blocked

# File Explinations
Explaining what each of the files is doing
## resolverFunctions.py
This file requires a bit of data cleaning in order to get it to a point where it can be usefull. It is based on domain data collection where domains are weighted or scored upon how good or bad they are or maybe just a particular class of data such as malicious, non malicious, work related, job seeking etc... it accepts a file 