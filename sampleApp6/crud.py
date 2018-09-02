from model import db, Puppy

""" CREATE """

jim = Puppy("Jimmy",10)

db.session.add(jim)
db.session.commit()


""" READ """
all_puppies = Puppy.query.all()
print(all_puppies)


""" Update """

pup = Puppy.query.get(29)
pup.name = "WeeWillieWinkie" 
db.session.add(pup)
db.session.commit()



""" Delete """

pup = Puppy.query.get(30)

print(pup)
db.session.delete(pup)
print(Puppy.query.all())