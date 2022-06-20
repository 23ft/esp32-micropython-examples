import urequests

userdata = 'seriex=50&tempx=50' 
resp = urequests.post('http://192.168.0.29/prueba3.php',
                      data= userdata,
                      headers = {'Content-Type': 'application/x-www-form-urlencoded'}) 

pas = resp.text
print(pas)
