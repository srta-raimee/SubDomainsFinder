
import dns.resolver

res = dns.resolver.Resolver()

with open("wordlist.txt", "r") as arquivo:
    # just to ignore blank spaces in the wordlist file
    subdominios = [linha.strip() for linha in arquivo.readlines()]  
alvo = "bancocn.com"

for subdominio in subdominios:
    try:
        sub_alvo = f"{subdominio}.{alvo}"
        print(sub_alvo)
        resultado = res.resolve(sub_alvo, "A")
        for ip in resultado:
            resultado_texto = f"{sub_alvo} -> {ip}\n"
            print(resultado_texto)
           
            with open("results.txt", "a") as arquivo_resultado:
                arquivo_resultado.write(resultado_texto)
    except:
        pass
