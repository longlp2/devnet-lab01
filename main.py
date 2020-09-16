
hv1 = dict(ten='hv1' , tuoi=25, donvi='vtnet')
hv2 = dict(ten='hv2' , tuoi=26, donvi='vtnet')
hv3 = dict(ten='hv3' , tuoi=27, donvi='vtnet')
hv4 = dict(ten='hv4' , tuoi=28, donvi='vtnet')
hv5 = dict(ten='hv5' , tuoi=29, donvi='vtnet')
ds=[hv1,hv2,hv3,hv4,hv5]
print('------------')
for i in ds:
    print('ten :' + i['ten'])
    print('tuoi :' + str(i['tuoi']))
    print('donvi :' + i['donvi'])
    print('----------------')
