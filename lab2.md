
**Проєкт:** Roamio — International Trip Planner


* **FR-01:** Реєстрація та управління профілем.
* **FR-02:** Створення подорожі (дати, країна).
* **FR-03:** Формування маршруту (додавання локацій).
* **FR-04:** Спільне планування з іншими користувачами.
* **FR-05:** Розрахунок бюджету подорожі (калькуляція).
* **FR-06:** Генерація списку речей.

Актори: Мандрівник (Tourist), База даних (Database).

```mermaid
flowchart LR
    %% Актори
    Tourist([Мандрівник])
    DB([База даних])

    %% Прецеденти
    subgraph Roamio System
        UC1(FR-01: Управління профілем)
        UC2(FR-02: Створити подорож)
        UC3(FR-03: Додати локацію)
        UC4(FR-04: Запросити друга)
        UC5(FR-05: Розрахувати бюджет)
        
        %% Зв'язки include/extend
        UC2 -. "<< include >>" .-> UC5
        UC2 -. "<< extend >>" .-> UC4
    end

    %% Зв'язки акторів
    Tourist --- UC1
    Tourist --- UC2
    Tourist --- UC3
    UC1 --- DB
    UC2 --- DB
```
## Крок 4. Діаграма класів (Class Diagram)

```mermaid
classDiagram
    class User {
        +int id
        +String name
        +String email
        +register()
        +login()
    }
    
    class Trip {
        +int tripId
        +String destination
        +Date startDate
        +Date endDate
        +createTrip()
        +shareTrip()
    }
    
    class Location {
        +String title
        +String address
        +addLocation()
    }
    
    class Budget {
        +float totalAmount
        +int days
        +calculateBudget()
    }

    %% Зв'язки
    User "1" -- "*" Trip : створює
    Trip "1" *-- "*" Location : містить (Композиція)
    Trip "1" *-- "1" Budget : має (Композиція)
```
## Крок 5. Діаграма послідовності (Sequence Diagram)
Сценарій: Розрахунок бюджету подорожі (FR-05).

```mermaid
sequenceDiagram
    actor User as Мандрівник
    participant UI as Інтерфейс (App)
    participant Sys as Система (Backend)
    
    User->>UI: Натискає "Розрахувати бюджет"
    UI->>User: Запитує кількість днів та витрати
    User->>UI: Вводить дані (дні, ціна готелю, їжа)
    UI->>Sys: Відправляє дані (calculate_travel_budget)
    
    alt Дані введені коректно
        Sys-->>UI: Повертає загальну суму (1050)
        UI-->>User: Показує бюджет на екрані
    else Помилка введення (наприклад, літери замість цифр)
        Sys-->>UI: Повертає помилку валідації
        UI-->>User: Просить ввести дані знову
    end
```

## Крок 6. Матриця трасовності

| Функціональна вимога | Прецедент (Use Case) | Задіяні класи | Діаграма послідовності |
| :--- | :--- | :--- | :--- |
| FR-01: Управління профілем | UC1: Управління профілем | User | Ні |
| FR-02: Створення подорожі | UC2: Створити подорож | Trip, User | Ні |
| FR-03: Додавання локації | UC3: Додати локацію | Trip, Location | Ні |
| FR-04: Спільне планування | UC4: Запросити друга | Trip, User | Ні |
| **FR-05: Розрахунок бюджету** | **UC5: Розрахувати бюджет** | **Trip, Budget** | **Так (див. Крок 5)** |