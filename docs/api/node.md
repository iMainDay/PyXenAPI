# ``getNode()`` 
Gets information about the specified node

## Parameters
| Parameter      | Type                          | Description                              |
| :---------: | :----------------------------------: | :----------------------------------: |
| `node_id`       | integer | required

## Response
| Output      | Type                          | Description                                 |
| :---------: | :----------------------------------: | :----------------------------------: |
| `node`       | 	<a href="https://xenforo.com/community/pages/api-endpoints/#type_Node">Node</a> |                                                       |

## Example
```py linenums="1"
from PyXenApi import XenForoAPI

xf = XenForoAPI('token', 'domain')

def main():
	data = xf.getNode(2)
	return print(json.dumps(data, indent=4, sort_keys=True))
	
if __name__ == '__main__':
	main()
```