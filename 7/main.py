class Store:
    def __init__(self,name,address,contacts,manager,storage):
        self.name=name
        self.address=address
        self.contacts=contacts
        self.manager=manager
        self.storage=storage
        
    def getList(self):
        print(self.storage)
    def setDiscount(self):
        pass
    def getContact(self):
        print('U can get in contact with manager',self.manager,'his(her) number is',self.contacts)
    def newItem(self):
        pass        
rozetka=Store('Rozetka','Geroiv UPA 10','38065421578','Oleg',[{
    'phones':[{
        'phone1':{
            'sim':2,
            'OS':'Android',
            'battery':'10000mAh',
            'front-camera':True,
            'RAM':4,
            'status':True,
            'amount':100,
            'price':3000
        }
    }],
    'TV':[{
        'tv1':{
            'size':40,
            'smartTV':True,
            'status':True,
            'amount':50,
            'price':10000
        }
    }],
    'Notebooks':[{
        'note1':{
            'core':'Intel i5 4500',
            'RAM':16,
            'video':'nvidia gtx1060',
            'status':False,
            'amount':0,
            'price':20000
        }
    }]
}])
rozetka.getList()
print('\n')
rozetka.getContact()

    
    
    