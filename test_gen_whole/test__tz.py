# Automatically generated by Pynguin.
from notebook import _tz as module0


def test_case_0():
    var0 = b''
    var1 = module0.tzUTC()
    assert var1 is not None
    var2 = var1.dst(var0)
    assert var2 is not None
    var3 = 'g?p~:'
    var4 = var1.dst(var3)
    assert var4 is not None
    var5 = {}
    var6 = module0.tzUTC(**var5)
    assert var6 is not None
    var7 = [var0, var0]
    var8 = module0.tzUTC(*var7)
    assert var8 is not None
    var9 = module0.utc_aware(var6)
    assert var9 is not None


def test_case_1():
    var0 = 'connect_'
    var1 = '5LS;Q|7CRotwL\r,\x0c`5Z'
    var2 = {var1}
    var3 = 'E\tu\tcXF'
    var4 = [var0]
    var5 = var2, var3, var4, var2
    var6 = True
    var7 = var5, var6
    var8 = [var0]
    var9 = {}
    var10 = module0.tzUTC(*var8, **var9)
    assert var10 is not None
    var11 = var10.utcoffset(var7)
    assert var11 is not None
    var12 = {var0: var0, var0: var0, var1: var1}
    var13 = module0.tzUTC(**var12)
    assert var13 is not None
    var14 = module0.tzUTC()
    assert var14 is not None
    var15 = var14.dst(var13)
    assert var15 is not None
