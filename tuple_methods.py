t=(1,2,3,4,5,6)

print(t.count(4))
print(t.index(2))
print(len(t))
print(sum(t))
print(sorted(t,reverse=True))

t1=(1,2,3,4,'Ganesh','Vishal','Onkar')
print(sorted(t1,key=lambda e:(isinstance(e,str),e)))



