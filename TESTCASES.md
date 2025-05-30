Автоматизированные тест-кейсы тематически разбиты на три файла по пунктам задания.

* testcases_open_gameсard.py
  
  В нем содержатся тест-кейсы для пользовательского сценария "Открытие карточки игры", а именно:
  
  * test_open_game_card()
    
    Производится открытие одной карточки игры по имени и проверка заголовка.
    
  * test_open_all_game_cards()
    
    Производится открытие поочередно всех карточек игр на странице и проверка заголовка,
    с возвратом на главную страницу по кнопке 'Back to main'.
    
* testcases_pagination_size_change.py
  
  В нем содержатся тест-кейсы для пользовательсткого сценария "Переход по страницам результата поиска с помощью пагинации", а именно:
  
  * test_navigation_buttons_w_nums_change_page()
    
    Производится проверка, что при нажатии на кнопки навигации с цифрами происходит
    переход на соответствующую страницу. Проверяет по появлению класса 'ant-pagination-item-active'.
    
  * test_navigation_arrows_change_page()
    
    Производится переключение между страницами с помощью кнопок-стрелок.
    Два шага вперед, один назад, от первой до последней страницы.
    (Так мы проверим сразу и левую, и правую кнопку на каждой странице)

  * test_navigation_jump_buttons()
 
    Производится проверка навигации с помощью кнопок "Next 5 Pages" и "Previous 5 Pages".

* testcases_pagination.py

  В нем содержатся тест-кейсы для пользовательсткого сценария "Отображение разного количества карточек игр на странице поиска", а именно:

  * test_display_different_number_of_game_cards()
 
    Производится отображение разного количества карточек игр на странице поиска,
    ввод значения в текстовое поле и сверка с фактическим количеством.


****Тест-кейсы:****

**Открытие карточки игры**

| Поле      | Значение                              |  |
| :----- | :--------------------------------------- | :---------------------------------------------------------- |
| Test Case Name       | E2E-сценарий просмотра сведений об игре          |                                                              |
| Test Case ID  | 1                                     |                                                              |
| Приоритет / серьезность | High / Critical                              |                                                              |
| Предусловия | Открыта главная страница сайта, фильтры не установлены |                                       |
| Steps      | 1. Кликнуть на карточку игры "Tarisland"     |                                     |
| ER | Открывается страница с описанием игры  | 

| Поле      | Значение                              |  |
| :----- | :--------------------------------------- | :---------------------------------------------------------- |
| Test Case Name       | E2E-сценарий просмотра сведений о всех играх         |                                                              |
| Test Case ID  | 2                                     |                                                              |
| Приоритет / серьезность | High / Critical                              |                                                              |
| Предусловия | Открыта главная страница сайта, фильтры не установлены |                                       |
| Steps      | 1. Кликнуть на карточку игры "Tarisland"     |                                     |
|       | 2. Кликнуть на кнопку "Back to Main"     |                                     |
|       | 3. Кликнуть на карточку игры "Overwatch 2"     |                                     |
|       | 4. Кликнуть на кнопку "Back to Main"     |                                     |
|       |  ---//---    |                                     |
|       | 19. Кликнуть на карточку игры "Game Of Thrones Winter Is Coming"     |                                     |
|       | 20. Кликнуть на кнопку "Back to Main"     |                                     |
| ER | 1. Открывается страница с описанием игры "Tarisland" | 
|  | 2. Открывается главная страница сайта, фильтры не установлены  | 
|  | 3. Открывается страница с описанием игры "Overwatch 2" | 
|  | 4. Открывается главная страница сайта, фильтры не установлены  | 
|  |  ---//---  | 
|  | 19. Открывается страница с описанием игры "Game Of Thrones Winter Is Coming" | 
|  | 20. Открывается главная страница сайта, фильтры не установлены  | 

**Отображение разного количества карточек игр на странице поиска**
| Поле      | Значение                              |  |
| :----- | :--------------------------------------- | :---------------------------------------------------------- |
| Test Case Name       | E2E-сценарий изменения количества отображающихся карточек на странице на 20          |                                                              |
| Test Case ID  | 3                                     |                                                              |
| Приоритет / серьезность | Low / Minor                              |                                                              |
| Предусловия | Открыта главная страница сайта, фильтры не установлены, отображаемое количество карточек игр на странице: 10 |                                       |
| Steps      | 1. Кликнуть на выпадающий список выбора количества отображаемых карочек игр на странице     |                                     |
|            | 2. В выпадающем списке выбрать "20 / page"     |                                     |
| ER | 1. Открывается выпадающий список с четыремя значениями: "10 / page", "20 / page", "50 / page", "100 / page" | 
|  | 2. Выпадающий список закрывается, значение установлено на "20 / page". На странцие отображаются 20 карточек игр | 

| Поле      | Значение                              |  |
| :----- | :--------------------------------------- | :---------------------------------------------------------- |
| Test Case Name       | E2E-сценарий изменения количества отображающихся карточек на странице  на 50         |                                                              |
| Test Case ID  | 4                                    |                                                              |
| Приоритет / серьезность | Low / Minor                              |                                                              |
| Предусловия | Открыта главная страница сайта, фильтры не установлены, отображаемое количество карточек игр на странице: 10 |                                       |
| Steps      | 1. Кликнуть на выпадающий список выбора количества отображаемых карточек игр на странице     |                                     |
|            | 2. В выпадающем списке выбрать "50 / page"     |                                     |
| ER | 1. Открывается выпадающий список с четыремя значениями: "10 / page", "20 / page", "50 / page", "100 / page" | 
|    | 2. Выпадающий список закрывается, значение установлено на "50 / page". На странцие отображаются 50 карточек игр | 
|Note| Провален|

| Поле      | Значение                              |  |
| :----- | :--------------------------------------- | :---------------------------------------------------------- |
| Test Case Name       | E2E-сценарий изменения количества отображающихся карточек на странице на 100        |                                                              |
| Test Case ID  | 5                                   |                                                              |
| Приоритет / серьезность | Low / Minor                              |                                                              |
| Предусловия | Открыта главная страница сайта, фильтры не установлены, отображаемое количество карточек игр на странице: 10 |                                       |
| Steps      | 1. Кликнуть на выпадающий список выбора количества отображаемых карточек игр на странице     |                                     |
|            | 2. В выпадающем списке выбрать "100 / page"     |                                     |
| ER | 1. Открывается выпадающий список с четыремя значениями: "10 / page", "20 / page", "50 / page", "100 / page" | 
|  | 2. Выпадающий список закрывается, значение установлено на "100 / page". На странцие отображаются 10 карточек игр | 


| Поле      | Значение                              |  |
| :----- | :--------------------------------------- | :---------------------------------------------------------- |
| Test Case Name       | E2E-сценарий изменения количества отображающихся карточек на странице на 10         |                                                              |
| Test Case ID  | 6                                     |                                                              |
| Приоритет / серьезность | Low / Minor                              |                                                              |
| Предусловия | Открыта главная страница сайта, фильтры не установлены, отображаемое количество карточек игр на странице: 20 |                                       |
| Steps      | 1. Кликнуть на выпадающий список выбора количества отображаемых карточек игр на странице     |                                     |
|            | 2. В выпадающем списке выбрать "10 / page"     |                                     |
| ER | 1. Открывается выпадающий список с четыремя значениями: "10 / page", "20 / page", "50 / page", "100 / page" | 
|  | 2. Выпадающий список закрывается, значение установлено на "10 / page". На странцие отображаются 10 карточек игр | 


**Переход по страницам результата поиска с помощью пагинации**
| Поле      | Значение                              |  |
| :----- | :--------------------------------------- | :---------------------------------------------------------- |
| Test Case Name       | E2E-сценарий пагинации с помощью кнопок с номерами страниц         |                                                              |
| Test Case ID  | 7                                     |                                                              |
| Приоритет / серьезность | Medium / Major                              |                                                              |
| Предусловия | Открыта главная страница сайта, фильтры не установлены, отображаемое количество карточек игр на странице: 10, открыта первая страница |                                       |
| Steps      | 1. Кликнуть на кнопку страницы номер 2     |                                     |
|            | 2. Повторить шаг 1, пока страницы не закончатся  (их всего 41, будь страниц больше, я бы так не написал))  |                                     |
| ER | 1. Открывается страница номер 2 | 
| | 40. Открывается страница номер 41 | 
|Note| Провален на последнем шаге|

| Поле      | Значение                              |  |
| :----- | :--------------------------------------- | :---------------------------------------------------------- |
| Test Case Name       | E2E-сценарий пагинации с помощью кнопок-стрелок         |                                                              |
| Test Case ID  | 8                                  |                                                              |
| Приоритет / серьезность | Medium / Major                              |                                                              |
| Предусловия | Открыта главная страница сайта, фильтры не установлены, отображаемое количество карточек игр на странице: 10, открыта первая страница |                                       |
| Steps      | 1. Кликнуть на кнопку-стрелку Вправо дважды     |                                     |
|       | 2. Кликнуть на кнопку-стрелку Влево единожды     |                                     |
|       | 3. Повторять шаги 1 и 2, пока не будет посещена 41я станица (их всего 41, будь страниц больше, я бы так не написал))     |                                     |
| ER | 1. Открывается страница номер 3 | 
| | 2. Открывается страница номер 2 | 
| | 3. Открыта страница 41 | 
|Note1| Провален|
|Note2| Позволяет определить, что кнопки-стрелки работют на каждой странице|

| Поле      | Значение                              |  |
| :----- | :--------------------------------------- | :---------------------------------------------------------- |
| Test Case Name       | E2E-сценарий пагинации с помощью кнопок перемотки на пять страниц         |                                                              |
| Test Case ID  | 9                                  |                                                              |
| Приоритет / серьезность | Medium / Major                              |                                                              |
| Предусловия | Открыта главная страница сайта, фильтры не установлены, отображаемое количество карточек игр на странице: 10, открыта первая страница |                                       |
| Steps      | 1. Кликнуть на кнопку перемотки на пять страниц Вправо дважды     |                                     |
|       | 2. Кликнуть на кнопку перемотки на пять страниц Влево единожды     |                                     |
|       | 3. Повторять шаги 2 и 3, пока не будет посещена страница 41   |                                     |
| ER | 1. Открывается страница номер 3 | 
| | 2. Открывается страница номер 2 | 
| | 3. Открывается страница номер 41 |
|Note1| Провален|
|Note2| Позволяет определить, что кнопки перемотки на пять страниц работют на каждой пятой странице|

