[中文说明]()

# TOOL DESCRIPTION #

This tool is used for processing raw CSV(*.gz) datasets, in order to make it usable as valid inputs when running ArcGIS GeoAnalytics tools. Functions including removing redundant fields, filtering rows, transforming time stamps and adding UUID. 

# HOW TO USE -- EXAMPLE: #
## 1. Organize raw data ##
Put all raw *.gz files under E:\OriginData:

![](http://i.imgur.com/4agHIs0.png)
![](http://i.imgur.com/7A8llmt.png)

## 2. Run the tool from cmd##
Put "DataCleaning.py" under E:\, and then run the tool from cmd:
E:\>python DataCleaning.py e:\OriginData e:\Result T

![](http://i.imgur.com/RCp5aTY.png)

## 3. Check results ##
Processed *.csv datasets will be output under E:\Result:

![](http://i.imgur.com/XlAx03Z.png)
![](http://i.imgur.com/5eHTcYf.png)

 
