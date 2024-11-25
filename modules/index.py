from flask import g, redirect, render_template, request, url_for
from functions.db_treco import get_all_trecos


def mod_index(mysql):

    # Se o usuário não está logado redireciona para a página de login
    if g.usuario == '':
        return redirect(url_for('login'))

    # Recebe valor da querystring, se existir → /?a=xxxxx
    acao = request.args.get('a')

    # Obtém todos os 'trecos' do usuário conectado
    rows = get_all_trecos(mysql)

    # Teste de mesa para verificar o retorno dos dados do banco de dados
    # print('\n\n\n DB:', rows, '\n\n\n')

    # Dados, variáveis e valores a serem passados para o template HTML
    pagina = {
        'titulo': 'CRUDTrecos',  # ← 'titulo' é obrigatório para todas as páginas / rotas
        'usuario': g.usuario,  # ← 'usuario' é obrigatório para todas as páginas / rotas
        'items': rows,
        'acao': acao,
    }

    # Renderiza o template HTML, passando valores (pagina) para ele
    return render_template('index.html', **pagina)
