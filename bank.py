class bank:
    Baname='SBI'
    MBI='Mysore'
    website='www.sbi.com'
    def __init__(self,name,phno,addre):
        self.name=name
        self.phno=phno
        self.addre=addre
    def drop_obj(self):
        print(self.name,self.phno,self.addre)
    def change_phno(self,new):
        self.phno=new
    def change_addre(self,new):
        self.addre=new
    @classmethod
    def drop_cls(cls):
        print(cls.Baname,cls.MBI,cls.website)
    @classmethod
    def change_website(self,new):
        self.website=new
naveen=bank('Naveen','90847344','basavanagudi')
class bank1(bank):
    def __init__(self,name,phno,addre,mailid,pan):
        super().__init__(name,phno,addre)
        self.mailid=mailid
        self.pan=pan
    def disp_obj(self):
        super().drop_obj()
        print(self.mailid,self.pan)

    def change_mailid(self,new):
        self.mailid=new
praveen=bank1('Praveen',13435644344,'rajajinaar','pruthhb@gmail.com','DWIK2345ik')
praveen.disp_obj()



