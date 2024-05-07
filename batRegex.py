import re

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())


"""

To recap:

-Groups are created in regex strigns with parentheses
-The first set of parenthese is group 1, the second is group 2, etc...
-Calling group() or group (0) returns the full matching string, group(1) returns group 1's matching string, etc...
-Use \(and \) to match literal parentheses in the regex string
-The | pipe can match one of many possible groups


"""