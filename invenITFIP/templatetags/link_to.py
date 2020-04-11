from django import template

register = template.Library()

@register.inclusion_tag('customtags/link_to.html', )
def link_to(namesp, view='', id_link=None, name='', cl='', icon=''):
	'''
	link_to(namespace, view, id(optional), nombre_cargo or value, class(optional), icon(optionl))
	'''
	return {
		'link': '/'+str(namesp)+'/'+(str(view)),
		'id':  id_link,
		'nombre_activo': name,
		'class': cl,
		'icon': icon,
	}