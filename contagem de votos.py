def contagem_de_votos(votos):
    contagem = {}
    
    # Contar votos
    for voto in votos:
        if voto in contagem:
            contagem[voto] += 1
        else:
            contagem[voto] = 1
    
    # Calcular a soma total de votos
    total_votos = sum(contagem.values())
    
    # Exibir resultados
    print("Resultado da contagem de votos:")
    for candidato, votos_contados in contagem.items():
        print(f"{candidato}: {votos_contados} votos ({(votos_contados / total_votos) * 100:.2f}%)")
    
    print(f"Total de votos: {total_votos}")

# Exemplo de uso
votos = ["Candidato_A", "Candidato_B", "Candidato_A", "Candidato_C", "Candidato_B", "Candidato_A"]
contagem_de_votos(votos)