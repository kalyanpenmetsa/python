import csv, sqlite3

con = sqlite3.connect('mydb')
cur = con.cursor()

with open('FL_insurance_sample1.csv') as f:
	reader = csv.DictReader(f)
#	data = [r for r in reader]
	for i in reader:
		cur.execute("INSERT INTO insurance (policyID, statecode, county, eq_site_limit, hu_site_limit, fl_site_limit, fr_site_limit, tiv_2011, tiv_2012, eq_site_deductible, hu_site_deductible, fl_site_deductible, fr_site_deductible, point_latitude, point_longitude, line, construction, point_granularity) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", (i['policyID'], i['statecode'], i['county'], i['eq_site_limit'], i['hu_site_limit'], i['fl_site_limit'], i['fr_site_limit'], i['tiv_2011'], i['tiv_2012'], i['eq_site_deductible'], i['hu_site_deductible'], i['fl_site_deductible'], i['fr_site_deductible'], i['point_latitude'], i['point_longitude'], i['line'], i['construction'], i['point_granularity']))

print("CSV successfully exported into the Database")
con.commit()
con.close()

#CREATE TABLE insurance (
#policyID	int,
#statecode varchar(255),
#county varchar(255),
#eq_site_limit decimal(20,2),
#hu_site_limit decimal(20,2),
#fl_site_limit decimal(20,2),
#fr_site_limit decimal(20,2),
#tiv_2011 decimal(20,2),
#tiv_2012 decimal(20,2),
#eq_site_deductible int,
#hu_site_deductible int,
#fl_site_deductible int,
#fr_site_deductible int,
#point_latitude decimal(15,6),
#point_longitude	decimal(15,6),
#line varchar(255),
#construction varchar(255),
#point_granularity int
#);
