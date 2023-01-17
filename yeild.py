# def gen():
#     print('hllo')
#     yield 1
#     print('hi')
#     yield 2
#     print('bye')
#     yield 3
#     print('pruthvi')
#     yield 4
# print(list(gen()))
#
# def gen():
#     print('hllo')
#     return 1
#     print('hi')
#     return 2
#     print('bye')
#     return 3
#     print('pruthvi')
#     return 4
# print(gen())




# def pru():
#     for i in range(0,101,2):
#         yield i
# print(list(pru()))

# n=5
# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n*fact(n-1)
# def gen():
#     for i in range(0,n):
#         yield fact(n)
# print(list(gen()))


# def exstr(t):
#     for i in t:
#         if type(i)==int:
#             yield i
# print(tuple(exstr((1,2.4,'hai,2+7j',1.7,90,34))))




demo=lambda st,ch:st.count(ch)
print(demo(st=str(input('enter any value')),ch=str(input('enter 1 char'))))


