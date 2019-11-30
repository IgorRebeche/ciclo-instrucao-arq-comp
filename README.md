# Ciclo de Instrução em python UVA
### Esse trabalho representa um esboço do funcionamento da funcionalidade de ciclo de instruções de uma CPU.

Separei os componentes (Hardware) da maquina em classes

Temos, **memoria principal**, **cpu**, **computador** (encapsula os outros 2)

Comandos da CPU:

| Comando | Descrição | OP Code |
| --- | --- | --- |
| ADD | Somar | 00000010 |
| SUB | Subtrair | 00000001 |
| JUMP | Pular para endereco | 00000100 |

### Exemplo:

Instrucoes:
```
def instruction(self):
        self.CPU.addInstruction('JUMP', 6) # Jump to third instruction
        self.CPU.addInstruction('ADD', 10, 10)
        self.CPU.addInstruction('ADD', 12, 10)
        self.CPU.addInstruction('EXIT')
```
Resultado:
```
Inicializando computador...
MemoriaPrincipal de 256 Bytes
Memory Information:
Stack Pointer: 6 | HEAD: 0 | Result HEAD: 9 | Result Stack Pointer: 10

Dumped Memory -----------------
['00000100', '00000110', '00000000', '00000010', '00001010', '00001010', '00000010', '00001100', '00001010', 
'11111111', '00010110', None, None, None, None, None, None, None, None, None, None, None, None, None, None, 
None, None, None, None, None, None, None, None, None....]
```


