from flask import Flask
app = Flask(__name__)

encounters = [
    {
        'id': '123456',
        "facility":"123",
        '98767':{'code': '98767',
                     'services': ['3234','13423','2322'],
                  'price': '3000'
                  }
    },
    {
        'id': '78912',
        "facility": "456",
        '23334': {'code': '23334',
                      'services': ['3234', '13423'],
                      'price': '500'
                      }
    },
{
        'id': '3563343',
        "facility": "789",
        '23434': {'code': '23434',
                      'services': ['3234', '13423',"1123"],
                      'price': '5004'
                      }
    },
{
        'id': '00989',
        "facility": "123",
        '45645': {'code': '45645',
                      'services': ['2245', '13423'],
                      'price': '200'
                      }
    },
{
        'id': '46545',
        "facility": "456",
        '9877': {'code': '98747',
                      'services': ['3234', '13423','23434'],
                      'price': '1000'
                      }
    },
{
        'id': '4646231',
        "facility": "789",
        '12993': {'code': '12993',
                      'services': ['578', '535',],
                      'price': '1500'
                      }
    }
]

facilities = [
    {
    'id':'123',
    'name': "phc jos",
    'no_of_enrolee':"50"
    },
    {
        'id': '456',
        'name': "phc mangu",
        'no_of_enrolee': "20"
    },
{
        'id': '789',
        'name': "phc pankshin",
        'no_of_enrolee': "35"
    }
]



@app.route('/')
def index():
    datas = []
    for data in facilities:
        if data["id"] == '123':
            name = data["name"]
            for num in encounters:
                if num["facility"] == "123":
                    num["name"] = name
                    datas.append(num)
    return {"data":datas, "status":True}


@app.route('/facility/<value>')
def details(value):
    values = []
    for facility in facilities:
        values.append(facility['id'])

    name = ""
    id = value
    n_enrolls = 0
    n_encounts = 0
    enct_datas = []


    if value in values:
        for i in facilities:
            for j in encounters:
                if i['id'] == value and j['facility'] == value:
                    name = i['name']
                    n_enrolls = i['no_of_enrolee']
                    n_encounts += 1
                    enct_data = j
                    enct_datas.append(enct_data)

        return {
            'names': name,
            'facility_ids': id,
            'no of enrollees': n_enrolls,
            'no of encounters': n_encounts,
            'encounter data': enct_datas,
            'status': True
        }
    else:
        return {'message':'invalid value',
                'status': False}

@app.route('/all_facilities')
def all_facilities():
    all_facilities = []
    for facility in facilities:
        id = facility["id"]
        enc = []
        enc_count = 0
        for encounter in encounters:
            if encounter["facility"] == id:
                enc.append(encounter)
                enc_count += 1
        facility["encounters"] = enc
        facility["number_of_encounters"] = enc_count
        all_facilities.append(facility)

    return {"result": all_facilities,"status":True}


if __name__ == "__main__":
    app.run(debug=True)