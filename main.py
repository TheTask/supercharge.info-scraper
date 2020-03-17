f = open("supercharge.txt", "r")
raw = f.read()

array = raw.split("</thead>\n<tbody>") #make sure there is only one of these with the data following
temp1 = array[ 1 ]
temp2 = temp1.split("</tbody>")
temp3 = temp2[ 0 ]
rows = temp3.split("<tr") # all rows information

rows_open = []

for r in rows:   #filter for OPEN
    if "OPEN" in r:
        rows_open.append(r)


#remove the day in date, keep month and year
d = {}

for r in rows_open:
    td = r.split("td")
    date = td[1]
    date_delim = date.split(" ")
    del date_delim[2]
    del date_delim[0]
    correct_date = date_delim[0] + " " + date_delim[1]
    correct_date = correct_date[:-2]

    kw = td[-2]
    kw_delim = kw.split(" ")
    if len(kw_delim) == 5:
        del kw_delim[1]
        del kw_delim[1]
        del kw_delim[-1]
        kw_delim[0] = kw_delim[0][1:]


        if not( int(kw_delim[1]) == 250 or int(kw_delim[1]) == 150 or int(kw_delim[1]) == 120 or int(kw_delim[1]) == 72 ):
            kw_delim[1] = 0
        # print(kw_delim)   ['8', '150']
        # print(correct_date)  Jan 2014

        # done parsing, now just count for each month
        if correct_date in d.keys():
            values = d[correct_date]

            if int(kw_delim[1]) in values.keys():
                values[int(kw_delim[1])] = int(kw_delim[0]) + int(values[int(kw_delim[1])])
                d[correct_date] = values
            else:
                values[int(kw_delim[1])] = int(kw_delim[0])
                d[correct_date] = values
        else:
            values = {}
            values[int(kw_delim[1])] = int(kw_delim[0])
            d[correct_date] = values

file = ""

# write into a file and format as csv
for (k,v) in d.items():
    file +=(k + ",")

    #for k1 in sorted(v.keys(),reverse=True):
    #    file+=( str(k1) + "," + str(v[k1]) + ",")

    #'''
    try:
        file += str(v[250] ) + ","
    except KeyError:
        file += ","             
                                
    try:
        file += str(v[150] ) + ","
    except KeyError:
        file += ","

    try:
        file += str(v[120] ) + ","
    except KeyError:
        file += ","

    try:
        file += str(v[72] ) + ","
    except KeyError:
        file += ","

    try:
        file += str(v[0]) + ","
    except KeyError:
        file += ","
        
    #'''
    file += "\n"

print(file)
f= open("mycsv.csv","w+")
f.write(file)
print("Done!")