
**Проєкт:** Roamio — International Trip Planner


* FR-01: Управління профілем.
* FR-02: Створення подорожі.
* FR-03: Додавання локації.
* FR-04: Запрошення друзів.
* FR-05: Розрахунок бюджету.


```mermaid
flowchart LR
    User([Мандрівник])
    DB([База даних])

    subgraph Roamio
        U1(FR-01: Профіль)
        U2(FR-02: Подорож)
        U3(FR-03: Локація)
        U4(FR-04: Друзі)
        U5(FR-05: Бюджет)
        
        U2 -. include .-> U5
        U2 -. extend .-> U4
    end

    User --- U1 & U2 & U3
    U2 --- DB
```


```mermaid
classDiagram
    class User {
        +String name
        +login()
    }
    class Trip {
        +String destination
        +create()
    }
    class Location {
        +String address
        +add()
    }
    class Budget {
        +float amount
        +calculate()
    }
    class Item {
        +String name
        +pack()
    }

    User "1" -- "*" Trip : створює
    Trip "1" *-- "*" Location : композиція
    Trip "1" *-- "1" Budget : композиція
    Trip "1" *-- "*" Item : композиція
```


```mermaid
sequenceDiagram
    actor U as Мандрівник
    participant UI as Додаток
    participant S as Сервер
    
    U->>UI: Ввести витрати
    UI->>S: calculate_budget()
    
    alt Дані вірні
        S-->>UI: Сума (1050)
        UI-->>U: Показати на екрані
    else Помилка
        S-->>UI: Помилка формату
    end
```


| Вимога | Use Case | Класи | Діаграма послідовності |
| :--- | :--- | :--- | :--- |
| FR-01 | Профіль | User | Ні |
| FR-02 | Подорож | Trip, User | Ні |
| FR-03 | Локація | Trip, Location | Ні |
| FR-04 | Друзі | Trip, User | Ні |
| FR-05 | Бюджет | Trip, Budget | Так |