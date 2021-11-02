# import minha_lib
from minha_lib import x
from minha_lib import x as x_lib
from minha_lib import soma
from minhas_funcoes.minha_lib import soma as soma_lib
# from .minhas_funcoes . referencia o diretorio atual
# from ..minhas_funcoes .. referencia o diretorio anterior (volta o diretorio)

print(soma_lib(1,2))
print(soma(1,2))
print(x)
print(x_lib)
# print(minha_lib.x)