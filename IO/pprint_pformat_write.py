import pprint

cats = [{'name':'Song', 'color':'gray'}, {'name':'Baby', 'color':'stripe'}]
print(pprint.pformat(cats))
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()