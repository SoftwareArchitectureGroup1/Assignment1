from django import template

register = template.Library()

@register.simple_tag
def sort_url(current_url, sort_by):
    current_sort_by = current_url.get('sort_by')
    current_sort_order = current_url.get('sort_order', 'asc')
    if current_sort_by == sort_by:
        sort_order = 'desc' if current_sort_order == 'asc' else 'asc'
    else:
        sort_order = 'asc'
    return f"?sort_by={sort_by}&sort_order={sort_order}"