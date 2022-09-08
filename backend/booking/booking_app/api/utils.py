from django.db.models import Q

def str_to_bool(value) :
  return value.lower() == 'true'

def custom_query(params):
  query = Q()

  for param in params :
      sub_query = Q()
      for value in params[param].split('|'):
          if value.lower() == 'true' or value.lower() == 'false' : value = str_to_bool(value)
          sub_query |= Q(**{'' + param : value})
      query &= sub_query
  return query