from flask import g, redirect, render_template, request, url_for


def mod_cadastro(mysql):

    jatem = ''
    success = False

    # Se o usuário está logado redireciona para a página de perfil
    if g.usuario != '':
        return redirect(url_for('perfil'))

    if request.method == 'POST':

        form = dict(request.form)

        # Verifica se usuário já está cadastrado, pelo e-mail
        sql = "SELECT u_id, u_status FROM usuario WHERE u_email = %s AND u_status != 'del'"
        cur = mysql.connection.cursor()
        cur.execute(sql, (form['email'],))
        rows = cur.fetchall()
        cur.close()

        # print('\n\n\n LEN:', len(rows), '\n\n\n')

        if len(rows) > 0:
            # Se já está cadastrado
            if rows[0]['u_status'] == 'off':
                jatem = 'Este e-mail já está cadastrado para um usuário inativo. Entre em contato para saber mais.'
            else:
                jatem = 'Este e-mail já está cadastrado. Tente fazer login ou solicitar uma nova senha.'
        else:
            # Se não está cadastrado, inclui os dados do form no banco de dados
            sql = "INSERT INTO usuario (u_nome, u_nascimento, u_email, u_senha) VALUES (%s, %s, %s, SHA1(%s))"
            cur = mysql.connection.cursor()
            cur.execute(
                sql, (
                    form['nome'],
                    form['nascimento'],
                    form['email'],
                    form['senha'],
                )
            )
            mysql.connection.commit()
            cur.close()

            success = True

    # Dados, variáveis e valores a serem passados para o template HTML
    pagina = {
        'titulo': 'CRUDTrecos - Cadastre-se',
        'jatem': jatem,
        'success': success,
    }

    return render_template('cadastro.html', **pagina)
