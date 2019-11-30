from pprint import pprint
class MemoriaPrincipal:

    def __init__(self):
        # MemoriaPrincipal de 256 bytes (256 endereços) com celulas de 8 bits
        self.memorySize = 2**8
        self.HEAD = 0
        self.RESULT_HEAD = 0
        self.STACK_POINTER = 0
        self.STACK_RESULT_POINTER = 0
        #MemoriaPrincipal Principal
        self.memoriaPrincipal = [None] * self.memorySize
    
    
    def insertBits(self, bits):
        BitsParaAlocar = bits.split(' ')
        bitsSize = len(BitsParaAlocar) - 1
        lastIndex =  self.STACK_POINTER if self.STACK_POINTER == 0 else self.STACK_POINTER + 1
        bitAdrress = lastIndex
        
        for i, byte in enumerate(BitsParaAlocar) :
            
            self.memoriaPrincipal[lastIndex] = byte
            if i != bitsSize:
                lastIndex += 1
        
        self.STACK_POINTER = lastIndex
        return bitAdrress
    
    def setResultHead(self):
        self.RESULT_HEAD = self.STACK_POINTER
        self.STACK_RESULT_POINTER = self.RESULT_HEAD
    
    def setResultValue(self, result):
        self.STACK_RESULT_POINTER += 1
        self.memoriaPrincipal[ self.STACK_RESULT_POINTER ] = result
    
    def setSTackPointer(self, index):
        self.STACK_POINTER = index
    
    def printMemory(self):
        print(self.memoriaPrincipal)
        print(self.HEAD)

class CPU:

    def __init__(self, memoria):
        self.mem = memoria
        self.PC = self.mem.HEAD
        self.RI = []
        self.instruction_count = 0
        
    def addInstruction(self, instruction, R1 = 0, R2 = 0):
        
        if instruction == 'ADD':
            self.mem.insertBits(f'00000010 {R1:08b} {R2:08b}')
        if instruction == 'SUB':
            self.mem.insertBits(f'00000001 {R1:08b} {R2:08b}')
        if instruction == 'JUMP':
            self.mem.insertBits(f'00000100 {R1:08b} {R2:08b}')
        
        self.instruction_count += 1

        if instruction == 'EXIT':
            self.mem.insertBits(f'11111111')
            self.mem.setResultHead()    

    def ULA(self, binary_instruction : list):
        
        if binary_instruction[0] == '00000010': #ADD
            #Sum in decimal base > convert to bin > convert to int and format number to 8 digits
            result = bin(int(binary_instruction[1], 2) + int(binary_instruction[2], 2))
            result = f'{int(result[2:]):08}'
            self.mem.setResultValue(result)
        
        if binary_instruction[0] == '00000001': #SUB
            result = bin(int(binary_instruction[1], 2) - int(binary_instruction[2], 2))
            result = f'{int(result[2:]):08}'
            self.mem.setResultValue(result)

        if binary_instruction[0] == '00000100': #JUMP Takes R1 as the adress
            JumpAdress = int(binary_instruction[1], 2)
            self.mem.setSTackPointer(JumpAdress)
            self.PC = JumpAdress
    
    def executeInstructions(self):

        while self.mem.memoriaPrincipal[self.PC]:
            
            #Stop Fetch Instructions
            if self.mem.memoriaPrincipal[self.PC] == '11111111':
                break
            
            #If size > 3
            if len(self.RI) < 3:
                self.RI.append(self.mem.memoriaPrincipal[self.PC])
                self.PC += 1 #increment Program Counter
            else:
                self.ULA(self.RI) #EXECUTE INSTRUCTION
                self.RI = []   #CLEAN RI    
                self.RI.append(self.mem.memoriaPrincipal[self.PC]) #append next instruction
                self.PC += 1 #increment Program Counter
            
        if len(self.RI) == 3:
                self.ULA(self.RI) #EXECUTE INSTRUCTION

class Computador():

    def __init__(self):
        self.mem = MemoriaPrincipal()
        self.CPU = CPU(self.mem)
        self.printComputerInformation()

    def printComputerInformation(self):
        memRamSize = self.mem.memorySize
        print('Inicializando computador...')
        print(f'MemoriaPrincipal de {memRamSize} Bytes')

    def dumpProgram(self):
        print(f'Memory Information: ')
        print(f'Stack Pointer: {self.mem.STACK_POINTER} | HEAD: {self.mem.HEAD} | Result HEAD: {self.mem.RESULT_HEAD} | Result Stack Pointer: {self.mem.STACK_RESULT_POINTER} ')
        print('Dumped Memory -----------------')
        self.mem.printMemory()
    def instruction(self):
        
        #Adicionando instrucao 1
        self.CPU.addInstruction('JUMP', 6) # Jump to third instruction
        self.CPU.addInstruction('ADD', 10, 10)
        self.CPU.addInstruction('ADD', 12, 10)
        self.CPU.addInstruction('EXIT')

    def runProgram(self):
        self.CPU.executeInstructions()
        

# Hardware da Maquina
computador = Computador()

# CICLO DE PROCESSAMENTO (SIMULANDO UMA ITERACAO DO CLOCK)
computador.instruction()

computador.runProgram()

computador.dumpProgram()



