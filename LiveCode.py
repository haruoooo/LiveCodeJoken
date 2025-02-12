import random

def get_computer_choice():
    """
    Retorna uma escolha aleatória do computador entre pedra, papel e tesoura.
    """
    return random.choice(["pedra", "papel", "tesoura"])

def get_user_choice():
    """
    Solicita ao usuário uma escolha válida e a retorna.
    """
    while True:
        choice = input("Escolha pedra, papel ou tesoura: ").strip().lower()
        if choice in ["pedra", "papel", "tesoura"]:
            return choice
        print("Escolha inválida! Tente novamente.")

def determine_winner(user_choice, computer_choice):
    """
    Determina o vencedor do jogo com base nas regras do Jokenpô.
    Retorna 'Usuário', 'Computador' ou 'Empate'.
    """
    if user_choice == computer_choice:
        return "Empate"
    
    win_conditions = {
        "pedra": "tesoura",  
        "papel": "pedra",     
        "tesoura": "papel"     
    }
    
    if win_conditions[user_choice] == computer_choice:
        return "Usuário"
    return "Computador"

def main():
    """
    Função principal que executa o jogo.
    """
    print("\nBem-vindo ao Jokenpô!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nVocê escolheu: {user_choice}")
        print(f"O computador escolheu: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "Empate":
            print("\nO jogo empatou! Vamos tentar novamente.\n")
        else:
            print(f"\n{winner} venceu!")
            break
    
    print("\nObrigado por jogar!")

if __name__ == "__main__":
    main()