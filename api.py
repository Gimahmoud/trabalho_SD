from sanic import Sanic
from sanic.response import json


app = Sanic(__name__)


@app.route('/soma')
async def soma(request):
    a = float(request.args['a'][0])
    b = float(request.args['b'][0])
    resultado = a + b
    return json({'resultado': resultado})



@app.route('/subtracao')
async def subtracao(request):
    a = float(request.args['a'][0])
    b = float(request.args['b'][0])
    resultado = a - b
    return json({'resultado': resultado})

@app.route('/multiplicacao')
async def multiplicacao(request):
    a = float(request.args['a'][0])
    b = float(request.args['b'][0])
    resultado = a * b
    return json({'resultado': resultado})

@app.route('/divisao')
async def divisao(request):
    a = float(request.args['a'][0])
    b = float(request.args['b'][0])
    resultado = a / b
    return json({'resultado': resultado})

@app.route('/raizquadrada')
async def raizquadrada(request):
    a = float(request.args['a'][0])
    resultado = a ** 0.5
    return json({'resultado': resultado})

@app.route('/potencia')
async def potencia(request):
    a = float(request.args['a'][0])
    b = float(request.args['b'][0])
    resultado = a ** b
    return json({'resultado': resultado})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


#http://localhost:8000/potencia?a=3&b=3 exemplo de como usar o link
