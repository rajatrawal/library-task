def make_id(city_name,id,length):
    if(len(city_name) > 3):
        city_name = city_name[:3]
    id = str(id)
    id_size = len(id)
    composite_id = f'AR{city_name} ' + (length-id_size) * '0' + id

    return composite_id


    