# Task 1
num = input()
if num == '1a':
    # write your answer for question 1a below
    a=int(input())
    b=int(input())
    c=int(input())
    if  a>0 and b>=a and c>=b :
        if  a**2 + b**2 == c**2:
            print("yes")
        else:
           print("no")
elif num == '1b':
    # write your answer for question 1b below
    n=int(input())
    for a in range(1,n+1):
        for b in  range(1,n+1):
            for c in range(1,n+1):
                if a>=0 and b>=a and c>=b and a**2 + b**2 == c**2:
                    print(a,b,c)
elif num == '1c':
    # write your answer for question 1c below
    a=int(input())
    b=int(input())
    c = a**2 + b**2
    if c**0.5 %1 == 0:
        print("yes")
    else:
        print("no")
elif num == '2a':
    # write your answer for question 2a below
    a0=int(input())
    n=int(input())
    d=int(input())
    fact=1
    if a0>=n :
        print("1")
    else:
        for i in range(1,n+1):
            if i>a0 and i % d == 0:
                fact=fact*i
    print(fact)
elif num == '2b':
   # write your answer for question 2b below
   n = int(input())
   m = int(input())
   a = 1
   x = (n + 1) // 2 + 1
   for i in range(1, x):
       if i <= x and (i ** 2 + (n - i + 1) ** 2) % m == 0:
           f = i ** 2 + (n - i + 1) ** 2
           a *= f
   print(a)
elif num == '2c':
    # write your answer for question 2c below
    n = int(input())
    m = int(input())
    factors = []
    occuares = 0
    output = 1
    new_output = 1
    b = 0
    # Check for 2 as a factor
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check for odd factors
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is still greater than 2, it must be prime
    if n > 2:
        factors.append(n)
    for i in factors:
        if i != b:
            occuares = factors.count(i)
            if occuares % m == 0:
                output = i ** occuares
            else:
                output = i * occuares
            new_output = new_output * output
            output = 0
            occuares = 0
            b = i

    print(new_output)

elif num == '3':
    # write your answer for question 3 below
    a=int(input())
    b=int(input())
    x=False
    if b%a==0:
        for i in (2 ,b+1):
            if (b//a)%i ==0 and a%i ==0:
                x +=True
        if x!=False:
            print("False")
        else:print("True")
    elif b%a!=0:
        print("False")

elif num == '4a':
      # write your answer for question 4a below
      a = str(input())
      d = int(input())
      i = 1
      a_new = ""
      while i < len(a):
          if i % d != 0:
              a_new = a_new + a[i - 1]
          i += 1
      print(a_new)

elif num == '4b':
     # write your answer for question 4b below
     s1 = str(input())
     s2 = str(input())
     s3 = str(input())
     s1_new = ''
     for i in range(len(s1) - 1):
         if s1[i] in s2:
             if s1[i - 1] in s3 or s1[i + 1] in s3:
                 continue
             elif s1[i - 1] and s1[i + 1] not in s3:
                 s1_new += s1[i]
         else:
             s1_new += s1[i]
     if s1[len(s1) - 1] in s2 and s1[len(s1) - 2] in s3:
         False
     else:
         s1_new = s1_new + s1[len(s1) - 1]
     print(s1_new)
elif num == '4c':
    # write your answer for question 4c below
    s1=input()
    new_s1=""
    v="aeiouAEIOU"#volwes
    s1_list=[]
    new_sentence=""
    word=1
    new_sentencea=""
    for char in s1:
        if char in v:
            new_s1+="*"+char+"*"
        else:new_s1+=char
    s1_list=new_s1.split()
    sentences=new_s1.split(", ")
    for sentence in sentences:
        for char in range(0,len(sentence)):
            if sentence[char]==" ":
                word+=1
            if word % 2==0:
                    new_sentence+=sentence[char].upper()
            else:new_sentence+=sentence[char].lower()
        word=1
        new_sentence+=", "
    sentences=new_sentence.split(", ")
    sentences.remove("") #because we add ", " in the last of the sences
    for sentence in range(len(sentences)):
        new_sentence=str(sentences[sentence])
        new_sentence=new_sentence.split()
        new_sentence.sort()
        new_sentence.reverse()
        for i in range(len(new_sentence)):
            if i!=len(new_sentencea)-1:
                new_sentencea+=new_sentence[i]+" "
            elif sentence != (len(sentences)-1):
                new_sentencea+=","
    print(new_sentencea)")
else:
     print('error')


