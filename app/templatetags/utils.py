def filter_item_id_list(parent, main_item: list, filter_item_id: list) -> list:
    items_id = []

    # Пока существует родительский элемент
    while parent:

        # Добавляем идентификатор текущего элемента в список
        items_id.append(parent.id)

        # Переходим к родительскому элементу
        parent = parent.parent
    else:

        # Когда цикл завершается (когда parent становится False), начинаем проверять основной список элементов
        for item in main_item:
            # Если идентификатор элемента из основного списка соответствует фильтру
            if item['id'] == filter_item_id:
                # Добавляем этот идентификатор в список items_id
                items_id.append(filter_item_id)

    # Возвращаем список идентификаторов элементов, которые прошли фильтрацию
    return items_id


def child(items_values, cur_id: int, filter_item_id_list: list) -> list:

    # Получаем список элементов, у которых родительский идентификатор равен текущему идентификатору
    lst_items = [it for it in items_values.filter(parent_id=cur_id)]

    # Для каждого элемента в списке
    for item in lst_items:
        # Если идентификатор элемента присутствует в списке фильтрованных идентификаторов
        if item['id'] in filter_item_id_list:
            # Рекурсивно вызываем функцию child для этого элемента,
            # чтобы получить его детей и добавляем их в атрибут 'childs'
            item['childs'] = child(
                items_values, item['id'], filter_item_id_list
            )

    # Возвращаем список элементов
    return lst_items


def additional_menu(context: dict, menu: str, querystring_args: list):
    """
    Получение дополнительного меню,
    для выводы нескольких меню на одной странице.
    """
    # Проходим по всем ключам GET запроса
    for key_menu in context['request'].GET:
        # Проверяем, если ключ не совпадает с текущим меню
        if key_menu != menu:
            # Если условие выполнено, добавляем параметры запроса в список
            # в формате "ключ=значение" для всех ключей, кроме текущего меню
            querystring_args.append(
                key_menu + '=' + context['request'].GET[key_menu]
            )
    # Возвращаем строку, содержащую все параметры запроса, кроме текущего меню,
    # объединенные символом '&' для формирования строки запроса
    return ('&').join(querystring_args)

