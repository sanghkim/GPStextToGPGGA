# GPStextToGPGGA
Python script for GPS data text file to GPGGA file

Recently, I have purchased Inertial lab INS-D with GNSS. 
It output two types of GPS data like INS based GPS data and GNSS based GPS data (like latitude, longitute, altitude)
But, I need extract INS's position data from its report text page. 
So, I made this code with Python 3.

Executing command)
$>python convinsdata.py [TEXT_file_name]

[Text_file_name] consists of spaces/blanks seperated text table file with header. 
So, I skipped 9 lines to get exact data index like 'Latitude', 'Longitude', 'Altitude' and 'ms_GPS'. 
Then I read a line and make array for data index. 
With these data, I convert latitude data to xxDyyMzzzzS from xx.yyyyyy for GPGGA format. 

ms_GPS value would be converted to HHMMSS.ms 

Hope you to make use of my code for your job. 

- Sanghyun Kim, Seoul, South Korea

