from playwright.sync_api import Page

# Отключаем загрузку статических ресурсов
def mock_static_resources(page: Page):
    page.route("**/*.{ico,png,jpg,webp,mp3,mp4,woff,woff2}", lambda route: route.abort()) # Отменяем загрузку ресурса
