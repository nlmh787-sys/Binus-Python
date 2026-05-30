# Input dari user
jari_jari = float(input("Masukkan jari-jari tabung: "))
tinggi = float(input("Masukkan tinggi tabung: "))

# Nilai phi
phi = 3.14

# Proses perhitungan volume tabung
volume = phi * (jari_jari ** 2) * tinggi

# Output hasil
print("\n=== HASIL PERHITUNGAN ===")
print("Volume tabung =", volume, "meter kubik")