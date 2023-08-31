from Classes import *

todo = ToDoList()

def adicionar():
    tarefaa = str
    todo.adicionar_tarefa(tarefaa)    

def excluir():
    a = int
    todo.excluir_tarefa(a)



def main():

    x = True
    while x == True:

        print("To-Do List \n O que deseja fazer? \n [1] Adicionar tarefa \n [2] Excluir tarefa \n [3] Vizualizar tarefas \n [4] Fechar")
        escolha = int(input(">> "))
        match escolha:
            case 1:
                adicionar()
                print("O que quer fazer? \n [1] Voltar ao menu \n [2] Adicionar outra tarefa")
                escolha2 = int (input(">> "))
                match escolha2:
                    case 1:
                        main()
                    case 2:
                        adicionar()
                    case _:
                        print("Inválido")

            case 2:
                excluir()


            case 3:
                todo.listar_tarefas()
                print("Selecione [1] para voltar ao menu")
                escolha3 = int (input(">> "))
                match escolha3:
                    case 1:
                        main()
                    case _:
                        print("Inválido")
            case 4:
                print("O sistema irá fechar. Obrigada.")
                x = False