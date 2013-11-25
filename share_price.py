import csv

def return_max():
	"""
	opening csv file having share prices data.
	"""
    f = open("share_prices.csv", "rb")
    csv_reader = csv.reader(f)
	"""
	taking header in comp_names
	"""
    comp_names = csv_reader.next()
    complete_data = {}
	"""
	company names start from third column so starting from 2(indexing)
	created a blank dictionary corresponding to each company name in complete_data dictionary
	"""
    for i in range(2, len(comp_names)):
        complete_data[comp_names[i]] = {}
    
	"""
	for rest of the rows, having price data, added each price value to a key
	key is concatenated form of year(r[0]) and month(r[1])""
	"""
    for r in csv_reader:
        values = r
        
        for i in range(2, len(values)):
            complete_data[comp_names[i]][r[0]+" "+r[1]] = values[i]
    
    max_values ={}
	"""
	iterating over the complete_data dictionary items and finding max 
	value using max function provided by python and passing key argument
	as every key of every company dictionary i.e. 
	complete_data['comapny A'] = {'1990 Jan':.., '1990 Feb':.., '1990 Mar':..}
	Iterating over '1990 Jan', '1990 Feb' and so on and taking its value and finding max of it.
	"""
    for key, values in complete_data.iteritems():
        max_value = max(values.iterkeys(), key= (lambda key: float(values[key])))
        max_values[key] = max_value
	
    return max_values

	"""
	to run this script stand alone
	"""
if __name__ == "__main__":
    print return_max()
