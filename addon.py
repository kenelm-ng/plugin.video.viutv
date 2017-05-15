import xbmcgui
import xbmcplugin
import xbmcaddon
import requests
import simplejson

addon = xbmcaddon.Addon()

url = "https://api.viu.now.com/p8/1/getLiveURL"

payload = "{\"channelno\":\"099\",\"format\":\"HLS\",\"deviceId\":\"0000anonymous_user\"}"

headers = {
    'cache-control': "no-cache",
    'user-agent': "NNC/1607081705 CFNetwork/711.1.12 Darwin/14.0.0" 
    }

response = requests.request("POST", url, data=payload, headers=headers)

#print(response.text)
parsed_data = simplejson.loads(response.text)

#username = parsed_data['responseCode']
url = parsed_data['asset']['hls']['adaptive'][0]

item = xbmcgui.ListItem('Viu TV')
xbmcplugin.addDirectoryItem(int(sys.argv[1]), url , item, isFolder=0)

xbmcplugin.endOfDirectory(int(sys.argv[1]))

