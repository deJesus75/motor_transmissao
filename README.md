# motor_transmissao
O pacote motor_transmissao é utilizado para simular um sistema de transmissão
com motor, redutor e eixo de saída , funções:
    - calcula_torque[Kgf.m]
    - velocidade_tangencial[m/min]
    - forca_puxada [força tangencial ao eixo de saida]

# Installation

pip install -i https://test.pypi.org/simple/ motor-transmissao==0.0.1

# Usage

from motor_transmissao import motor
rd = motor.Roda(0.076,40)
print(rd.velocidade_tangencial())

# Author
Wilian Oliveira de Jesus

# License
