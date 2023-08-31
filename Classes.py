class ToDoList:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descrição: str):
        self.descrição = descrição
        print("-- ADICIONAR TAREFA --")
        indice = int (input(">> Número da tarefa: "))
        tarefa = str(input(">> Nome da tarefa:  "))
        if indice and tarefa not in self.tarefas:
            self.tarefas.append(tarefa)
        else:
            ("Essa tarefa já foi adicionada")


    def excluir_tarefa(self, indice: int):
        self.indice = indice
        print("Qual tarefa deseja excluir?")
        print(self.tarefas)
        excluir = int(input(">> "))
        if indice in self.tarefas:
            self.tarefas.pop(excluir)
            print("A tarefa foi esxcluida")
        else:
            print("Esse valor não existe")


    def listar_tarefas(self):
        print(self.tarefas)