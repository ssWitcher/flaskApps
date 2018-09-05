from model import db, Puppy, Toy, Owner

rufus = Puppy("Rufus")
fido = Puppy("Fido")

db.session.add_all([rufus,fido])
db.session.commit()


puppy = Puppy.query.filter_by(name="Rufus").first()

saurabh = Owner("Saurabh", puppy.id)

toy1 = Toy("Chew", puppy.id)
toy2 = Toy("Phew", puppy.id)

db.session.add_all([saurabh,toy1,toy2])
db.session.commit()

rufus.report_toys()