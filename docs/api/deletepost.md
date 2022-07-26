# ``deletePost()`` 
Deletes the specified post. Default to soft deletion.

## Parameters
| Parameter      | Type                          | Description                              |
| :---------: | :----------------------------------: | :----------------------------------: |
| `post_id`       | integer | required
| `hard_delete`       | boolean | 
| `reason`       | string | 
| `author_alert`       | boolean | 
| `author_alert_reason`       | string | 


## Response
| Output      | Type                          | Description                                 |
| :---------: | :----------------------------------: | :----------------------------------: |
| `success`       | 	true |                                                 |

## Example
```py linenums="1"
from PyXenApi import XenForoAPI

xf = XenForoAPI('token', 'domain')

def main():
	data = xf.deletePost(1, False, 'test reason')
	return print(json.dumps(data, indent=4, sort_keys=True))
	
if __name__ == '__main__':
	main()
```