# ``getProfilePostComment()`` 
Gets information about the specified profile post comment.

## Parameters
| Parameter      | Type                          | Description                              |
| :---------: | :----------------------------------: | :----------------------------------: |
| `comment_id`       | integer | required

## Response
| Output      | Type                          | Description                                 |
| :---------: | :----------------------------------: | :----------------------------------: |
| `node`       | 	<a href="https://xenforo.com/community/pages/api-endpoints/#type_ProfilePostComment">ProfilePostComment</a> |                                                       |

## Example
```py linenums="1"
from PyXenApi import XenForoAPI

xf = XenForoAPI('token', 'domain')

def main():
	data = xf.getProfilePostComment(1)
	return print(json.dumps(data, indent=4, sort_keys=True))
	
if __name__ == '__main__':
	main()
```