import json
from pprint import pprint

block_id_table = open("block_id_table.txt", "w")
points_table = open("points_table.txt", "w")
file_names = ["Clayton_Block_Population.json", "Cobb_Block_Population.json", "DeKalb_Block_Population.json", "Fulton_Block_Population.json"]

'''
these json files have nasty formatting :)
        
        data - dictionary obatined by calling json.load() on a json file
        data keys ----------------------------------------------------------------
        type - "FeatureCollection" 
        features - list of all features we care about

        
        data["features"] -list of blocks
        data["features"][i] - block i
        
        data["features"][i]["geometry"]["coordinates"] - 3d array containing coordinates as an array: [lat, lon]
        [
            [
                [lat_1, lon_1],
                [lat_2, lon_2],
                ...
                [lat_i, lon_i]
            ]
        ]
        data["features"][i]["geometry"]["coordinates"] is a 3d array of coordinates in block i
        

        block_properties = data["features"]["properties"] - dictionary of properties for each block
        block_properties keys -----------------------------------------------------------
        STATEFP10 - state fips
        COUNTYFP10 - county fips
        TRACTCE10 - tract fips
        BLOCKCE10 - block fips
        GEOID10 - state+county+tract+block fips (complete fips)
        NAME10 - census tabulation block name; concatenation of ‘Block’, and the current tabulation block number
        MTFCC10 - MAF/TIGER feature class code 
        UR10 - urban/rural indicator
        UACE10 - urban area code
        UATYP10 - urban area type
        FUNCSTAT10 - cnsus functional status
        ALAND10 - land area
        AWATER10 - water area
        INTPTLAT10 - interpolation latitude
        INTPTLON10 - interpolation longitude
        GEOid
        <county_name>n-bl - internal county block number

        for more info about this census (2010) visit: https://www2.census.gov/geo/pdfs/maps-data/data/tiger/tgrshp2010/TGRSHP10SF1CH5.pdf
'''

for file in file_names:
    with open(file, "r") as data_file:
        data = json.load(data_file, strict=False)
    
        block_array = data["features"]
       
        for block in block_array:
            block_properties = block["properties"]
            block_fips = block_properties["GEOID10"]
            
            coordinate_array = block["geometry"]["coordinates"]
            
            block_id_table.write(block_fips+",\n")
            for i in range(len(coordinate_array)):
                line_group = coordinate_array[i]
                for j in range(len(line_group)):
                    coordinate = line_group[j]
                    #format: block id (fips), group number, coordinate number, lat, lon
                    points_table.write(block_fips+","+str(i)+","+str(j)+","+str(coordinate[0])+","+str(coordinate[1])+"\n")
                    
 
