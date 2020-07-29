try:
   from googlesearch import search
except ImportError:
       print("module error")
qery=input()
for j in search(query, t1d="co.in", num=10, stop=1, pause=2):
      print(j)
