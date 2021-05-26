# the try block will generate an error, because x is not defined:
print('contoh 1')
try :
    print(x)
except :
    print("an exception occured")
print("=========================================================")
# the try block will generate an error, because x is not defined:
print('contoh 2')
try :
    x = 'teknik'
    print(x)
except :
    print("an exception occured")
print("=========================================================")
print('contoh 3')
x = -1
if x<0:
    raise Exception("sorry, no numbers below zero")
print("=========================================================")
print('contoh 4')
x = "hello"
if not type(x) is int:
    raise Exception("only integers are allowed")
print("=========================================================")
print("blok try...except")
try:
    teks = input("ketikkan sesuatu:")
except EOFError:
    print('\nKenapa sudah EOF?')
except KeyboardInterrupt:
    print('\nAnda membatalkan operasi')
else:
    print('anda mengetikkan "%s"'% teks)
print("=========================================================")
print("blok try...except lebih dari satu")
try:
    teks = input("ketikkan sesuatu:")
except EOFError:
    print('\nKenapa sudah EOF?')
except KeyboardInterrupt:
    print('\nAnda membatalkan operasi')
else:
    print('anda mengetikkan "%s"'% teks)
print("=========================================================")
print("blok try...finally")
import time
try:
    f=open('contoh.txt')
    while True:
        baris = f.readline()
        if len(baris)==0:
            #EOF
            break
        print(' ', baris)
        time.sleep(2) #delay 2 detik
except KeyboardInterrupt:
    print('\nAnda membatalkan operasi')
finally:
    f.close()
    print('file ditutup')