from groupy import Client
from groupy import attachments


client = Client.from_token('YOUR_TOKEN_HERE')

groups = client.groups
test_api_group = groups.get('YOUR_GROUP_ID_HERE') #get id with curl

for message in test_api_group.messages.list_all():
    print(message.text)



# # for group in groups.autopage():
# #     print(group.name)

# group = groups[0]


# # message = group.post(text='hi')

# for message in group.messages.list_all():
#     print(message.text)

with open('maru.png', 'rb') as f:
    image = client.images.from_file(f)
    # image = client.images.upload(f)
    message = test_api_group.post(text="Say hi to Maru!!!",attachments=[image])
    # print(image)
