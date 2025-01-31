# Polylingua

### Предварительные требования

- Python 3.8+
- pip (пакетный менеджер Python)
- Git

Проверьте версии Python и pip:
```bash
python --version
pip --version
```

### Установка

1. Склонируйте репозиторий:
```bash
git clone https://github.com/MusarskayaM/PyQT-project.git
cd PyQT-project
```

2. Создайте виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

### Настройка базы данных

При первом запуске приложение автоматически создаст файл базы данных, если он отсутствует. Вы также можете вручную добавить или настроить файл базы данных в корневой директории.

### Запуск приложения

Для запуска используйте следующую команду:
```bash
python main21.py
```

### Описание приложения

Polylingua — это интуитивно понятный симулятор для изучения иностранных языков. Возможности:

- **Добавление слов:** возможность добавлять новые иностранные слова с переводами.
- **Тренировка:** режим, где можно практиковаться, вводя свои переводы и проверяя ответы.
- **Редактирование слов:** обновление неправильных переводов.
- **Удаление слов:** удаление ненужных слов из словаря.

Программа предотвращает добавление дублирующихся иностранных слов, делая процесс обучения удобным и эффективным. Polylingua подходит для пользователей любого возраста, предоставляя доступный интерфейс и простой в использовании функционал.
