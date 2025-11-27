senha = input("Digite a senha: ")
tamanho_ok = len(senha) >= 8
maiuscula_ok = any(c.isupper() for c in senha)
minuscula_ok = any(c.islower() for c in senha)
digito_ok = any(c.isdigit() for c in senha)
especial_ok = any(not c.isalnum() for c in senha)

if tamanho_ok and maiuscula_ok and minuscula_ok and digito_ok and especial_ok:
    print("Senha forte!")
else:
    print("Senha fraca. Regras não atendidas:")
    if not tamanho_ok:
        print("- Mínimo de 8 caracteres")
    if not maiuscula_ok:
        print("- Deve conter letra maiúscula")
    if not minuscula_ok:
        print("- Deve conter letra minúscula")
    if not digito_ok:
        print("- Deve conter número")
    if not especial_ok:
        print("- Deve conter caractere especial")
        