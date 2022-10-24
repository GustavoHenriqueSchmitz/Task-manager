from Packages import Interface
from Packages import Color

while True:
    taskType = Interface.menu(
        ["Tarefas Diárias", "Tarefas Temporárias", "Sair do Programa"],
        colorOne=Color.magenta(),
        colorTwo=Color.blue(),
        title="GERENCIADOR DE TAREFAS",
    )
    
    if taskType == 1:
        continue
    
    elif taskType == 2:
        continue
    
    elif taskType == 3:
        break
    
    
