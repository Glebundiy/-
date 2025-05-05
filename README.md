# Микросервис на ВМ
Развернуть микросервис на виртуальной машине (ВМ), используя систему управления конфигурациями

Инструкция по установке 

1. Запуск гипервизора и стандартная настройка ВМ с помощью образа CentOS-Stream-9-latest-x86_64-dvd1.iso

2. Установка WSL на Windows хост с помощью PowerShell: wsl –install

2.1 Установка Ansible: sudo apt install ansible -y

3. Получение IP ВМ для файла инвентаря: ip a или ifconfig или ip addr | grep inet
3.1 Создание папки для проекта: mkdir -p ~/microservice_ansible
3.2 Копирование файлов из архива в эту директорию 
3.3 Обновление IP и данных пользователя для Вашей машины в файле inventory.ini

4. Запуск Playbook с флагом: ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i inventory.ini deploy.yml

5. Проверка на виртуальной машине с помощью браузера ,введя там http://localhost:8080/metrics
