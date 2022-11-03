"""
@Author Reyce Salisbury
Uses the square and multiply algorithm to provide a
systematic way for finding the sequence in which to perform
squarings and multiplications by A for computing A^B mod C.

Argument 1 = A (int)
Argument 2 = B (int)
Argument 3 = C (int)
Argument 4 = Table on/off (Bool) default=off

Program computes: A**B % C
"""
import sys

''' '''
def padding(val, size=int, placement='left'):
    '''
    :param: val = any
    :param: size = int
            * should be the total size that the val should fill
    :param: placement = 'center', 'left', or 'right' 
            * placement defaults to 'left', even when placement is entered incorrectly
    
    '''
    if val is None:
        val = '-' * size
        return val

    val=str(val)

    if not(placement == 'center' or placement == 'left' or placement == 'right'):
        placement == 'left'

    padNum = size - len(val)
    if padNum < 0:
        padNum == 0

    if placement == 'left':
        val = val + " " * padNum

    if placement == 'right':
        val = " " * padNum + val

    if placement == 'center':
        padNumLeft = padNum//2
        padNumRight = padNum - padNumLeft
        val = " " * padNumLeft + val + " " * padNumRight

    return val

def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    modval = int(sys.argv[3])
    try:
        table = sys.argv[4]
        if table.capitalize() == "True":
            table = True
        elif table.capitalize() == "False":
            table = False
        else:
            print("Table Failure: Improper boolean")
            table = False
    except:
        table = False
    
    if table:
        size = 3
        if len(str(modval)) > 3:
            size = len(str(modval))
        
        titleStr = (f"| {padding('stp', size, 'center')} |\t| {padding('bit', size, 'center')} |\t| " +
        f"{padding('sqr', size, 'center')} |\t| {padding('mul', size, 'center')} |")
        print(titleStr)

    stepstr = str(bin(b))[2:]
    final = 1
    for i in range(len(stepstr)):
        mul = None
        sqr = final = (final ** 2) % modval
        if stepstr[i] == '1':
            mul = final = (final * a) % modval

        if table:
            print(f"| {padding(i+1, size, 'center')} |\t| {padding(stepstr[i], size, 'center')} |\t|" + 
            f" {padding(sqr, size, 'center')} |\t| {padding(mul, size, 'center')} |")

    print(f"\n{a}^{b} % {modval} = {final}")


if __name__ == '__main__':
    main()