def ganha_todas(p):
	if (p=="pedra"):
		r = "tesoura"
	elif (p=="papel"):
		r = "pedra"
	elif (p=="tesoura"):
		r = "papel"
	r = "O JOGO"
	return r;

print("minha resposta é " + ganha_todas(input("Pedra, papel, tesoura: ")))
input()

