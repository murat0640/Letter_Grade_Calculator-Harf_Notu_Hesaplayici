print("""
*****
    Welcome to Letter Grade Calculator
(Harf Notu Hesaplama Programina Hosgeldiz)
*****
""")

a = int(input("Enter your first semester exam score (ilk vize notunuzu giriniz):"))
b = int(input("Enter your second semester exam score (ikinci vize notunuzu giriniz):"))
c = int(input("Enter your final semester exam score (final notunuzu giriniz):"))

if ((a * 0.3) + (b * 0.3) + (c * 0.4)) >= 90:
    print("Your Letter Grade (Harf notunuz) AA ")
elif ((a * 0.3) + (b * 0.3) + (c * 0.4)) >= 85:
    print("Your Letter Grade (Harf notunuz) BA ")
elif ((a * 0.3) + (b * 0.3) + (c * 0.4)) >= 80:
    print("Your Letter Grade (Harf notunuz) BB ")
elif ((a * 0.3) + (b * 0.3) + (c * 0.4)) >= 75:
    print("Your Letter Grade (Harf notunuz) CB ")
elif ((a * 0.3) + (b * 0.3) + (c * 0.4)) >= 70:
    print("Your Letter Grade (Harf notunuz) CC ")
elif ((a * 0.3) + (b * 0.3) + (c * 0.4)) >= 65:
    print("Your Letter Grade (Harf notunuz) DC ")
elif ((a * 0.3) + (b * 0.3) + (c * 0.4)) >= 60:
    print("Your Letter Grade (Harf notunuz) DD ")
elif ((a * 0.3) + (b * 0.3) + (c * 0.4)) >= 55:
    print("Your Letter Grade (Harf notunuz) FD ")
elif ((a * 0.3) + (b * 0.3) + (c * 0.4)) < 55:
    print("Your Letter Grade (Harf notunuz) FF ")