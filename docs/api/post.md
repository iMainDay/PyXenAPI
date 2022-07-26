# ``getPost()`` 
Gets information about the specified post

## Parameters
| Parameter      | Type                          | Description                              |
| :---------: | :----------------------------------: | :----------------------------------: |
| `post_id`       | integer | required

## Response
| Output      | Type                          | Description                                 |
| :---------: | :----------------------------------: | :----------------------------------: |
| `post`       | <a href="https://xenforo.com/community/pages/api-endpoints/#type_Post">Post</a> |  

## Example
```py linenums="1"
from PyXenApi import XenForoAPI

xf = XenForoAPI('token', 'domain')

def main():
	data = xf.getPost(1)
	return print(json.dumps(data, indent=4, sort_keys=True))
	
if __name__ == '__main__':
	main()
```