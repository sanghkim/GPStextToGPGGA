import sys
from collections import defaultdict
if(len(sys.argv)>2):
    print("Error: Too many arguments")

columns = defaultdict(list) # each value in each column is appended to a list

# Read file.txt as f
#with open(sys.argv[1]) as f:
if (len(sys.argv)==2):
    outputname = "%s_gpgga.csv" % (sys.argv[1])
else:
    outputname = "noname_gpgga.csv"

with open(outputname,'w') as ofile:
    with open(sys.argv[1]) as f:
        # read file with delimiter blank[_]
        #reader = csv.reader(f,delimiter=" +")
        
        for ni in range(9): 
            next(f)

        reader = f.readline().strip()
        row = reader.split()  
        sizerow = len(row)
        for i,j in enumerate(row):
            if j == 'Latitude': latindx = i
            if j == 'Longitude': lonindx = i
            if j == 'Altitude': altindx = i
            if j == 'ms_gps': msindx = i
        
        while True:        
            reader = f.readline().strip()
            if reader == '':
                break
            row = reader.split()  
            sizerow = len(row)
            complat = float(row[latindx])
            complat = (int(complat)*100)+(complat-int(complat))*60
            complon = float(row[lonindx])
            complon = (int(complon)*100)+(complon-int(complon))*60
            compalt = float(row[altindx])
            compms = int(row[msindx])
            tempms = (compms)%1000
            tempms = int((tempms)/10)
            tempsec = int(compms/1000)%60
            tempmin = int(compms/(1000*60))%60
            temphr = int(compms/(1000*60*60))%24
            timefmt = "%02d%02d%02d.%02d" % (temphr, tempmin, tempsec, tempms)

            gpggafmt = "$GPGGA,%s,%.4f,N,%.4f,E,1,06,1.3,%.02f,M,0.00,M,,*62\n\n" % (timefmt, complat, complon,compalt)
            ofile.write(gpggafmt)
            
            #print(gpggafmt)
    f.close()
ofile.close()