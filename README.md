# 🧮 Calculadora Interactiva en Docker

Este proyecto es una calculadora simple desarrollada en Python que puede ejecutarse dentro de un contenedor Docker. Soporta operaciones básicas, logging de resultados, pruebas automáticas con pytest y despliegue en Docker Hub.

## 🚀 Tecnologías utilizadas

- Python 3.12
- Docker
- Pytest
- Makefile
- Volúmenes Docker

---

## ⚙️ Funcionalidades

- Menú interactivo con operaciones: sumar, restar, multiplicar, dividir
- Registra operaciones en `logs/log.txt` (persistente fuera del contenedor)
- Incluye pruebas automatizadas con `pytest`
- Automatización con `Makefile`
- Versionamiento y despliegue en Docker Hub

---

## 📦 Cómo usar

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/calculadora-docker.git
cd calculadora-docker
