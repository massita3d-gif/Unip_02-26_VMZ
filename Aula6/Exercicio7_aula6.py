def validar_email_basico(email):
    if " " in email:
         print("EMAIL NAO PODE TER ESPACOS")
    elif "@" not in email or ".com" not in email:
        print("EMAIL INVALIDO")       
    else:
        print("EMAIL VALIDO!")
email=input("DIGITE SEU EMAIL: ")
validar_email_basico(email)