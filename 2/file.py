theatres=[{
    'name':'thr1',
    'seats':'100',
    'actors':[
        'ac1','ac2','ac3'
    ],
    'performances':[{
        'date':'xxx',
        'name':'name1',
        'price':'100',
        'actors':[
            'ac1','ac3'
        ],
        'soldTickets':'80',
        'recent':True
    },
    {
         'date':'xxx',
         'name':'name2',
         'price':'90',
         'actors':[
             'ac1','ac2'
         ],
         'soldTickets':'100',
         'recent':False
    }
  ]
},
        {
            'name':'thr2',
            'seats':'120',
            'actors':[
            'ac4','ac5','ac6'
             ],
            'performances':[{
               'date':'xxx',
               'name':'name3',
               'price':'200',
               'actors':[
                   'ac4','ac6'
             ],
             'soldTickets':'70',
             'recent':True
             },
             {
               'date':'xxx',
               'name':'name4',
               'price':'80',
               'actors':[
                   'ac5','ac6'
             ],
             'soldTickets':'120',
             'recent':False
        }] 
    }]
#Вивід вистав 1 та 2-го театру
print(theatres[0]['performances'],theatres[1]['performances'] )
#Вивід акторів 1 театру
print(theatres[0]['actors'])
#Додаю виставу до 2 театру
theatres[1]['performances'].append({
    'performances':[{
        'date':'yyy',
        'name':'name5',
        'price':'150',
        'actors':[
            'ac4'
        ],
        'soldTickets':'0',
        'recent': True
    }]
})
#print(theatres[1]['performances'] ) /перевірка

#Вивід к-ості вільних квитків на 1 виставу 1 театру
print(int(theatres[0]['seats'])-int(theatres[0]['performances'][0]['soldTickets']))
#Вивід прибутку з 1 вистави 2 театру на основі проданих квитків
print(int(theatres[1]['performances'][0]['soldTickets'])*int(theatres[1]['performances'][0]['price']))
