# ``getForum()`` 
Gets information about the specified forum

## Parameters
| Parameter      | Type                          | Description                              |
| :---------: | :----------------------------------: | :----------------------------------: |
| `forum_id`       | integer | required

## Response
| Output      | Type                          | Description                                 |
| :---------: | :----------------------------------: | :----------------------------------: |
| `forum`       | 	<a href="https://xenforo.com/community/pages/api-endpoints/#type_Forum">Forum</a> |
| `threads`       | 	<a href="https://xenforo.com/community/pages/api-endpoints/#type_Thread">Thread[]</a> | Threads on this page                                                       |

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