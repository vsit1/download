# Fixers
import string
import datetime as dt
# Fixer 1
baddata=" Data Science is a Fun "
print('>', baddata,'<')
cleandata=baddata.strip()
print('>', cleandata,'<')
print('Removed leading or lagging from a data entry')
# Fixer 2
printable=set(string.printable)
baddata="VSIT\x00 is a \x02good college !!!"
cleandata=''.join(filter(lambda x:x in string.printable,baddata))
print('Bad data : ',baddata)
print('Clean data : ',cleandata)
print('Removed non printable characters from a data entry')
# Fixer 3
baddate = dt.date(2022, 12, 3)
baddata=format(baddate,'%Y-%m-%d')
gooddate = dt.datetime.strptime(baddata,'%Y-%m-%d')
gooddata=format(gooddate,'%d %B %Y')
print('Bad Data : ',baddata)
print('Good Data : ',gooddata)
print('Reformatting data entry to match specific formatting criteria.')