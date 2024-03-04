from django import template

from app.models import Item
from app.templatetags.utils import additional_menu, child, filter_item_id_list

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context: dict, menu):
    """Метод для построения древовидного меню."""

    try:
        # Пытаемся получить идентификатор фильтра из GET запроса и преобразовать его в целое число
        filter_item_id = int(context['request'].GET[menu])
        # Получаем все элементы меню с именем menu
        items = Item.objects.filter(menu__name=menu)
        # Получаем значения всех элементов меню
        items_values = items.values()
        # Получаем основные элементы меню (без родительских)
        main_item = [item for item in items_values.filter(parent=None)]
        # Фильтруем идентификаторы элементов в соответствии с переданным фильтром
        filter_items_id_list = filter_item_id_list(
            items.get(id=filter_item_id), main_item, filter_item_id
        )

        # Для каждого основного элемента проверяем, есть ли он в списке отфильтрованных элементов
        for item in main_item:
            if item['id'] in filter_items_id_list:
                # Если да, то добавляем дочерние элементы, соответствующие фильтру
                item['childs'] = child(
                    items_values, item['id'], filter_items_id_list
                )
        # Формируем словарь элементов меню
        item_dict = {'items': main_item}

    except Exception:
        # В случае возникновения исключения (например, если идентификатор фильтра не найден в GET запросе)
        # получаем основные элементы меню без фильтрации
        item_dict = {
            'items': [
                item
                for item in Item.objects.filter(
                    menu__name=menu, parent=None
                ).values()
            ]
        }

    # Добавляем имя меню и строку дополнительных параметров в словарь элементов меню
    item_dict['menu'] = menu
    item_dict['additional_menu'] = additional_menu(context, menu, [])
    # Возвращаем сформированный словарь
    return item_dict

