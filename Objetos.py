class Vehiculo :
    color = "Verde"
    ruedas = 14
    puertas = 5

class Coche (Vehiculo) :
    velocidadMax = 100
    cilindrada = 1200

c = Coche()


print("El color del coche es hermoso",c.color, "Montaña ", "con unas ruedas en rin de tamaño", c.ruedas
      , ", que le otorgan un exelente agarre y estavilidad al momento de rodar, es un coche de", c.puertas,
      "puertas que brinda una gran comodidad. Del 0 a",c.velocidadMax, "en 6.3 segundos. Y un motor de",
      c.cilindrada,"Cm3." )
