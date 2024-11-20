import string

alpl = string.ascii_lowercase
alph = string.ascii_uppercase

# def make_matrix():
#     mat = []
#     for i in range(26):
#         mat.append(alp[-i:] + alp[:-i])
#     return mat

def encrypt_mssg(key, mssg):
    encrypt = ""
    matl = []
    for i in range(26):
        matl.append(alpl[-i:] + alpl[:-i])

    for i in range(len(mssg)):
        if 'a' <= mssg[i] <= 'z':
            a = b = 0
            for j in range(26):
                if matl[j][0] == key[i % len(key)]:
                    a = j
                if matl[0][j] == mssg[i]:
                    b = j
            encrypt += matl[a][b]
        else:
            encrypt += mssg[i]
    return encrypt

def decrypt_mssg(key,mssg):

    decrypt = ""
    matl = []
    for i in range(26):
        matl.append(alpl[-i:] + alpl[:-i])
    for i in range(len(mssg)):

        if 'a' <= mssg[i] <= 'z':
            a = b = 0
            for j in range(26):
                if matl[j][0] == key[i % len(key)]:
                    a = j
                    for k in range(26):
                        if matl[a][k] == mssg[i]:
                            b = k
            decrypt += matl[0][b]
        else:
            decrypt += mssg[i]
    return decrypt

def main():

    key = "a"
    mssg = "hello"
    print("------Substitution Cipher-------")
    while True:
        print("1) New message")
        print("2) New key")
        print("3) View Message")
        print("4) Get decrypted message")
        print("5) Exit")
        choice = int(input("Enter choice: "))
        print()
        if choice == 1:
            mssg = input("Enter message: ")
        elif choice == 2:
            key = input("Enter key: ")
        elif choice == 3:
            encrypt_mssg(key, mssg, matrix)
        elif choice == 4:
            decrypt_mssg(key, matrix)
        elif choice == 5:
            break
        else:
            print("Invalid choice")
        print()

if __name__ == "__main__":
    main()