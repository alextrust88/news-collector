# GitHub Actions Workflows

Этот каталог содержит конфигурации для GitHub Actions CI/CD.

## Workflows

### 1. CI (`.github/workflows/ci.yml`)

Автоматически запускается при:
- Push в ветки `main` или `develop`
- Создании Pull Request в ветки `main` или `develop`

**Что проверяется:**
- Тесты на разных ОС (Ubuntu, macOS) и версиях Python (3.11, 3.12)
- Синтаксис Python файлов
- Импорты модулей

### 2. Build and Push Docker Image (`.github/workflows/docker-build.yml`)

Автоматически запускается при:
- Push в ветку `main`
- Создании тега `v*` (например, `v1.0.0`)
- Pull Request в `main` (только сборка, без публикации)

**Что делает:**
- Собирает Docker образ
- Публикует в GitHub Container Registry (ghcr.io)
- Использует кеширование для ускорения

**Результат:**
Образ доступен по адресу: `ghcr.io/alextrust88/trusted-news:latest`

### 3. Deploy to Server (`.github/workflows/deploy.yml`)

Автоматически запускается при:
- Push в ветку `main` (после успешной сборки образа)
- Ручной запуск через `workflow_dispatch`

**Что делает:**
1. Собирает Docker образ
2. Публикует в GitHub Container Registry
3. Копирует конфигурационные файлы на сервер
4. Подключается к серверу по SSH
5. Обновляет и перезапускает контейнеры
6. Выполняет health check

**Требуемые секреты:**
- `DEPLOY_HOST` - IP или домен сервера
- `DEPLOY_USER` - пользователь для SSH
- `DEPLOY_SSH_KEY` - приватный SSH ключ
- `DEPLOY_PORT` (опционально) - SSH порт (по умолчанию 22)
- `DEPLOY_PATH` (опционально) - путь к проекту (по умолчанию `/opt/newsagent`)

## Настройка секретов

1. Перейдите в Settings → Secrets and variables → Actions
2. Добавьте необходимые секреты (см. DEPLOY.md)

## Ручной запуск деплоя

1. Перейдите в Actions → Deploy to Server
2. Нажмите "Run workflow"
3. Выберите environment (production/staging)
4. Нажмите "Run workflow"

## Отладка

Если workflow не работает:
1. Проверьте логи в разделе Actions
2. Убедитесь что все секреты настроены
3. Проверьте что SSH ключ правильный
4. Проверьте что на сервере установлены Docker и Docker Compose
