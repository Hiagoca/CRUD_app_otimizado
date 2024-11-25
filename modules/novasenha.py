from flask import g, redirect, render_template, request, url_for
from functions.db_usuario import get_by_email_birth, save_new_password
from functions.geral import gerar_senha


def mod_novasenha(mysql):

    novasenha = ''
    erro = False

    # Se o usuário está logado, redireciona para a página de perfil
    if g.usuario != '':
        return redirect(url_for('perfil'))

    # Se o formulário foi enviado
    if request.method == 'POST':

        # Obtém dados preenchidos
        form = dict(request.form)

        # Teste de mesa
        # print('\n\n\n FORM:', form, '\n\n\n')

        row = get_by_email_birth(mysql=mysql, form=form)

        # Teste de mesa
        # print('\n\n\n DB:', row, '\n\n\n')

        # Se o usuário não existe
        if row == None:
            # Exibe mensagem no frontend
            erro = True
        else:
            # Gera uma nova senha
            novasenha = gerar_senha()

            # Salva a nova senha
            save_new_password(mysql=mysql, novasenha=novasenha, id=row['u_id'])

    # Dados, variáveis e valores a serem passados para o template HTML
    pagina = {
        'titulo': 'CRUDTrecos - Nova Senha',
        'erro': erro,
        'novasenha': novasenha,
    }

    return render_template('novasenha.html', **pagina)
