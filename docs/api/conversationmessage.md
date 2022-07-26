# ``getConversationMessage()`` 
Gets the specified conversation message.

## Parameters
| Parameter      | Type                          | Description                              |
| :---------: | :----------------------------------: | :----------------------------------: |
| `message_id`       | integer | required

## Response
| Output      | Type                          | Description                                 |
| :---------: | :----------------------------------: | :----------------------------------: |
| `message`       | 	<a href="https://xenforo.com/community/pages/api-endpoints/#type_ConversationMessage">ConversationMessage</a> |                                                       |

## Example
```py linenums="1"
from PyXenApi import XenForoAPI

xf = XenForoAPI('token', 'domain')

def main():
	data = xf.getConversationMessage(1)
	return print(json.dumps(data, indent=4, sort_keys=True))
	
if __name__ == '__main__':
	main()
```