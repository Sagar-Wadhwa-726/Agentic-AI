from operator import itemgetter as itm

base_liquid = ["Water", "Milk"]
extra_flavor = ["ginger"]
full_liquid_mix = base_liquid + extra_flavor
print(f"Full liquid mix : {full_liquid_mix}")


strong_brew = ["black tea", "water"] * 3
print(f"Strong brew : {strong_brew}")

# Bytearray
raw_spice_data = bytearray(b"CINNAMOM")
print(f"Raw spice data : {raw_spice_data}")
raw_spice_data = raw_spice_data.replace(b"CINNA",b"CARD")
print(f"Raw spice data after replace : {raw_spice_data}")