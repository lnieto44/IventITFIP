from django import template

register = template.Library()

@register.inclusion_tag('customtags/link_to.html')
def link_to(**kwargs):
	'''
	link_to(**kwargs (namespace, url_name, id_link, link_class, icon_class, icon))
	'''
	return {
		'namespace': kwargs.get('namespace', ''),
		'url_name': kwargs.get('url_name', ''),
		'link': kwargs['namespace']+':'+kwargs.get('url_name', ''),
		'id':  kwargs.get('id_link', None),
		'nombre_cargo': kwargs.get('text', ''),
		'a_class': kwargs.get('link_class', ''),
		'i_class': kwargs.get('icon_class', ''),
		'icon': kwargs.get('icon', ''),
	}