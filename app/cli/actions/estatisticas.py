# Exibe estatísticas do sistema
def exibir_estatisticas(db):
    limpar_tela()
    print("=" * TERMINAL_WIDTH)
    print("ESTATÍSTICAS DO SISTEMA".center(TERMINAL_WIDTH))
    print("=" * TERMINAL_WIDTH)
    print()

    try:
        total = db.query(Aluno).count()
        ativos = db.query(Aluno).filter(Aluno.ativo == 1).count()
        inativos = db.query(Aluno).filter(Aluno.ativo == 0).count()

        if total > 0:
            media_geral = db.query(Aluno).filter(Aluno.ativo == 1).all()
            media_sistema = (
                sum([a.media_geral for a in media_geral]) / len(media_geral)
                if media_geral
                else 0
            )
        else:
            media_sistema = 0

        # Cursos
        cursos = {}
        alunos = db.query(Aluno).all()

        for aluno in alunos:
            if aluno.curso in cursos:
                cursos[aluno.curso] += 1
            else:
                cursos[aluno.curso] = 1

        print(f"📊 Total de alunos cadastrados: {total}")
        print(f"✅ Alunos ativos: {ativos}")
        print(f"❌ Alunos inativos: {inativos}")
        print(f"📈 Média geral do sistema: {media_sistema:.2f}")

        if cursos:
            print(f"\n📚 Alunos por curso:")

            for curso, quantidade in sorted(
                cursos.items(), key=lambda x: x[1], reverse=True
            ):
                print(f"   • {curso}: {quantidade} aluno(s)")

    except Exception as e:
        print(f"\n❌ Erro ao calcular estatísticas: {e}")

    pausar()
