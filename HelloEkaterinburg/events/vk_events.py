import vk


def get_events():

    api = vk.API(v="5.131",
                 access_token="vk1.a.GS11RDLs8bfRMsncVbGtzff1pWcr6ygfBR4vWbS_z-baB1_-X6y0w_Mo6Sgp4fe3NW-lBnSL3U8aogiMLEYZOEQSkH6MHJEdVyzTnAYlYhIK1gN7e9CMq5k0yRz6JoM3BHkX0D169uRhaXXmi_LFZvqnxfmV8WO1XBHrUz-TZUwUpHfb6BplDwCEenHJOc5VZsNqu8jigCzsexYuu2xXTg")
    response = api.wall.get(owner_id='-93837381')
    posts = response['items']
    descriptions = [post['text'] for post in posts if post['text']]

    return descriptions


print(get_events())