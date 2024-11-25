import json
from flask import g, make_response, redirect, render_template, request, url_for
from functions.db_usuario import get_usuario
from functions.geral import datetime_para_string, remove_prefixo


def mod_login(mysql):

    # Se o usuário está logado, redireciona para a página de perfil
    if g.usuario != '':
        return redirect(url_for('perfil'))

    erro = False

    # Se o formulário foi enviado
    if request.method == 'POST':

        # Pega os dados preenchidos no formulário
        form = dict(request.form)

        # Teste mesa
        # print('\n\n\n FORM:', form, '\n\n\n')

        usuario = get_usuario(mysql=mysql, form=form)

        # Teste mesa
        # print('\n\n\n DB:', usuario, '\n\n\n')

        if usuario == None:
            # Se o usuário não foi encontrado
            erro = True
        else:
            # Se achou o usuário, apaga a senha do usuário
            del usuario['u_senha']

            # Extrai o primeiro nome do usuário
            usuario['u_pnome'] = usuario['u_nome'].split()[0]

            # Formata as datas para usar no JSON
            usuario = datetime_para_string(usuario)

            # Remove o prefixo das chaves do dicionário
            cookie_valor = remove_prefixo(usuario)

            # Converte os dados em JSON (texto) para gravar no cookie,
            # porque cookies só aceitam dados na forma texto
            cookie_json = json.dumps(cookie_valor)

            # Teste de mesa
            # print('\n\n\n JSON:', cookie_json, '\n\n\n')

            # Prepara a página de destino → index
            resposta = make_response(redirect(url_for('index')))

            # Cria o cookie
            resposta.set_cookie(
                key='usuario',  # Nome do cookie
                value=cookie_json,  # Valor a ser gravado no cookie
                max_age=60 * 60 * 24 * 365  # Validade do cookie em segundos
            )

            # Redireciona para a página de destino → index
            return resposta

    # Dados, variáveis e valores a serem passados para o template HTML
    pagina = {
        'titulo': 'CRUDTrecos - Login',
        'erro': erro
    }

    return render_template('login.html', **pagina)
