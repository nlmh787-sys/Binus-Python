import math

# Input dari user
longitude_a = float(input("Masukkan Longitude Titik A: "))
latitude_a = float(input("Masukkan Latitude Titik A: "))

longitude_b = float(input("Masukkan Longitude Titik B: "))
latitude_b = float(input("Masukkan Latitude Titik B: "))

# Konversi derajat ke radian
lon_a = math.radians(longitude_a)
lat_a = math.radians(latitude_a)

lon_b = math.radians(longitude_b)
lat_b = math.radians(latitude_b)

# Selisih koordinat
delta_lon = lon_b - lon_a
delta_lat = lat_b - lat_a

# Rumus Haversine
a = (math.sin(delta_lat / 2) ** 2) + \
    math.cos(lat_a) * math.cos(lat_b) * \
    (math.sin(delta_lon / 2) ** 2)

c = 2 * math.asin(math.sqrt(a))

# Radius bumi dalam kilometer
r = 6371

# Menghitung jarak
jarak = r * c

# Output hasil
print("\n=== HASIL PERHITUNGAN ===")
print("Jarak antara dua titik =", jarak, "km")