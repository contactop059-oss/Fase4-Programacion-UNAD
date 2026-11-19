
# Sistema Integral de Gestión de Clientes, Servicios y Reservas

## Universidad Nacional Abierta y a Distancia - UNAD

**Curso:** Programación  
**Código:** 213023  
**Actividad:** Fase 4 - Prácticas simuladas  
**Empresa simulada:** Software FJ

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de gestión de clientes, servicios y reservas utilizando Python y programación orientada a objetos.

La aplicación permite registrar clientes, consultar servicios, crear reservas, confirmar operaciones, procesar costos y cancelar reservas, incorporando validaciones y manejo de excepciones.

## Objetivo

Desarrollar una aplicación modular que implemente abstracción, herencia, polimorfismo, encapsulación y manejo de excepciones para garantizar la estabilidad del sistema.

## Funcionalidades

- Registro y consulta de clientes.
- Validación de datos personales.
- Consulta de servicios disponibles.
- Creación y confirmación de reservas.
- Consulta y cancelación de reservas.
- Procesamiento de reservas con descuentos.
- Manejo de excepciones personalizadas.
- Registro de errores y eventos en sistema.log.

## Servicios disponibles

1. Reserva de salas.
2. Alquiler de equipos.
3. Asesorías especializadas.

## Archivos del proyecto

- main.py: menú principal y gestión del sistema.
- cliente.py: clase Cliente y validaciones.
- servicio.py: clases de servicios y cálculos.
- reserva.py: gestión de reservas y excepciones.
- sistema.log: registro generado durante la ejecución.

## Ejecución del programa

El proyecto requiere Python 3.

Para ejecutar el sistema:

```bash
python main.py
```

También puede ejecutarse en Google Colab descargando el repositorio y utilizando el comando anterior.

## Pruebas realizadas

Se han diseñado pruebas para verificar:

- Registro y consulta de clientes.
- Consulta de servicios.
- Creación y procesamiento de reservas.
- Cancelación de reservas.
- Validación de clientes duplicados.
- Validación de correos incorrectos.
- Manejo de clientes inexistentes.
- Creación correcta e incorrecta de servicios.

## Almacenamiento

El sistema utiliza listas y objetos en memoria, sin bases de datos. Los eventos y errores se registran en un archivo de logs.

## Referencias

Python Software Foundation. (2024). El tutorial de Python. https://docs.python.org/es/3.12/tutorial/errors.html

