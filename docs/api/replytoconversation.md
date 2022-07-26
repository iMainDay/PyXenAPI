# ``replyToConversation()`` 
Replies to a conversation

## Parameters
| Parameter      | Type                          | Description                              |
| :---------: | :----------------------------------: | :----------------------------------: |
| `conversation_id`  | integer | required
| `message`       | string | required 
| `attachment_key`       | string | API attachment key to upload files.


## Response
| Output      | Type                          | Description                                 |
| :---------: | :----------------------------------: | :----------------------------------: |
| `success`       | 	true |                                                 |
| `message`       | 	<a href="https://xenforo.com/community/pages/api-endpoints/#type_ConversationMessage">ConversationMessage</a> | The newly inserted message                                                 |

## Example
```py linenums="1"
from PyXenApi import XenForoAPI

xf = XenForoAPI('token', 'domain')

def main():
	data = xf.replyToConversation(1, "Hello, world!")
	return print(json.dumps(data, indent=4, sort_keys=True))
	
if __name__ == '__main__':
	main()
```