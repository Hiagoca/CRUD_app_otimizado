from flask import abort, g, redirect, render_template, request, url_for
from functions.db_treco import get_one_treco, update_treco


def mod_edita(mysql, id):

    # Se o usuário não está logado redireciona para a página de login
    if g.usuario == '':
        return redirect(url_for('login'))

    # Se o formulário foi enviado
    if request.method == 'POST':
        form = dict(request.form)

        # print('\n\n\n FORM:', form, '\n\n\n')

        # Salva atualização do registro
        update_treco(mysql=mysql, form=form, id=id)

        # Após editar, retorna para a lista de itens
        return redirect(url_for('index', a='editado'))

    # Obtém um registro pelo id
    row = get_one_treco(mysql=mysql, id=id)

    # print('\n\n\n DB:', row, '\n\n\n')

    if row == None:
        abort(404)

    pagina = {
        'titulo': 'CRUDTrecos',
        'usuario': g.usuario,
        'item': row,
    }

    return render_template('edita.html', **pagina)
