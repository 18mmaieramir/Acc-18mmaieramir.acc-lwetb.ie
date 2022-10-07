import plotly.express as px
yr=[]
cp=[]
yr.append( int(input("Enter Starting Year")))
cp.append( int(input("Enter current population(thousands)")))
cd = int(input("Enter death rate(per 1000 population)"))
cb = int(input("Enter birth rate(per 1000 population)"))
cm = int(input("Enter migration rate(per 1000 Population)"))
pd = int(input("Enter projected death rate per year per 1000 population"))
pb = int(input("Enter projected change in birth rate per year per 1000 population"))
pm = int(input("Enter projected change in migration rate per year per 1000 population"))
yrm = int(input("Enter the amount of years for modelling"))

for i in range(yrm):
    cp[i] -= cp[i]*(cd/1000) + cp[i]*(cb/1000) + cp[i]*(cm/1000)
    cp.append(cp[i])
    print(cp[i])     
    
     
cd = cd + pd;
cb = cb + pb;
cm = cm + pm;
     
fig = px.line(yr, y = cp)
fig.show()
