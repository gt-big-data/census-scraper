from census import Census
from us import states

cen = Census("0e9003e5efaa23ac9b9812907f245f903a0d4cb2", year=2010)

fulton = (cen.sf1.get("H011001", geo={'for': 'block:*', 'in': 'state:{} county:121'.format(states.GA.fips)}))
dekalb = (cen.sf1.get("H011001", geo={'for': 'block:*', 'in': 'state:{} county:089'.format(states.GA.fips)}))
cobb = (cen.sf1.get("H011001", geo={'for': 'block:*', 'in': 'state:{} county:067'.format(states.GA.fips)}))
clayton = (cen.sf1.get("H011001", geo={'for': 'block:*', 'in': 'state:{} county:063'.format(states.GA.fips)}))

fulton_tracts = []
dekalb_tracts = []
cobb_tracts = []
clayton_tracts = []


for elem in fulton:
    fulton_tracts.append(elem['tract'])
    
for elem in dekalb:
    dekalb_tracts.append(elem['tract'])
    
for elem in cobb:
    cobb_tracts.append(elem['tract'])
    
for elem in clayton:
    clayton_tracts.append(elem['tract'])

print("dekalb:",dekalb_tracts)
print(len(dekalb_tracts))
##print("fulton:",fulton_tracts)
##print("cobb:",cobb_tracts)
##print("clayton:",clayton_tracts)
