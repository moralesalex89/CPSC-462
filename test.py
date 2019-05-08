import datetime
x = '03/22/19'
y = '03/25/19'
start_date = datetime.datetime.strptime(x,'%m/%d/%y')
end_date = datetime.datetime.strptime(y,'%m/%d/%y')

diff = end_date - start_date
print(diff.days * 100.43)