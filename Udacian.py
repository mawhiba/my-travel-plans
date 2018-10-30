class Udacian:
    def __init__(self,name,city,enrollment,nanodegree,status):
        self.name = name
        self.city = city
        self.enrollment = enrollment
        self.nanodegree = nanodegree
        self.status = status

    def print_udacian(self):
        print(self.name + " is enrolled in " + self.city + " studying "+
        self.nanodegree + " with Ms. Elham," + self.enrollment +" ,she is " + self.status)

udaci = Udacian("Mawhiba","Dammam","Session A.M","Full Stack Web Developer",
"On track")
udaci.print_udacian()
