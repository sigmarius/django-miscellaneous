# Python Django Project
## Учебный проект - применение возможностей Django

### Что сделано:
+ запуск проекта на Django;
+ обработка исключений, создание редиректов;
+ определение моделей. Миграции: создание и выполнение;
+ базовые операции добавления, чтения, изменения и удаления записей из таблицы БД с использованием ORM-интефрейса Django;
+ шаблоны - наследование, передача параметров из БД
+ подключена статика, сформированы URL-адреса в шаблонах
+ создание связей между моделями через класс ForeignKey
+ настроена админ-панель
+ пользовательские теги шаблонов
+ добавление данных из форм, не связанных с моделями, в БД
+ формы, связанные с моделями. Пользовательские валидаторы
+ FBV переписан на CBV - ListView, DetailView, CreateView
+ для исключения дублирования кода добавлены Mixins
+ постраничная навигация (пагинация)
+ регистрация пользователей на сайте
+ авторизация пользователей - класс представления LoginView и форма AuthenticationForm
+ оптимизация сайта с Django Debug Toolbar