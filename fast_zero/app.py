from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.routers import auth, users
from fast_zero.schemas import Message

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


# @app.get('/exercicio-html', response_class=HTMLResponse)
# def exercicio_html():
#     return """
#     <html>
#         <head>
#             <title>Nosso olá mundo</title>
#         </head>
#         <body>
#             <h1> Olá Mundo </h1>
#         </body>
#     </html>"""
