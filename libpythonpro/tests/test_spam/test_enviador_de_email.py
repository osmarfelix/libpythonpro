import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None



@pytest.mark.parametrize(
    'destinatario',
    ['osmarfelix@gmail.com','teste@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado=enviador.enviar(
        destinatario,
        'osmar@gmail.com',
        'Cursos Python Pro',
        'Primeira Turma GUIDO.'
    )

    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['','osmar']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'osmar@gmail.com',
            'Cursos Python Pro',
            'Primeira Turma GUIDO.'
    )




