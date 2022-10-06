import rsa
from time import sleep

chavepub, chavepriv = rsa.newkeys(1110)
opc = 0
while opc != 3:
    print('''   Por favor selecione uma opção:    
    [1] Criptografar uma mensagem
    [2] Descriptografar uma mensagem
    [3] Sair do programa''')
    opc = int(input('>>>>>Qual sua opção?: '))
    if opc == 1:
        mensagem = input(str('Digite a mensagem que gostaria de criptografar: '))
        encMsg = rsa.encrypt(mensagem.encode(), chavepub)
        print('Criptografando sua mensagem...')
        for cont in range(3, 0, -1):
            print(cont)
            sleep(1)
        print('Mensagem criptografada: {}'.format(encMsg))
    elif opc == 2:
        msgdec: str = input(str('Digite a mensagem criptografada: '))
        decMessage = rsa.decrypt(encMsg, chavepriv).decode()
        print('Descriptografando sua mensagem...')
        for cont in range(3, 0, -1):
            print(cont)
            sleep(1)
        print('Mensagem descriptografada: {}'.format(decMessage))

    elif opc == 3:
        print('Finalizando...')
        for cont in range(3, 0, -1):
            print(cont)
            sleep(1)
        print('=-=' * 20)
        print('Fim do programa! Volte sempre!')
    else:
        print('Opção invalida! Tente novamente.')
