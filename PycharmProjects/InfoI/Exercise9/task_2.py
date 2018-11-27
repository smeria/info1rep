

from abc import ABC, abstractclassmethod

class Toy(object):
    def __init__(self, is_assembled= False, is_painted=False, is_wrapped= False):
        self.is_assembled = is_assembled
        self.is_painted = is_painted
        self.is_wrapped = is_wrapped

    def is_complete(self):
        if self.is_wrapped ==True and self.is_assembled == True and self.is_painted == True:
            return True
        else:
            return False

class AssemblyLine(object):
    def __init__(self, toys):
        self.__toys = toys

    def get_toys(self):
        return self.__toys

    def get_number_of_toys(self):
        return len(self.__toys)

    def take_toy(self):
        if len(self.__toys) >= 0:
            toy = self.__toys[0]
            self.__toys = self.__toys[1:]
            return toy
        else:
            return None

    def put_toy_back(self):
        if self.take_toy() != None:
            self.__toys.append(self.take_toy())
        else:
            pass

class Elf(ABC):
    _toy_working_on = None

    def __init__(self, assembly_line):
        self.assembly_line = assembly_line


    @abstractclassmethod
    def do_job(self):
        pass

    def take_from(self):
        if Elf._toy_working_on == None:
            toy = AssemblyLine.get_toys(self.assembly_line)
            Elf._toy_working_on = toy
        else:
            pass

    def put_back(self):
        AssemblyLine.put_toy_back(self.assembly_line)
        Elf._toy_working_on = None


class AssemblerElf(Elf):
    def __init__(self):
        super().__init__(self)


    def do_job(self):
        if Elf._toy_working_on != None:
            Toy.is_assembled = True
            return Toy.is_assembled
        else:
            pass

class PainterElf(Elf):

    def do_job(self):
        if Elf._toy_working_on != None:
            Toy.is_painted = True
            return Toy.is_painted
        else:
            pass


class WrapperElf(Elf):

    def do_job(self):
        if Elf._toy_working_on != None:
            if Toy.is_painted == True and Toy.is_assembled == True:
                Toy.is_wrapped = True
                return Toy.is_wrapped
            else:
                return Toy.is_wrapped
        else:
            return Elf._toy_working_on

class Santa(object):

    def __init__(self):
        pass

    def verify(self, assembly_line):
        self.assembly_line = assembly_line
        for i in assembly_line:
            if i == True:
                pass
            else:
                return False



if __name__ == '__main__':
    # Create three toys
    toy1 = Toy("Toy1")
    toy2 = Toy("Toy2")
    toy3 = Toy("Toy3")

    # Create an assembly line with three toys
    line = AssemblyLine([toy1, toy2, toy3])

    # Create three elves, one of each subclass
    assembler = AssemblerElf()
    painter = PainterElf()
    wrapper = WrapperElf()

    # Create a Santa :-)
    santa = Santa()

    # Let the elves work through the assembly line
    for elf in [assembler, wrapper, painter]:  # Wrong order: wrapping can't happen before painting!
        for i in range(line.get_number_of_toys()):
            elf.take_from(line)
            elf.do_job()
            elf.put_back(line)

    # The line cannot be verified because the toys are not wrapped
    assert not santa.verify(line)

    # Create three new toys...
    toy4 = Toy("Toy4")
    toy5 = Toy("Toy5")
    toy6 = Toy("Toy6")

    # ... and a new assembly line
    line2 = AssemblyLine([toy4, toy5, toy6])

    # This time, let the elves work through the assembly line in the right order
    for elf in [painter, assembler, wrapper]:  # Right order: wrap at the end!
        for i in range(line2.get_number_of_toys()):
            elf.take_from(line2)
            elf.do_job()
            elf.put_back(line2)

    # Now the line can be verified
    assert santa.verify(line2)
