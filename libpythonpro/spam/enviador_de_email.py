class Enviador:
    def enviar(param, remetente, destinatario, assunto,corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email do remetente inválido: {remetente}')
        return remetente


class EmailInvalido(Exception):
    pass