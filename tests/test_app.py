from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


# def test_exercicio_ola_mundo_em_html(client):
#     response = client.get('/exercicio-html')

#     assert response.status_code == HTTPStatus.OK
#     assert '<h1> Olá Mundo </h1>' in response.text
