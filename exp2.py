B_S = float(input("Enter the basic salary:"))

d_a = 0.70*B_S
t_a = 0.30*B_S
h_r_a = 0.10*B_S

g_s = d_a + t_a + h_r_a + B_S

print("\n SALARY DETAILS")
print(f"The Basic salary:{B_S}")
print(f"The Dear:{d_a}")
print(f"The travel:{t_a}")
print(f"H.R.A>:{h_r_a}")
print(f"The Gross salary:{g_s}")