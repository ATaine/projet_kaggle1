# projet kaggle numéro 1

import netCDF4
import numpy as np

f_18 = netCDF4.Dataset(
    "C:/Users/alexis/projet_reconversion_pro/projet_kaggle/bd_projet_kaggle_1/tavg1_2d_ocn_Nx-202109201458output.17833.webform.nc4"
)

f_21 = netCDF4.Dataset(
    "C:/Users/alexis/projet_reconversion_pro/projet_kaggle/bd_projet_kaggle_1/tavg1_2d_ocn_Nx-202109201500output.18042.webform.nc4"
)

# print(file_2018)

# get all variable names
print(f_18.variables.keys())
print(f_21.variables.keys())

pres = f_18.variables["tbar"]  # temperature variable
print(pres)

for d in f_18.dimensions.items():
    print(d)

print(f"Les dimension de pres sont : {pres.dimensions}")
print(f"La shape de pres est : {pres.shape}")

lat, lon = f_18.variables["latitude"], f_18.variables["longitude"]
print(lat)
print(lon)
print(lat[:])

# extract lat/lon values (in degrees) to numpy arrays
latvals = lat[:]
lonvals = lon[:]

# a function to find the index of the point closest pt
# (in squared distance) to give lat/lon value.
def getclosest_ij(lats, lons, latpt, lonpt):
    # find squared distance of every point on grid
    dist_sq = (lats - latpt) ** 2 + (lons - lonpt) ** 2
    # 1D index of minimum dist_sq element
    minindex_flattened = dist_sq.argmin()
    # Get 2D index for latvals and lonvals arrays from 1D index
    return np.unravel_index(minindex_flattened, lats.shape)


iy_min, ix_min = getclosest_ij(latvals, lonvals, 50.0, -140)
print(iy_min)
print(ix_min)

tdrop = f_18.variables["tdrop"]
# Read values out of the netCDF file for temperature and salinity
print("%7.4f %s" % (pres[0, 0, iy_min, ix_min], pres.units))
print("%7.4f %s" % (tdrop[0, 0, iy_min, ix_min], tdrop.units))

# Attention !
# exemple où chaque latitude, longitude a un x et y, hors nous avons directement une colonne latidude et une colonne longitude dans nos fichiers
