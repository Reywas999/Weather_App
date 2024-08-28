# Weather_App
Requisites: 
1) Open Weather API key (FREE)
2) tkinter (library)
3) PIL (library)
4) requests (library)
5) geopy (library)
\
\
Simple weather app to find weather conditions for an input city or your current location.\
Data retrieved from: https://home.openweathermap.org \
(I've just realized I've been retrieving 3-hour forecasts rather than daily by accident -- easy fix)
\
\
After retrieving an API key, simply insert it into the script at the top of the document in place of 'YOURAPIKEY'.\
\
\
The script forms a simple UI that asks the user to either input a town to recieve the town's current weather or the five-day forecast,
or allows the user to find the weather for their current geolocation. The script builds URL requests from the API key and input town(s),
then displays the data found on the open weather website.\
\
![Screenshot 2024-08-28 083044](https://github.com/user-attachments/assets/247d3593-bba5-4feb-b0cf-24fff046b914)

