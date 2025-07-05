import re

def validador(cpf):
    if not isinstance(cpf, str):
        return False

    cpf = re.sub(r'[^0-9]', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calcular_digito(cpf_parcial, peso_inicial):
        soma = 0
        peso = peso_inicial
        for digito in cpf_parcial:
            soma += int(digito) * peso
            peso -= 1
        resto = 11 - (soma % 11)
        return 0 if resto > 9 else resto

    primeiro_digito = calcular_digito(cpf[:9], 10)
    if primeiro_digito != int(cpf[9]):
        return False

    segundo_digito = calcular_digito(cpf[:10], 11)
    if segundo_digito != int(cpf[10]):
        return False

    return True

def formatar_cpf(cpf):
    cpf_limpo = re.sub(r'[^0-9]', '', cpf)

    if len(cpf_limpo) == 11:
        return f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
    else:
        return cpf
