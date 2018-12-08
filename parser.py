import vk_api
vk_session = vk_api.VkApi('login', 'password')
vk_session.auth()









































#import csv
#group_id = -92876084#юморески
group_id = -33366598#брат за брата
vk = vk_session.get_api()
count = int(vk.wall.get(owner_id=group_id)['count'])
result =[]
_offset = 0
while True:
	response = vk.wall.get(owner_id=group_id, offset=_offset, count=100)
	for item in response['items']:
		if len(item['text']) > 40:
			result.append(item['text'])
	_offset += 100
	if not response['items']:
		break
result = list(set(result))
#jsonFile = ''
with open('result2.txt', 'w') as f:
	#result = dict(enumerate(result))
	for i in range(len(result)):
		result[i] = result[i].replace('\n', '')

	f.write('\n'.join(result))
