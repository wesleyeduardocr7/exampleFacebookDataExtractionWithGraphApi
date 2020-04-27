
import json
import facebook

def main():

    token = 'EAAIBY0GbxwEBAJfoHNOh2ozx36yBGZBCl50D6UVlpZC7JsDRvnfcnjZC2ow04EVBk3AXhCbWtBacnTFGvZCX606aWOQ7QZAmnenYpmTACJ92Mgvs7ZCEpMlHifOYn1rC7hMajjaa40Ejb6A9KutsdJqWXJgyYiXgEdlrtXOUwPpskbLUgZBrf0nu9TGPDMtpV0fZAZBPNmTmRyVIPpOaUFZCLpapJzcuXSDDAI8haskfZA8rAZDZD'

    graph = facebook.GraphAPI(token)

    fields = ['id,name,email,birthday,friends,link,feed']

    profile = graph.get_object('me',fields = fields)

    print(json.dumps(profile,indent=4))

main()