class person:
    def per(self):
        return 'unknown'
class male(person):
    def male(self):
        return "Male"
class female(person):
    def female(self):
        return "female" 

p=person()
m=male()
f=female()
print(p.per())
print(m.male())
print(f.female())          