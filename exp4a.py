jee_studs = { "Aryan Sharma", "Neha Verma", "Rahul Mehta", "Sneha Iyer" }
cet_studs =  { "Rahul Mehta", "Priya Deshmukh", "Karan Joshi", "Sneha Iyer" }
neet_studs =  { "Neha Verma", "Priya Deshmukh", "Aman Khan", "Aisha Patel" }

all_studs = cet_studs|jee_studs|neet_studs
print("All studs:", all_studs)

cet_jee_common = cet_studs&jee_studs
print("Studs Common in cet and jee:", cet_jee_common)

cet_neet_diff = cet_studs - neet_studs
print("Studs in cet but not in neet:", cet_neet_diff)

neet_jee_symdiff = neet_studs ^ jee_studs
print("Studs in either neet or jee but not in both:", neet_jee_symdiff)
