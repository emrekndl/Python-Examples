def is_palindrome(num):
    # tek haneli değerleri yoksay
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False

def infinite_palindromes():

    num = 0

    while True:

        if is_palindrome(num):

            #  send() ile gelen yeni değer i ye atılır
            i = (yield num)

            if i is not None:

                num = i

        num += 1

pal_gen = infinite_palindromes()
for i in pal_gen:
    print(f"palindrom sayı: {i}")
    digits = len(str(i))
    #  send() kullanımı, yield geri yeni değer gönderir
    print(f"yeni num degeri: {10 ** (digits)}")
    #  throw() kullanımı, generator lerde hata yakalama işlemi sağlar
    if digits == 5:
        #  pal_gen.throw(ValueError("5 basamak sınırı!"))
        #  close() kullanımı, generatorü durdurmayı sağlar
        pal_gen.close()
    pal_gen.send(10 ** (digits))

