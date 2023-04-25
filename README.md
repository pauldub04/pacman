# Pacman Game
Аналог игры Pacman на Python. Командный проект для курса Промышленное программирование в Московской Школе Программистов, 2021

<img src="https://user-images.githubusercontent.com/49102209/234391160-915439ac-c57d-4acd-a144-9097e8157007.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/49102209/234391171-3f3d6b2a-80a6-4597-b1cc-4f004cb07f5a.png" width="30%"></img> <img src="https://user-images.githubusercontent.com/49102209/234391175-0e430245-7cc4-46fa-88fa-d11eca336f49.png" width="30%"></img> 

### Цель
Разработать и продемонстрировать игровое приложение, подобное всемирно известной игре [Pac-man](https://ru.wikipedia.org/wiki/Pac-Man). Всё действие происходит на игровом поле, наполненном точками (зёрнами). Также на поле присутствуют 4 привидения, цель которых - игрок.
Задача игрока — управляя Пакманом, съесть все точки в лабиринте, избегая встречи с привидениями

### Технологический стек:
- python 3.6+
- pygame 1.9+
- pandas 1.1+

### Инструкция по настройке проекта:
1. Склонировать проект:
   ```bash
   git clone https://github.com/pauldub04/pacman
   ```
2. Создать и активировать виртуальное окружение Python:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Обновить pip:
   ```bash
   pip install --upgrade pip
   ```
4. Установить в виртуальное окружение необходимые пакеты: 
   ```bash
   pip install -r requirements.txt
   ```
5. Запустить игру: 
   ```bash
   python run.py 
   ```
6. По окончании игры отключить виртуальное окружение Python: 
   ```bash
   deactivate 
   ```
