e: int = 13
N: int = 95
p: int = 19
q: int = 5
phi: int = (p - 1) * (q - 1)
print("Phi:", phi)
d: int = 61
C: int = 88
Message = (C**d) % N
print("Message:", Message)