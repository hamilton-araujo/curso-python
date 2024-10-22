velocidade = 61 #velocidade atual do carro
local_carro = 90 #local atual do carro

RADAR_1 = 60 #velocidade máxima
LOCAL_1 = 100 #posição do radar
RADAR_RANGE = 1 #distância em que o radar pega

range_min = LOCAL_1 - RADAR_RANGE
range_max = LOCAL_1 + RADAR_RANGE

carro_alem_do_limite_de_velocidade = velocidade > RADAR_1
carro_no_range_do_radar = range_min < local_carro < range_max

if carro_alem_do_limite_de_velocidade and carro_no_range_do_radar:
    print("O carro está multado")
elif carro_no_range_do_radar and not carro_alem_do_limite_de_velocidade:
    print("O carro está dentro da velocidade permitida.")
elif carro_alem_do_limite_de_velocidade and not carro_no_range_do_radar:
    print("Apesar do carro ultrapassar o limite de velocidade, o carro está fora do range do radar.")
else:
    print("O carro não está multado. Ele está fora do range do radar e dentro do limite de velocidade")