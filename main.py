from Packages import Interface
from Packages import Color

while True:
    taskType = Interface.menu(
        ["Tarefas Diárias", "Tarefas Temporárias", "Sair do Programa"],
        colorOne=Color.magenta(),
        colorTwo=Color.blue(),
        title="GERENCIADOR DE TAREFAS",
    )
    break
