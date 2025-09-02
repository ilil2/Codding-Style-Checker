import re

class Naming():
    """
    Class for the naming convention in C
    """

    def defineChecker(line:str) -> bool:
        """
        Check the #define names
        """

        define = (' '.join(line.split('\t'))).split(' ')
        for i in define[1]:
            if i != '_' and (i < 'A' or i > 'Z'):
                return False
        return True
    
    def multipleDefineCheckers(lines:list[str]) -> bool:
        """
        Check multiple #defines names
        """

        index = -1
        for line in lines:
            b = Naming.defineChecker(line)
            if not b:
                return False
            
            define = (' '.join(line.split('\t'))).split(' ')
            define = [i for i in define if i != ''][2]

            line = line.expandtabs(4)
            index2 = line.find(define)

            if index == -1:
                index = index2

            elif index != index2:
                return False
            
        return True
    
    def capitalizationChecker(word:str) -> bool:
        return re.fullmatch(r"[a-z][a-z0-9_]*")
    
    def prefixesChecker(line:str) -> bool:
        tab = [i for i in line.split(' ') if i != '']
        match tab[0]:
            case "typedef struct":
                if line[-1] != '};':
                    if not line[-1].startswith('s_'):
                        return False


if __name__ == "__main__":
    print(Naming.defineChecker("#define THIS_IS_A_VALID_DEFINE 1001"))
    print(Naming.defineChecker("#define THIS_IS_A_no_VALID_DEFINE 1001"))
    print(Naming.defineChecker("#define THIS_IS_A_NO-VALID_DEFINE 1001"))

    print(Naming.multipleDefineCheckers(["#define THIS_IS_A_VALID_DEFINE 1001",
                                         "#define THIS_IS_A_VALID_DEFINE '1001'"]))
    print(Naming.multipleDefineCheckers(["#define THIS_IS_A_VALID_DEFINE    1001",
                                         "#define THIS_IS_A_VALID_DEFINE    '1001'"]))
    print(Naming.multipleDefineCheckers(["#define THIS_IS_A_VALID_DEFINE    1001",
                                         "#define THIS_IS_A_VALID_DEFINE   '1001'"]))